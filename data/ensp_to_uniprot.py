import argparse
from urllib import parse, request
import os
from multiprocessing import Pool
import pandas as pd


def text_to_csv(text_file: str):
    """
    Converts space-delimited .txt file to .csv
    :param text_file: input file
    :return: path to .csc file
    """

    csv_path = "./data/sources/ppi_links.csv"

    with open(os.path.join("./data/sources", text_file), 'r') as in_file, open(csv_path,'w') as out_file:
        in_lines = in_file.readlines()
        out_lines = [line.replace(" ", ",") for line in in_lines]
        out_file.writelines(out_lines)

    return csv_path


def chunks(lst: [], n: int):
    """
    Divides lists into chunks of size N
    :param lst: input list
    :param n: desired chunk length
    :return: List of chunks
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_uniprot_id_mappings(protein_csv: str):
    """
    Retrieves all UniProt ID mappings for StringDB ensp IDs.
    Most ensp ID's have cross-references in UniProt, so they can be
    retrieved in batches. ID's that are one-way (not cross-referenced)
    must be retrieved one by one, to keep track of input ensp ID.
    Saves the mapping as a .csv file.

    NOTE: There are roughly ~100 ensp IDs without UniProt IDs as of 3/29/2020

    :param protein_csv: path to .csv containing all ensp IDs
    :return:
    """

    with open(protein_csv, 'r') as in_file:
        all_ensp_ids = [line.split(",")[0] for line in in_file.readlines()]

    unique_ensp_ids = list(set(all_ensp_ids))

    chunked_list = chunks(unique_ensp_ids, 100)

    # multi-proc
    pool = Pool(4)
    all_uniprot_repsonses = pool.map(retrieve_mapping_one_chunk, chunked_list)
    pool.close()

    response_list = [response.split("\n") for response in all_uniprot_repsonses]

    rows = []
    for response in response_list:
        for row in response[1:]: # exclude header
            if row != "" and "Homo sapiens" in row:
                rows.append(row.rstrip(";").split("\t"))

    df = pd.DataFrame(rows)

    df.columns = ["uniprot_id", "organism", "ensp_id"]

    # check for IDs without a mapping
    incomplete_ensps = [ensp_id for ensp_id in unique_ensp_ids if ensp_id not in set(df["ensp_id"])]

    # multi-proc
    pool = Pool(4)
    missing_entries = pool.map(retrieve_one_mapping, incomplete_ensps)
    pool.close()

    missing_rows = []
    for ensp_id, response in missing_entries:
        if response != "" and "Homo sapiens" in response:
            row = response.split("\t")
            row.append(ensp_id)
            missing_rows.append(row)

    df_missing = pd.DataFrame(missing_rows)

    df_missing.columns = ["uniprot_id", "organism", "ensp_id"]

    # combine DFs, and filter to non-null values
    df_complete = pd.concat([df,df_missing])
    df_complete = df_complete.drop(columns=["organism"])
    df_complete = df_complete[df_complete["ensp_id"] != ""]

    df_complete.to_csv("./sources/ensp_uniprot.csv", index=False)


####################################
# Multiprocessing Worker Functions #
####################################

def retrieve_mapping_one_chunk(chunk: [str]):
    """
    Retrieves ensp -> UniProt mappings for list of ensp_ids, through UniProt's REST API
    :param chunk: List of ensp_ids
    :return: tab-delimited string response
    """

    data_dict = {"query": "+OR+".join([ensp_id.lstrip("9606.") for ensp_id in chunk]),
                 "columns": "id,organism,database(STRING)",
                 "format": "tab"}

    data = parse.urlencode(data_dict).encode()

    req = request.Request("https://www.uniprot.org/uniprot/", data=data)

    response = request.urlopen(req).read().decode('utf-8')

    return response


def retrieve_one_mapping(ensp_id: str):
    """
    Retrieves ensp -> UniProt mapping for one ensp_id, through UniProt's REST API
    :param ensp_id:
    :return: input ensp id, and the tab-delimited string response
    """
    data_dict = {"query": ensp_id.lstrip("9606."),
                 "columns": "id,organism",
                 "format": "tab"}
    data = parse.urlencode(data_dict).encode()
    req = request.Request("https://www.uniprot.org/uniprot/", data=data)  # this will make the method "POST"
    response = request.urlopen(req).read().decode('utf-8').strip("\n").split("\n")[-1]

    return ensp_id, response


def main():
    """ Parse command line args and run """
    parser = argparse.ArgumentParser(
        description="Converts StringDB .txt file dump to .csv format, and then retrieves"
                    "ENSP_id -> UniProt_id mapping through UniProt's REST API, saving as "
                    "a .csv file with column names: [ensp_id, uniprot_id]"
    )

    parser.add_argument("text_file", type=str, help="name of StringDB Protein Links .txt file")

    args = parser.parse_args()

    protein_link_csv = text_to_csv(args.text_file)

    get_uniprot_id_mappings(protein_link_csv)


if __name__ == '__main__':
    main()

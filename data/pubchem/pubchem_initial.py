# -*- coding: utf-8 -*-
"""
@author Daniel Margolis
"""

import pubchempy as pc
import pandas as pd
import urllib
import json

compounds = pd.DataFrame(columns = ['name', 'cid', 'aids', 'link'])
link = "https://pubchem.ncbi.nlm.nih.gov/compound/"
for i in range(1,3000):
    try:
        c = pc.get_compounds(i)[0]
        compounds = compounds.append({'name':c.synonyms[0], 'cid':c.cid, 'aids':c.aids, 'link':link + str(i)}, ignore_index=True)
    except Exception:
        pass
compounds.to_csv("compounds.csv")

global aids
aids = set()
compounds = pd.read_csv("compounds.csv")
for index, value in compounds['aids'].iteritems():
    val2 = value.split('[')[1].split(']')[0]
    for aid in val2.split(','):
        aid2 = aid.split()
        if aid2 != [''] and aid2 != []:
            aids |= set(aid2)
            
link = "https://pubchem.ncbi.nlm.nih.gov/bioassay/"
df = pd.DataFrame(columns= ['Name', 'AID', 'desc', 'results', 'revision', 'link'])

for i in aids:
    try:
        c = pc.Assay.from_aid(int(i))
        '''
        name        -> The short assay name, used for display purposes.
        aid         -> The PubChem Substance Idenfitier (SID).
        description -> Description
        results     -> A list of dictionaries containing details of the results from this Assay.
        target      -> A list of dictionaries containing details of the Assay targets.
        revision    -> Revision identifier for textual description.

        '''
    #         row_df = pd.DataFrame([c.name, c.aid, c.description, c.results, c.target, c.revision])
    #         print(row_df)
    #         df = pd.append([[df, row_df]])
        print(i)
        df = df.append({'Name':c.name, 'AID':c.aid, 'desc':c.description, 'results':c.results,
                        'revision':c.revision, 'link':link + str(i)}, ignore_index = True)
    except:

        pass
    
genes = pd.DataFrame(columns = ['aid', 'JSON'])
for index, aid in aids.iteritems():
    print(aid)
    try:
        req  = urllib.request.Request(url="https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/" + str(aid) + 
                                  "/targets/ProteinGI,ProteinName,GeneID,GeneSymbol/json")
        response = urllib.request.urlopen(req)
        genes = genes.append({'aid':aid, 'JSON':json.load(response)}, ignore_index=True)
    except:
        pass
    
genes.to_csv('genes.csv')
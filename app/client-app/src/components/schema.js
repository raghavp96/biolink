const schema = [
    {
        entityType: "gene",
        propertiesOfImportance: [
            "geneName", "geneId"
        ],
        nameKey: "geneName"
    },
    {
        entityType: "disease",
        propertiesOfImportance: [
            "diseaseName", "diseaseId"
        ],
        nameKey: "diseaseName"
    },
    {
        entityType: "compound",
        propertiesOfImportance: [
            "name", "link"
        ],
        nameKey: "name"
    },
    {
        entityType: "assay",
        propertiesOfImportance: [
            "Name", "link", "desc"
        ],
        nameKey: "Name"
    }
]

export default schema

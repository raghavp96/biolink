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
        entityType: "protein",
        propertiesOfImportance: [
            "proteinName", "proteinId"
        ],
        nameKey: "proteinName"
    }
]

export default schema
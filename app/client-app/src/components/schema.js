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
            "ensp_id"
        ],
        nameKey: "ensp_id"
    }
]

export default schema
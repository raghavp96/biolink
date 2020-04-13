schema = [
    {
        "entityType" : "Gene",
        "entityIdKey" : "geneId",
        "entityNameKey" : "geneName",
        "properties" : [
            "geneDPI",
            "geneDSI",
            "geneId",
            "genePLI"
        ],
        "relationships" : [
            {
                "NeighborType" : "Disease",
                "NeighborNameKey" : "diseaseName",
                "RelationName" : "AssociatesWith",
                "FromNode" : "Gene"
            }
        ]
    },
    {
        "entityType" : "Disease",
        "entityIdKey" : "diseaseId",
        "entityNameKey" : "diseaseName",
        "properties" : [
            "diseaseType"
        ],
        "relationships" : [
            {
                "NeighborType" : "Gene",
                "NeighborNameKey" : "geneName",
                "RelationName" : "AssociatesWith",
                "FromNode" : "Gene"
            }
        ]
    },
    {
        "entityType" : "Protein",
        "entityIdKey" : "ensp_id",
        "entityNameKey" : "ensp_id",
        "properties" : [],
        "relationships" : [
            {
                "NeighborType" : "Protein",
                "NeighborNameKey" : "ensp_id",
                "RelationName" : "InteractsWith",
                "FromNode" : "Protein",
                "ScoreAttribute" : "combined_score",
                "RelationshipType" : "bidirectional"
            },
            {
                "NeighborType" : "Gene",
                "NeighborNameKey" : "geneName",
                "RelationName" : "EncodesFor",
                "FromNode" : "Gene",
                "RelationshipDirection" : "incoming"
            }
        ]
    }
]
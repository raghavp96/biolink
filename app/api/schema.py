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
                "FromNode" : "Gene",
                "ScoreName" : "score"
            },
            {
                "NeighborType" : "Protein",
                "NeighborNameKey" : "ensp_id",
                "RelationName" : "EncodesFor",
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
                "FromNode" : "Gene",
                "ScoreName" : "score"
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
                "ScoreName" : "combined_score",
                "AcceptableAssociationScore" : 975
            },
            {
                "NeighborType" : "Gene",
                "NeighborNameKey" : "geneName",
                "RelationName" : "EncodesFor",
                "FromNode" : "Gene"
            }
        ]
    }
]
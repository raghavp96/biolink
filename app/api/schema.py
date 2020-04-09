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
        "entityType" : "Compound",
        "entityIdKey" : "cid",
        "entityNameKey" : "name",
        "properties" : [
            "link"
        ],
        "relationships" : [
            {
                "NeighborType" : "Assay",
                "NeighborNameKey" : "Name",
                "RelationName" : "TestsFor",
                "FromNode" : "Compound"
            }
        ]
    },
    {
        "entityType" : "Assay",
        "entityIdKey" : "AID",
        "entityNameKey" : "Name",
        "properties" : [
            "link",
            "desc"
        ],
        "relationships" : [
            {
                "NeighborType" : "Gene",
                "NeighborNameKey" : "geneName",
                "RelationName" : "InteractsWith",
                "FromNode" : "Assay"
            }
        ]
    }
]

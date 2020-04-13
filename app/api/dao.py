from db import DB
import schema as config

class EntityDao(object):

    def __init__(self, entityType):
        self.dbq = DB()
        self.schema = None
        for schema in config.schema:
            if schema["entityType"] == entityType:
                self.schema = schema


    def getEntities(self, page):
        entityType = self.schema["entityType"]
        entityIdKey = self.schema["entityIdKey"]
        entityNameKey = self.schema["entityNameKey"]

        entities = self.dbq.queryDB_Entities(
            entityType=entityType,
            entityIdKey=entityIdKey,
            entityNameKey=entityNameKey,
            page=page)

        info = {
            "Entities" : [],
            "Page" : page
        }

        for ent in entities:
            obj = {
                entityIdKey : ent[entityIdKey],
                entityNameKey : ent[entityNameKey],
            }

            for prop in self.schema["properties"]:
                obj[prop] = ent[prop]

            info["Entities"].append(obj)

        return info
        

    def getEntityInfo(self, entityName):
        info = {
            "EntityName" : entityName,
            "Neighbors" : {},
            "Related" + self.schema["entityType"] : {}
        }

        for rel in self.schema["relationships"]:
            neighborType = rel["NeighborType"]
            neighborNameKey = rel["NeighborNameKey"]
            fromNode = rel["FromNode"]


            info["Neighbors"][neighborType] = self.dbq.queryDB_Neighbors(
                entityType=self.schema["entityType"], 
                entityNameKey=self.schema["entityNameKey"], 
                entityName=entityName, 
                relationship_details=rel,
                acceptable_association_score=rel.get("AcceptableAssociationScore", 0.5))
            info["Related" + self.schema["entityType"]]["RelatedBy" + neighborType] = self.dbq.queryDB_SimilarByNeighbor(
                entityType=self.schema["entityType"], 
                entityNameKey=self.schema["entityNameKey"], 
                entityName=entityName, 
                relationship_details=rel,
                acceptable_association_score=rel.get("AcceptableAssociationScore", 0.5))

        return info


    def searchEntities(self, entityValue):
        entityType = self.schema["entityType"]
        entityIdKey = self.schema["entityIdKey"]
        entityNameKey = self.schema["entityNameKey"]

        info = {
            "Entities" : []
        }


        for keyName in [entityIdKey, entityNameKey]:

            try: 
                entities = self.dbq.queryDB_EntitiesFilter(
                    entityType=entityType,
                    entityKey=keyName,
                    entityValue=entityValue)

                for ent in entities:
                    obj = {
                        entityIdKey: ent[entityIdKey],
                        entityNameKey: ent[entityNameKey],
                    }
                    
                    for prop in self.schema["properties"]:
                        obj[prop] = ent[prop]
                        
                    info["Entities"].append(obj)
            except ValueError:
                continue

        return info

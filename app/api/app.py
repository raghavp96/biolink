from flask import Flask, jsonify, request
from flask_cors import CORS
import simplejson
import json

from dao import EntityDao

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    info = {}
    return jsonify(info)


@app.route('/<node>', methods=['GET'])
def getNodes(node):
    page = 0
    if "page" in request.args:
        page = int(request.args.get("page"))

    if node == "gene":
        dao = EntityDao("Gene")
    elif node == "disease":
        dao = EntityDao("Disease")
    elif node == "protein":
        dao = EntityDao("Protein")
        # TODO returning dummy data for now
        test_protein_info = {
            "Entities": [
                {
                    "proteinId": 1,
                    "proteinName": "Protein 1"
                },
                {
                    "proteinId": 2,
                    "proteinName": "Protein Numbah 2"
                }
            ],
            "Page": page
        }
        return jsonify(test_protein_info)
    else:
        return jsonify({})
    entities = dao.getEntities(page)
    print(entities)
    return jsonify(dao.getEntities(page))


@app.route('/<node>/<nodeName>', methods=['GET'])
def getNodeDetails(node, nodeName):
    if node == "gene":
        dao = EntityDao("Gene")
    elif node == "disease":
        dao = EntityDao("Disease")
    elif node == "protein":
        return jsonify({
            'test': 'hello world'
        })
    else:
        return jsonify({})

    return jsonify(dao.getEntityInfo(nodeName))


@app.route('/search', methods=['GET'])
def searchNodes():
    import schema as config
    resp = {}
    nodeVal = ""
    if "nodeVal" in request.args:
        nodeVal = request.args.get("nodeVal")

        # TODO fix this later, this is just going to return dummy data
        if nodeVal == "protein":
            test_protein_info = [
                {
                    "proteinId": 1,
                    "proteinName": "Protein 1"
                },
                {
                    "proteinId": 2,
                    "proteinName": "Protein Numbah 2"
                }
            ]

            return jsonify(test_protein_info)

        for entity_schema in config.schema:
            dao = EntityDao(entity_schema["entityType"])
            resp[entity_schema["entityType"]] = dao.searchEntities(nodeVal)
    
    return jsonify(resp)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
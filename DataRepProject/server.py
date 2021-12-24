from flask import Flask, url_for, request, redirect, abort, jsonify
from partDao import partDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"
#get all



@app.route('/Equipment')
def getAll():
    return jsonify(partDAO.getAll())
# find By id


@app.route('/Equipment/<int:part_ID>')
def findById(part_ID):
    return jsonify(partDAO.findByID(part_ID))


# create
# curl -X POST -d "{\"part_name\":\"test\", \"checkedInBy\":\"some guy\", \"quantity\":123}" http://127.0.0.1:5000/ Equipment


@app.route('/Equipment', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    
    part = {
        "part_ID": request.json["part_ID"],
        "part_name": request.json["part_name"],
        "checkedInBy": request.json["checkedInBy"],
        "quantity": request.json["quantity"]
    }
    return jsonify(partDAO.create(part))

    return "served by Create "

#update
# curl -X PUT -d "{\"part_name\":\"new part_name\", \"quantity\":999}" -H "content-type:application/json" http://127.0.0.1:5000/ Equipment/1

@app.route('/Equipment/<int:part_ID>', methods=['PUT'])
def update(part_ID):
    foundpart = partDAO.findByID(part_ID)
    print(foundpart)
    if foundpart == {}:
        return jsonify({}), 404
    currentpart = foundpart
    if 'part_name' in request.json:
        currentpart['part_name'] = request.json['part_name']
    if 'checkedInBy' in request.json:
        currentpart['checkedInBy'] = request.json['checkedInBy']
    if 'quantity' in request.json:
        currentpart['quantity'] = request.json['quantity']
    partDAO.update(currentpart)

    return jsonify(currentpart)

#delete
# curl -X DELETE http://127.0.0.1:5000/ Equipment/1
@app.route('/Equipment/<int:part_ID>', methods=['DELETE'])
def delete(part_ID):
    partDAO.delete(part_ID)
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)
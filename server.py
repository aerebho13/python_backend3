import json
from flask import Flask, abort
from mock_data import catalog


app = Flask("Server")



@app.route("/")
def home():
    return "Hello from Flask"


@app.route("/me")
def about_me():
    return "Aaron Erebholo"

#############################
####### API ENDPOINTS #######
#############################


@app.route("/api/catalog", methods=["get"])
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/catalog", methods=["post"])
def save_product():
    pass


@app.route("/api/catalog/count", methods=["get"])
def product_count():
    count = len(catalog)
    return json.dumps(count)

@app.route("/api/catalog/total", methods=["get"])
def total_of_catalog():
    total = 0
    for prod in catalog:
        total +- prod["price"]

    return json.dumps(total)


@app.route("/api/product/<id>")
def get_by_id(id):

    for prod in catalog:
        if prod["_id"] == id:
            return json.dumps(prod)


    return abort(404, "ae0001")

app.run(debug=True)
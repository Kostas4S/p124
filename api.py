import json
from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        "ID":1,
        "Title":u"buy groceries",
        "Description":u"Milk,Cheese,Bread,Lettuce",
        "Done":False
    },{
        "ID":2,
        "Title":u"Learn Python",
        "Description":u"Command Prompt,For loop",
        "Done":False 
    }]
    
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please Provide The Data"
        },400)
    task = {
        "ID":tasks[-1]["ID"]+1,
        "Title":request.json["Title"],
        "Description":request.json.get("Description",""),
        "Done":False
    }
    tasks.append(task)    
    return jsonify({
        "status":"Success",
        "message":"Task Added Successfully"
    })
    
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if(__name__ == "__main__"):
    app.run(debug = True)



        



from flask import Flask , redirect , request , jsonify
from flask_cors import CORS
from pymongo import MongoClient

client = MongoClient("mongodb+srv://sriram65raja:1324sriram@cluster0.dejys.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['ai']
CLOUDFLARE_URLS = db['CLOUDFLARE_URLS']

app = Flask(__name__)
CORS(app)

@app.route('/get-url')
def Get_url():
    gets = CLOUDFLARE_URLS.find({}).sort("_id" , -1).limit(1)
    for i in gets:  
     i["_id"] = str(i["_id"])
     return i

@app.route("/post-url")
def Post_url():
    d = request.args.get("url")
    
    data = {
        "url":d
    }
    
    CLOUDFLARE_URLS.insert_one(data)
    return jsonify({"Suess":"yes"})


if __name__ == "__main__":
    app.run(debug=True)

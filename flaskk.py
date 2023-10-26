from flask import Flask, render_template, request,jsonify
from main import VideoCheck
import os
import pymongo

app = Flask(__name__)




@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def index():
    return render_template('app.html')

@app.route('/SMV')
def SMV():
    return render_template('result.html')

mongodb_url = "mongodb://localhost:27017/"
database = "ergonomics"
collection = "values"

client = pymongo.MongoClient(mongodb_url)
db = client[database]
collection = db[collection]


@app.route('/get_mongodb_data', methods=['GET'])
def get_mongodb_data():
    # Retrieve MongoDB data here
    collection = db["values"]
    data_from_db = list(collection.find())
    # Return data as JSON
    return jsonify(data_from_db)
#for the manual id
next_id = 1
#get the values of the data
@app.route('/', methods=["GET", "POST"])
# id manual change
def show_output():
   global next_id

   highest_id = collection.find_one(sort=[("_id", pymongo.DESCENDING)])

   if highest_id is None:
       next_id = 1  # If the collection is empty, start with 1
   else:
       next_id = highest_id["_id"] + 1
#request method for the video
   if request.method == "POST":
        #searchterm = request.form.get("file")
        #file check
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return 'No selected file'
        filename = file.filename
        #file path analysis
        file.save(os.path.join(app.root_path, 'static/videos', filename))
        #path finder for the video and analysis
        getdatas=VideoCheck("static/videos/"+filename)
        username = request.form.get('value1')
        data_to_insert = {
            "username":username,
                "_id": next_id,
                "tony": getdatas["tony"],
                "caption": getdatas["caption"],
                "miller": getdatas["miller"],
                "lp": getdatas["lp"],
                "wanda": getdatas["wanda"],
                "hulk": getdatas["hulk"],
                "panther": getdatas["panther"],
                "lg": getdatas["lg"],
                "clr": getdatas["clr"],
                'value1': request.form.get('value1'),
                'value2': request.form.get('value2'),
                'value3': request.form.get('value3'),
                'value4': request.form.get('value4'),
                'value5': request.form.get('value5'),
                'value6': request.form.get('value6'),
                'value7': request.form.get('value7'),
                'value8': request.form.get('value8'),
                'value9': request.form.get('value9'),
            }

        # Insert the dictionary into the MongoDB collection
        collection.insert_one(data_to_insert)

        next_id += 1
        #values were return for the re analysis
        #return render_template('app.html', output=output, out=out, leg=leg, grade=grade, upp=upp, low=low, wri=wri, gra=gra, final=final)
        output = getdatas["tony"]
        out = getdatas["caption"]
        leg = getdatas["miller"]
        grade = getdatas["lp"]
        upp = getdatas["wanda"]
        low = getdatas["hulk"]
        wri = getdatas["panther"]
        gra = getdatas["lg"]
        final = getdatas["clr"]

        return render_template('app.html', output=output, out=out, leg=leg, grade=grade, upp=upp, low=low, wri=wri,
                               gra=gra, final=final)
   else:
       return render_template('app.html', output="", out="", leg="", grade="", upp="", low="", wri="", gra="",
                           final="")

#id for the manual input
@app.route('/result', methods=['POST'])
def show_result():
    data_from_db = collection.find()

    # Pass the fetched data to the HTML template
    return render_template('result.html', data_from_db=data_from_db)

# @app.route('/display_data', methods=['GET'])
# def display_data():
#     data =collection.find()
#     # print(data)# Retrieve data from MongoDB collection
#     return render_template('result.html', data_from_db=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
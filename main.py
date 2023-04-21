from flask import Flask, render_template,request,redirect,url_for,jsonify,session
import geopandas
import controllerModule as cm
import json

app = Flask(__name__)



@app.route('/')
def home():            
    #session['userName'] = "Please Login"
    return render_template("index.html")

@app.route('/map')
def displayMap():
    boundaries = []
    try:
        username = session["userName"]
    except:
        username = "please login asasa"
    try:
        path = session["path"]
    except:
        path = [1]
        
    featureArr = json.loads(gdf)
    
    for x in range (len(featureArr["features"])):
        if featureArr["features"][x]["properties"]["userName"] == username:
            boundaries.append(featureArr["features"][x])
            
    boundaries = json.dumps(boundaries)
    
    #path = jsonify(path)
    return render_template("map.html", boundaries=boundaries, path=path, username=username)

@app.route('/mapAuth' , methods = ["post"])
def displayMapAuth():
    session['userName'] = "init"
    username = request.form['userName']
    if username != session["userName"]:
        session["path"] = [1]
    session['userName'] = username
    #path = [1]
    #path = jsonify(path)
    #return render_template("map.html", boundaries=gdf, path=path, username=username)
    return redirect("/map")


@app.route('/about')
def displayAbout():            
    return render_template("about.html")

@app.route('/requestPath', methods = ["post"])
def requestPath():
    username = session["userName"]
    startNodeStr = request.form['stNode']
    targetNodeStr = request.form['tgtNode']

    startNodeArr = startNodeStr.split(",")
    targetNodeArr = targetNodeStr.split(",")
    startNode = [float(startNodeArr[1]), float(startNodeArr[0])]
    targetNode = [float(targetNodeArr[1]), float(targetNodeArr[0])]
    path = cm.getRoute(startNode, targetNode, username)
    session['path'] = path
    #return render_template("map.html", boundaries=gdf, path=path)
    return redirect("/map")

if __name__ == "__main__":
    
    gdf = geopandas.read_file("propertyDetails.geojson").to_json()
    #gdf2 = geopandas.read_file("propertyDetails.geojson")
    app.secret_key = 'super secret key s'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)

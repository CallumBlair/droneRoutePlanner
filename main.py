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
    gdf = geopandas.read_file("propertyDetails.geojson").to_json()
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
    node1Arr = request.form['1Node'].split(",")
    node2Arr = request.form['2Node'].split(",")
    node3Arr = request.form['3Node'].split(",")
    node4Arr = request.form['4Node'].split(",")
    
    #return str(node4Arr)

    if(node1Arr == ["undefined"]):
        node1Arr = [0,0]

    if(node2Arr == ["undefined"]):
        node2Arr = [0,0]

    if(node3Arr == ["undefined"]):
        node3Arr = [0,0]

    if(node4Arr == ["undefined"]):
        node4Arr = [0,0]

    
    startNodeArr = startNodeStr.split(",")
    targetNodeArr = targetNodeStr.split(",")

    
    startNode = [float(startNodeArr[1]), float(startNodeArr[0])]
    targetNode = [float(targetNodeArr[1]), float(targetNodeArr[0])]
    
    node1 = [float(node1Arr[1]), float(node1Arr[0])]
    node2 = [float(node2Arr[1]), float(node2Arr[0])]
    node3 = [float(node3Arr[1]), float(node3Arr[0])]
    node4 = [float(node4Arr[1]), float(node4Arr[0])]
    
    path = cm.getRoute(startNode, targetNode, username, node1, node2, node3, node4)
    session['path'] = path
    #return(str(path))
    #return render_template("map.html", boundaries=gdf, path=path)
    return redirect("/map")

if __name__ == "__main__":
    
    gdf = geopandas.read_file("propertyDetails.geojson").to_json()
    #gdf2 = geopandas.read_file("propertyDetails.geojson")
    app.secret_key = 'super secret key s'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)

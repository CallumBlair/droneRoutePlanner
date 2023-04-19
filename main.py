from flask import Flask, render_template,request,redirect,url_for,jsonify
import geopandas
import controllerModule as cm

app = Flask(__name__)



@app.route('/')
def home():            
    
    return render_template("index.html")

@app.route('/map')
def displayMap():
    path = [1]
    #path = jsonify(path)
    return render_template("map.html", boundaries=gdf, path=path)


@app.route('/about')
def displayAbout():            
    return render_template("about.html")

@app.route('/requestPath', methods = ["post"])
def requestPath():
    startNodeStr = request.form['stNode']
    targetNodeStr = request.form['tgtNode']

    startNodeArr = startNodeStr.split(",")
    targetNodeArr = targetNodeStr.split(",")
    startNode = [float(startNodeArr[1]), float(startNodeArr[0])]
    targetNode = [float(targetNodeArr[1]), float(targetNodeArr[0])]
    path = cm.getRoute(startNode, targetNode)
    return render_template("map.html", boundaries=gdf, path=path)

if __name__ == "__main__":
    
    gdf = geopandas.read_file("propertyDetails.geojson").to_json()
    
    app.run(debug=True)

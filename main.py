from flask import Flask, render_template,request,redirect,url_for
import geopandas
app = Flask(__name__)

@app.route('/')
def home():            
    return render_template("test.html", boundaries=gdf)


if __name__ == "__main__":
    
    gdf = geopandas.read_file("dorsetUrbanAreas.geojson").to_json()
    
    app.run(debug=True)


# Drone Route Planner

This project aims to create an artefact that will aid farmers planning on utilizing drones within their farm. The artefact aims to use an adaptive routing algorithm that will allow farms to create a route avoiding areas within their property.

It requires the following python modules:

Flask

GeoPandas

These can be installed with pip. 





## Usage

To utilize this artefact please navigate to the map page (/map) from here you can access a pre-created property by entering either "Test1" or "Test2" in the username slot. 

Following this please open the side bar by clicking the 3 horizontal lines to the left of the screen.

To create a route please click a spot within the property but not withing a obstacle and then select "Set start node", select another spot and select "Set target node".

After you are happy with the two nodes you may select "Request Route" to request a route between the 2 selected nodes. 

After a few seconds a red line shall apear. 

You can include more stops within the route by selecting "Add stop to route" and you can remove a current created path by selecting "Remove currently displayed line".

## Deployment

To deploy this project run main.py.


## Authors

- [@CallumBlair](https://github.com/CallumBlair/)


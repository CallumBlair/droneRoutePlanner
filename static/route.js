function setStart() {
    /*  setStart
        sets the starting node to the current marker placed on the map
    */
    if(previewLine){
        previewLine.remove(map)
                
    }
    if(currentLocation.length == 0){
        document.getElementById("startNode").innerHTML = "Unselected";
        document.getElementById("startButton").innerHTML = "Please select start again";
        map.removeLayer(startMarker);

    }else{
        document.getElementById("startNode").innerHTML = currentLocation;
        document.getElementById("startButton").innerHTML = "Set start node";
        startingNode = currentLocation
        if(startMarker){
            map.removeLayer(startMarker);
        }
                
        startMarker = new L.marker(currentLocation, {icon: startIcon}).addTo(map);
        map.removeLayer(marker);
        if(startMarker && marker1){
            previewLine = new L.Polyline([startMarker.getLatLng(), marker1.getLatLng()], {
                color: "purple",
                    weight: 3,})
            previewLine.addTo(map)
        }else if(startMarker && targetMarker){
            previewLine = new L.Polyline([startMarker.getLatLng(), targetMarker.getLatLng()], {
                color: "purple",
                    weight: 3,})
            previewLine.addTo(map)
        }

    }
    currentLocation = []
}

function setStop1() {
    /*  setStop1
        sets the stop1 node to the current marker placed on the map
    */
    if(startMarker){
        if(previewLine1){
            previewLine1.remove(map)
                    
        }
        if(previewLine){
            previewLine.remove(map)
        }
        if(currentLocation.length == 0){
            document.getElementById("stop1Node").innerHTML = "Unselected";
            document.getElementById("stop1Button").innerHTML = "Please select target again";
            map.removeLayer(targetMarker);
        }else{
            document.getElementById("stop1Node").innerHTML = currentLocation;
            document.getElementById("stop1Button").innerHTML = "Set target node";
            if(marker1){
                map.removeLayer(marker1);
            }
            marker1 = new L.marker(currentLocation, {icon: oneIcon}).addTo(map);
            map.removeLayer(marker);
            if(marker1 && marker2){
                previewLine1 = new L.Polyline([marker1.getLatLng(), marker2.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine1.addTo(map)
            }else if(marker1 && targetMarker){
                previewLine1 = new L.Polyline([marker1.getLatLng(), targetMarker.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine1.addTo(map)
            }

            if(startMarker && marker1){
                previewLine = new L.Polyline([startMarker.getLatLng(), marker1.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine.addTo(map)
            }
            targetedNode = currentLocation
                    
            node1 = currentLocation
        }
        currentLocation = []
    }else{
        alert("Please place a start point")
    }
}


function setStop2() {
    /*  setStop2
        sets the stop2 node to the current marker placed on the map
    */
    if(marker1){
        if(previewLine2){
            previewLine2.remove(map)
        }
        if(previewLine1){
            previewLine1.remove(map)
        }
        if(currentLocation.length == 0){
            document.getElementById("stop2Node").innerHTML = "Unselected";
            document.getElementById("stop2Button").innerHTML = "Please select target again";
            map.removeLayer(targetMarker);
        }else{
            document.getElementById("stop2Node").innerHTML = currentLocation;
            document.getElementById("stop2Button").innerHTML = "Set target node";
            if(marker2){
                map.removeLayer(marker2);
            }
            marker2 = new L.marker(currentLocation, {icon: twoIcon}).addTo(map);
            map.removeLayer(marker);
            if(marker2 && marker3){
                previewLine2 = new L.Polyline([marker2.getLatLng(), marker3.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine2.addTo(map)
            }else if(marker2 && targetMarker){
                previewLine2 = new L.Polyline([marker2.getLatLng(), targetMarker.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine2.addTo(map)
            }

            if(marker1 && marker2){
                previewLine1 = new L.Polyline([marker1.getLatLng(), marker2.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine1.addTo(map)
            }

            node2 = currentLocation
        }
        currentLocation = []
    }else{
        alert("Please place the previous node")
    }
}


function setStop3() {
    /*  setStop3
        sets the stop3 node to the current marker placed on the map
    */
    if(marker2){
        if(previewLine3){
            previewLine3.remove(map)
        }
        if(previewLine2){
            previewLine2.remove(map)
        }
        if(currentLocation.length == 0){
            document.getElementById("stop3Node").innerHTML = "Unselected";
            document.getElementById("stop3Button").innerHTML = "Please select target again";
            map.removeLayer(targetMarker);
        }else{
            document.getElementById("stop3Node").innerHTML = currentLocation;
            document.getElementById("stop3Button").innerHTML = "Set target node";
            if(marker3){
                map.removeLayer(marker3);
            }
            marker3 = new L.marker(currentLocation, {icon: threeIcon}).addTo(map);
            map.removeLayer(marker);
            if(marker3 && marker4){
                previewLine3 = new L.Polyline([marker3.getLatLng(), marker4.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine3.addTo(map)
            }else if(marker3 && targetMarker){
                previewLine3 = new L.Polyline([marker3.getLatLng(), targetMarker.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine3.addTo(map)
            }

            if(marker2 && marker3){
                previewLine2 = new L.Polyline([marker2.getLatLng(), marker3.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine2.addTo(map)
            }

            node3 = currentLocation
        }
        currentLocation = []
    }else{
        alert("Please place the previous node")
    }
}


function setStop4() {
    /*  setStop4
        sets the stop4 node to the current marker placed on the map
    */
    if(marker3){
        if(previewLine4){
            previewLine4.remove(map)  
        }
        if(previewLine3){
            previewLine3.remove(map)
        }
        if(currentLocation.length == 0){
            document.getElementById("stop4Node").innerHTML = "Unselected";
            document.getElementById("stop4Button").innerHTML = "Please select target again";
            map.removeLayer(targetMarker);
        }else{
            document.getElementById("stop4Node").innerHTML = currentLocation;
            document.getElementById("stop4Button").innerHTML = "Set target node";
            if(marker4){
                map.removeLayer(marker4);
            }
            marker4 = new L.marker(currentLocation, {icon: fourIcon}).addTo(map);
            map.removeLayer(marker);
            if(marker4 && targetMarker){
                previewLine4 = new L.Polyline([marker4.getLatLng(), targetMarker.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine4.addTo(map)
            }

            if(marker3 && marker4){
                previewLine3 = new L.Polyline([marker3.getLatLng(), marker4.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine3.addTo(map)
            }


            node4 = currentLocation
        }
        currentLocation = []
    }else{
        alert("Please place the previous node")
    }
}

function setTarget() {
    /*  setTarget
        sets the target node to the current marker placed on the map
    */
    if((stopCounter == 0 && startMarker)||(stopCounter == 1 && marker1)||(stopCounter == 2 && marker2)||(stopCounter == 3 && marker3)||(stopCounter == 4 && marker4)){
        if(currentLocation.length == 0){
            document.getElementById("targetNode").innerHTML = "Unselected";
            document.getElementById("targetButton").innerHTML = "Please select target again";
            map.removeLayer(targetMarker);
        }else{
            document.getElementById("targetNode").innerHTML = currentLocation;
            document.getElementById("targetButton").innerHTML = "Set target node";
            if(targetMarker){
                map.removeLayer(targetMarker);
            }
            targetMarker = new L.marker(currentLocation, {icon: defaultIcon}).addTo(map);
            map.removeLayer(marker);
            if(marker4 && targetMarker){
                if(previewLine4){
                    previewLine4.remove(map)    
                }
                previewLine4 = new L.Polyline([marker4.getLatLng(), targetMarker.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine4.addTo(map)
            }else if(marker3 && targetMarker){
                if(previewLine3){
                    previewLine3.remove(map)    
                }
                previewLine3 = new L.Polyline([marker3.getLatLng(), targetMarker.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine3.addTo(map)
            }else if(marker2 && targetMarker){
                if(previewLine2){
                    previewLine2.remove(map)    
                }
                previewLine2 = new L.Polyline([marker2.getLatLng(), targetMarker.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine2.addTo(map)
            }else if(marker1 && targetMarker){
                if(previewLine1){
                    previewLine1.remove(map)    
                }
                previewLine1 = new L.Polyline([marker1.getLatLng(), targetMarker.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine1.addTo(map)
            }else if(startMarker && targetMarker){
                if(previewLine){
                    previewLine.remove(map)    
                }
                previewLine = new L.Polyline([startMarker.getLatLng(), targetMarker.getLatLng()], {
                    color: "purple",
                    weight: 3,})
                previewLine.addTo(map)
            }
        }



            targetedNode = currentLocation
                
        currentLocation = []
    }else{
        alert("Please ensure you have placed the previous node")
    }
}
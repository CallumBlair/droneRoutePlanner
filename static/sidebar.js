function w3_open() {
    /*  w3_open
        Opens the sidebar
     */
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("maper").style.width = "75%";
}

function w3_close() {
    /*  w3_close
        closes the sidebar
     */
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("maper").style.width = "100%";
}

function addStop(){
    /*  addStop
        adds another stop to the side bar up to a max of 4
    */
    if(stopCounter < 4){
        var nodes = ["setStop1","setStop2","setStop3","setStop4"];
        document.getElementById(nodes[stopCounter]).style.display = "block";
        stopCounter++;
    }else {
        alert("Max stops reached")
    }
}

function removeStop(){
    /*  removeStop
        removes a stop from the side bar, redrawing the preview lines that need redrawing
    */
    if(stopCounter > 0){
        stopCounter = stopCounter - 1;
    }
    var nodes = ["setStop4","setStop3","setStop2","setStop1"];
    var node2 = ["stop4Node","stop3Node","stop2Node","stop1Node"]
            
    for(let i = 0; i<nodes.length; i++) {
        if(document.getElementById(nodes[i]).style.display  == "block"){
            document.getElementById(nodes[i]).style.display = "none";
            document.getElementById(node2[i]).innerHTML = "Unselected";
            if(i==0){
                
                try{
                    previewLine3.remove(map) 
                    previewLine4.remove(map)
                    map.removeLayer(marker4);
                }catch(err){}
                node4 = [0,0];
                marker4 = undefined;
                if(targetMarker){
                    currentLocation = [targetMarker.getLatLng().lat, targetMarker.getLatLng().lng]
                    setTarget()
                }
            }else if (i==1){
                
                try{
                previewLine2.remove(map) 
                previewLine3.remove(map) 
                map.removeLayer(marker3);
                }catch(err){}

                node3 = [0,0];
                marker3 = undefined;
                if(targetMarker){
                    currentLocation = [targetMarker.getLatLng().lat, targetMarker.getLatLng().lng]
                    setTarget()
                }
            }else if(i==2){
                
                try{
                    previewLine1.remove(map) 
                    previewLine2.remove(map) 
                    map.removeLayer(marker2);
                }catch(err){}
                node2 = [0,0];
                marker2 = undefined;
                if(targetMarker){
                    currentLocation = [targetMarker.getLatLng().lat, targetMarker.getLatLng().lng]
                    setTarget()
                }
            }else if (i==3){
                
                try {
                    previewLine.remove(map);
                    previewLine1.remove(map);
                    map.removeLayer(marker1);
                }catch(err){}
                     

                node1 = [0,0];
                marker1 = undefined;
                if(targetMarker){
                    currentLocation = [targetMarker.getLatLng().lat, targetMarker.getLatLng().lng]
                    setTarget()
                }
            }
                    
            break;
        }
    }
}

function removeLine(){
    /*  removeLine
        removes the currently drawn route line from the map
    */
    line.remove(map)
    document.getElementById("removeLineDiv").style.display = "none";
    document.getElementById("requestDownload").value = "Download previous path as CSV";
    map.removeLayer(lineMarkerStart);
    map.removeLayer(lineMarkerEnd);

}


function fireRequest(){
    /*  fireRequest
        sends a post request to the flask server with the selected nodes
    */
    if(document.getElementById("startNode").innerHTML == "Unselected" || document.getElementById("targetNode").innerHTML == "Unselected"){
        alert("Ensure both start and target nodes are selected")
    }else{
        document.getElementById("stNode").value = (startingNode);
        document.getElementById("tgtNode").value = (targetedNode);
        document.getElementById("1Node").value = (node1);
        document.getElementById("2Node").value = (node2);
        document.getElementById("3Node").value = (node3);
        document.getElementById("4Node").value = (node4);

        document.getElementById("myForm").submit(); 
    }
}
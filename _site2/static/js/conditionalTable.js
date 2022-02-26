

function assignColorToTableColumn(tableId, attributeIndex){
    var tableNode = document.getElementById(tableId);
    var tBodyNode = tableNode.getElementsByTagName("tbody")[0];
    var trNodes = tBodyNode.getElementsByTagName("tr");

    var minMax = findMinMax(tableId, attributeIndex);
    //console.log("min " + minMax[0] + " " + minMax[1]);
    for(var i = 0 ; i < trNodes.length; ++i){
        var cellNode = trNodes[i].getElementsByTagName("td");

        var coef = (parseFloat(cellNode[attributeIndex].innerHTML)-minMax[0])/(minMax[1]-minMax[0]);
        cellNode[attributeIndex].style.cssText += "background-color: hsl(" + (coef*360/3.) + ", 70%, 50%);";
    }
}

function findMinMax(tableId, attributeIndex){
    var tableNode = document.getElementById(tableId);
    var tBodyNode = tableNode.getElementsByTagName("tbody")[0];
    var trNodes = tBodyNode.getElementsByTagName("tr");

    var res = [Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY];
    for(var i = 0; i < trNodes.length; ++i){
        //console.log(i + " " + res[0] + " " + res[1]);
        var cellNode = trNodes[i].getElementsByTagName("td");
        var value = parseFloat(cellNode[attributeIndex].innerHTML);
        //console.log("   check " + value);
        if(res[0] > value){
            res[0] = value;
        }
        if(res[1] < value){
            res[1] = value;
        }
    }
    return res;
}

function GetCords() { 
var inXYList='103.8471120197759,1.2777459830532'; 
var inputSR=4326;
var outputSR =3414;
var CoordConvertorObj= new CoordConvertor();
CoordConvertorObj.ConvertCoordinate(inXYList,inputSR,outputSR,showVals);
} 

function showVals(outXY) 
{
 var outputResult =outXY; 
 console.log(outputResult);
}


      // function GetCords() { 
      //   var listitem=JSON.parse(document.getElementById ("list_address").innerText);
      //   console.log(listitem);
      //   for (i=0;i<Object.keys(listitem).length;i++)
      //   {
      //   var inXYList="'"+listitem[i]['x']+","+listitem[i]['y']+"'"; 
      //   console.log(inXYList)
      //   var inputSR=3414;
      //   var outputSR =4326;
      //   var CoordConvertorObj= new CoordConvertor();
      //   CoordConvertorObj.ConvertCoordinate(inXYList,inputSR,outputSR,showVals);
      //   }
      // }
      //   function showVals(outXY) 
      //   {
      //    var outputResult =outXY; 
      //    console.log(outputResult);
      //   }


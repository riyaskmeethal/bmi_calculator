function hide_meter(){

   document.getElementById('id_meters').style.display = "none";
   document.getElementById('id_centi_meters').style.display = "none";
   document.getElementById('id_foots').style.display = "block";
   document.getElementById('id_inches').style.display = "block";
}
function  hide_foot(){

   document.getElementById('id_foots').style.display = "none";
   document.getElementById('id_inches').style.display = "none";
   document.getElementById('id_meters').style.display = "block";
   document.getElementById('id_centi_meters').style.display = "block";
}


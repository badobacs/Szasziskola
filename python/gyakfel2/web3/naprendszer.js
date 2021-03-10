function expedicio(melyik){
    document.getElementById('expediciokszovegkeret').style.display='none';
    document.getElementById('expediciokkep').src=melyik+'.jpg';
    document.getElementById('expediciokkepkeret').style.display='block';   
}

function keprejt(melyik){
  document.getElementById('expediciokkepkeret').style.display='none';
  document.getElementById('expediciokszovegkeret').style.display='block';    
}
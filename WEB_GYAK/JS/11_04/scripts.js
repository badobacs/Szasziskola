let pupil = document.querySelector(".pupil");
let lashes = document.querySelector(".lashes");

window.addEventListener("load", () =>{
    lashes.style.visibility = "hidden";
})
 
window.addEventListener("mousemove", (e) => {

    const width = window.innerWidth;
    const height = window.innerHeight;
 
    let diff = e.clientX - width/2;
    let scale = (360 / (width/2)) / 3;
    let rotateValue = 0;

    if(e.clientY < height / 2+30){
        rotateValue = e.clientX < width/2 ? ((diff*scale)-230) : ((diff*scale)-230);
     }else{
        rotateValue = e.clientX < width/2 ? ((diff*scale)+50)*-1 : ((diff*scale)-1)-50;
     }

     pupil.style.transform = `rotate(${rotateValue}deg)`;
 
});

pupil.addEventListener("mouseover", (e) => {
    e.target.style.transform = "scale(1.3)";
    lashes.style.visibility="visible";
    console.log(lashes.clientHeight);
});

pupil.addEventListener("mouseout", (e) => {
    e.target.style.transform = "scale(1)";
    lashes.style.visibility="hidden";
    
});







/*let pupil = document.querySelector(".pupil");

window.addEventListener("mousemove", function (e) {
  console.log(e.clientX, e.clientY);
  const width = window.innerWidth;
  let diff = e.clientX - width / 2;
  let scale = 360 / (width / 2) / 3;
  if (e.clientX > width / 2) {
    pupil.style.transform = `rotate(-${diff * scale + 25}deg)`;
  } else {
    pupil.style.transform = `rotate(${diff * scale * -1 - 40}deg)`;
  }
});*/







/*let pupil = document.querySelector("pupil");

window.addEventListener("mousemove", (e) => {
    const width = window.innerWidth;
    let diff = e.clientX - width / 2;
    let scale = (360/(width/2)) /3;
    let rotateValue = e.clientX > width / 2? ((diff*scale)+50)*-1:(diff*scale*-1)-50;
    pupil.style.transform = `rotate(${rotateValue}deg)`;
});*/



/*let pupil = document.querySelector("pupil");

const width = window.innerWidth;

window.addEventListener("mousemove", (e) => {
    console.log(e.clientX + " " + e.clientY);
    let diff = e.clientX - width / 2;
    if (e.clientX > width / 2) {
        pupil.style.transform = `rotate(-${(diff*scale)+30}deg)`;
    } else {
        pupil.style.transform = `rotate(${(diff*scale)*-1}deg)`;
    }
});*/

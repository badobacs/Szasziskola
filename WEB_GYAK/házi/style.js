window.addEventListener("mousemove", function (e){

 let mouseX =e.x;
 let mouseY = e.y;
 console.log(mouseX,mouseY);
 const width=window.innerWidth;
 const height=window.innerHeight;
 if (mouseX < width / 2 && mouseY < height / 2) {
     document.querySelector("#egyes").style.backgroundColor="green";
     document.querySelector("#kettes").style.backgroundColor="white";
     document.querySelector("#harmas").style.backgroundColor="white";
     document.querySelector("#negyes").style.backgroundColor="white";
 } else if(mouseX < width / 2 && mouseY < height / 2) {
    document.querySelector("#egyes").style.backgroundColor="white";
    document.querySelector("#kettes").style.backgroundColor="green";
    document.querySelector("#harmas").style.backgroundColor="white";
    document.querySelector("#negyes").style.backgroundColor="white";
} else if(mouseX < width / 2 && mouseY < height / 2) {
    document.querySelector("#egyes").style.backgroundColor="white";
    document.querySelector("#kettes").style.backgroundColor="white";
    document.querySelector("#harmas").style.backgroundColor="green";
    document.querySelector("#negyes").style.backgroundColor="white";
} else if(mouseX < width / 2 && mouseY < height / 2) {
    document.querySelector("#egyes").style.backgroundColor="white";
    document.querySelector("#kettes").style.backgroundColor="white";
    document.querySelector("#harmas").style.backgroundColor="white";
    document.querySelector("#negyes").style.backgroundColor="green";
} 
});
let x = 10;
let name = "jani";
let bool = true;


console.console.log("x értéke: " + x);
console.console.log("x tipusa: " + typeof(x));
console.console.log("name értéke: " + name);
console.console.log("ame tipusa: " + typeof(name));
console.console.log("bool értéke: " + bool);
console.console.log("bool tipusa: " + typeof(bool));
console.console.log("");
console.console.log("");

//Vezérlési szerkezetek
//Elágazások

console.console.log(x === "10");

if (x === "10") {
    console.log("A nevem Jani")
} else if (name === "Jani") {
    console.log("A nevem tényleg Jani")
} else {
    console.log("A nevem NEM Jani")
}
//ciklus

for (let i = 0; i < 10; i++) {
    console.log(i);
}

while (j < 10) {
    console.log(j);
    j++;
}
window.onload = function () {
  const name = document.querySelector("#name");
  const race = document.querySelector("#race");
  const gender = document.querySelector("#gender");
  const caste = document.querySelector("#caste");
  const charName = document.querySelector("#char-name");
  const charRace = document.querySelector("#char-race");
  const charGender = document.querySelector("#char-gender");
  const charCaste = document.querySelector("#char-caste");
  const newCharBtn = document.querySelector("#newChar");
  const charTable = document.querySelector("#charTable");

  name.addEventListener("blur", function () {
    charName.innerHTML = name.nodeValue;
  });

  name.addEventListener("input", function () {
    charRace.innerHTML = race.nodeValue;
  });

  name.addEventListener("input", function () {
    charGender.innerHTML = gender.nodeValue;
  });

  name.addEventListener("input", function () {
    charCaste.innerHTML = caste.nodeValue;
  });

  newCharBtn.addEventListener("click" function () {
    let row =charTable.insertRow(-1);
    let nameCell= row.insertCell(0);
    let genderCell = row.insertCell(1);
    let raceCell = row.insertCell(2);
    let casteCell=row.insertCell(3);
    nameCell.innerHTML=name.value;
    genderCell.innerHTML=gender.value;
    raceCell.innerHTML=race.value;
    casteCell.innerHTML=caste.value;
    charName.innerHTML="";
    charRace.innerHTML="";
    charGender.innerHTML="";
    charCaste.innerHTML="";
    document.getElementById("data-input").requestFullscreen();

  })
};

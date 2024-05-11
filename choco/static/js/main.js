// Choosing a chocolate category

let input_category_festive = document.getElementById("festive");
let input_category_standard = document.getElementById("standard");
let input_category_animals = document.getElementById("animals");
let input_category_items = document.getElementById("items");
let input_category_all = document.getElementById("all");

let div_category_festive = document.querySelector(".category_festive");
let div_category_standard = document.querySelector(".category_standard");
let div_category_animals = document.querySelector(".category_animals");
let div_category_items = document.querySelector(".category_items");

function active_category_festive() {
  input_category_festive.disabled = true;
  input_category_standard.disabled = false;
  input_category_animals.disabled = false;
  input_category_items.disabled = false;
  input_category_all.disabled = false;

  div_category_festive.style.display = "block";
  div_category_standard.style.display = "none";
  div_category_animals.style.display = "none";
  div_category_items.style.display = "none";

  input_category_festive.style.color = "grey";
  input_category_standard.style.color = "rgb(55, 55, 55)";
  input_category_animals.style.color = "rgb(55, 55, 55)";
  input_category_items.style.color = "rgb(55, 55, 55)";
  input_category_all.style.color = "rgb(55, 55, 55)";
}

function active_category_standard() {
  input_category_festive.disabled = false;
  input_category_standard.disabled = true;
  input_category_animals.disabled = false;
  input_category_items.disabled = false;
  input_category_all.disabled = false;

  div_category_festive.style.display = "none";
  div_category_standard.style.display = "block";
  div_category_animals.style.display = "none";
  div_category_items.style.display = "none";

  input_category_festive.style.color = "rgb(55, 55, 55)";
  input_category_standard.style.color = "grey";
  input_category_animals.style.color = "rgb(55, 55, 55)";
  input_category_items.style.color = "rgb(55, 55, 55)";
  input_category_all.style.color = "rgb(55, 55, 55)";
}

function active_category_animals() {
  input_category_festive.disabled = false;
  input_category_standard.disabled = false;
  input_category_animals.disabled = true;
  input_category_items.disabled = false;
  input_category_all.disabled = false;

  div_category_festive.style.display = "none";
  div_category_standard.style.display = "none";
  div_category_animals.style.display = "block";
  div_category_items.style.display = "none";

  input_category_festive.style.color = "rgb(55, 55, 55)";
  input_category_standard.style.color = "rgb(55, 55, 55)";
  input_category_animals.style.color = "grey";
  input_category_items.style.color = "rgb(55, 55, 55)";
  input_category_all.style.color = "rgb(55, 55, 55)";
}

function active_category_items() {
  input_category_festive.disabled = false;
  input_category_standard.disabled = false;
  input_category_animals.disabled = false;
  input_category_items.disabled = true;
  input_category_all.disabled = false;

  div_category_festive.style.display = "none";
  div_category_standard.style.display = "none";
  div_category_animals.style.display = "none";
  div_category_items.style.display = "block";

  input_category_festive.style.color = "rgb(55, 55, 55)";
  input_category_standard.style.color = "rgb(55, 55, 55)";
  input_category_animals.style.color = "rgb(55, 55, 55)";
  input_category_items.style.color = "grey";
  input_category_all.style.color = "rgb(55, 55, 55)";
}

function active_category_all() {
  input_category_festive.disabled = false;
  input_category_standard.disabled = false;
  input_category_animals.disabled = false;
  input_category_items.disabled = false;
  input_category_all.disabled = true;

  div_category_festive.style.display = "block";
  div_category_standard.style.display = "block";
  div_category_animals.style.display = "block";
  div_category_items.style.display = "block";

  input_category_festive.style.color = "rgb(55, 55, 55)";
  input_category_standard.style.color = "rgb(55, 55, 55)";
  input_category_animals.style.color = "rgb(55, 55, 55)";
  input_category_items.style.color = "rgb(55, 55, 55)";
  input_category_all.style.color = "grey";
}

input_category_festive.onclick = active_category_festive;
input_category_standard.onclick = active_category_standard;
input_category_animals.onclick = active_category_animals;
input_category_items.onclick = active_category_items;
input_category_all.onclick = active_category_all;

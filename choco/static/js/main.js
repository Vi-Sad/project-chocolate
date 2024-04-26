let input_category_festive = document.getElementById("festive");
let input_category_standard = document.getElementById("standard");
let input_category_animals = document.getElementById("animals");
let input_category_items = document.getElementById("items");
let input_category_all = document.getElementById("all");

let div_category_festive = document.querySelector(".category_festive");
let div_category_standard = document.querySelector(".category_standard");

function active_category_festive() {
  input_category_festive.disabled = true;
  input_category_standard.disabled = false;
  input_category_animals.disabled = false;
  input_category_items.disabled = false;
  input_category_all.disabled = false;

  div_category_festive.style.display = "block";
  div_category_standard.style.display = "none";
}

function active_category_standard() {
  input_category_festive.disabled = false;
  input_category_standard.disabled = true;
  input_category_animals.disabled = false;
  input_category_items.disabled = false;
  input_category_all.disabled = false;

  div_category_festive.style.display = "none";
  div_category_standard.style.display = "block";
}

function active_category_animals() {
  input_category_festive.disabled = false;
  input_category_standard.disabled = false;
  input_category_animals.disabled = true;
  input_category_items.disabled = false;
  input_category_all.disabled = false;

  div_category_festive.style.display = "none";
  div_category_standard.style.display = "none";
}

function active_category_items() {
  input_category_festive.disabled = false;
  input_category_standard.disabled = false;
  input_category_animals.disabled = false;
  input_category_items.disabled = true;
  input_category_all.disabled = false;

  div_category_festive.style.display = "none";
  div_category_standard.style.display = "none";
}

function active_category_all() {
  input_category_festive.disabled = false;
  input_category_standard.disabled = false;
  input_category_animals.disabled = false;
  input_category_items.disabled = false;
  input_category_all.disabled = true;

  div_category_festive.style.display = "block";
  div_category_standard.style.display = "block";
}

input_category_festive.onclick = active_category_festive;
input_category_standard.onclick = active_category_standard;
input_category_animals.onclick = active_category_animals;
input_category_items.onclick = active_category_items;
input_category_all.onclick = active_category_all;

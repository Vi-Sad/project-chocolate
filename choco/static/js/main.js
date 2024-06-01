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
let div_category_all = document.querySelector(".category_all");

function active_category_all() {
  input_category_festive.disabled = false;
  input_category_standard.disabled = false;
  input_category_animals.disabled = false;
  input_category_items.disabled = false;
  input_category_all.disabled = true;

  div_category_festive.style.display = "none";
  div_category_standard.style.display = "none";
  div_category_animals.style.display = "none";
  div_category_items.style.display = "none";
  div_category_all.style.display = "block";

  input_category_festive.style.color = "rgb(55, 55, 55)";
  input_category_standard.style.color = "rgb(55, 55, 55)";
  input_category_animals.style.color = "rgb(55, 55, 55)";
  input_category_items.style.color = "rgb(55, 55, 55)";
  input_category_all.style.color = "grey";
}

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
  div_category_all.style.display = "none";

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
  div_category_all.style.display = "none";

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
  div_category_all.style.display = "none";

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
  div_category_all.style.display = "none";

  input_category_festive.style.color = "rgb(55, 55, 55)";
  input_category_standard.style.color = "rgb(55, 55, 55)";
  input_category_animals.style.color = "rgb(55, 55, 55)";
  input_category_items.style.color = "grey";
  input_category_all.style.color = "rgb(55, 55, 55)";
}

input_category_festive.onclick = active_category_festive;
input_category_standard.onclick = active_category_standard;
input_category_animals.onclick = active_category_animals;
input_category_items.onclick = active_category_items;
input_category_all.onclick = active_category_all;

// Viewing chocolate additives (header)

let but_left = document.querySelector(".but_left");
let but_right = document.querySelector(".but_right");

let img_heart_raspberries = document.getElementById("heart_raspberries");
let img_heart_heart_nuts = document.getElementById("heart_nuts");
let img_heart_pineapple = document.getElementById("heart_pineapple");

let span_taste = document.querySelector(".taste");

let slider = 1;

function but_right_active() {
  if (slider === 1) {
    img_heart_raspberries.setAttribute(
      "src",
      "../../../media/img/heart_nuts.webp"
    );
    img_heart_heart_nuts.setAttribute(
      "src",
      "../../../media/img/heart_pineapple.webp"
    );
    img_heart_pineapple.setAttribute(
      "src",
      "../../../media/img/heart_raspberries.png"
    );
    slider = 2;
    span_taste.style.color = "rgb(156, 90, 54)";
    span_taste.innerHTML = "орехом";
  } else if (slider === 2) {
    img_heart_raspberries.setAttribute(
      "src",
      "../../../media/img/heart_pineapple.webp"
    );
    img_heart_heart_nuts.setAttribute(
      "src",
      "../../../media/img/heart_raspberries.png"
    );
    img_heart_pineapple.setAttribute(
      "src",
      "../../../media/img/heart_nuts.webp"
    );
    slider = 3;
    span_taste.style.color = "rgb(253, 196, 1)";
    span_taste.innerHTML = "ананасом";
  } else {
    img_heart_raspberries.setAttribute(
      "src",
      "../../../media/img/heart_raspberries.png"
    );
    img_heart_heart_nuts.setAttribute(
      "src",
      "../../../media/img/heart_nuts.webp"
    );
    img_heart_pineapple.setAttribute(
      "src",
      "../../../media/img/heart_pineapple.webp"
    );
    slider = 1;
    span_taste.style.color = "rgb(214, 80, 97)";
    span_taste.innerHTML = "малиной";
  }
}

function but_left_active() {
  if (slider === 1) {
    img_heart_raspberries.setAttribute(
      "src",
      "../../../media/img/heart_pineapple.webp"
    );
    img_heart_heart_nuts.setAttribute(
      "src",
      "../../../media/img/heart_raspberries.png"
    );
    img_heart_pineapple.setAttribute(
      "src",
      "../../../media/img/heart_nuts.webp"
    );
    slider = 2;
    span_taste.style.color = "rgb(253, 196, 1)";
    span_taste.innerHTML = "ананасом";
  } else if (slider === 2) {
    img_heart_raspberries.setAttribute(
      "src",
      "../../../media/img/heart_nuts.webp"
    );
    img_heart_heart_nuts.setAttribute(
      "src",
      "../../../media/img/heart_pineapple.webp"
    );
    img_heart_pineapple.setAttribute(
      "src",
      "../../../media/img/heart_raspberries.png"
    );
    slider = 3;
    span_taste.style.color = "rgb(156, 90, 54)";
    span_taste.innerHTML = "орехом";
  } else {
    img_heart_raspberries.setAttribute(
      "src",
      "../../../media/img/heart_raspberries.png"
    );
    img_heart_heart_nuts.setAttribute(
      "src",
      "../../../media/img/heart_nuts.webp"
    );
    img_heart_pineapple.setAttribute(
      "src",
      "../../../media/img/heart_pineapple.webp"
    );
    slider = 1;
    span_taste.style.color = "rgb(214, 80, 97)";
    span_taste.innerHTML = "малиной";
  }
}

but_right.onclick = but_right_active;
but_left.onclick = but_left_active;

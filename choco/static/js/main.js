// Choosing a chocolate category

let section_category_festive = document.querySelector(
  ".section_category_festive"
);
let section_category_standard = document.querySelector(
  ".section_category_standard"
);
let section_category_animals = document.querySelector(
  ".section_category_animals"
);
let section_category_items = document.querySelector(".section_category_items");
let section_category_all = document.querySelector(".section_category_all");

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

let img_category_festive = document.querySelector(".img_category_festive");
let img_category_standard = document.querySelector(".img_category_standard");
let img_category_animals = document.querySelector(".img_category_animalse");
let img_category_items = document.querySelector(".img_category_items");
let img_category_all = document.querySelector(".img_category_all");

function active_category_all() {
  div_category_festive.style.display = "none";
  div_category_standard.style.display = "none";
  div_category_animals.style.display = "none";
  div_category_items.style.display = "none";
  div_category_all.style.display = "block";

  section_category_festive.style.transform = "scale(1)";
  section_category_standard.style.transform = "scale(1)";
  section_category_animals.style.transform = "scale(1)";
  section_category_items.style.transform = "scale(1)";
  section_category_all.style.transform = "scale(1.3)";

  section_category_festive.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_standard.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_animals.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_items.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_all.style.backgroundColor = "rgb(235, 222, 215)";

  input_category_festive.style.color = "rgb(55, 55, 55)";
  input_category_standard.style.color = "rgb(55, 55, 55)";
  input_category_animals.style.color = "rgb(55, 55, 55)";
  input_category_items.style.color = "rgb(55, 55, 55)";
  input_category_all.style.color = "rgb(156, 90, 54)";
}

function active_category_festive() {
  div_category_festive.style.display = "block";
  div_category_standard.style.display = "none";
  div_category_animals.style.display = "none";
  div_category_items.style.display = "none";
  div_category_all.style.display = "none";

  section_category_festive.style.transform = "scale(1.3)";
  section_category_standard.style.transform = "scale(1)";
  section_category_animals.style.transform = "scale(1)";
  section_category_items.style.transform = "scale(1)";
  section_category_all.style.transform = "scale(1)";

  section_category_festive.style.backgroundColor = "rgb(235, 222, 215)";
  section_category_standard.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_animals.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_items.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_all.style.backgroundColor = "rgb(235, 222, 215, 0)";

  input_category_festive.style.color = "rgb(156, 90, 54)";
  input_category_standard.style.color = "rgb(55, 55, 55)";
  input_category_animals.style.color = "rgb(55, 55, 55)";
  input_category_items.style.color = "rgb(55, 55, 55)";
  input_category_all.style.color = "rgb(55, 55, 55)";
}

function active_category_standard() {
  div_category_festive.style.display = "none";
  div_category_standard.style.display = "block";
  div_category_animals.style.display = "none";
  div_category_items.style.display = "none";
  div_category_all.style.display = "none";

  section_category_festive.style.transform = "scale(1)";
  section_category_standard.style.transform = "scale(1.3)";
  section_category_animals.style.transform = "scale(1)";
  section_category_items.style.transform = "scale(1)";
  section_category_all.style.transform = "scale(1)";

  section_category_festive.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_standard.style.backgroundColor = "rgb(235, 222, 215)";
  section_category_animals.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_items.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_all.style.backgroundColor = "rgb(235, 222, 215, 0)";

  input_category_festive.style.color = "rgb(55, 55, 55)";
  input_category_standard.style.color = "rgb(156, 90, 54)";
  input_category_animals.style.color = "rgb(55, 55, 55)";
  input_category_items.style.color = "rgb(55, 55, 55)";
  input_category_all.style.color = "rgb(55, 55, 55)";
}

function active_category_animals() {
  div_category_festive.style.display = "none";
  div_category_standard.style.display = "none";
  div_category_animals.style.display = "block";
  div_category_items.style.display = "none";
  div_category_all.style.display = "none";

  section_category_festive.style.transform = "scale(1)";
  section_category_standard.style.transform = "scale(1)";
  section_category_animals.style.transform = "scale(1.3)";
  section_category_items.style.transform = "scale(1)";
  section_category_all.style.transform = "scale(1)";

  section_category_festive.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_standard.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_animals.style.backgroundColor = "rgb(235, 222, 215)";
  section_category_items.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_all.style.backgroundColor = "rgb(235, 222, 215, 0)";

  input_category_festive.style.color = "rgb(55, 55, 55)";
  input_category_standard.style.color = "rgb(55, 55, 55)";
  input_category_animals.style.color = "rgb(156, 90, 54)";
  input_category_items.style.color = "rgb(55, 55, 55)";
  input_category_all.style.color = "rgb(55, 55, 55)";
}

function active_category_items() {
  div_category_festive.style.display = "none";
  div_category_standard.style.display = "none";
  div_category_animals.style.display = "none";
  div_category_items.style.display = "block";
  div_category_all.style.display = "none";

  section_category_festive.style.transform = "scale(1)";
  section_category_standard.style.transform = "scale(1)";
  section_category_animals.style.transform = "scale(1)";
  section_category_items.style.transform = "scale(1.3)";
  section_category_all.style.transform = "scale(1)";

  section_category_festive.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_standard.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_animals.style.backgroundColor = "rgb(235, 222, 215, 0)";
  section_category_items.style.backgroundColor = "rgb(235, 222, 215)";
  section_category_all.style.backgroundColor = "rgb(235, 222, 215, 0)";

  input_category_festive.style.color = "rgb(55, 55, 55)";
  input_category_standard.style.color = "rgb(55, 55, 55)";
  input_category_animals.style.color = "rgb(55, 55, 55)";
  input_category_items.style.color = "rgb(156, 90, 54)";
  input_category_all.style.color = "rgb(55, 55, 55)";
}

section_category_festive.onclick = active_category_festive;
section_category_standard.onclick = active_category_standard;
section_category_animals.onclick = active_category_animals;
section_category_items.onclick = active_category_items;
section_category_all.onclick = active_category_all;

// Viewing chocolate additives (header)

let but_left = document.querySelector(".but_left");
let but_right = document.querySelector(".but_right");

let img_heart_raspberries = document.getElementById("heart_raspberries");
let img_heart_nuts = document.getElementById("heart_nuts");
let img_heart_pineapple = document.getElementById("heart_pineapple");

let span_taste = document.querySelector(".taste");

let slider = 1;

function but_right_active() {
  if (slider === 1) {
    slider = 2;
    span_taste.style.color = "rgb(156, 90, 54)";
    span_taste.innerHTML = "орехом";

    img_heart_raspberries.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_raspberries.setAttribute(
        "src",
        "../../../media/img/heart_nuts.webp"
      );
    }, 500);
    img_heart_raspberries.animate({ transform: "scale(1)" }, 1000);

    img_heart_nuts.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_nuts.setAttribute(
        "src",
        "../../../media/img/heart_pineapple.webp"
      );
    }, 500);
    img_heart_nuts.animate({ transform: "scale(1)" }, 1000);

    img_heart_pineapple.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_pineapple.setAttribute(
        "src",
        "../../../media/img/heart_raspberries.png"
      );
    }, 500);
    img_heart_pineapple.animate({ transform: "scale(1)" }, 1000);
  } else if (slider === 2) {
    slider = 3;
    span_taste.style.color = "rgb(253, 196, 1)";
    span_taste.innerHTML = "ананасом";

    img_heart_raspberries.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_raspberries.setAttribute(
        "src",
        "../../../media/img/heart_pineapple.webp"
      );
    }, 500);
    img_heart_raspberries.animate({ transform: "scale(1)" }, 1000);

    img_heart_nuts.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_nuts.setAttribute(
        "src",
        "../../../media/img/heart_raspberries.png"
      );
    }, 500);
    img_heart_nuts.animate({ transform: "scale(1)" }, 1000);

    img_heart_pineapple.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_pineapple.setAttribute(
        "src",
        "../../../media/img/heart_nuts.webp"
      );
    }, 500);
    img_heart_pineapple.animate({ transform: "scale(1)" }, 1000);
  } else {
    slider = 1;
    span_taste.style.color = "rgb(214, 80, 97)";
    span_taste.innerHTML = "малиной";

    img_heart_raspberries.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_raspberries.setAttribute(
        "src",
        "../../../media/img/heart_raspberries.png"
      );
    }, 500);
    img_heart_raspberries.animate({ transform: "scale(1)" }, 1000);

    img_heart_nuts.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_nuts.setAttribute("src", "../../../media/img/heart_nuts.webp");
    }, 500);
    img_heart_nuts.animate({ transform: "scale(1)" }, 1000);

    img_heart_pineapple.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_pineapple.setAttribute(
        "src",
        "../../../media/img/heart_pineapple.webp"
      );
    }, 500);
    img_heart_pineapple.animate({ transform: "scale(1)" }, 1000);
  }
}

function but_left_active() {
  if (slider === 1) {
    slider = 2;
    span_taste.style.color = "rgb(253, 196, 1)";
    span_taste.innerHTML = "ананасом";

    img_heart_raspberries.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_raspberries.setAttribute(
        "src",
        "../../../media/img/heart_pineapple.webp"
      );
    }, 500);
    img_heart_raspberries.animate({ transform: "scale(1)" }, 1000);

    img_heart_nuts.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_nuts.setAttribute(
        "src",
        "../../../media/img/heart_raspberries.png"
      );
    }, 500);
    img_heart_nuts.animate({ transform: "scale(1)" }, 1000);

    img_heart_pineapple.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_pineapple.setAttribute(
        "src",
        "../../../media/img/heart_nuts.webp"
      );
    }, 500);
    img_heart_pineapple.animate({ transform: "scale(1)" }, 1000);
  } else if (slider === 2) {
    slider = 3;
    span_taste.style.color = "rgb(156, 90, 54)";
    span_taste.innerHTML = "орехом";

    img_heart_raspberries.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_raspberries.setAttribute(
        "src",
        "../../../media/img/heart_nuts.webp"
      );
    }, 500);
    img_heart_raspberries.animate({ transform: "scale(1)" }, 1000);

    img_heart_nuts.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_nuts.setAttribute(
        "src",
        "../../../media/img/heart_pineapple.webp"
      );
    }, 500);
    img_heart_nuts.animate({ transform: "scale(1)" }, 1000);

    img_heart_pineapple.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_pineapple.setAttribute(
        "src",
        "../../../media/img/heart_raspberries.png"
      );
    }, 500);
    img_heart_pineapple.animate({ transform: "scale(1)" }, 1000);
  } else {
    slider = 1;
    span_taste.style.color = "rgb(214, 80, 97)";
    span_taste.innerHTML = "малиной";

    img_heart_raspberries.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_raspberries.setAttribute(
        "src",
        "../../../media/img/heart_raspberries.png"
      );
    }, 500);
    img_heart_raspberries.animate({ transform: "scale(1)" }, 1000);

    img_heart_nuts.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_nuts.setAttribute("src", "../../../media/img/heart_nuts.webp");
    }, 500);
    img_heart_nuts.animate({ transform: "scale(1)" }, 1000);

    img_heart_pineapple.animate({ transform: "scale(-3)" }, 1000);
    setTimeout(() => {
      img_heart_pineapple.setAttribute(
        "src",
        "../../../media/img/heart_pineapple.webp"
      );
    }, 500);
    img_heart_pineapple.animate({ transform: "scale(1)" }, 1000);
  }
}

but_right.onclick = but_right_active;
but_left.onclick = but_left_active;

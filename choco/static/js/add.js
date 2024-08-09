let but_favourites = document.getElementById("but_favourites");
let but_basket = document.getElementById("but_basket");
let form_add = document.getElementById("form_add");
let add_basket = document.getElementById("add_basket");
let add_favourites = document.getElementById("add_favourites");

let id_product = document.querySelector(".id_product").value;
let start_url = document.querySelector(".start_url").value;

function submit_basket() {
  form_add.setAttribute(
    "action",
    `${start_url}/user/chocolate/basket/add/id_product=${id_product}/`
  );
  add_basket.style.display = "block";
}

function submit_favourites() {
  form_add.setAttribute(
    "action",
    `${start_url}/user/chocolate/favourites/add/id_product=${id_product}/`
  );
}

but_basket.onclick = submit_basket;
but_favourites.onclick = submit_favourites;

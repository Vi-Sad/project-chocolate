let but_favourites = document.getElementById("but_favourites");
let but_basket = document.getElementById("but_basket");
let form_add = document.getElementById("form_add");

let user_active = document.querySelector(".user_active").value;
let id_product = document.querySelector(".id_product").value;

function submit_basket() {
  form_add.setAttribute(
    "action",
    `http://127.0.0.1:8000/user/chocolate/${user_active}/basket/add/id_product=${id_product}/`
  );
}

function submit_favourites() {
  form_add.setAttribute(
    "action",
    `http://127.0.0.1:8000/user/chocolate/${user_active}/favourites/add/id_product=${id_product}/`
  );
}

but_basket.onclick = submit_basket;
but_favourites.onclick = submit_favourites;

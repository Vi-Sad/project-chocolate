let but_favourites = document.getElementById("but_favourites");
let but_basket = document.getElementById("but_basket");
let form_add = document.getElementById("form_add");

let user_active = document.querySelector(".user_active").value;
let user_hard_id = document.querySelector(".user_hard_id").value;
let id_product = document.querySelector(".id_product").value;
let start_url = document.querySelector(".start_url").value;

function submit_basket() {
  form_add.setAttribute(
    "action",
    `${start_url}/user/chocolate/${user_active}/basket/add/id_product=${id_product}/${user_hard_id}/`
  );
}

function submit_favourites() {
  form_add.setAttribute(
    "action",
    `${start_url}/user/chocolate/${user_active}/favourites/add/id_product=${id_product}/${user_hard_id}/`
  );
}

but_basket.onclick = submit_basket;
but_favourites.onclick = submit_favourites;

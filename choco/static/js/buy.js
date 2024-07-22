let but_buy = document.getElementById("buy");
let buy_products = document.getElementById("buy_products");

function display_basket() {
  if (buy_products.style.display == "none") {
    buy_products.style.display = "block";
  } else {
    buy_products.style.display = "none";
  }
  console.log('Hello')
}

but_buy.onclick = display_basket;

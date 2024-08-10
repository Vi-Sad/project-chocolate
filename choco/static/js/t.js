let radio_square = document.getElementById("square");
let radio_heart = document.getElementById("heart");
let radio_circle = document.getElementById("circle");
let radio_triangle = document.getElementById("triangle");

let radio_milk = document.getElementById("milk");
let radio_white = document.getElementById("white");
let radio_no_sugar = document.getElementById("no_sugar");
let radio_bitter = document.getElementById("bitter");

let checkbox_raspberry = document.getElementById("raspberry");
let checkbox_pineapple = document.getElementById("pineapple");
let checkbox_strawberry = document.getElementById("strawberry");
let checkbox_nuts = document.getElementById("nuts");

let but_chocolate = document.getElementById("but_chocolate");
let but_basket = document.getElementById("but_basket");
let res_count = document.getElementById("res_count");

let all_chocolate = [radio_square, radio_heart, radio_circle, radio_triangle];
let all_basic = [radio_milk, radio_white, radio_no_sugar, radio_bitter];
let all_additives = [checkbox_raspberry, checkbox_pineapple, checkbox_strawberry, checkbox_nuts];

let message_click_price = document.getElementById("message_click_price");

let add_basket = document.getElementById("add_basket");

function res_chocolate(e) {
    e.preventDefault();
    let res_price = document.getElementById("res_price");
    let res_price_2 = document.getElementById("res_price_2");
    let count = 20;
    for (let i = 0; i < all_additives.length; i++) {
        if (all_additives[i].checked) {
            count += 10;
        };
    };
    count = count * res_count.value;
    res_price.innerHTML = `${count}₽`;
    res_price_2.value = count;
    but_basket.disabled = false;
    message_click_price.innerHTML = '';
};

but_chocolate.onclick = res_chocolate;

for (let i = 0; i < all_chocolate.length; i++) {
    all_chocolate[i].addEventListener('change', () => {
        res_price.innerHTML = "?₽";
        but_basket.disabled = true;
        message_click_price.innerHTML = 'Нажмите на кнопку "Узнать цену"';
    });
};

for (let i = 0; i < all_basic.length; i++) {
    all_basic[i].addEventListener('change', () => {
        res_price.innerHTML = "?₽";
        but_basket.disabled = true;
        message_click_price.innerHTML = 'Нажмите на кнопку "Узнать цену"';
    });
};

for (let i = 0; i < all_additives.length; i++) {
    all_additives[i].addEventListener('change', () => {
        res_price.innerHTML = "?₽";
        but_basket.disabled = true;
        message_click_price.innerHTML = 'Нажмите на кнопку "Узнать цену"';
    });
};

res_count.addEventListener('change', () => {
    res_price.innerHTML = "?₽";
    but_basket.disabled = true;
    message_click_price.innerHTML = 'Нажмите на кнопку "Узнать цену"';
});

function message_create() {
    add_basket.style.display = "block";
};

but_basket.onclick = message_create;

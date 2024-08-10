let inp_image = document.getElementById("inp_image");
let label_image = document.getElementById("label_image");
let div_image = document.querySelector(".div_image");
let src_image = document.getElementById("src_image");
let p_message_big_size = document.getElementById("message_big_size");

let image = [];

let but_update_email = document.getElementById("but_update_email");
let inp_update_email = document.getElementById("inp_update_email");
let span_update_email = document.getElementById("span_update_email");

let but_update_phone = document.getElementById("but_update_phone");
let inp_update_phone = document.getElementById("inp_update_phone");
let span_update_phone = document.getElementById("span_update_phone");

let add_image = () => {
    let file = inp_image.files[0];
    if (file.size <= 1048576) {
        if (!file) return;
        let reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            let img_image = document.getElementById("img_image");
            src_image.value = reader.result;
            img_image.src = reader.result;
            div_image.insertBefore(img_image, label_image);
        };
        image.push(file);
        label_image.innerHTML = "Заменить фото";
        p_message_big_size.innerHTML = '';
        return;
    } else {
        p_message_big_size.innerHTML = 'Выберите файл меньше 1МБ';
    }
};

inp_image.addEventListener("change", add_image);

function update_email(e) {
    if (inp_update_email.style.display == 'none') {
        e.preventDefault();
        but_update_email.innerHTML = 'Применить';
        inp_update_email.style.display = 'block';
        inp_update_email.style.width = '35%';
        span_update_email.style.display = 'none';
        but_update_email.setAttribute('type', 'submit');
    } else {
        but_update_email.innerHTML = 'Изменить эл. почту';
        inp_update_email.style.display = 'none';
        span_update_email.style.display = 'block';
    }
};

but_update_email.onclick = update_email;

function update_phone(e) {
    if (inp_update_phone.style.display == 'none') {
        e.preventDefault();
        but_update_phone.innerHTML = 'Применить';
        inp_update_phone.style.display = 'block';
        inp_update_phone.style.width = '30%';
        span_update_phone.style.display = 'none';
        but_update_phone.setAttribute('type', 'submit');
    } else {
        but_update_phone.innerHTML = 'Изменить номер телефона';
        inp_update_phone.style.display = 'none';
        span_update_phone.style.display = 'block';
    }
};

but_update_phone.onclick = update_phone;
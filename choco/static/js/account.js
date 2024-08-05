let inp_image = document.getElementById("inp_image");
let label_image = document.getElementById("label_image");
let div_image = document.querySelector(".div_image");
let src_image = document.getElementById("src_image");

let image = [];

let add_image = () => {
    let file = inp_image.files[0];
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
    return;
};

inp_image.addEventListener("change", add_image);
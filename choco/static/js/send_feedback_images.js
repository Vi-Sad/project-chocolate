let inp_feedback_image = document.getElementById("inp_feedback_image");
let label_feedback_image = document.getElementById("label_feedback_image");
let div_feedback_image = document.querySelector(".div_feedback_image");

let src_feedback_1 = document.getElementById("src_feedback_1");
let src_feedback_2 = document.getElementById("src_feedback_2");
let src_feedback_3 = document.getElementById("src_feedback_3");

let all_images = [];
let all_src_feedbacks = [src_feedback_1, src_feedback_2, src_feedback_3];
let num = -1;

let add_image = () => {
    let file = inp_feedback_image.files[0];
    if (!file) return;
    let reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => {
        let new_img = document.createElement("img");
        new_img.src = reader.result;
        div_feedback_image.insertBefore(new_img, label_feedback_image);
        all_src_feedbacks[num].value = reader.result;
    };
    if (all_images.length === 2) {
        label_feedback_image.style.display = "none";
        num += 1;
    } else {
        all_images.push(file);
        inp_feedback_image.value = "";
        num += 1;
        return;
    }
};

inp_feedback_image.addEventListener("change", add_image);
let form_feedback = document.getElementById("form_feedback");
let but_feedback = document.getElementById("but_feedback");

let user_active = document.querySelector(".user_active").value;
let id_product = document.querySelector(".id_product").value;

function send_feedback() {
  form_feedback.setAttribute(
    "action",
    `http://127.0.0.1:8000/user/feedback/${user_active}/id_product=${id_product}/`
  );
}

but_feedback.onclick = send_feedback;

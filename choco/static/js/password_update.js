let but_password_update = document.getElementById("but_password_update");
let form_password_update = document.getElementById("form_password_update");

let message = document.querySelector(".message").value;
let start_url = document.querySelector(".start_url").value;
let hard_id = document.querySelector(".hard_id").value;

function new_message_password_update() {
    if (message == 'Ваш пароль был успешно обновлен. Нажмите на кнопку "Применить" еще раз') {
        form_password_update.setAttribute(
            "action",
            `${start_url}/user/login/`
        );
    } else {
        form_password_update.setAttribute(
            "action",
            `${start_url}/user/update_password/check/${hard_id}/`
        );
    };
};

but_password_update.onclick = new_message_password_update;
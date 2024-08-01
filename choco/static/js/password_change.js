let but_password_change = document.getElementById("but_password_change");
let form_password_change = document.getElementById("form_password_change");

let but_password_update = document.getElementById("but_password_update");
let form_password_update = document.getElementById("form_password_update");

let message = document.querySelector(".message").value;
let start_url = document.querySelector(".start_url").value;

function new_message_password_change() {
    if (message == 'Ваш пароль был успешно изменен. Нажмите на кнопку "Применить" еще раз') {
        form_password_change.setAttribute(
            "action",
            `${start_url}`
        );
    } else {
        form_password_change.setAttribute(
            "action",
            `${start_url}/user/change_password/check/`
        );
    };
};

but_password_change.onclick = new_message_password_change;

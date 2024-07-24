let form_login = document.getElementById("form_login");
let but_login = document.getElementById("but_login");

let start_url = document.querySelector(".start_url").value;
let message = document.querySelector(".message").value;

function submit_login() {
    if (message == 'Вы успешно вошли. Нажмите на кнопку "Войти" еще раз') {
        form_login.setAttribute(
            "action",
            `${start_url}`
        );
    } else {
        form_login.setAttribute(
            "action",
            `${start_url}/user/login/check`
        );
    }
}

but_login.onclick = submit_login;

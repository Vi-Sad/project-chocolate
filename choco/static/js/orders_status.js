let status_0 = document.querySelector(".status_0")
let status_1 = document.querySelector(".status_1")
let status_2 = document.querySelector(".status_2")

let but_status_0 = document.querySelector(".but_status_0")
let but_status_1 = document.querySelector(".but_status_1")
let but_status_2 = document.querySelector(".but_status_2")

function active_status_0() {
    status_0.style.display = 'flex';
    status_1.style.display = 'none';
    status_2.style.display = 'none';

    but_status_0.style.backgroundColor = 'rgb(156, 90, 54)';
    but_status_0.style.color = 'white';

    but_status_1.style.backgroundColor = 'white';
    but_status_1.style.color = 'rgb(156, 90, 54)';

    but_status_2.style.backgroundColor = 'white';
    but_status_2.style.color = 'rgb(156, 90, 54)';
}

function active_status_1() {
    status_0.style.display = 'none';
    status_1.style.display = 'flex';
    status_2.style.display = 'none';

    but_status_0.style.backgroundColor = 'white';
    but_status_0.style.color = 'rgb(156, 90, 54)';

    but_status_1.style.backgroundColor = 'rgb(156, 90, 54)';
    but_status_1.style.color = 'white';

    but_status_2.style.backgroundColor = 'white';
    but_status_2.style.color = 'rgb(156, 90, 54)';
}

function active_status_2() {
    status_0.style.display = 'none';
    status_1.style.display = 'none';
    status_2.style.display = 'flex';

    but_status_0.style.backgroundColor = 'white';
    but_status_0.style.color = 'rgb(156, 90, 54)';

    but_status_1.style.backgroundColor = 'white';
    but_status_1.style.color = 'rgb(156, 90, 54)';

    but_status_2.style.backgroundColor = 'rgb(156, 90, 54)';
    but_status_2.style.color = 'white';
}

but_status_0.onclick = active_status_0;
but_status_1.onclick = active_status_1;
but_status_2.onclick = active_status_2;
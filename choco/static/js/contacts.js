let x = document.getElementById("x");
let contacts = document.getElementById("contacts");
let a_view_contacts = document.getElementById("a_view_contacts");
let a_view_contacts_2 = document.getElementById("a_view_contacts_2");

function click_x() {
    contacts.style.display = "none";
}

function click_contacts(e) {
    e.preventDefault();
    contacts.style.display = "block";
}

x.onclick = click_x;
a_view_contacts.onclick = click_contacts;
a_view_contacts_2.onclick = click_contacts;
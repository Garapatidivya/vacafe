// core/static/js/script.js
{% load static %}
document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector(".home button");
    if (button) {
        button.addEventListener("click", () => {
            alert("Thanks for visiting VA Cafe ☕");
        });
    }
});


const navSlide = ()=>{
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    // Toggle nav
    burger.addEventListener('click', ()=>{
        nav.classList.toggle('nav-active');
    });
    // Animate links
    navLinks.forEach((link, index)=>{
        link.style.animation = `navlinkfade 2s ease forwards ${index / 5 + 1.5}s`;
    });
}

navSlide();

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("active");

    /* Toggle between hiding and showing the active panel */
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}

var button = document.getElementById("submitButton");
button.addEventListener("click", refresh);

function refresh() {
    var choice = document.getElementById("js-choice");
    var content = choice.innerHTML;
    choice.innerHTML = content;
    console.log("Refreshed");
}



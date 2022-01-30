
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
        console.log(index / 7)
    });
}

navSlide();
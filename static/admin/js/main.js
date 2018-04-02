var trigger = document.getElementById("nav-trigger");

function open_nav() {
  document.getElementById("side-nav").classList.toggle('visible');
  document.getElementById('right').classList.toggle('right');
}

trigger.addEventListener("click", open_nav);





var trigger = document.getElementById("nav-trigger");

function open_nav() {
  document.getElementById("side-nav").classList.toggle('visible');
  document.getElementById('right').classList.toggle('right');
}

function updateClock() {
  var now = new Date();
  time = now.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: true });
  date = [now.getDate(),now.getMonth(),now.getFullYear()].join('/');

  document.getElementById('time').innerHTML =  date+' '+time;

   //loop
}


trigger.addEventListener("click", open_nav);

window.onload = setInterval(updateClock, 1000);





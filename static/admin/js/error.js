var starryNight = {
  container1: document.getElementById('container1'),
  container2: document.getElementById('container2'),
  container3: document.getElementById('container3'),
  containertest: document.getElementById('container4'),
  body: document.getElementsByClassName('night-background')[0],

  init: function() {

    starryNight.setStars();
    
  },

  setStars: function() {
    for (var i = 0; i < 80; i++) {
      starryNight.container1.innerHTML += "<div class='star'></div>";
      starryNight.container2.innerHTML += "<div class='star'></div>";
      starryNight.container3.innerHTML += "<div class='star'></div>";
      starryNight.containertest.innerHTML += "<div class='star'></div>";
    }
  }
}

document.addEventListener('DOMContentLoaded', starryNight.init, false);
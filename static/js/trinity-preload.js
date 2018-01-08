  function preloader(){
    document.getElementById("loading").style.display = "none";
    document.getElementById("content").style.display = "block";
    document.getElementById("animate").className += "animated slideInDown";
  }


  window.onload = preloader;
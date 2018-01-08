function open_nav() {
  document.getElementById("side-nav").classList.toggle('visible');
  document.getElementById('content').classList.toggle('right');

  console.log("nav==>open");
}

function open_modal() {
  var modal = document.getElementById('modal-test');
  modal.classList.toggle('visible');
  console.log("modal==>open");

    // listen for close request
    console.log("modal==>listen for close");
    var closeModal = document.getElementsByClassName('close-modal')[0];
    closeModal.addEventListener('click', function(){
      modal.classList.remove('visible');
      console.log("modal==>closed");
    });
  }


  document.addEventListener('DOMContentLoaded', function () {
    //listen for modal
    document.getElementById('open-modal').addEventListener('click', open_modal, false);

    // listen for nav trigger
    document.getElementById("nav-trigger").addEventListener("click", open_nav, false);
  });




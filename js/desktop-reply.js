var maria = document.querySelector(".feedback__name--maria");
var petr = document.querySelector(".feedback__name--petr");
var ark = document.querySelector(".feedback__name--ark");
var txtMaria = document.querySelector(".feedback__txt--maria");
var txtPetr = document.querySelector(".feedback__txt--petr");
var txtArk = document.querySelector(".feedback__txt--ark");

maria.addEventListener("click", function(event){
  event.preventDefault();
  txtMaria.classList.add("js-feedback-on");
  txtPetr.classList.remove("js-feedback-on");
  txtArk.classList.remove("js-feedback-on");
});

petr.addEventListener("click", function(event){
  event.preventDefault();
  txtPetr.classList.add("js-feedback-on");
  txtMaria.classList.remove("js-feedback-on");
  txtArk.classList.remove("js-feedback-on");
});

ark.addEventListener("click", function(event){
  event.preventDefault();
  txtArk.classList.add("js-feedback-on");
  txtMaria.classList.remove("js-feedback-on");
  txtPetr.classList.remove("js-feedback-on");
});

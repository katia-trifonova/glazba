var maria = document.querySelector(".feedback__name--user01");
var petr = document.querySelector(".feedback__name--user02");
var ark = document.querySelector(".feedback__name--user03");
var txtMaria = document.querySelector(".feedback__txt--user01");
var txtPetr = document.querySelector(".feedback__txt--user02");
var txtArk = document.querySelector(".feedback__txt--user03");




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

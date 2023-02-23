const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});





function ValidMail() {
  var re = /^[\w-\.]+@[\w-]+\.[a-z]{2,4}$/i;
  var myMail = document.getElementById('email').value;
  var valid = re.test(myMail);
  if (valid) output = 'Адрес эл. почты введен правильно!';
  else output = 'Адрес электронной почты введен неправильно!';
  document.getElementById('message').innerHTML = output;
  return valid;
}

function ValidPhone() {
  var re = /^[\d\+][\d\(\)\ -]{4,14}\d$/;
  var myPhone = document.getElementById('phone').value;
  var valid = re.test(myPhone);
  if (valid) output = 'Номер телефона введен правильно!';
  else output = 'Номер телефона введен неправильно!';
  document.getElementById('message').innerHTML = document.getElementById('message').innerHTML+'<br />'+output;
  return valid;
}  

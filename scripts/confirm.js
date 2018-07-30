// add later: will actually check if new object exists in database
function confirmSubmit() {
  alert("Form submitted")
};

let submitbutton = document.querySelector('#submit-button')

submitbutton.addEventListener('click', confirmSubmit());

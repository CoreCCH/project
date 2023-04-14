$('.alert').alert()

$(function (){
    window.history.replaceState(null, null, window.location.href);
})

document.getElementById("email").addEventListener('click', function(event){
    var emailError = document.getElementById('email-error');
    emailError.innerHTML = null;
});

document.getElementById('submit-btn').addEventListener('click', function(event) {
    var emailLayout = document.getElementById('email');
    var emailInput = document.getElementById('email');
    var emailError = document.getElementById('email-error');
    var email = emailInput.value;

    if (!emailIsValid(email)) {
        event.preventDefault();
        emailError.innerHTML = "Please enter a valid email address";
        emailInput.classList.add('invalid');
    } else {
        emailError.innerHTML = "";
        emailInput.classList.remove('invalid');
    }
});

function emailIsValid(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}
const alert = document.querySelector('.alert')
const closeAlert = document.querySelector('.alert__close')
//formulario
function validateInput(input) {
    switch (input.target.name) {
        case 'username':
            if (input.target.value.length > 0) {
                document.getElementsByClassName('form__label')[0].classList.add('hide')
            } else {
                document.getElementsByClassName('form__label')[0].classList.remove('hide')
            }
            break;
        case 'password':
            if (input.target.value.length > 0) {
                document.getElementsByClassName('form__label')[1].classList.add('hide')
            } else {
                document.getElementsByClassName('form__label')[1].classList.remove('hide')
            }
            break;
        case 'new_password1':
            if (input.target.value.length > 0) {
                document.getElementsByClassName('form__label')[0].classList.add('hide')
            } else {
                document.getElementsByClassName('form__label')[0].classList.remove('hide')
            }
            break;
        case 'new_password2':
            if (input.target.value.length > 0) {
                document.getElementsByClassName('form__label')[1].classList.add('hide')
            } else {
                document.getElementsByClassName('form__label')[1].classList.remove('hide')
            }
            break;
        case 'email':
            if (input.target.value.length > 0) {
                document.getElementsByClassName('form__label')[1].classList.add('hide')
            } else {
                document.getElementsByClassName('form__label')[1].classList.remove('hide')
            }
            break;  
    }
}
const form = document.getElementsByClassName('form__login')
const inputs = document.querySelectorAll('.form__input')
inputs.forEach(input => {
    input.addEventListener('blur', validateInput)
})

if (closeAlert){
    closeAlert.addEventListener('click',()=>{
      alert.classList.add('no_active')
    }
    )
  }
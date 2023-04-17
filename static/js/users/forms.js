var completeForm = false
function validateInput(input) {
    switch (input.target.name) {
        case 'name':
            if (regularExpressions.name.test(input.target.value)) {
                document.getElementsByClassName('form__container')[0].classList.add('correct')
                document.getElementsByClassName('form__container')[0].classList.remove('incorrect')
                completeForm = true
            } else {
                document.getElementsByClassName('form__container')[0].classList.remove('correct')
                document.getElementsByClassName('form__container')[0].classList.add('incorrect')
                completeForm = false
            }
            break;
        case 'last_name':
            if (regularExpressions.last_name.test(input.target.value)) {
                document.getElementsByClassName('form__container')[1].classList.add('correct')
                document.getElementsByClassName('form__container')[1].classList.remove('incorrect')
                completeForm = true
            } else {
                document.getElementsByClassName('form__container')[1].classList.remove('correct')
                document.getElementsByClassName('form__container')[1].classList.add('incorrect')
                completeForm = false
            }
            break;
        case 'user':
            if (regularExpressions.user.test(input.target.value)) {
                document.getElementsByClassName('form__container')[2].classList.add('correct')
                document.getElementsByClassName('form__container')[2].classList.remove('incorrect')
                completeForm = true
            } else {
                document.getElementsByClassName('form__container')[2].classList.remove('correct')
                document.getElementsByClassName('form__container')[2].classList.add('incorrect')
                completeForm = false
            }
            break;
        case 'password':
            if (regularExpressions.password.test(input.target.value)) {
                document.getElementsByClassName('form__container')[3].classList.add('correct')
                document.getElementsByClassName('form__container')[3].classList.remove('incorrect')
                completeForm = true
            } else {
                document.getElementsByClassName('form__container')[3].classList.remove('correct')
                document.getElementsByClassName('form__container')[3].classList.add('incorrect')
                completeForm = false
            }
            break;
        case 'email':
            if (regularExpressions.email.test(input.target.value)) {
                document.getElementsByClassName('form__container')[4].classList.add('correct')
                document.getElementsByClassName('form__container')[4].classList.remove('incorrect')
                completeForm = true
            } else {
                document.getElementsByClassName('form__container')[4].classList.remove('correct')
                document.getElementsByClassName('form__container')[4].classList.add('incorrect')
                completeForm = false
            }
            break;
        case 'checkbox':
            break;
    }
}
const regularExpressions = {
    name: /^[a-zA-ZÄ-ÿ\s]{1,40}$/,
    last_name: /^[a-zA-ZÄ-ÿ\s]{1,40}$/,
    user: /^[a-zA-ZÄ-ÿ\W\d\_]{4,16}$/,
    email: /^[\w\d.-]*@?[\w\d]*\.[\w\d]+$/,
    password: /^(?=.*\d)(?=.*[\u0021-\u002b\u003c-\u0040])(?=.*[A-Z])(?=.*[a-z])\S{8,16}$/
}
const forms = document.getElementsByClassName('main__form')
const inputs = document.querySelectorAll('.main__form input')
inputs.forEach(input => {
    input.addEventListener('keyup', validateInput)
    input.addEventListener('blur', validateInput)
})
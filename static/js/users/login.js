function validarInputs(input) {
    switch (input.target.name) {
        case 'name':
            if (input.target.value.length > 0) {
                document.getElementsByClassName('form__label')[0].classList.add('oculto')
            } else {
                document.getElementsByClassName('form__label')[0].classList.remove('oculto')
            }
            break;
        case 'email':
            if (input.target.value.length > 0) {
                document.getElementsByClassName('form__label')[1].classList.add('oculto')
            } else {
                document.getElementsByClassName('form__label')[1].classList.remove('oculto')
            }
            break;
        case 'subject':
            if (input.target.value.length > 0) {
                document.getElementsByClassName('form__label')[2].classList.add('oculto')
            } else {
                document.getElementsByClassName('form__label')[2].classList.remove('oculto')
            }
            break;
        case 'text__area':
            if (input.target.value.length > 0) {
                document.getElementsByClassName('form__label')[3].classList.add('oculto')
            } else {
                document.getElementsByClassName('form__label')[3].classList.remove('oculto')
            }
            break;
    }
}

const formulario = document.getElementById('form')
const inputs = document.querySelectorAll('.form__input')
inputs.forEach(input => {
    input.addEventListener('blur', validarInputs)
})
const togglePasswordField = (id,icon) => {
    const passwordInput = document.getElementById(id);
    let passwordIcon = document.getElementById(icon);
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text'
        passwordIcon.classList.remove('fa-eye')
        passwordIcon.classList.add('fa-eye-slash')
        console.log(passwordIcon.classList)
    }
    else if(passwordInput.type === 'text'){
        passwordInput.type = 'password'
        passwordIcon.classList.add('fa-eye')
        passwordIcon.classList.remove('fa-eye-slash')
        console.log(passwordIcon.classList)
    }
}
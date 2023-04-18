console.log('hello profiles')

const avatarBox = document.getElementById('avatar-box')
const profileForm = document.getElementById('profile-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const bioInput = document.getElementById('id_bio')
const avatarInput = document.getElementById('id_avatar')

const alertBox = document.getElementById('alert-box')

profileForm.addEventListener('submit', e=>{

    e.preventDefault()

    const formData = new FormData()
    formData.append('csrfmiddlewaretoken', csrf[0].value)
    formData.append('bio', bioInput.value)
    formData.append('avatar', avatarInput.files[0])

    $.ajax({
        type: 'POST',
        url: '',
        enctype: 'multipart/form-data',
        data: formData,
        success: function(response){
            console.log(response)
            avatarBox.innerHTML = `
            <img src= "${response.avatar}" class = "round" height="200px" width = "auto" alt = "${response.user}">
            `
            bioInput.value = response.bio
            handleAlerts('success', 'your profile has been updated')
        },
        error: function(error){
            console.log(error)
            handleAlerts('danger', 'error updating')
        },
        processData: false,
        contentType: false,
        cache: false,
    })

})
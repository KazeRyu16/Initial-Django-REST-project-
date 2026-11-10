const loginform = document.getElementById('login-form')
const BaseEndpoint = "http://127.0.0.1:8000/api"

if (loginform) {
    loginform.addEventListener('submit',handlelogin)
}

function handlelogin(event) {
    console.log(event)
    event.preventDefault()
    let loginformdata = new FormData(loginform)
    let loginObjectData = Object.fromEntries(loginformdata)
    let bodystring = JSON.stringify(loginObjectData)
    console.log(loginObjectData,bodystring)
    const loginendpoint = `${BaseEndpoint}/token/`
    const options = {
        method : "POST",
        headers : {
            "Content-Type":"application/json"
        },
        body:bodystring
    }
    fetch (loginendpoint,options)
    .then(response =>{
        console.log(response)
        return response.json()
    })
    .then(x =>{
        console.log(x)
    })
    .catch(err=>{
        console,log('err',err)
    })
}
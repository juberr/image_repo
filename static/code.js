

let uploadbtn = document.getElementById('upload')

uploadbtn.addEventListener("click", e => {
    e.preventDefault();
    // define upload path
    const endpoint = '/upload'
    //get uploaded files
    let uploadFiles = document.getElementById('img');
    const form = document.getElementById('uploadForm');
    const formData = new FormData();
    const headers = new Headers();

    headers.append('Content-Type', 'application/json')

    const files = uploadFiles.files;

    formData.append('file', files[0], files[0].name) // declaring form data for POST request
    console.log(formData)
    let req = new Request(endpoint, {method: 'POST', body: formData}) // assembling the request


    fetch(req).then(response => console.log(response.json())); // sending the request and logging the result


    });

let deletebtn = document.getElementById('delete')

deletebtn.addEventListener('click', e => {

    e.preventDefault();

    let record = document.getElementById('nbr').value;
    const endpoint = '/remove/' + record;
    
    fetch(endpoint, {method: 'DELETE'});


});
    


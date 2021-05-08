

let submitbtn = document.getElementById('submit')

submitbtn.addEventListener("click", e => {
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

    formData.append('file', files[0], 'test.png')
    console.log(formData)
    let req = new Request(endpoint, {method: 'POST', body: formData})


    fetch(req);


    });
    




let uploadbtn = document.getElementById('upload');

// defining delete function for later
const remove = function() {
    let record = $(this).attr('id');
    const endpoint = '/remove/' + record;
    fetch(endpoint, {method: 'DELETE'});
    $('.'+record).remove()

};

uploadbtn.addEventListener("click", e => {
    e.preventDefault();
    // define upload path
    const endpoint = '/upload'
    //get uploaded files
    let uploadFiles = document.getElementById('img');
    const form = document.getElementById('uploadForm');
    const headers = new Headers();
    headers.append('Content-Type', 'application/json')

    const files = uploadFiles.files;

    //upload each file and append to htlm
    for (i=0; i<files.length; i++){
        let formData = new FormData();
        formData.append('file', files[i], files[i].name) // declaring form data for POST request
    console.log(formData)
    let req = new Request(endpoint, {method: 'POST', body: formData}) // assembling the request


    fetch(req).then(response => 
        response.json()).then((data) => {
        $('.row').append(`<div class='col-sm-4 ${data.count[0]}'>
        <div class="card" href="static/images/${data.data[2]}">
            <a href="static/images/${data.data[3]}" target='_blank'>
                <img src="static/thumbnails/${data.data[2]}" class="card-img-top img-responsive" alt="${data.data[2]}">
            </a>
            <div class="card-body">
              <h5 class="card-title">${data.data[2]}</h5>
              <p>Date Uploaded: ${data.data[0]}</p>
              <p>Size:${data.data[1]} MB</p>
              <a href="static/images/${data.data[2]}" class="btn btn-primary" target="_blank">View Fullsize</a>
              <a class="btn btn-danger delete" id='${data.count[0]}'>Delete Image</a>
            </div>
          </div>
        </div>`)})
    }

    }); // sending the request and logging the result




// using delete function 
$('.row').on('click', '.delete',remove);



    


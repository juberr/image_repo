console.log('hello')



const input = document.getElementById('img');
console.log(input)
var bstrings = [];
// get binary strings for uploaded files (accepts multiple)
input.addEventListener("change", function () {

    let files = this.files;

    for (i=0; i < files.length; i++) {
        let reader = new FileReader();

        reader.onloadend = function () {
            bstrings.push(reader.result)
        }
        
        reader.readAsDataURL(files[i]);
        
    }

    console.log(bstrings);
});

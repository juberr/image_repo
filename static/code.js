console.log('hello')


let reader = new FileReader();



const input = document.getElementById('img');
console.log(input)

input.addEventListener("change", function () {
    let files = this.files;
    console.log(files);
});

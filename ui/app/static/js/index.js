const dragArea = document.querySelector('.drag-area')
const dragText = document.querySelector('.header');

let button= document.querySelector('.button');
let input = document.querySelector('#filePiker');
let predict = document.querySelector('#predict');

let file;

button.onclick = () => {
    input.click();
};

predict.onclick = () => {
    send_req();
};

input.addEventListener('change', function () {
    file = this.files[0];
    dragArea.classList.add('active');
    displayFile();
})

dragArea.addEventListener('dragover', (event)=>{
    event.preventDefault();
    dragText.textContent = "Release to upload";
    dragArea.classList.add('active');
    // console.log('File is inside drag area');
});

dragArea.addEventListener('dragleave', (event)=>{
    dragText.textContent = "Drag & Drop";
    dragArea.classList.remove('active');
    // console.log('File left the drag area');
});

dragArea.addEventListener('drop', (event)=>{
    event.preventDefault();

    file = event.dataTransfer.files[0];
    displayFile();
});

function displayFile(){
    let fileType = file.type;

    let validExtension = ['image/jpeg', 'image/jpg', 'image/png'];

    if(validExtension.includes(fileType)){
        let fileReader = new FileReader();
        fileReader.onload = () => {
            let fileURL = fileReader.result;

            // console.log(fileURL);
            let imgTag = `<img src="${fileURL}" alt="">`;
            dragArea.innerHTML = imgTag;
        };

        fileReader.readAsDataURL(file);

        predict.classList.remove('disabled');
    }else{
        alert("This file is not an image");
        dragArea.classList.remove('active')
        predict.classList.add('disabled');
    }
}


function send_req(){
    // create a FormData object to hold the file data
    const formData = new FormData();
    formData.append('image', file);

    // send a POST request to the Flask endpoint with the file data
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        // Parse the JSON data into a JavaScript object
        const json_data = JSON.parse(data);
        console.log(json_data);
        // Navigate to a new URL
        window.location.replace("/home?predict=" +  json_data.predict + "&image_name="+json_data.image_name);
    })
    .catch(error => console.error(error));
}
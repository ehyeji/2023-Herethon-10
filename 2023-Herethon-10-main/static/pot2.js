function updateTime() {
    var date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var timeString = hours.toString().padStart(2, '0') + ':' + minutes.toString().padStart(2, '0');
    document.getElementById('time').textContent = timeString;
}

updateTime();
setInterval(updateTime, 1000);

function selectImage(imageSrc) {
    var selectedImageSrc = encodeURIComponent(imageSrc);
    localStorage.setItem("selectedImageSrc", selectedImageSrc);
    
    var selectedImagesData = JSON.parse(localStorage.getItem("selectedImagesData")) || [];
    selectedImagesData.push(selectedImageSrc);
    localStorage.setItem("selectedImagesData", JSON.stringify(selectedImagesData));
}

function goToNextPage() {
    var selectedImageSrc = localStorage.getItem("selectedImageSrc");
    if (selectedImageSrc) {
        window.location.href = "pot.html?selectedImageSrc=" + selectedImageSrc;
    }
}
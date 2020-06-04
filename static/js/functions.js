const inputBtn = document.querySelector( 'input[type="file"]' )
 
// Submit button javascript
function myFunction() {
    if (inputBtn.value == '' | 'image'){
        alert('Please upload an image.');
        return false;
    } 
}

// Feedback javascript
window.onload=function(){
    const clickBtn = document.getElementById('yes');
    const clickBtn2 = document.getElementById('no');
    
    clickBtn.addEventListener('click', clickyes);
    clickBtn2.addEventListener('click', clickno);
  }

// if yes is clicked, do not allow user to click the same or another option again vice versa
function clickyes() {
    clickBtn = document.getElementById('yes');
    clickBtn2 = document.getElementById('no');
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "https://api.countapi.xyz/hit/label.me/yesclick");
    xhr.responseType = "json";
    xhr.onload = function() {
        alert(`${this.response.value} users agree with our predictions.`);
        clickBtn.removeEventListener('click', clickyes);
        clickBtn2.removeEventListener('click', clickno);
    }
    xhr.send();
}

function clickno() {
    clickBtn = document.getElementById('yes');
    clickBtn2 = document.getElementById('no');
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "https://api.countapi.xyz/hit/label.me/noclick");
    xhr.responseType = "json";
    xhr.onload = function() {
        alert(`${this.response.value} users do not agree with our predictions.`);
        clickBtn2.removeEventListener('click', clickno);
        clickBtn.removeEventListener('click', clickyes);
    }
    xhr.send();
}
$(document).ready(function() {
    var counter;
    counter = 5;
    setInterval(function () {
        document.getElementById("counterarea").innerHTML = counter;
        counter = counter - 1;
        if(counter === 0){
            window.location.href = '/';
        }
    }, 1000);
});
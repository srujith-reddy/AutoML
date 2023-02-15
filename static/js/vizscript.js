const clicked_button=document.getElementById('colbutton');
const tv=document.getElementById('targettext');
const subtn=document.getElementById('targetsubmit')
targetsubmit.addEventListener('click',function(){
        let targetoutput=tv.value;
        console.log(targetoutput);
})


function handleButtonClick(event) {
    var col = event.target.getAttribute("data-col");
    console.log("Button clicked: " + col);

}

function sendClickedButtonToServer(col) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/handle-clicked-button");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ col: col }));
  }
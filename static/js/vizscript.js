// const clicked_button=document.getElementById('colbutton');
const tv=document.getElementById('targettext');
const submitbtn=document.getElementById('targetsubmit');
var targetoutput;
submitbtn.addEventListener('click',function(){
        targetoutput=tv.value;
        console.log(targetoutput);
        tv.value="";
        postData();
})

var clicked_buttons_array=[];

const buttons = document.querySelectorAll('.colbutton');
buttons.forEach(button => {
  button.addEventListener('click', function() {
    var col=button.textContent;
    // console.log('button clicked:'+col);
    button.classList.toggle('clicked');
    clicked_buttons_array.push(col);

  });
});

function postData() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "/processdata", true);
  xhttp.setRequestHeader("Content-Type", "application/json");
  var data = {
    "clicked_buttons_array": clicked_buttons_array,
    "targetvalue":targetoutput
  };
  var json_data = JSON.stringify(data);
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4) {
      if (this.status == 200) {
          console.log(this.responseText);
          var form = document.createElement('form');
          form.method = 'POST';
          form.action = '/FeatureEngineering';
          document.body.appendChild(form);
          form.submit();
        } else {
          console.error('Server error: ' + this.status);
          alert('Error: ' + this.status + ' ' + this.statusText);
      }
    }
  };
  xhttp.send(json_data);
}



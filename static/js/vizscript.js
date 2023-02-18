// const clicked_button=document.getElementById('colbutton');
const tv=document.getElementById('targettext');
const subtn=document.getElementById('targetsubmit')
targetsubmit.addEventListener('click',function(){
        let targetoutput=tv.value;
        console.log(targetoutput);
})

clicked_buttons_array=[];




// function handleButtonClick(event) {
//     var col = event.target.getAttribute("data-col");
//     console.log("Button clicked: " + col);
//     col.classList.add('clicked');

// }

const buttons = document.querySelectorAll('.colbutton');
buttons.forEach(button => {
  button.addEventListener('click', function() {
    var col=button.textContent;
    // console.log('button clicked:'+col);
    button.classList.toggle('clicked');
    clicked_buttons_array.push(col);
    for(let i=0;i<clicked_buttons_array.length;i++)
{
  console.log(clicked_buttons_array[i]);
}

    

  });
});


const processbutton=document.getElementById('trainpage');
processbutton.addEventListener('click',function(){
        window.location.href="/processdata";
})

myArray=clicked_buttons_array;
$.ajax({
  type: "POST",
  url: "/processdata",
  data: JSON.stringify(myArray),
  contentType: "application/json; charset=utf-8",
  dataType: "json",
  success: function(response) {
      console.log(response);
  },
  error: function(error) {
      console.log(error);
  }
});

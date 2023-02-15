const clicked_button=document.getElementById('colbutton');
const tv=document.getElementById('targettext');
const subtn=document.getElementById('targetsubmit')
targetsubmit.addEventListener('click',function(){
        let targetoutput=tv.value;
        console.log(targetoutput);
})

clicked_button.addEventListener('click',function(){
    let content=clicked_button.textContent;
    console.log(content);
})



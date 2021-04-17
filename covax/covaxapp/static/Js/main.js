const inputs=document.querySelectorAll('.input')

function focusFunc(){
    let parent=this.parentNode.parentNode;
    parent.classList.addd('focus');
}

inputs.forEach(input =>{
    input.addEventListener('focus',focusFunc);
})
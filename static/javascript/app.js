const updateButtons = document.querySelectorAll(".update");
// const oldTexts = document.querySelectorAll(".text");
let oldText;
let form;
// const forms = document.querySelectorAll(".reveal")
let task_id;

console.log("testing")
function getId(button_id){
    task_id = button_id.replace('update-', '')
}

updateButtons.forEach(btn => {
    btn.addEventListener("click", e => {
        e.preventDefault();
        oldText = document.getElementById(`text-${task_id}`);
        form = document.getElementById(`form-${task_id}`);
        console.log(oldText, form, btn, `text-${task_id}`)

        form.style.display == 'none' ? form.style.display = 'block' : form.style.display = 'none';
        !oldText.style.display || oldText.style.display == 'block' ? oldText.style.display = 'none' : oldText.style.display = 'block';
        
    });
});
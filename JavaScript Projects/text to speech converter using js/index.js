var form = document.getElementById('form');
form.addEventListener('submit',function(event){
    event.preventDefault()
    var text = document.getElementById('text').value
    console.log(text)
    let utterance = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(utterance)
})
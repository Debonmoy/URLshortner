
function generate_url() {
    var data = document.getElementById("data").value
    eel.generate_url(data)(setOutput)
}

function setOutput(outputUrl){
    document.getElementById('output').value = outputUrl
}

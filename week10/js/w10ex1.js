console.log("Test1");

function showGreeting(){
    //console.log("Hello");
    let fname = window.prompt("What is your first name?");
    window.alert("Hello" + fname)
}

//showGreeting();

document.querySelector("#btnGO").addEventListener("click", showGreeting);
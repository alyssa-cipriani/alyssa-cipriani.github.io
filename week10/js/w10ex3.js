
console.log ("Test 3");

function multiple () { 
    let fnumber = document.querySelector("#fnumber").value;
    let snumber = document.querySelector("#snumber").value;
    let product = fnumber * snumber;

    document.querySelector("#output").textContent = "The multiplication of " + fnumber + " and " + snumber + " is " + product;

}

document.querySelector("#btnCal").addEventListener("click", multiple);
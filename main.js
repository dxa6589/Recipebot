const URL = "http://34.67.246.127:5000/"

function showInput() {
    moveUp();
    var message = document.getElementById("uinput").value;
    document.getElementById('p2').innerHTML = "You: " + message;
    document.getElementById("indicator").innerHTML = "ChefDuck typing:";
    document.textbox.reset();
}

function showResponse() {
    showInput();
    var message = document.getElementById("uinput").value;
    
    /*console.log(message);
    fetch(`${URL}/extract/${message}`, {
        method: "GET",
        headers: {
            "Content-Type": "text/plain"
        }
    })
    .then(response => {
        fetch(`${URL}/all/${response.body.text()}`, {
            method: "GET",
            headers: {
                "Content-Type": "text/plain"
            }
        })
        .then(data => {
        let output = data;
        document.getElementById('p1').innerHTML = "Duck: " + data;
        document.getElementById("indicator").innerHTML = "";
    }
    )}*/
    )
    document.getElementById('p1').innerHTML = "Duck: " + message;
    document.getElementById("indicator").innerHTML = "";

}

function moveUp() {

    var botlog = document.getElementsByClassName("incoming");
    
    for (var i = 1; i < botlog.length; i+=1) {
        botlog[i-1].innerHTML = botlog[i].textContent;
    }

    var userlog = document.getElementsByClassName("outgoing");
    
    for (var j = 1; j < userlog.length; j+=1) {
        userlog[j-1].innerHTML = userlog[j].textContent;
    }
}

let text = "I want to make an apple pie";
let recipes = [];
let name = "apple pie";
localStorage.setItem("total", 0);

/*$.get({
    url: "http://34.67.246.127:5000/all/" + text,
    crossDomain: true,
    headers: {"Access-Control-Allow-Origin": "*"},
    success: function(response) {
    recipes = JSON.parse(response);

    recipes.forEach(function(recipe) {
        $("#recipes").append(`<option value='${recipe[0]}'>${recipe[0]}</option>`);
    });
    }
})

function getRecipeIngredients(name) {
    let ingredients = [];
    localStorage.setItem("total", 0);

    recipes.forEach(function(recipe) {
    if(name == recipe[0]) {
        ingredients = recipe[1].replace("[", "").replace("]", "").split(",");
        
        ingredients.forEach(function(ing) {
        ing = ing.trim().replace(/'/g, "");
        getSku(ing);
        });
    }
    });

    console.log(localStorage.getItem("total"));
}

function getSku(ing) {
    $.get({
    url: `https://api.wegmans.io/products/search?query=${ing}&api-version=2018-10-18&subscription-key=55031caddc374e1d88ba2b369e8be8da`,
    success: function(response) {
        let sku = response.results[0]["sku"];
        getPrice(sku);
    }
    })
}

function getPrice(sku) {
    $.get({
    url: `https://api.wegmans.io/products/${sku}/prices?api-version=2018-10-18&subscription-key=c455d00cb0f64e238a5282d75921f27e`,
    success: function(response) {
        let stores = response.stores;
        localStorage.setItem("total", parseInt(localStorage.getItem("total")) + stores[0].price);
    }
    })
}

function getStore(id) {
    $.get({
    url: `https://api.wegmans.io/stores/${id}?api-version=2018-10-18&subscription-key=55031caddc374e1d88ba2b369e8be8da`,
    success: function(response) {
        return "At " + response.name + ", " + response.address.street + " " + response.address.city + " " + response.address.state.abbreviation;
    }
    })
}*/
function showInput() {
    moveUp();
    var message = document.getElementById("uinput").value;
    document.getElementById('p2').innerHTML = "You: " + message;
    //document.getElementById("textbox")[0].reset();
}

function showResponse() {
    time = 1000;
    while (time > 0) {
        document.getElementById('p1').innerHTML = "Bot: " + message;
        pause(100);
        time-=100;
        document.getElementById('p1').innerHTML = "Bot: ." + message;
        pause(100);
        time-=100;
        document.getElementById('p1').innerHTML = "Bot: .." + message;
        pause(100);
        time-=100;
        document.getElementById('p1').innerHTML = "Bot: ..." + message;
        pause(100);
        time-=100;
    }
}

function moveUp() {
    var botlog = document.getElementsByClassName("chatlog_bot");
    
    for (var i = 1; i < botlog.length; i+=1) {
        //print("changing "+botlog[i-1].getAttribute("id")+(" to ")+botlog[i].getAttribute("id"))
        botlog[i-1].innerHTML = botlog[i].textContent;
    }

    var userlog = document.getElementsByClassName("chatlog_user");
    
    for (var j = 1; j < userlog.length; j+=1) {
        userlog[j-1].innerHTML = userlog[j].textContent;
    }
}

function pause( waitTime ) {
    var start = new Date().getTime();
    var end = start;
    while(end < start + waitTime) {
        end = new Date().getTime();
    }
}
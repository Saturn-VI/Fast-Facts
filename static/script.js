let response = {}

function apiOn(event) {
    return new Promise(resolve => {
      api.on(event, response => resolve(response));
    });
  }
  

function httpGet(theUrl) {
    return new Promise((resolve, reject) => {
        let req = new XMLHttpRequest();
        req.open("GET", theUrl, true);

        req.onload = (e) => {
            if (req.status === 200) {
                resolve(req.responseText);
            } else {
                reject(new Error(req.statusText));
            }
        };

        req.onerror = (e) => {
            reject(new Error("Network error"));
        };

        req.send(null);
    });
}




async function get_data() {
    let response = await httpGet('/api')
    return response
};

function reset() {
    if (confirm("Reset test?") == true) {
        window.location.href = "";
    }
}

get_data()
    .then(function(response){
    JASON = JSON.parse(response)
    document.getElementById("topic_1").innerText = JASON.topics[0]
    document.getElementById("topic_2").innerText = JASON.topics[1]
    document.getElementById("topic_3").innerText = JASON.topics[2]
    document.getElementById("topic_4").innerText = JASON.topics[3]
    document.getElementById("topic_5").innerText = JASON.topics[4]

    document.getElementById("letter_1").innerText = JASON.letters[0]
    document.getElementById("letter_2").innerText = JASON.letters[1]
    document.getElementById("letter_3").innerText = JASON.letters[2]
    document.getElementById("letter_4").innerText = JASON.letters[3]
    document.getElementById("letter_5").innerText = JASON.letters[4]
    })

    
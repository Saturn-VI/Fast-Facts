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

function reset_grid() {
    get_data()
        .then(function(response){
            console.log(response)
        })
}

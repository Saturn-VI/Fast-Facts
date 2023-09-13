let response = {}

function httpGet(theUrl)
{
    var req = new XMLHttpRequest();
    req.open( "GET", theUrl, true );
    req.send();
    return req.responseText;
} // stealing my own code :DD



async function get_data() {
    let post = JSON.parse(httpGet('/api'));
    return post
}

get_data()
console.log(get_data())
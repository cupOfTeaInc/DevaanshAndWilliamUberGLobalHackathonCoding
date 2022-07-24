function postTo(url){
    //https://stackoverflow.com/a/38982661 -John G (im not very good at js)
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send();
}
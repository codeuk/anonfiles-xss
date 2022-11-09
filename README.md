# AnonFiles XSS Generator 🕷️
**Custom dashboard for generating a malicious AnonFiles XSS download link!**
- You can spoof the file name & extension (so no one thinks it can be malicious)
- Uploads and generates AnonFiles download link with embedded javascript payload
- When someone tries to *download* this file, the javascript payload will be activated
- User information sent to your Discord Webhook! (IP, useragent, browser, etc.)

# Usage 💾
- Download/Clone the repository
- Execute install.bat
- Execute start.bat (or start src/main.py)
- Wait for the web server to start, then go to *http://localhost*
- Make sure you put your Discord Webhook inside the **Webhook** input box
- From here, it's pretty simple, just input the file attributes you want and press **GENERATE URL**

When the page refreshes, it will have an alert pop up with the generated AnonFiles URL.

When someone goes to this URL and presses the download button, the payload will execute.

# Images 🖼️
**None Yet**

# Notes 📒
***THIS WAS MADE FOR EDUCATIONAL PURPOSES ONLY...***

**I AM NOT RESPONSIBLE FOR WHAT YOU DO WITH THIS PROGRAM AND I DO NOT ENDORSE USING IT MALICIOUSLY!**

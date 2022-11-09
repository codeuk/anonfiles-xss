**RELEASING CODE AT 10 STARS**

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
**Nice little dashboard :>)**

![image](https://user-images.githubusercontent.com/75194878/200929342-9595fddb-b6dc-43b9-a05f-65b77b4d28ef.png)

**Generating the malicious URL**

![image](https://user-images.githubusercontent.com/75194878/200929151-52243ac1-e1b9-42cf-be4f-f6ec77a31179.png)

**Alert for when someone presses the download button on AnonFiles** *(payload.js will be rewritten soon)*

![image](https://user-images.githubusercontent.com/75194878/200932611-f6855697-8432-41d7-b250-2ce40305a138.png)

# Notes 📒
***THIS WAS MADE FOR EDUCATIONAL PURPOSES ONLY...***

**I AM NOT RESPONSIBLE FOR WHAT YOU DO WITH THIS PROGRAM AND I DO NOT ENDORSE USING IT MALICIOUSLY!**

# Automated Image Sender
Sends a random image from an Imgur album to a Facebook friend, using the <a href="https://github.com/carpedm20/fbchat">fbchat</a> module.

<h2>Purpose</h2>

 A Python script that sends images from a chosen Imgur gallery to Facebook friends, while keeping track of what is sent to each person to prevent repetition. 
<h2>Usage</h2>

1. Change image_gallery to your Imgur gallery of choice, fb_username and fb_password to your Facebook username and password. 
2. Run the script and input the full name of the person to send an image to and the number of images you wish to send.

The pickle module creates a file "image_sender_storage" that stores each person that images have been sent to, and what has been sent.


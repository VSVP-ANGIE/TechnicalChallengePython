# Aptoide API Challenge - Python Script
As part of a technical challenge to connect with the Aptoide API, this Python script was developed. 
Searching and showing a list of apps, displaying the description of an app, and downloading an APK file are its three primary functions. 
An overview of the process and steps for executing the script are provided below.

## Thought Process
1. Search and display to the console the list of apps obtained from the API call:
   Getting a list of apps from the Aptoide API was the first step. 
   A base64-encoded 'q' parameter that gathered up device specs was included in the URL that was sent. 
   After decoding this parameter's contents, I showed the list of applications and their package names. 
   I made sure the base64 string has the appropriate padding before decoding in order to address any possible decoding problems.

2. Display App Description:
   I decided to add a personal touch to the second assignment by choosing one app at random from the list that was retrieved in Step 1. 
   This method not only satisfied the specifications but also gave the script a sense of surprise. 
   The script handled this cordially by notifying the user if there was no description submitted.
 
3. Download the app file (APK) by requesting the following URL:
   Getting an APK file was the third task. A missing aptoide_uid option caused the first URL to produce an error. 
   I fixed this by substituting a dummy value (testchallenge) for the missing parameter. 
   The APK file was then successfully downloaded and saved locally by the script.

## How to Run the Script
Prerequisites
Ensure Python is installed.
Install the requests library if not already available.

Steps to Run
Save the script to a file (e.g. aptoide_challenge.py).
Open a terminal or command prompt and navigate to the directory where the script is saved.

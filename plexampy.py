from pypresence import Presence, Client
import requests
import time
import datetime
from xml.dom import minidom
#Start PyPresence Client
client_id = ""
client = Client(client_id)
client.start()
#Infinite Loop for Infinite Readings
while True:
    #PUT YOUR PLEXSERVER URL HERE!!
    plexserver_sessions = ""
    #Use a sleep to avoid overloading your server
    time.sleep(2)
    getresponse = requests.get(plexserver_sessions)
    #Save XML to file to read off of during checking
    plexsessionswrite = open("plexsessions.xml","w")
    plexsessionswrite.write(getresponse.text)
    plexsessionswrite.close()
    session_file = open("plexsessions.xml")
    parser = minidom.parse(session_file)
    try:
        taga = parser.getElementsByTagName("Player")[0]
        paused = (taga.attributes['state'].value)
        tag = parser.getElementsByTagName("Track")[0]
        songname = (tag.attributes['grandparentTitle'].value)
        artistname = (tag.attributes['title'].value)
        albumname = (tag.attributes['parentTitle'].value)
        timefinder = parser.getElementsByTagName("Media")[0]
        #Set Discord activity as songname, artistname
        if paused == "paused":
            client.set_activity(state="Nothing on PlexAmp", details="Listening To:", large_image="https://github.com/mattqze/plexampy/blob/main/img/plexamp.png?raw=true", large_text="PlexAmp", small_text="PlexAmPy by Sudoq", small_image="https://github.com/mattqze/plexampy/blob/main/img/python.jpg?raw=true")
            print("Nothing is playing.")
        if paused == "playing":
            client.set_activity(state=songname + " - " + artistname + " on PlexAmp", details="Listening To:", large_image = "https://github.com/mattqze/plexampy/blob/main/img/plexamp.png?raw=true", large_text="PlexAmp", small_text="PlexAmPy by Sudoq", small_image="https://github.com/mattqze/plexampy/blob/main/img/python.jpg?raw=true")
            print("Current Song: " + songname + " by " + artistname + " on " + albumname)
    except IndexError:
        print("Nothing is playing.")
        songname = ''
        artistname = ''

# plexampy
A Discord RPC that displays what you're listening to on Plex.<br>
Flex your Plex server and legally obtained music collection to your friends on Discord.<br>
This version is not very good, I need to port it to C# or use a different discord library to make it look and function better.
# Screenshots
![PlexAmPy on my profile](https://github.com/mattqze/plexampy/blob/main/shots/plexampyonprofile.jpg?raw=true)
# Setup
You will need:<br>
A Discord Account<br>
A Plex Server<br>
Plex Pass<br>
Tunes<br>
## Discord App
Open [Discord Dev Page](https://discord.com/developers/applications/me) and sign in.<br>
Click "New Application" at the top and name it anything, This will show up on your profile so give it a good name, like PlexAmPy.<br>
Copy your Application ID and paste it in the quotes on line 7.
## Plex Server
Open [Plex Web](https://app.plex.tv) and click on one of your movies.<br>
Click on the 3 dots
![Instructions](https://github.com/mattqze/plexampy/blob/main/shots/3dots.png?raw=true)<br>
Click "Get Info" then click on View XML and copy the first part of the url shown below
![Instructions](https://github.com/mattqze/plexampy/blob/main/shots/url.png?raw=true)<br>
You'll also need your Plex-Token, located at the end of that url, it starts with "&X-Plex-Token="<br>
Add it all together as: https://not-area-lu-rl.jdoj432kodj3kjf43ijf0439j.plex.direct:32400/status/sessions?X-Plex-Token=NUMBERSANDSTUFF12312<br>
Put this url on line 12 in the quotes.<br>
Launch PlexAmPy through Command Prompt and starting listening.

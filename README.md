# audios-amigos
## Helps in downloading audio from "" music streaming platform

This certain music streaming platform breaks their music file into many smaller segments, and the order of which to play the files and directory of each segment in a m3u file.

Usually, the whole audio file can be downloaded upon opening the web browser's web development tools (Google Chrome, in my case), however this platform opted to do as I stated above--to circumvent more novice users from downloading the file.  The URLs found in the m3u file also uses a sessions_id, so it would be quite difficult to attempt to manually download each segment. This is why I created this Python script.

audios-amigos takes in the m3u file and parses the URL links, downloads each segment and concatenates the segments back into one audio file.

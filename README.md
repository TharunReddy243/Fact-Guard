# Fact-Guard
Project - FACT GUARD

Filename:dictassai.py
Transcription: Uses AssemblyAI's api. 
Works by downloading the audio content of the youtube url with the pytube module. this mp3 file gets sent to the assemblyai api, wherein it gets converted to text.
The text is iterated thru and individual words are extracted, along with thier timestamps. with the usual sentence forming logic(if "." appears a new sentence starts) tghey are converted into sentences and put inside a dict.
The essential details of the video(video name etc) are extracted from the pytube module and encoded(converted to byte stream) and sent to another file,pipeusertest, using python pipes. similarly, the dict is converted to a string and it gets encoded and sent to the next file too.Similarly, the straight string format of the transcription gets encoded and sent to the pipeusertest.py with the help of pipes too.
Finally, The mp3 file gets deleted.

Filename:pipeusertest.py
This file gets connected to dictassai.py thru pipes. that file sends three individual inputs to this file where it simply gets printed.


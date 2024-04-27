from pytube import YouTube 
import os
import subprocess


yt = YouTube( 
	str(input("Enter the URL of the video you want to download: \n>> ")))  
video = yt.streams.filter(only_audio=True).first() 

destination = '.'

out_file = video.download(output_path=destination) 

base, ext = os.path.splitext(out_file) 
new_file = base + '.mp3'
os.rename(out_file, new_file) 

import assemblyai as aai

aai.settings.api_key = "be1fe3d7d78f4ab88d050d2b0ddd2ac0"

transcript = aai.Transcriber().transcribe(new_file)

sentence = ""
start_time = None
dict={}
for word in transcript.words:
    if not sentence:
        start_time = word.start
    sentence += " " + word.text

    if word.text.endswith("."):
        dict[sentence.strip()]=(str((start_time)/1000)+":"+str((word.end)/1000))
        sentence = ""
print(dict)
details="channel_name:"+ str(yt.author)+"\nvideo_title:"+str(yt.title)+"\nvideo_length:"+str(yt.length)+"\npublication_date:"+str(yt.publish_date)+"/n"
process = subprocess.Popen(['python', 'pipeusertest.py'], stdin=subprocess.PIPE)

process.communicate((details).encode('utf-8'))

process = subprocess.Popen(['python', 'pipeusertest.py'], stdin=subprocess.PIPE)

process.communicate(str(dict).encode('utf-8'))

os.remove(new_file)

from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import datetime
import os
import subprocess
def get_transcription_dict(youtube_url):
    q=youtube_url[17:]
    q1=q.split("?")
    query=q1[0]
    try:
        result_dict={}
        transcript_list = YouTubeTranscriptApi.get_transcript(query)
        for d in transcript_list:
            result_dict[d['text']] = d['start']
        return result_dict
    except Exception as e:
        return str(e)
    


def get_transcription(youtube_url):
    q=youtube_url[17:]
    q1=q.split("?")
    query=q1[0]
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(query)
        transcript_text = ' '.join([line['text'] for line in transcript_list])
        return transcript_text
    except Exception as e:
        return str(e)
    
def get_video_info(youtube_url):
    try:
        yt = YouTube(youtube_url)
        video_info = "channel_name:"+ str(yt.author)+"\nvideo_title:"+str(yt.title)+"\nvideo_length:"+str(yt.length)+"\npublication_date:"+str(yt.publish_date)
        return video_info
    except Exception as e:
        print("An error occurred:", e)
        return None
    

def generate_filenames():
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    straight_string_filename = f"StraightString_{current_datetime}.txt"
    dict_string_filename = f"DictString_{current_datetime}.txt"
    details_filename = f"Details_{current_datetime}.txt"
    return straight_string_filename, dict_string_filename, details_filename



youtube_url = input("Enter YouTube URL: ")
transcription = get_transcription(youtube_url)
dicttranscription=get_transcription_dict(youtube_url)
dicttranscription=str(dicttranscription)
details=get_video_info(youtube_url)

straight_string_filename, dict_string_filename, details_filename = generate_filenames()
directory = "/Users/narsi/OneDrive/Desktop/transcriptions"


straight_string_filename, dict_string_filename, details_filename = generate_filenames()
f1=os.path.join(directory, straight_string_filename)
f2=os.path.join(directory, dict_string_filename)
f3=os.path.join(directory, details_filename)
print(f1,"\n",f2,"\n",f3)
file1=open(f1,'a')
file2=open(f2,'a')
file3=open(f3,'a')

file1.write(transcription)

file2.write(dicttranscription)

file3.write(details)

file1.close()

file2.close()

file3.close()

subprocess.run(["python", "printingstuff.py", f1, f2, f3])
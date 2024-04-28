# Fact-Guard
Project - FACT GUARD

Filename:dictassai.py
Transcription: Uses AssemblyAI's api. 
Works by downloading the audio content of the youtube url with the pytube module. this mp3 file gets sent to the assemblyai api, wherein it gets converted to text.
The text is iterated thru and individual words are extracted, along with thier timestamps. with the usual sentence forming logic(if "." appears a new sentence starts) tghey are converted into sentences and put inside a dict.
This dict is then

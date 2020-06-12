import os
from moviepy.editor import *
from pydub import AudioSegment

AudioSegment.from_file("Movement.mp4").export("Movement.mp3", format="mp3")

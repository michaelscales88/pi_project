from src.factory import get_scribe
<<<<<<< HEAD
=======
from lib.read import read
>>>>>>> c959e80ced4eea41fb46fbf19ca56c0e13a2b1a5


def main(*wav_files):
    scribe = get_scribe()
    for text in scribe.transcribe(wav_files):
        read(text)

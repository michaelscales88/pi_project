from RaspberryPi_Project.src.factory import get_scribe


def main(*wav_files):
    scribe = get_scribe()
    for text in scribe.transcribe(wav_files):
        print(text)

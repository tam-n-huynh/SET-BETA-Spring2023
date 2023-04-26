import socket
import sys
import pyaudio
import threading
import time

# HOST, PORT = "localhost", 9999  # replace localhost with vincents ip address
# data = "sugma"

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second


def stream_audio_to_server(host, port):
    p = pyaudio.PyAudio()

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))

        while True:
            data = stream.read(chunk)
            sock.send(data)


stream_audio_to_server("localhost", 9999)

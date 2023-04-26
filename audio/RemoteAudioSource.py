import speech_recognition as sr
import threading
import socketserver
import queue
import time


HOST, PORT = "localhost", 9999
count = 0


class AudioQueue:
    """
    Singleton class which manages a queue to transmit audio from the tcp server to RemoteAudioSource class
    """
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if self._initialized:
            return
        self.audio_queue = queue.Queue()
        self.initialized = True

    def __new__(cls, *args, **kwargs):

        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance

        # if not hasattr(cls, 'instance'):
        #     with cls._lock:
        #         cls._instance = super(AudioQueue, cls).__new__(cls)
        #         cls._initialized = False
        # return cls._instance

    def read(self):
        print(self.audio_queue.qsize())
        if self.audio_queue.empty():
            return
        return self.audio_queue.queue[0]


class RemoteAudioSource(sr.AudioSource):
    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate
        self.stream = AudioQueue()

        self.server = socketserver.TCPServer((HOST, PORT), TCPHandler)

        def serve(server):
            print("Serving on localhost 9999")
            server.serve_forever()

        thread = threading.Thread(target=serve, args=(self.server,))
        thread.start()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024)
            if not self.data:
                return

            lock = threading.Lock()
            with lock:
                aq = AudioQueue().audio_queue
                aq.put(self.data)


ras = RemoteAudioSource()

while True:
    data = ras.stream.read()
    print(data)

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

    def read(self, chunk):
        print(self.audio_queue.qsize())
        if self.audio_queue.empty():
            return

        return self.audio_queue.queue[0]


class RemoteAudioSource(sr.AudioSource):
    def __init__(self, device_index=None, sample_rate=16000, chunk_size=1024):
        assert device_index is None or isinstance(device_index, int), "Device index must be None or an integer"
        assert sample_rate is None or (
                    isinstance(sample_rate, int) and sample_rate > 0), "Sample rate must be None or a positive integer"
        assert isinstance(chunk_size, int) and chunk_size > 0, "Chunk size must be a positive integer"

        self.sample_rate = sample_rate
        self.chunk_size = chunk_size

        self.stream = None
        self.audio = None

        self.server = socketserver.TCPServer((HOST, PORT), TCPHandler)

        def serve(server):
            print("Serving on localhost 9999")
            server.serve_forever()

        thread = threading.Thread(target=serve, args=(self.server,))
        thread.start()

    def __enter__(self):
        assert self.stream is None, "This audio source is already in a context manager"

        self.stream = AudioQueue()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stream = None


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024)
            if not self.data:
                return

            aq = AudioQueue().audio_queue
            aq.put(self.data)


with RemoteAudioSource() as source:
    while True:
        data = source.stream.read(1024)
        print(data)

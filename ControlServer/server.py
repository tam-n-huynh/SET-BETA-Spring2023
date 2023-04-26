from http.server import BaseHTTPRequestHandler, HTTPServer
import time


host = "localhost"
port = 8080


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        print(self.client_address)
        print(self.request)
        print(self.command)
        print(self.connection)
        print("ligma")
        self.send_response(200)
        self.send_header("Content-Length", "6")
        self.end_headers()
        self.wfile.write(bytes("sugma\n", "utf-8"))

    def do_PUT(self):
        pass

    def do_POST(self):
        pass


if __name__ == "__main__":
    webServer = HTTPServer((host, port), Server)
    print(f"Server started at {host}:{port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()

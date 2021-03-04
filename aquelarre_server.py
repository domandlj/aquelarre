from aquelarre_syntax import *
from aquelarre_interpreter import * 
from http.server import BaseHTTPRequestHandler, HTTPServer
from functools import partial
import time
import sys

# Server Config.
hostName = "localhost"
serverPort = 8080

class HandleHTTP(BaseHTTPRequestHandler):
    def __init__(self, code:Code ,*args, **kwargs): 
        self.code = code
        super().__init__(*args, **kwargs)

    def run_fun(self, fun, stdin=None):
        for cond in fun.body:
            response = run_cond(self.code,cond,get_params_or_args(self.path,'args'),
                    stdin)
            # print(response)
            if response != 'skip':
                self.send_response(cond.status)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes(response, "utf-8"))
    
    def body_payload(self):
        content_len = int(self.headers.get('Content-Length'))
        return self.rfile.read(content_len)

    def do_GET(self):
        fun = get_fun('get', self.path, self.code)
        self.run_fun(fun)

    def do_POST(self):
        fun = get_fun('post', self.path, self.code)
        self.run_fun(fun,stdin = self.body_payload())
    
    def do_PUT(self):
        fun = get_fun('put', self.path, self.code)
        self.run_fun(fun,stdin = self.body_payload())
    
    def do_DELETE(self):
        fun = get_fun('delete', self.path, self.code)
        self.run_fun(fun)
    
    def do_PATCH(self):
        fun = get_fun('put', self.path, self.code)
        self.run_fun(fun,stdin = self.body_payload())
    
        
def run_server(code: Code):
    server = HTTPServer((hostName, serverPort), partial(HandleHTTP,code))
    print(" 🐐 Aquelarre server started http://%s:%s" % (hostName, serverPort))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Server stopped.")


import socket
import re
import multiprocessing
import ssl
import urllib.parse
from error import *

class HTTP:
    def __init__(self, host, port=80, ssl=False):
        self.host = host
        self.port = port
        self.ssl = ssl
        self.response = ''
    
    def get_req(self, path, params=None):
        if params:
            path = f"{path}?{urllib.parse.urlencode(params)}"
        self.request('GET', path)
        return self.response

    def post_req(self, path, data, params=None):
        if params:
            path = f"{path}?{urllib.parse.urlencode(params)}"
        self.request('POST', path, data)
        return self.response

    def put_req(self, path, data, params=None):
        if params:
            path = f"{path}?{urllib.parse.urlencode(params)}"
        self.request('PUT', path, data)
        return self.response

    def request(self, method, path, data=''):
        self.response = ''
        if self.ssl:
            socket_ = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        else:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.connect((self.host, self.port))
        if data:
            socket_.send(
                f"{method.upper()} {path} HTTP/1.0\r\nHost: {self.host}\r\nContent-Length: {len(data)}\r\n\r\n{data}".encode('utf-8')
            )
        else:
            socket_.send(
                f"{method.upper()} {path} HTTP/1.0\r\nHost: {self.host}\r\n\r\n".encode('utf-8')
            )
        data = socket_.recv(4096)
        if socket_.fileno() != -1:
            socket_.close()
        if not data:
            raise RequestError(data)
        self.response = data
        self.decode_response()
    
    def decode_response(self):
        response_header = self.response[:self.response.find(b'\r\n\r\n')].decode('utf-8')
        response_data = self.response[self.response.find(b'\r\n\r\n') + 4:]
        status_code = re.findall(r'HTTP/1.0 (.*?) ', response_header)[0]
        response_headers = re.findall(r'(.*?): (.*?)\r\n', response_header)
        self.response = {
            'status_code': status_code,
            'headers': {header[0]: header[1] for header in response_headers},
            'data': response_data.decode(self.response.get('headers').get('Content-Type', 'utf-8'))
        }


    def request_multiprocess(self, method, path, data='', process_count=1000):
        p = multiprocessing.Pool(process_count)
        results = []
        for _ in range(process_count):
            results.append(p.apply_async(method, args=[path, data]))
        p.close()
        p.join()
        return results

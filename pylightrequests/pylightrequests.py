import ssl
import socket
import multiprocessing
import re
from error import *

class HTTP:

    def __init__(self):
        self.code = None
        self.header = None
        self.data = None
        self.json = None
        self.status = None
        self.json_data = None

    def get_req(self, host, path, port=80, ssl=False):
        if ssl:
            socket_ = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        else:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.connect((host, port))
        socket_.send(
            f"GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n".encode('utf-8')
        )
        data = socket_.recv(4096)
        if socket_.fileno() != -1:
            socket_.close()
        if not data:
            raise GetError(data)
        return data


    def post_req(self, host, path, data, port=80, ssl=False):
        if ssl:
            socket_ = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        else:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.connect((host, port))
        socket_.send(
            f"POST {path} HTTP/1.0\r\nHost: {host}\r\nContent-Length: {len(data)}\r\n\r\n{data}".encode('utf-8')
        )
        data = socket_.recv(4096)
        if socket_.fileno() != -1:
            socket_.close()
        if not data:
            raise PostError(data)
        return data


    def put_req(self, host, path, data, port=80, ssl=False):
        if ssl:
            socket_ = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        else:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.connect((host, port))
        socket_.send(
            f"PUT {path} HTTP/1.0\r\nHost: {host}\r\nContent-Length: {len(data)}\r\n\r\n{data}".encode('utf-8')
        )
        data = socket_.recv(4096)
        if socket_.fileno() != -1:
            socket_.close()
        if not data:
            raise PutError(data)
        return data


    def request(self, method, host, path, data='', port=80, ssl=False):
        if ssl:
            socket_ = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        else:
            socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.connect((host, port))
        if data:
            socket_.send(
                f"{method.upper()} {path} HTTP/1.0\r\nHost: {host}\r\nContent-Length: {len(data)}\r\n\r\n{data}".encode('utf-8')
            )
        else:
            socket_.send(
                f"{method.upper()} {path} HTTP/1.0\r\nHost: {host}\r\n\r\n".encode('utf-8')
            )
        data = socket_.recv(4096)
        if socket_.fileno() != -1:
            socket_.close()
        if not data:
            raise RequestError(data)
        self._parse_data(data)
        return data


    def request_multiprocess(self, method, host, path, data='', port=80, ssl=False, process_count=1000):
        p = multiprocessing.Pool(process_count)
        results = []
        for _ in range(process_count):
            results.append(p.apply_async(method, args=[host, path, data, port, ssl]))
        p.close()
        p.join()
        return results


    def _parse_data(self, data):
        self.code = re.findall('HTTP/1.0 \d\d\d .+\r\n', data)[0].split(' ')[1]
        self.json_data = re.findall('\{.+\}', data)
        self.json = self.json_data[0] if self.json_data else None
        self.data = re.findall('\r\n\r\n.+\r\n', data)[0] if re.findall('\r\n\r\n.+\r\n', data) else None
        self.header = re.findall('HTTP/1.0 \d\d\d .+\r\n.+\r\n', data)[0] if re.findall('HTTP/1.0 \d\d\d .+\r\n.+\r\n', data) else None
        self.status = self.code if self.code else None


    def parse_data(self, data):
        self._parse_data(data)
        return self.__dict__


    def get_response_code(self):
        return self.code


    def get_status(self):
        return self.status


    def get_header(self):
        return self.header


    def get_json(self):
        return self.json


    def get_json_data(self):
        return self.json_data


    def get_data(self):
        return self.data

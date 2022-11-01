import traceback, logging

class GetError(Exception):
    def __init__(self, data):
        tb = traceback.format_exc()
        logging.error(tb)
        self.error = f"GetError({data}) | {tb}"

    def __str__(self):
        return self.error

class PostError(Exception):
    def __init__(self, data):
        tb = traceback.format_exc()
        logging.error(tb)
        self.error = f"PostError({data}) | {tb}"

    def __str__(self):
        return self.error

class PutError(Exception):
    def __init__(self, data):
        tb = traceback.format_exc()
        logging.error(tb)
        self.error = f"PutError({data}) | {tb}"

    def __str__(self):
        return self.error

class RequestError(Exception):
    def __init__(self, data):
        tb = traceback.format_exc()
        logging.error(tb)
        self.error = f"RequestError({data}) | {tb}"

    def __str__(self):
        return self.error

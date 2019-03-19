import os
import sys
from datetime import datetime
import inspect


global_data = {'process':'os.getpid()', 'module':'os.path.split(inspect.stack()[2][1])[1].replace(".py","")',
               'function':'inspect.stack()[2][3]', 'line':'inspect.stack()[2][2]',
               'asctime':'getCurrentTimestamp()'}

class Logger:


    def __init__(self, keys: list, path: str='default.log'):
        """
        @param keys:
        @param path:
        """
        self.keys = keys
        dir_path, tail =  os.path.split(path)
        if not os.path.exists(dir_path):
            os.makedirs(path)
        self.log_file_path = path


    def info(self, data: str, extra: dict={}):
        """

        @param data:
        @param extra:
        @return:
        """
        meta = {}
        for key in self.keys:
            try:
                meta.update({'{}'.format(key):eval(global_data[key])})
            except Exception:
                pass
        meta.update(extra)
        with open(self.log_file_path, "a") as writer:
            material = ""
            for key in self.keys:
                material += "{}: ".format(meta[key])

            writer.write("{}: INFO: {}\n".format(material, data))

    def warning(self, data: str, extra: dict={}):
        """

        @param data:
        @param extra:
        @return:
        """
        meta = {}
        for key in self.keys:
            try:
                meta.update({'{}'.format(key): eval(global_data[key])})
            except Exception:
                pass
        meta.update(extra)
        with open(self.log_file_path, "a") as writer:
            material = ""
            for key in self.keys:
                material += "{}: ".format(meta[key])

            writer.write("{}: WARNING: {}\n".format(material, data))

    def error(self, data: str, extra: dict={}):
        """

        @param data:
        @param extra:
        @return:
        """
        meta = {}
        for key in self.keys:
            try:
                meta.update({'{}'.format(key): eval(global_data[key])})
            except Exception:
                pass
        meta.update(extra)
        with open(self.log_file_path, "a") as writer:
            material = ""
            for key in self.keys:
                material += "{}: ".format(meta[key])

            writer.write("{}: ERROR: {}\n".format(material, data))

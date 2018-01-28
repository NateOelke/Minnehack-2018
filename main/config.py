import os
import sys
import logging


class Config (object):
    def __init__(self, testing=False):
        self.port = int(os.getenv("PORT", "8000"))

        self.SECRET_KEY = Config.get_secret_key()
        self.SQLALCHEMY_TRACK_MODIFICATIONS = True


    @staticmethod
    def get_secret_key():
        key = os.getenv("SECRET_KEY") or "injuries"
        if key:
            return key
        sys.stderr.write(
            "SECRET_KEY not specified, application is exiting..\n")
        sys.stderr.flush()
        sys.exit(1)
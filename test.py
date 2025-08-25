import time
from pathlib import Path

from toomanythreads import ThreadedServer

from fastj2.src.fastj2 import FastJ2
from loguru import logger as log


class Server(FastJ2, ThreadedServer):
    def __init__(self):
        FastJ2.__init__(
            self,
            cwd=Path.cwd()
        )
        ThreadedServer.__init__(
            self
        )

        @self.get("/")
        def home():
            return self.render("null.html")


if __name__ == "__main__":
    Server().thread.start()
    time.sleep(100)

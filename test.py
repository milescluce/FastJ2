from fastj2.src.fastj2 import FastJ2
from loguru import logger as log

if __name__ == "__main__":
    j2 = FastJ2()
    j2.safe_render("null.html", foo = "bar")
    log.debug(j2.safe_render_string(""))
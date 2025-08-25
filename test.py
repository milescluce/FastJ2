from pathlib import Path

from fastj2.src.fastj2 import FastJ2
from loguru import logger as log

if __name__ == "__main__":
    j2 = FastJ2("other_file.html", cwd=Path.cwd() / "tests")
    j2.safe_render("null.html", foo = "bar")

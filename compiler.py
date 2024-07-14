import compileall
from pathlib import Path

(
    print("\nCompile completed")
    if compileall.compile_dir(Path(__file__).parent)
    else print("\nError occured")
)

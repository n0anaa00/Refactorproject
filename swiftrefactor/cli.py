import argparse
from refactor_engine import RefactorEngine

parser = argparse.ArgumentParser(description="PyRefactorX - AI-powered Python Refactoring")
parser.add_argument("file", help="Python file to refactor")
args = parser.parse_args()

with open(args.file, "r") as f:
    code = f.read()

engine = RefactorEngine(code)
print(engine.refactor_code())
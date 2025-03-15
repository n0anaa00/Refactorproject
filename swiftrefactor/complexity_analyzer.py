import os
import radon.complexity as cc
from radon.visitors import ComplexityVisitor

"This file does each git commit's code complexity analysis"


def analyze_complexity(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    visitor = ComplexityVisitor.from_code(code)
    results = {fn.name: fn.complexity for fn in visitor.functions}
    return results

if __name__ == "__main__":
    folder = "./sample_code"
    for file in os.listdir(folder):
        if file.endswith(".py"):
            complexity = analyze_complexity(os.path.join(folder, file))
            print(f"Complexity for {file}: {complexity}")
import libcst as cst

"This file does the suggestion for refactoring"

class RefactorSuggester(cst.CSTVisitor):
    def visit_FunctionDef(self, node):
        if len(node.body.body) > 20:
            print(f"Function '{node.name.value}' is too long ({len(node.body.body)} lines). Consider splitting it.")

    def visit_If(self, node):
        if len(node.body.body) > 10:
            print("Deeply nested 'if' statement detected. Consider simplifying.")

if __name__ == "__main__":
    with open("./sample_code/example.py", "r") as f:
        tree = cst.parse_module(f.read())
    tree.visit(RefactorSuggester())
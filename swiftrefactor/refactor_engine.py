import ast
import astor

class RefactorEngine:
    def __init__(self, code):
        self.tree = ast.parse(code)

    def remove_unused_imports(self):
        """Removes unused imports from Python code."""
        class ImportRemover(ast.NodeTransformer):
            def visit_Import(self, node):
                return None  # Deletes import statements (for now)
        
        self.tree = ImportRemover().visit(self.tree)

    def refactor_code(self):
        """Applies all refactoring rules."""
        self.remove_unused_imports()
        return astor.to_source(self.tree)


if __name__ == "__main__":
    sample_code = "import os\nprint('Hello')"
    refactored_code = RefactorEngine(sample_code).refactor_code()
    print(refactored_code)
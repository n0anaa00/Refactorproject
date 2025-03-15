import pytest
from pyrefactorx.refactor_engine import RefactorEngine

def test_unused_import_removal():
    code = "import os\nprint('Hello')"
    refactored = RefactorEngine(code).refactor_code()
    assert "import os" not in refactored

def test_refactor_no_change():
    code = "print('Hello')"
    refactored = RefactorEngine(code).refactor_code()
    assert refactored.strip() == code.strip()
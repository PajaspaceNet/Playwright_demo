import pytest
import sys
import os

if __name__ == "__main__":
    # Spustí všechny testy v aktuální složce (run_test2)
    sys.exit(pytest.main([os.path.dirname(__file__)]))

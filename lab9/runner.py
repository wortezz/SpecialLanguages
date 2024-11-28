import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(root_path)

from main import main

if __name__ == "__main__":
    main()

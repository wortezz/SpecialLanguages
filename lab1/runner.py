import os
import sys

lab1_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(lab1_root)

from functions import main

if __name__ == "__main__":
    main()
# run.py
import sys
import os

# cython compiled module ကို import လုပ်ခြင်း (build ထွက်လာတဲ့ so/pyd ဖိုင်နာမည်အတိုင်း import လုပ်ပါ)
try:
    import ttakstar
except ImportError:
    print("[-] Compiled .so module not found! Please run setup.py first.")
    sys.exit(1)

if __name__ == "__main__":
    # ttakstar module ထဲက main() function ကို ခေါ်သုံးခြင်း
    if hasattr(ttakstar, 'main'):
        ttakstar.main()
    else:
        print("[-] Main entry point not found in compiled module.")

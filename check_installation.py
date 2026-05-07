#!/usr/bin/env python3
"""
Example script demonstrating how to use the background blur tool.
This creates a sample test to verify the installation is correct.
"""

import os
import sys

def check_installation():
    """Check if all required packages are installed."""
    try:
        import cv2
        print("✓ OpenCV installed")
    except ImportError:
        print("✗ OpenCV not installed. Run: pip install opencv-python")
        return False
    
    try:
        import mediapipe
        print("✓ MediaPipe installed")
    except ImportError:
        print("✗ MediaPipe not installed. Run: pip install mediapipe")
        return False
    
    try:
        import numpy
        print("✓ NumPy installed")
    except ImportError:
        print("✗ NumPy not installed. Run: pip install numpy")
        return False
    
    try:
        from PIL import Image
        print("✓ Pillow installed")
    except ImportError:
        print("✗ Pillow not installed. Run: pip install Pillow")
        return False
    
    return True


def main():
    """Main function to check installation."""
    print("Checking installation...")
    print("-" * 40)
    
    if check_installation():
        print("-" * 40)
        print("\n✓ All dependencies installed successfully!")
        print("\nYou can now use the background blur tool:")
        print("  python blur_background.py <input_image> [output_image] [blur_strength]")
        print("\nExample:")
        print("  python blur_background.py photo.jpg photo_blurred.jpg 35")
    else:
        print("-" * 40)
        print("\n✗ Some dependencies are missing.")
        print("Please install them using: pip install -r requirements.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()

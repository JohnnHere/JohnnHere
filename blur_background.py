#!/usr/bin/env python3
"""
Script to blur the background of an image while keeping the person in focus.
Uses MediaPipe for person segmentation and OpenCV for image processing.
"""

import cv2
import numpy as np
import mediapipe as mp
from PIL import Image
import sys


def blur_background(image_path, output_path, blur_strength=35):
    """
    Blur the background of an image while keeping the person in focus.
    
    Args:
        image_path: Path to input image
        output_path: Path to save output image
        blur_strength: Strength of blur effect (higher = more blur)
    """
    # Initialize MediaPipe Selfie Segmentation
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image from {image_path}")
        return False
    
    # Convert BGR to RGB for MediaPipe
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image with MediaPipe
    with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_segmentation:
        results = selfie_segmentation.process(image_rgb)
        
        # Get the segmentation mask
        mask = results.segmentation_mask
        
        # Create a binary mask (person vs background)
        # Values close to 1 are foreground (person), close to 0 are background
        mask_binary = (mask > 0.5).astype(np.uint8)
        
        # Smooth the mask edges for better blending
        mask_smooth = cv2.GaussianBlur(mask_binary.astype(float), (21, 21), 0)
        mask_smooth = np.clip(mask_smooth, 0, 1)
        
        # Create blurred version of the entire image
        blurred = cv2.GaussianBlur(image, (blur_strength, blur_strength), 0)
        
        # Expand mask to 3 channels
        mask_3channel = np.stack([mask_smooth] * 3, axis=-1)
        
        # Blend original (person) with blurred (background)
        output = (image * mask_3channel + blurred * (1 - mask_3channel)).astype(np.uint8)
        
        # Save the output
        cv2.imwrite(output_path, output)
        print(f"✓ Background blurred successfully!")
        print(f"✓ Output saved to: {output_path}")
        
        return True


def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python blur_background.py <input_image> [output_image] [blur_strength]")
        print("\nExample: python blur_background.py input.jpg output.jpg 35")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "output_blurred.jpg"
    blur_strength = int(sys.argv[3]) if len(sys.argv) > 3 else 35
    
    # Ensure blur strength is odd (required for GaussianBlur)
    if blur_strength % 2 == 0:
        blur_strength += 1
    
    print(f"Processing image: {input_path}")
    print(f"Blur strength: {blur_strength}")
    print(f"Output will be saved to: {output_path}")
    print("\nProcessing...")
    
    success = blur_background(input_path, output_path, blur_strength)
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()

# Background Blur Tool

A Python tool to blur the background of images while keeping the person in focus.

## Features

- Automatic person detection and segmentation
- Smooth background blur effect
- Adjustable blur strength
- Easy to use command-line interface

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python blur_background.py input.jpg
```

Specify output file:
```bash
python blur_background.py input.jpg output.jpg
```

Adjust blur strength (default is 35):
```bash
python blur_background.py input.jpg output.jpg 45
```

## How it works

The tool uses:
- **MediaPipe Selfie Segmentation** for accurate person detection
- **OpenCV** for image processing and blur effects
- Gaussian blur for smooth background effect
- Automatic edge smoothing for natural-looking results

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy
- Pillow

See `requirements.txt` for specific versions.

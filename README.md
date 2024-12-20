# Face Anonymizer

Face Anonymizer is a Python project that detects and anonymizes faces in images and videos. This project uses computer vision techniques to ensure privacy by blurring the face.

## Features

- Detect faces in images and videos
- Anonymize faces by blurring or pixelating
- Support for multiple image and video formats
- Easy to use command-line interface

## Tools Used

- OpenCV
- MediaPipe

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JenilPadshala/Face-Anonymizer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Face-Anonymizer
   ```
3. Install the required dependencies:
   ```bash
   poetry install
   ```

## Usage

### Anonymize an Image

To anonymize faces in an image, run the following command:

```bash
python main.py --mode image --srcPath ./data/testImg.png --dstFileName output_image.png
```

### Anonymize a Videos

To anonymize faces in a video, run the following command:

```bash
python main.py --mode video --srcPath ./data/testVideo.mp4 --dstFileName output_video.mp4
```

### Anonymize in a Webcam

To anonymize face in a webcam video, run the following command:

```bash
python main.py --mode webcam
```

### Command-Line Arguments

- `--mode`: Specifies the mode of operation. It can be one of the following:

  - `image`(default): Process a single image.
  - `video`: Process a video file.
  - `webcam`: Process video from the webcam.

- `--srcPath`: Specifies the source path of the input file (image or video). This argument is required for `image` and `video` modes.

- `--dstFileName`:Specifies the destination filename for the output file (image or video).

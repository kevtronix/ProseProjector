# ProseProjector

This project generates a narrated video using user-defined input text. The narration is presented alongside relevant images and user-specified background music.

## Features

    Converts user input into narrated speech.
    Fetches and presents relevant images based on the narration.
    Allows users to overlay custom background music over the narration.

## Prerequisites
System Requirements

    Python 3.7+
    NVIDIA CUDA compatible GPU. Tested specifically on an NVIDIA RTX 3080 GPU.

## Essential Dependancies 
for a full list see requirements.txt


    moviepy==1.0.3         # For video generation and editing
    noisereduce==2.0.1    # For audio noise reduction
    diffusers==0.19.3     # For using language models
    nltk==3.8.1           # Natural Language Toolkit
    numpy==1.24.4         # Numerical computations
    touch==2.0.1          # PyTorch deep learning framework
    torchaudio==2.0.2     # Audio processing for PyTorch
    torchvision==0.15.2   # Image processing for PyTorch
    transformers==4.31.0  # Huggingface's transformers library
    opencv-python==4.8.0.76 # Computer vision library
    Pillow==10.0.0         # Image processing library
    beautifulsoup4==4.12.2 # For web scraping 


You can install these dependencies using pip:


    pip install -r requirements.txt

## Language Models

The project specifically uses the following models from the diffusers library:

    Image generation: "kandinsky-community/kandinsky-2-2-decoder"
    Music generation: "facebook/musicgen-small"
    Voice generation: "suno/bark"

## Quick Start

Clone the repository

Install the required packages:


    pip install -r requirements.txt

Create .env file with the following:

    DEBUG
    URL
    VOICE_PRESET
    MUSIC_PRESET

Run the main script (example):

    python main.py 

## Progress:
- basic webscrapping 
- voice generation using bark model 
- music generation functionality 
- image generation ability
- video compliation ability
- error checking in code
- refactor code


## TODO:
- optimizations for user (set more items as enviornment variables)
- ability to regenerate specific content and not everything all at once
- ability to additonal keywords and to each model to refine generated content 
- optimize voice generation to remove hallucinations using local bark model
- optimize generated music
- optimize generated images
- different image and voice generation modules to generate low and high quality content
- abiltity to customize content generation parameters via enviorment variables
- test main functionality
# MLOps-1
# Image Classification with ResNet18

## Overview

This project demonstrates an image classification application using a pre-trained ResNet18 model from PyTorch's torchvision library. The application is built with Gradio, providing a user-friendly interface for uploading images and receiving predictions. The model is trained on the ImageNet dataset and classifies images into one of 1,000 categories.

## Project Files

- `app.py`: The main application file containing the image classification logic and Gradio interface.
- `requirements.txt`: A file listing the dependencies required to run the project.
- `MLOps.ipynb`: A Jupyter notebook that demonstrates how to use the model and the Gradio interface.

## Setup Instructions

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/ramday/MLOps-1.git

2. **Navigate to the Project Directory:**
cd MLOps-1

3. **Create a Virtual Environment (optional but recommended):**
   python -m venv venv
4. **Activate the Virtual Environment:**
   window:
   venv\Scripts\activate
   macOS/Linux:
   source venv/bin/activate
5. **Install Dependencies:**
   pip install -r requirements.txt
6. **Run the Application:**
   python app.py
7.**Open the Application in Your Browser:**
   The Gradio interface will be accessible in your default web browser, usually at http://localhost:7860.

**Dependencies**
The project requires the following Python packages:

torch: A deep learning framework for training and deploying models.
torchvision: A library for computer vision tasks, including pre-trained models.
gradio: A library for creating user interfaces for machine learning models.
requests: A library for making HTTP requests to download resources.

**To install these dependencies, use:**

pip install -r requirements.txt

**How to Use**
1.Open the Application:
Launch the Gradio interface using the command python app.py.

2.Upload an Image:
Click the "Upload Image" button to select an image file from your computer.

3.Get Prediction:
The application will process the image and display the predicted label based on the ResNet18 model.

**Custom Styling**
The Gradio interface includes custom CSS styling for a sleek and modern look. The background is dark with contrasting text and button colors for improved visibility.

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Contact**
If you have any questions or feedback, please contact me.



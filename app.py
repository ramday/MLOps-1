import torch
import torchvision
from torchvision.models import resnet18
import gradio as gr
import requests

# Download ImageNet class labels
url = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
response = requests.get(url)
imagenet_labels = response.json()

def predict_image(image):
    try:
        # Load the pre-trained ResNet18 model
        model = resnet18(weights=torchvision.models.ResNet18_Weights.IMAGENET1K_V1)
        model.eval()

        # Preprocess the input image
        transform = torchvision.transforms.Compose([
            torchvision.transforms.Resize(256),
            torchvision.transforms.CenterCrop(224),
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        image_tensor = transform(image)
        image_tensor = image_tensor.unsqueeze(0)

        # Use the model to make a prediction
        with torch.no_grad():
            output = model(image_tensor)
            _, predicted = torch.max(output.data, 1)

        # Get the class label
        predicted_label = imagenet_labels[predicted[0].item()]

        return f"The image is a {predicted_label}."
    except Exception as e:
        return f"Error: {str(e)}"

# Create the Gradio interface
gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image Classification",
    description="Upload an image and I'll classify it using a pre-trained ResNet18 model.",
    theme="dark"
).launch()

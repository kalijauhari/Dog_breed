import ast
from PIL import Image
import torchvision.transforms as transforms
import torchvision.models as models
import torch 

# Load pre-trained models
resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

# Dictionary mapping class indices to class names
with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

# Function to classify the image using the specified model
def classifier(img_path, model_name):
    # Load the image
    img_pil = Image.open(img_path)

    # Define image transformations
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # Preprocess the image
    img_tensor = preprocess(img_pil)
    img_tensor.unsqueeze_(0)  # Add batch dimension

    # Load the specified model
    model = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}[model_name]

    # Set the model to evaluation mode
    model = model.eval()

    # Perform inference
    with torch.no_grad():
        output = model(img_tensor)

    # Get the predicted class index
    pred_idx = output.data.numpy().argmax()

    # Map the predicted class index to class name
    classification_result = imagenet_classes_dict[pred_idx]

    return classification_result

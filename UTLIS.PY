from PIL import Image
import torch
from torchvision import transforms

def load_image(path, max_size=400):
    image = Image.open(path).convert('RGB')

    size = max_size if max(image.size) > max_size else max(image.size)

    transform = transforms.Compose([
        transforms.Resize(size),
        transforms.ToTensor(),
    ])

    image = transform(image).unsqueeze(0)
    return image

def save_image(tensor, path):
    image = tensor.clone().detach().squeeze(0)
    image = transforms.ToPILImage()(image)
    image.save(path)

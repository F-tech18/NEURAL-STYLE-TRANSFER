import torch
from style_transfer import StyleTransfer
from utils import load_image, save_image

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

content = load_image("content.jpg").to(device)
style = load_image("style.jpg").to(device)

model = StyleTransfer(device)

output = model.transfer(content, style, steps=300)

save_image(output, "output/styled_image.jpg")

print("✅ Style transfer completed! Check output folder.")import torch
from style_transfer import StyleTransfer
from utils import load_image, save_image

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

content = load_image("content.jpg").to(device)
style = load_image("style.jpg").to(device)

model = StyleTransfer(device)

output = model.transfer(content, style, steps=300)

save_image(output, "output/styled_image.jpg")

print("✅ Style transfer completed! Check output folder.")

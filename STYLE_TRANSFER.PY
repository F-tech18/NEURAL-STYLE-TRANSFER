import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models

class StyleTransfer:
    def __init__(self, device):
        self.device = device
        self.cnn = models.vgg19(pretrained=True).features.to(device).eval()

    def gram_matrix(self, input):
        b, c, h, w = input.size()
        features = input.view(c, h * w)
        G = torch.mm(features, features.t())
        return G.div(c * h * w)

    def get_features(self, image, layers=None):
        if layers is None:
            layers = {
                '0': 'conv1_1',
                '5': 'conv2_1',
                '10': 'conv3_1',
                '19': 'conv4_1',
                '28': 'conv5_1'
            }

        features = {}
        x = image
        for name, layer in self.cnn._modules.items():
            x = layer(x)
            if name in layers:
                features[layers[name]] = x
        return features

    def transfer(self, content, style, steps=300):
        content_features = self.get_features(content)
        style_features = self.get_features(style)

        style_grams = {layer: self.gram_matrix(style_features[layer])
                       for layer in style_features}

        target = content.clone().requires_grad_(True).to(self.device)
        optimizer = optim.Adam([target], lr=0.003)

        for step in range(steps):
            target_features = self.get_features(target)

            content_loss = torch.mean(
                (target_features['conv4_1'] - content_features['conv4_1'])**2
            )

            style_loss = 0
            for layer in style_grams:
                target_feature = target_features[layer]
                target_gram = self.gram_matrix(target_feature)
                style_gram = style_grams[layer]

                _, c, h, w = target_feature.shape
                style_loss += torch.mean((target_gram - style_gram)**2)

            total_loss = content_loss + 1e6 * style_loss

            optimizer.zero_grad()
            total_loss.backward()
            optimizer.step()

            if step % 50 == 0:
                print(f"Step {step}, Loss: {total_loss.item()}")

        return target

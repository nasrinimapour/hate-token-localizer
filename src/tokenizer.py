import torch
from taming.models.vqgan import VQModel
from torchvision import transforms
from PIL import Image
import numpy as np


class VQGANTokenizer:
    def __init__(self, config_path, checkpoint_path, device='cuda'):
        from omegaconf import OmegaConf
        from taming.models.vqgan import VQModel

        self.device = device
        config = OmegaConf.load(config_path)
        model = VQModel(**config.model.params)
        model.eval().requires_grad_(False)
        model.load_state_dict(torch.load(checkpoint_path, map_location=device)['state_dict'])
        self.model = model.to(device)

        self.preprocess = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor(),
            transforms.Normalize([0.5], [0.5])
        ])

    def tokenize(self, image: Image.Image):
        image_tensor = self.preprocess(image).unsqueeze(0).to(self.device)
        z, _, [_, _, indices] = self.model.encode(image_tensor)
        z_q = self.model.quantize.get_codebook_entry(indices, shape=None)
        return indices.squeeze().cpu().numpy(), z_q.squeeze().cpu().numpy()

    def get_codebook(self):
        return self.model.quantize.embedding.weight.data.cpu().numpy()

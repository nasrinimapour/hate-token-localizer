import clip
import torch


class HatePromptEncoder:
    def __init__(self, prompts, device='cuda'):
        self.model, _ = clip.load("ViT-B/32", device=device)
        self.device = device
        self.prompts = prompts
        self.embeddings = self.encode_prompts(prompts)

    def encode_prompts(self, prompts):
        text_tokens = clip.tokenize(prompts).to(self.device)
        with torch.no_grad():
            embeddings = self.model.encode_text(text_tokens)
            return embeddings / embeddings.norm(dim=-1, keepdim=True)

    def get_embeddings(self):
        return self.embeddings

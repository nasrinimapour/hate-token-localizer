from .utils import cosine_similarity, token_to_box
import torch

class HateLocalizer:
    def __init__(self, tokenizer, hate_encoder, threshold=0.3, grid_size=16):
        self.tokenizer = tokenizer
        self.hate_encoder = hate_encoder
        self.threshold = threshold
        self.grid_size = grid_size

    def localize(self, image):
        token_indices, token_embeddings = self.tokenizer.tokenize(image)
        hate_embs = self.hate_encoder.get_embeddings()

        sims = cosine_similarity(token_embeddings, hate_embs)
        max_sims, _ = sims.max(dim=1)

        boxes = [token_to_box(i, self.grid_size)
                 for i, s in enumerate(max_sims) if s > self.threshold]

        return {"boxes": boxes, "sims": max_sims.tolist()}

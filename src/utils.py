import torch

def cosine_similarity(a, b):
    a = torch.tensor(a).float()
    b = torch.tensor(b).float()
    a = a / a.norm(dim=-1, keepdim=True)
    b = b / b.norm(dim=-1, keepdim=True)
    return torch.mm(a, b.T)

def token_to_box(index, grid_size, patch_size=16):
    row = index // grid_size
    col = index % grid_size
    x = col * patch_size
    y = row * patch_size
    return (x, y, x + patch_size, y + patch_size)

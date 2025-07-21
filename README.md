## Hate Token Localizer 🔍

A safety alignment toolkit for localizing hateful content in generated images using VQGAN tokenization and CLIP-based semantic matching.

### 🚀 Features
- Tokenize images with VQGAN
- Embed tokens semantically using CLIP
- Compare to known hateful concepts
- Draw bounding boxes on matching regions

### 📦 Installation

```bash
git clone https://github.com/nasrinimapour/hate-token-localizer.git
cd hate-token-localizer
pip install .
```

Or for development:

```bash
pip install -e .
```

### 🧪 Usage

```python
from src.localizer import HateLocalizer
from src.hate_embeddings import HatePromptEncoder
from src.tokenizer import VQGANTokenizer
from src.visualize import visualize_boxes
from PIL import Image

# Initialize models
tokenizer = VQGANTokenizer("configs/vqgan.yaml", "vqgan.ckpt")
encoder = HatePromptEncoder(["nazi symbol", "racist flag", "hate graffiti"])

localizer = HateLocalizer(tokenizer, encoder)
image = Image.open("your_image.jpg").convert("RGB")
results = localizer.localize(image)

# Draw and show
out = visualize_boxes(image, results["boxes"])
out.show()
```

---

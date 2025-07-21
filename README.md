## Hate Token Localizer 🔍

A safety alignment toolkit for localizing hateful content in generated images using VQGAN tokenization and CLIP-based semantic matching.

### 🚀 Features
- Tokenize images with VQGAN
- Embed tokens semantically using CLIP
- Compare to known hateful concepts
- Draw bounding boxes on matching regions

### 📦 Installation

This project requires a specific version of Python and several dependencies with strict version requirements. Please follow these steps carefully to set up the environment using Conda.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/nasrinimapour/hate-token-localizer.git](https://github.com/nasrinimapour/hate-token-localizer.git)
    cd hate-token-localizer
    ```

2.  **Create and activate the Conda environment:**
    This project requires **Python 3.8**. The following command will create a new Conda environment with the correct Python version.
    ```bash
    conda create --name hate-token-legacy-env python=3.8
    conda activate hate-token-legacy-env
    ```

3.  **Install PyTorch and Torchvision:**
    These packages must be installed manually from the PyTorch download server before installing the rest of the project.
    ```bash
    pip install torch==1.7.1+cpu torchvision==0.8.2+cpu -f [https://download.pytorch.org/whl/torch_stable.html](https://download.pytorch.org/whl/torch_stable.html)
    ```

4.  **Install the project and remaining dependencies:**
    This command will install the `hate-token-localizer` package and all other required libraries listed in `setup.py`.
    ```bash
    pip install .
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

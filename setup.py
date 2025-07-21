from setuptools import setup, find_packages

setup(
    name="hate-token-localizer",
    version="0.1.0",
    description="Localize hateful content in images using tokenization and CLIP similarity.",
    author="Nasrin",
    author_email="nasrin.imanpour@gmail.com",
    url="https://github.com/nasrinimanpour/hate-token-localizer",
    packages=find_packages(include=["src", "src.*"]),
    install_requires=[
        "torch==1.7.1",
        "clip-by-openai",
        "taming-transformers",
        "omegaconf",
        "Pillow",
        "numpy",
        "torchvision==0.8.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

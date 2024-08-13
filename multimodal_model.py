# models/multimodal_model.py

from transformers import CLIPProcessor, CLIPModel
import torch
from PIL import Image
import requests
from io import BytesIO

class MultimodalModel:
    def __init__(self, model_path: str):
        # Initialize the CLIP model and processor
        self.model = CLIPModel.from_pretrained(model_path)
        self.processor = CLIPProcessor.from_pretrained(model_path)

    def process_text(self, text: str) -> torch.Tensor:
        # Tokenize and encode the text
        inputs = self.processor(text=[text], return_tensors="pt", padding=True)
        text_features = self.model.get_text_features(**inputs)
        return text_features

    def process_image(self, image_url: str) -> torch.Tensor:
        # Load and preprocess the image
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        inputs = self.processor(images=image, return_tensors="pt")
        image_features = self.model.get_image_features(**inputs)
        return image_features

    def compare_text_and_image(self, text: str, image_url: str) -> float:
        # Compare text and image to see if they match
        text_features = self.process_text(text)
        image_features = self.process_image(image_url)
        # Calculate cosine similarity between text and image features
        similarity = torch.nn.functional.cosine_similarity(text_features, image_features)
        return similarity.item()

    def process_text_and_image(self, text: str, image_url: str) -> str:
        # Process both text and image and provide a combined result
        similarity_score = self.compare_text_and_image(text, image_url)
        return f"The similarity between the text and image is: {similarity_score:.4f}"


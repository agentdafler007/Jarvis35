from agents.base_agent import BaseAgent
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
import cv2
import numpy as np
from skimage import filters, color, transform
import imageio
import os
import torch
import torchvision.transforms as T
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from wand.image import Image as WandImage
import cairo

class PhotoshopAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.model = fasterrcnn_resnet50_fpn(pretrained=True)
        self.model.eval()

    async def perform_task(self, task_description: str, image_path: str):
        self.log(f"PhotoshopAgent performing task: {task_description}")
        try:
            image = Image.open(image_path)

            # Apply a series of advanced image processing techniques
            if "blur" in task_description:
                image = self.apply_blur(image)
            if "contrast" in task_description:
                image = self.adjust_contrast(image, 1.5)
            if "edge detection" in task_description:
                image = self.apply_edge_detection(image)
            if "grayscale" in task_description:
                image = self.convert_to_grayscale(image)
            if "resize" in task_description:
                image = self.resize_image(image, (800, 600))
            if "text" in task_description:
                image = self.add_text(image, "Sample Text", position=(50, 50))
            if "rotate" in task_description:
                image = self.rotate_image(image, 45)
            if "colorize" in task_description:
                image = self.colorize_image(image)
            if "object detection" in task_description:
                image = self.object_detection(image)

            output_path = self.save_image(image, image_path)
            return f"Image processed and saved to {output_path}"
        except Exception as e:
            return f"Failed to perform task: {str(e)}"

    def apply_blur(self, image):
        return image.filter(ImageFilter.GaussianBlur(radius=2))

    def adjust_contrast(self, image, factor):
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(factor)

    def apply_edge_detection(self, image):
        open_cv_image = np.array(image)
        open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
        edges = cv2.Canny(open_cv_image, 100, 200)
        edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        return Image.fromarray(cv2.cvtColor(edges_colored, cv2.COLOR_BGR2RGB))

    def convert_to_grayscale(self, image):
        return image.convert("L")

    def resize_image(self, image, size):
        return image.resize(size, Image.ANTIALIAS)

    def add_text(self, image, text, position, font_size=20):
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial", font_size)
        draw.text(position, text, (255, 255, 255), font=font)
        return image

    def rotate_image(self, image, angle):
        return image.rotate(angle)

    def colorize_image(self, image):
        with WandImage(blob=image.tobytes(), format='png') as wand_image:
            wand_image.type = 'grayscale'
            wand_image.colorize(color='blue', alpha='rgb(0, 0, 255)')
            return Image.frombytes('RGB', wand_image.size, wand_image.make_blob('rgb'))

    def object_detection(self, image):
        transform = T.Compose([
            T.Resize((800, 600)),
            T.ToTensor(),
        ])
        image_tensor = transform(image).unsqueeze(0)

        with torch.no_grad():
            outputs = self.model(image_tensor)

        # Process outputs to draw bounding boxes on the image
        # This is a placeholder for drawing logic
        # You would iterate over outputs and draw boxes on the image

        return image

    def save_image(self, image, original_path):
        base, ext = os.path.splitext(original_path)
        output_path = f"{base}_processed{ext}"
        image.save(output_path)
        return output_path

    def log(self, message: str):
        print(message)

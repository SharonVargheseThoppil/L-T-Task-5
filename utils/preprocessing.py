import numpy as np
from PIL import Image


# CIFAR-10 class names
CLASS_NAMES = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]


def preprocess_image(image):
    """
    Preprocess an uploaded image for the CIFAR-10 CNN model.

    Steps:
    1. Convert image to RGB
    2. Resize to 32x32
    3. Convert to NumPy array
    4. Normalize pixel values to 0-1
    5. Add batch dimension
    """

    image = image.convert("RGB")
    image = image.resize((32, 32))

    image_array = np.array(image, dtype=np.float32)

    # Normalize pixel values
    image_array = image_array / 255.0

    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    return image_array
from PIL import Image
import numpy as np
import random

def analyze_style():
    return random.choice(["Casual", "Formal", "Sporty", "Streetwear"])

def suggest_sneaker_type(style):
    mapping = {
        "Casual": ["White Leather Sneakers", "Low-top Canvas"],
        "Formal": ["Minimalist Black Sneakers"],
        "Sporty": ["Running Shoes", "Cross Trainers"],
        "Streetwear": ["Chunky Sneakers", "High-tops"]
    }
    return random.choice(mapping[style])

def get_dominant_color(image):
    img = image.resize((100, 100))
    data = np.array(img).reshape(-1, 3)
    dominant = np.mean(data, axis=0)
    return tuple(int(c) for c in dominant)

def color_suggestion(rgb):
    r, g, b = rgb
    if r > 200 and g > 200 and b > 200:
        return "White or light-colored sneakers"
    elif r < 80 and g < 80 and b < 80:
        return "Black or dark-themed sneakers"
    else:
        return "Neutral or color-block sneakers"

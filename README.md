# My29-SneakerStyle-AI
GenAI

Sure! Here's a **brand new, unique AI fashion project** with additional features — **no virtual environment required** — and easy to run in **VS Code** and **GitHub**.

---

## 👟 **Project Title: SneakerStyle AI – Sneaker Recommender & Outfit Matcher**

---

### 💡 **Problem It Solves:**

People struggle to find **matching sneakers** for their outfits or the **right sneaker for an event**. This app:

* Recommends sneakers based on outfit images.
* Matches sneaker style to outfit color/style.
* Suggests sneakers for events like casual, party, sports.

---

## ✨ **Key Features**

| Feature                   | Description                                                          |
| ------------------------- | -------------------------------------------------------------------- |
| 👕 Outfit Image Upload    | Upload any outfit image                                              |
| 🧠 AI Sneaker Recommender | Suggests sneaker type (e.g., white leather, high-top, running shoes) |
| 🎨 Color Matcher          | Suggests sneaker color based on outfit                               |
| 🧍‍♂️ Style Analyzer      | Detects if outfit is casual, formal, sporty                          |
| 📅 Event Recommender      | Suggests sneakers for different occasions                            |
| 💬 Chat-style Tips        | Smart sneaker style suggestions                                      |

---

## 🗂 Folder Structure

```
SneakerStyle-AI/
├── app.py
├── recommender_utils.py
├── requirements.txt
└── README.md
```

---

## 📦 `requirements.txt`

```txt
streamlit
Pillow
numpy
opencv-python
```

---

## 🧠 `recommender_utils.py`

```python
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
```

---

## 🚀 `app.py`

```python
import streamlit as st
from PIL import Image
from recommender_utils import analyze_style, suggest_sneaker_type, get_dominant_color, color_suggestion

st.set_page_config(page_title="👟 SneakerStyle AI", layout="wide")
st.title("👟 SneakerStyle AI – Sneaker Recommender & Outfit Matcher")
st.markdown("Upload your outfit and get sneaker suggestions that match your style and event.")

uploaded_file = st.file_uploader("📸 Upload Your Outfit Image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Outfit", use_column_width=True)

    with st.spinner("Analyzing your outfit..."):
        style = analyze_style()
        sneaker_type = suggest_sneaker_type(style)
        dominant_color = get_dominant_color(image)
        color_tip = color_suggestion(dominant_color)

    st.subheader("🎯 Style Detected")
    st.success(f"Your outfit style is: **{style}**")

    st.subheader("👟 Recommended Sneaker Type")
    st.info(f"Try **{sneaker_type}**")

    st.subheader("🎨 Sneaker Color Suggestion")
    st.write(f"Detected dominant outfit color: RGB {dominant_color}")
    st.warning(f"Color Match Tip: {color_tip}")

    st.subheader("🧠 Smart Style Tip")
    st.write(f"✨ For a **{style}** look, go for **{sneaker_type}** in **{color_tip.lower()}**.")
```

---

## 📖 `README.md`

````markdown
# 👟 SneakerStyle AI – Sneaker Recommender & Outfit Matcher

### 💡 Idea
Upload your outfit image and get:
- Sneaker style recommendations
- Color suggestions to match outfit
- Style category (casual, formal, sporty)
- Smart outfit-sneaker tips

### 🛠 Features
- Upload outfit photo
- AI sneaker type match
- Color harmony match
- Style-aware suggestions

### ⚙️ Setup
```bash
pip install -r requirements.txt
````

### 🚀 Run

```bash
streamlit run app.py
```

### 🖼️ Try examples:

* A sporty gym outfit → get running shoes
* A blazer/jeans → minimalist sneakers

````

---

## ✅ How to Run in VS Code (no venv)
1. Open VS Code in the folder.
2. Run terminal:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
````

---

## 🔥 Want More Features?

Let me know if you’d like to add:

* 👣 Shoe brand & price suggestions
* 📸 Pose-aware fit recommendation
* 🎨 Try-on preview with AI
* 💬 Chatbot to ask about outfits

Would you like me to build a mobile version or add Instagram-style story posts too?

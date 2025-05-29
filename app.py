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

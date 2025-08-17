import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Group Project Dashboard", layout="wide")
st.title("Data Visualization: Main Results of Country Specific Data and General")

root = Path(".")
figdir = root / "figures"



img_paths = [p for p in figdir.glob("*") if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]
if not img_paths:
    st.error("No image files found in figures/. Double-check branch, folder name, and filenames.")
else:
    img_paths = sorted(img_paths, key=lambda p: p.name.lower())
    cols = st.columns(2)
    for i, p in enumerate(img_paths):
        with cols[i % 2]:
            st.image(str(p), caption=p.stem, use_container_width=True)




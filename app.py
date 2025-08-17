import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Group Project Dashboard", layout="wide")
st.title("Main results (screenshots)")

root = Path(".")
figdir = root / "figures"

# Debug info (remove later)
st.write("Branch/repo working dir:", root.resolve().as_posix())
st.write("figures/ exists:", figdir.exists())
if figdir.exists():
    st.write("Files in figures/:", sorted(p.name for p in figdir.iterdir()))

# Load whatever images actually exist
img_paths = [p for p in figdir.glob("*") if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]
if not img_paths:
    st.error("No image files found in figures/. Double-check branch, folder name, and filenames.")
else:
    img_paths = sorted(img_paths, key=lambda p: p.name.lower())
    cols = st.columns(2)
    for i, p in enumerate(img_paths):
        with cols[i % 2]:
            st.image(str(p), caption=p.stem, use_container_width=True)




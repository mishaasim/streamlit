import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Group Project Dashboard", layout="wide")
st.title("Main results (screenshots + captions)")

IMG_DIR = Path("figures")
CSV_PATH = IMG_DIR / "captions.csv"

# Safety checks
if not CSV_PATH.exists():
    st.error("Missing captions file at figures/captions.csv")
else:
    df = pd.read_csv(CSV_PATH)

    cols = st.columns(2)
    missing = []
    for i, row in df.iterrows():
        fname = str(row["filename"]).strip()
        cap = str(row["caption"]).strip()
        p = IMG_DIR / fname
        if p.exists():
            with cols[i % 2]:
                st.image(str(p), caption=cap, use_container_width=True)
        else:
            missing.append(fname)

    if missing:
        st.warning("Missing files in figures/: " + ", ".join(missing))

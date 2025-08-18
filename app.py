import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Group Project Dashboard", layout="wide")
st.title("Implications of Factors on CO2 Emissions in Pakistan")
st.caption("A Case Study by Dylan Hayes and Misha Asim")
st.subheader("📓 Run the Jupyter Notebook")

st.markdown(
    """
    [![Binder](https://mybinder.org/badge_logo.svg)](
    https://mybinder.org/v2/gh/mishaasim/streamlit/main?labpath=Group%20Project%20MA%26DH%20Final%20%281%29.ipynb)
    &nbsp;&nbsp;
    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
    https://colab.research.google.com/github/mishaasim/streamlit/blob/main/Group%20Project%20MA%26DH%20Final%20%281%29.ipynb)
    """,

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
import streamlit as st

st.subheader("📓 Run the Jupyter Notebook")

st.markdown(
    """
    [![Binder](https://mybinder.org/badge_logo.svg)](
    https://mybinder.org/v2/gh/mishaasim/streamlit/main?labpath=Group%20Project%20MA%26DH%20Final%20%281%29.ipynb)
    &nbsp;&nbsp;
    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
    https://colab.research.google.com/github/mishaasim/streamlit/blob/main/Group%20Project%20MA%26DH%20Final%20%281%29.ipynb)
    """,
    unsafe_allow_html=True,
)

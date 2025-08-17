import streamlit as st

import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Group Project Dashboard", layout="wide")
st.title("Main results (screenshots)")

# Auto-load every image in figures/ and display in two columns
img_paths = sorted(list(Path("figures").glob("*.png")) + list(Path("figures").glob("*.jpg")),
                   key=lambda p: p.name.lower())

cols = st.columns(2)
for i, p in enumerate(img_paths):
    with cols[i % 2]:
        st.image(str(p), caption=p.stem, use_container_width=True)


files = [
    "CO2 Emissions Per Year.png",
    "Pakistan CO2 Emissions Per Year.png",
    "Top 10 CO2 Emitters.png",
    "Top 10 CO2 Emitters Tile Plot.png",
    "Countries CO2 Emissions.png",
    "Distribution Of Indicators.png",
    "Dist. of Indic. Pakistan.png",
    "ScatterPlot CO2 Emissions.png",
    "Pak Emissions and Temp ScatterPlot.png",
    "Pak Emissions and Temp Line of Best Fit.png",
    "Pak Scaled Emissions and Temp.png",
]
for i, name in enumerate(files):
    with cols[i % 2]:
        st.image(f"figures/{name}", caption=name, use_container_width=True)

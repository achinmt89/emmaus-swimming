import streamlit as st
import pandas as pd
import numpy as np

bs_URL = "https://www.environment.nsw.gov.au/beachmapp/Beach/WoolwichBaths"

st.write("BeachSafe by DataBooth.com.au")

st.markdown(bs_URL)

# Add a slider:
    # add_slider = st.sidebar.slider(
add_slider = st.slider(
'What do you consider as the ideal temperature range?',
0.0, 50.0, (15.0, 25.0)
)

# add map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50,50] + [-33.87, 151.2],
    columns=['lat', 'lon'])


st.map(map_data)

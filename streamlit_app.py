import streamlit as st
import pandas as pd
import math
from pathlib import Path
import pandas as pd
import streamlit as st
import math
from pathlib import Path
import plotly.express as px
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import statsmodels.api as sm
import plotly.graph_objects as go

df = pd.read_csv(r'C:\Users\Admin\Documents\Data Science\Python\climate_change_p\climate_change_mod.csv')

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Climate dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.
url = "https://raw.githubusercontent.com/kenzyxriah/Climate-change-analysis/main/climate_change_mod.csv"

@st.cache_data
def load_data():
    return pd.read_csv(url)  

df = load_data()

# Define columns
cat_cols = ['Year', 'Country', 'ISO Country Code', 'Continent']
numeric_cols = ['Avg Temperature (°C)', 'CO2 Emissions (Tons/Capita)', 'Sea Level Rise (mm)', 
                'Rainfall (mm)', 'Population', 'Renewable Energy (%)', 'Extreme Weather Events',
                'Forest Area (%)', 'Rainfall (mm)_per_100', 'Pop_Density(per_100m)']

# Streamlit UI
st.title("Density Plot and Histogram App")

# User selection
x = st.selectbox("Select the numerical column:", numeric_cols)
y = st.selectbox("Select the categorical column for grouping:", cat_cols)
include_hist = st.checkbox("Include Histogram", value=True)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.kdeplot(data=df, x=x, hue=y, fill=False, common_norm=False, ax=ax)

if include_hist:
    ax1 = ax.twinx()
    sns.histplot(data=df, x=x, hue=y, element="step", common_norm=False, alpha=0.3, ax=ax1)

ax.set_title("KDE Density Plot with Optional Histogram")
ax.set_xlabel(x)
ax.set_ylabel("Density")
ax.legend(title=y)

st.pyplot(fig)

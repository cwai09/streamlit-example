import streamlit as st
import numpy as np
import pandas as pd

st.header("Efficiensy of Making Icecream")
st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]
}))

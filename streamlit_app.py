import streamlit as st
import pickle
from model import Recommendation

recommend = Recommendation()

# Streamlit app layout
st.title('Product Recommendation System')

user = st.text_input("User ID", "")

if st.button('Get Recommendations'):
    if user:
        data = recommend.getTopProducts(user)
        if data:
            st.text(data)
        else:
            st.text("No recommendations available.")
    else:
        st.write("Please enter a User ID.")

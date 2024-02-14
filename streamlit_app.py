import streamlit as st
import pickle
from model import Recommendation

recommend = Recommendation()

# Streamlit app layout
st.title('Product Recommendation System')

user = st.text_input("User ID", "", placeholder= "Try kimmie, warren or danielle maybe? Sample users for you")

if st.button('Get Recommendations'):
    if user:
        data = recommend.getTopProducts(user)
        if data:
            st.markdown(data, unsafe_allow_html=True)
        else:
            st.text("No recommendations available.")
    else:
        st.write("Please enter a User ID.")

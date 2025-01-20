import streamlit as st
import pickle
from model import Recommendation

recommend = Recommendation()

# Streamlit app layout
st.title('Product Recommendation System')

user = st.text_input("User ID", "", placeholder= "Try kimmie, warren or danielle maybe?")

if st.button('Get Recommendations'):
    if user:
        data = recommend.getTopProducts(user)
        if data:
            st.markdown(data, unsafe_allow_html=True)
        else:
            st.text("No recommendations available.")
    else:
        st.write("Please enter a User ID.")

# Adding the note at the bottom
st.markdown("---")  # Adds a horizontal rule for separation
st.markdown(
    "**Note:** *This system is for demonstration purposes only.* "
    "*Providing a list of all usernames is not practical in this case. Please try out the test names. If you need more, you can always reach out*"
)

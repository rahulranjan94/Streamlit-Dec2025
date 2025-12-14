import streamlit as st

st.title("My Streamlit App")
st.subheader("Deploying using :blue[Streamlit Cloud]")
st.write("We are learning streamlit for the first time")
agree = st.checkbox("I agree with Rahul ")

if agree:
    st.write("You are great!")

genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy","Drama", "Documentary"],
)

if genre == "Comedy":
    st.write("You comedy me ... Hahaha!!")
elif genre == "Drama":
    st.write("You drama me ... Boohoo!")
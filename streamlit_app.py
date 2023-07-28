import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My Parents New Healthy Diner')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text(' 🥣Omega3 and Blueberry Oatmeal')
streamlit.text(' 🥗Kale,Spinach and Rocket smoothie')
streamlit.text(' 🐔Hard Boiled Free Range Eggs')
streamlit.text(' 🥑🍞Hard Boiled Free Range Eggs')
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

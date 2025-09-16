import pandas as pd
import streamlit as st
import plotly.express as px

books_df = pd.read_csv('file.csv')

st.title('Best-selling books')
st.write('This app shows the best-selling books from Amazon 2009-2025')
st.subheader('Summary Statistics')
total_books = books_df.shape[0]
unique_title = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1,col2,col3,col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_title)
col3.metric("Average Rating", average_rating)
col4.metric("Average Price", average_price)

# df = pd.DataFrame({
#     'Name': ['Lisa', 'Suela', 'Rita'],
#     'Age' : [15,16,17],
#     'City' : ['Stockholm', 'Edinburgh', 'Paris']
# }
# )

# st.write(df)
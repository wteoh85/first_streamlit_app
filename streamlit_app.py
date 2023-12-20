import streamlit
import pandas
import requests
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

streamlit.text("THE FRIUT LOAD LIST CONTAINS:")
streamlit.text(my_data_row)

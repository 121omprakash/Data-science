import streamlit as st
import datetime
st.header('1. Text Input')
# taking input from user
name =st.text_input('Enter your name',value='Om Prakash')
st.write('Hello',name)

st.subheader('2. Text Area')
text_area = st.text_area('Tell me your summary',height=100,max_chars=200)
st.subheader('3. Password_Input')
password = st.text_input('Enter your password',type='password',max_chars=10)
st.subheader('4. Numeric Input')
num = st.number_input('Enter your age',min_value=10 ,max_value=50)

st.subheader('5. Date')
today = datetime.date.today()
date = st.date_input('Enter the date',min_value=today, max_value=today.replace(year=today.year+1))

st.subheader('6. ')
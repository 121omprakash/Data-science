#export PATH="$PATH:$HOME/.local/bin" --> cd Streamlit --> streamlit run filename
import streamlit as st
#title
st.title('Portfolio')
#header
st.header('Header')
#subheader
st.subheader('Subheader')
#text
st.text('Text')
#markdown
st.markdown('# This is h1')
st.markdown('## This is h2')
st.markdown('### This is h3')
st.markdown('#### This is h4')
st.markdown('##### This is h5')
st.markdown('###### This is h6')
#paragraph tag
st.markdown('This is paragraph tag')
#bold
st.markdown('This is **bold**')
st.markdown('This is __bold__')
#italics
st.markdown('This is *italics*')
st.markdown('This is _italics_')

#italics and bold
st.markdown('This is ***bold+italics***')
st.markdown('This is ___bold+italics___')
#ordered list
st.markdown('''1.First point''')
#Unordered list
st.markdown('- First Point')
st.markdown('- second Point')

# writitng
st.write('This is write tag')
st.write(range(10,20))
st.write('range(10,20)')
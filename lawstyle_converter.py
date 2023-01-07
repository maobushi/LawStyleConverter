import streamlit as st

st.title("国際法フォーマット変換(ver:1.0)")


last_name = st.text_input('First Name (名前)')
middle_name = st.text_input('Middle Name')
first_name = st.text_input('Last Name(苗字)')

title = st.text_input('書名')
quotation = st.text_input('引用項')
ver = st.text_input('版')
publication_year = st.text_input('出版年')

if len(first_name) != 0:
    st.write(first_name[0].upper() + ". " + last_name.upper() + ", " + title.upper() + " " + quotation + " (" + ver + "th ed. " + publication_year + ").")


st.markdown("[this site made by maobushi](https://twitter.com/maobushi)")

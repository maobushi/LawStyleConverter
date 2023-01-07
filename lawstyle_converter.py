import streamlit as st

st.title("国際法フォーマット変換(ver:1.1)")


last_name = st.text_input('First Name (名前)')
middle_name = st.text_input('Middle Name')
first_name = st.text_input('Last Name(苗字)')

title = st.text_input('書名')
quotation = st.text_input('引用項')
ver = st.text_input('版')
publication_year = st.text_input('出版年')

st.markdown("""---""") 



if len(first_name) != 0:
    output = first_name[0].upper() + ". " + last_name.upper() + ", " + title.upper() + " " + quotation + " (" + ver + "th ed. " + publication_year + ")."
    st.success(output)

st.markdown("""---""") 
st.markdown("this site made by [@maobushi](https://twitter.com/maobushi)")
st.markdown("If you have any problems or requests, please let us know via Twitter DM.")

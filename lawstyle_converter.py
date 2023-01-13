import streamlit as st

st.title("国際法フォーマット変換(ver:1.2)")

choice_list = ["書籍","論文","判例","条約"]
choice = st.selectbox('モードを選択してください',choice_list)


if choice ==  "書籍":
    first_name = st.text_input('First Name (名前)')
    middle_name = st.text_input('Middle Name')
    last_name = st.text_input('Last Name(苗字)')

    title = st.text_input('書名')
    quotation = st.text_input('引用項')
    ver = st.text_input('版')
    publication_year = st.text_input('出版年')

    st.markdown("""---""") 

    if len(first_name) != 0:
        output = first_name[0].upper() + ". " + last_name.upper() + ", " + title.upper() + " " + quotation + " (" + ver + "th ed. " + publication_year + ")."
        st.success("[著者名], [書名] [引用頁] ([版] ed. [出版年]).")
        st.success(output)


elif choice == "論文":
    first_name = st.text_input('First Name (名前)')
    middle_name = st.text_input('Middle Name')
    last_name = st.text_input('Last Name(苗字)')

    title = st.text_input('Title(題名)')
    journal = st.text_input('雑誌名')
    start_page = st.text_input('開始ページ')
    quote_page = st.text_input('引用ページ')
    publication_year = st.text_input('出版年')

    st.markdown("""---""") 

    if len(first_name) != 0:
        output = first_name[0].upper() + ". " + last_name + ", " + title + ", " + journal.upper() + ", " + start_page + ", " + quote_page + " (" + publication_year + ")."
        st.success("[著者], [題名], [巻(号)], [雑誌名], [開始頁], [引用頁] ([年]).")
        st.success(output)

elif choice == "判例":
    
    
    title = st.text_input('Title(題名)')
    
    applicant = st.text_input('Applicant(原告国)')
    respondent = st.text_input('Respondent(被告国)')
    case_type = st.selectbox('種別',('Judgment','Advisory Opinion','Order','Preliminary Objection'))
    publication_year = st.text_input('出版年')
    start_page = st.text_input('Start Page(開始頁)')
    quote_paragraph = st.text_input('Quote Paragraph(引用パラグラフまたは引用頁)')
    date = st.text_input('Date(日付)')
    st.markdown("""---""") 

    if len(title) != 0:
        output = title + "(" + applicant + " v. " + respondent + "), " + case_type+", " + publication_year + " I.C.J. " + start_page + ", ¶ " + quote_paragraph + " (" + date + ")."
        st.success("[事件名] ([原告国] v. [被告国]), [種別], [年] I.C.J. [開始頁], [引用パラグラフ又は引用頁] ([日付]).")
        st.success(output)
elif choice == "条約":
    title = st.text_input('Title(題名)')
    quotation_clause = st.text_input('Quotation Clause(引用条項)')
    date = st.text_input('Date(日付)')
    publication_year = st.text_input('Year(年)')
    volume = st.text_input('Volume(巻)')
    start_page = st.text_input('Start Page(開始頁)')
    st.markdown("""---""") 

    if len(title) != 0:
        output = title + ", " + quotation_clause + ", " + date + ", " + publication_year + ", " + volume + ", U.N.T.S. " + start_page + "."
        st.success("[条約名], [引用条項], [日付], [年], [巻], U.N.T.S. [開始頁].")
        st.success(output)
        
st.markdown("""---""") 
st.markdown("[this site made by maobushi](https://twitter.com/maobushi)")


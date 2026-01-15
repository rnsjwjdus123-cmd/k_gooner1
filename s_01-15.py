import streamlit as st      
#pip install --upgrade streamlit
st.title("이것이 타이틀이다")

st.header("이것이 헤더이다")
st.subheader("이것이 서브헤더이다")
st.text("이것이 텍스트이다")

st.markdown("## 이것이 마크다운이다")

#코드 표시
sample_code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(sample_code, language='python')


st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 :blue[파란색] 볼드체를 설정할 수 있다.")

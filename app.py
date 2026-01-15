import streamlit as st
from processor import process_lecture

st.set_page_config(page_title="Smart Lecture AI", layout="wide")

st.title("🎓 Smart Lecture AI Assistant")
st.write("Upload a lecture audio file to get AI-based explanations.")

uploaded_file = st.file_uploader("Upload Lecture Audio (.wav)", type=["wav"])

if uploaded_file:
    st.audio(uploaded_file)

    if st.button("Analyze Lecture"):
        with st.spinner("Processing using AI..."):
            result = process_lecture(uploaded_file)

        st.success("Done!")

        st.header("📝 Transcript")
        st.write(result["transcript"])

        st.header("📌 Summary")
        st.write(result["summary"])

        st.header("❓ Questions")
        for q in result["questions"]:
            st.write(f"- {q}")

        st.divider()
        st.header("🧠 Concept Explanation")

        with st.expander("Open Explanation Window"):
            for c in result["concepts"]:
                st.subheader(c.capitalize())
                st.write(
                    f"This concept is automatically identified using "
                    f"AI-based Natural Language Processing techniques."
                )

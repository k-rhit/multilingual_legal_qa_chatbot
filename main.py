import streamlit as st
from dotenv import load_dotenv
import os

from app.loader import load_text_from_files
from app.processor import split_into_chunks
from app.vectorstore import build_vectorstore, load_vectorstore
from app.qa_chain import get_chain
from app.translator import detect_language, translate_text
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is missing from .env")
genai.configure(api_key=api_key)

def main():
    st.set_page_config(page_title="🧑‍⚖️ Multilingual Legal Chatbot", layout="wide")

    st.title("📚 Multilingual Legal Q&A Chatbot")
    st.write("Upload legal documents and ask questions related to Indian labor laws.")

    if st.button("🔍 Process Documents"):
        with st.spinner("Reading and processing documents..."):
            raw_text = load_text_from_files()
            chunks = split_into_chunks(raw_text)
            build_vectorstore(chunks)
            st.success("Documents processed and indexed!")

    question = st.text_input("💬 Ask a question in any language:")
    if st.button("🧠 Get Answer"):
        if not question:
            st.warning("Please enter a question.")
            return

        # 🌍 Detect language
        original_lang = detect_language(question)

        # 🌐 Translate question to English if needed
        if original_lang != "en":
            question_in_english = translate_text(question, target_lang="en")
        else:
            question_in_english = question

        # 🔎 Run QA Chain
        qa_chain = get_chain()
        vectorstore = load_vectorstore()
        docs = vectorstore.similarity_search(question_in_english)
        response = qa_chain(
            {"input_documents": docs, "question": question_in_english},
            return_only_outputs=True
        )
        answer_in_english = response.get("output_text", "⚠️ No answer found.")

        # 🔁 Translate answer back to original language
        if original_lang != "en":
            final_answer = translate_text(answer_in_english, target_lang=original_lang)
        else:
            final_answer = answer_in_english

        # Display both
        st.subheader("📜 Answer:")
        st.markdown(f"**Translated Answer:** {final_answer}")
        if original_lang != "en":
            st.markdown(f"<small><i>Original (English):</i></small> {answer_in_english}", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

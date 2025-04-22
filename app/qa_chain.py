from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI

def get_chain():
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        Answer the question as detailed as possible using the context below.
        If not found in context, say:
        "Answer is not available in provided context."

        Context: {context}
        Question: {question}

        Answer:
        """
    )
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
    return load_qa_chain(llm, chain_type="stuff", prompt=prompt_template)

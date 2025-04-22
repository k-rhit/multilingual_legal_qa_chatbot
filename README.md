# multilingual_legal_qa_chatbot
Multilingual Legal Q&A Chatbot answers queries related to Indian labor laws. The chatbot supports multiple languages and leverages Google's Generative AI and Retrieval-Augmented Generation (RAG) for its natural language processing.

Prerequisites
1. Python 3.x (preferably 3.8+)
2. Google API Key: You need a Google API key for accessing Google services like translation.
3. VS Code (or any other IDE)
4. Git for version control (optional but recommended)

Setup & Installation
1. Clone the Repository: Clone the repository to your local machine by running the following command in your terminal
2. Create a Virtual Environment: It's highly recommended to use a virtual environment to manage dependencies. Activate pre-tested environment.yml using conda > conda env create -f environment.yml > conda activate legal_chatbot
 or otherwise pip user can follow steps below mentioned steps
   For Windows: python -m venv legal_chatbot_env
   For Linux/Mac: python3 -m venv legal_chatbot_env
3. Activate the virtual environment:
   For Windows: legal_chatbot_env\Scripts\activate
   For Linux/Mac: source legal_chatbot_env/bin/activate
4. Install Dependencies: Install all the necessary dependencies from the requirements.txt file: pip install -r requirements.txt
   or manually install using: pip install streamlit python-dotenv google-generativeai googletrans==4.0.0-rc1 faiss-cpu langchain
5. Configure the .env File: Create a .env file in the root directory of your project. Inside .env, add your Google API Key as- GOOGLE_API_KEY=your_google_api_key
   You can obtain a Google API Key by following the official guide for setting up the Google Cloud API.

Run the Application
1. Start Streamlit App: run command- streamlit run main.py > This will launch the chatbot interface in your default browser.
2. Upload Documents: Once the app is loaded, you can upload your legal documents (PDF, text, etc.) for processing. The app will read and process these documents and prepare them for querying.
3. Ask a Question: Enter a question related to Indian labor laws in any language. The app will automatically detect the language, translate it to English, process it through the question-answering pipeline, and then translate the answer back to your original language.

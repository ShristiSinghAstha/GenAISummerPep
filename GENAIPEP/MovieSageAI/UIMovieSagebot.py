import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# Page Config
st.set_page_config(
    page_title="MovieSage AI",
    page_icon="🎬",
    layout="centered"
)

# Model
model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0
)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are MovieSage AI, an intelligent movie information extraction assistant.

Your Tasks:
1. Read the movie description.
2. Extract important movie details.
3. Generate a concise summary.
4. Return the result strictly in JSON format.

Extract:
- movie_title
- genre
- release_year
- director
- cast
- language
- rating
- plot_keywords
- summary

Output Format:

                {{
                    "movie_title": "",
                    "genre": [],
                    "release_year": "",
                    "director": "",
                    "cast": [],
                    "language": "",
                    "rating": "",
                    "plot_keywords": [],
                    "summary": ""
                }}

Rules:
- Use null if information is missing.
- Keep summary under 100 words.
- Return ONLY valid JSON.
- Do not use markdown code blocks.
"""
    ),
    ("human", "{movie_description}")
])

# UI
st.title("🎬 MovieSage AI Bot")
st.markdown(
    "Paste a movie description and get structured information in JSON format."
)

movie_description = st.text_area(
    "Movie Description",
    height=250,
    placeholder="Enter or paste a movie paragraph here..."
)

if st.button("Analyze Movie"):

    if movie_description.strip() == "":
        st.warning("Please enter a movie description.")
    else:
        with st.spinner("Analyzing movie..."):

            final_prompt = prompt.invoke({
                "movie_description": movie_description
            })

            response = model.invoke(final_prompt)

        st.success("Analysis Complete!")

        st.subheader("JSON Output")
        st.code(response.content, language="json")
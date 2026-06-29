# MovieSage AI Bot
# Take a raw para about a Movie
# extract important structured info
# generate a clean summary
# returns it into json format

from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate

class Movie(BaseModel):
    title: str
    genre: List[str]
    release_year: Optional[int] 
    cast: List[str]
    director: Optional[str]
    language: Optional[str]
    country: Optional[str]
    plot_summary: List[str] = {"description": "There should be a brief description of the movie plot."}
    main_characters: List[str]=None
    theme: Optional[str]
    notable_awards: List[str]
    box_office_performance: Optional[str]

parser = PydanticOutputParser(pydantic_object=Movie)


from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List,Optional

model = ChatMistralAI(model="mistral-small-2603")

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

{
    "movie_title": "",
    "genre": [],
    "release_year": "",
    "director": "",
    "cast": [],
    "language": "",
    "rating": "",
    "plot_keywords": [],
    "summary": ""
}

Rules:
- Use null if information is missing.
- Keep summary under 100 words.
- Return ONLY valid JSON.
"""
    ),
    ("human", "{movie_description}")
])
para = input("give your paragraph")
final_prompt = prompt.invoke({"movie_description":para},
                                {"format_instructions": parser.get_format_instructions()})
res = model.invoke(final_prompt)
print(res.content)


#AI->JSON->Backend->API->Frontend
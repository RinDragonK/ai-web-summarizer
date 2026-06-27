
from openai import OpenAI

client = OpenAI()


def summarize(text: str):

    response = client.responses.create(

        model="gpt-5-mini",

        input=f"""
Summarize the following article.

{text}
"""

    )

    return response.output_text
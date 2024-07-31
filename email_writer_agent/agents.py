# agents.py

import os
from prompts import *
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key from environment variables
client = Groq(
    api_key = os.getenv("GROQ_API_KEY"),
)

# Define the model to be used
llama_8b = "llama-3.1-8b-instant"

def search_query_generator(user_input):
    """
    Generate search queries based on user input.

    Args:
        user_input (str): The user's input for which to generate search queries.

    Returns:
        list: A list of generated search queries.
    """
    print("\n########\nGenerating the search query for : ", user_input)
    
    # Make API call to generate search queries
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": search_query_generator_system_prompt
            },
            {
                "role": "user",
                "content": search_query_generator_user_prompt.format(user_input=user_input),
            }
        ],
        model=llama_8b,
        temperature=0.7,
    )

    # Extract and return the generated queries
    response = chat_completion.choices[0].message.content.split("\n")
    print("\nThe generated search queries are : ", response)
    return response

def paragraph_writer(query):
    """
    Generate a paragraph based on a given query.

    Args:
        query (str): The query to base the paragraph on.

    Returns:
        str: The generated paragraph.
    """
    print("\n########\nWriting the paragraph for : ", query)
    
    # Make API call to generate a paragraph
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": paragraph_writer_system_prompt,
            },
            {
                "role": "user",
                "content": paragraph_writer_system_prompt.format(query=query),
            }
        ],
        model=llama_8b,
    )
    
    # Extract and return the generated paragraph
    response = chat_completion.choices[0].message.content
    print("\nThe generated paragraph is : ", response)
    return response

def email_writer(user_input, paragraph):
    """
    Generate an email based on user input and a given paragraph.

    Args:
        user_input (str): The user's original input.
        paragraph (str): A paragraph to be included in the email.

    Returns:
        str: The generated email content.
    """
    print("\n########\nWriting the email for : ", user_input)
    
    # Make API call to generate an email
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": email_writer_system_prompt,
            },
            {
                "role": "user",
                "content": email_writer_user_prompt.format(user_input=user_input, paragraph=paragraph),
            }
        ],
        model=llama_8b,
        temperature=0,
    )
    
    # Extract and return the generated email
    response = chat_completion.choices[0].message.content
    print("\nThe generated email is : ", response)
    return response

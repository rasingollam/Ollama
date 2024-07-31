# main.py

from agents import search_query_generator, paragraph_writer, email_writer
from utils import get_user_input

# Get the initial user query
user_query = get_user_input()

# Generate search queries based on the user's input
generated_queries = search_query_generator(user_query)

# Initialize an empty list to store generated paragraphs
generated_paragraphs = []

# Generate a paragraph for each search query
for query in generated_queries:
    paragraph = paragraph_writer(query)
    generated_paragraphs.append(paragraph)

# Convert all paragraphs to strings (in case they aren't already)
generated_paragraphs = [str(paragraph) for paragraph in generated_paragraphs]

# Combine all paragraphs into a single string, separated by newlines
combined_paragraphs = "\n\n".join(generated_paragraphs)

# Generate the final email using the original user query and the combined paragraphs
email_writer(user_query, combined_paragraphs)

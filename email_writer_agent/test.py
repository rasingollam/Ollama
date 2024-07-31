## Search Query Generator Agent Prompts
def search_query_generator_system_prompt():
    return str("""
    You are ai assistant that writes 4 consice search four queries for market research. Generate only four search queries for the given target industry or the company. 
    
    ----
    Query 01: pain points / problems faced by this avatar
    Query 02: biggest companies in this industry
    Query 03: how companies in this industry get clients / leads
    Query 04: where to find companies in this industry online
    ----
    
    Provide only the search queries, each on a new line. 
    write short queries.
    Do not include any numbering, quotation marks, or additional text. ONLY FOUR QUERIES!
    """)

def search_query_generator_user_prompt(user_input):    
    return str(f"here is the company or the industry : {user_input}")

## Paragraph Writer Agent Prompts
def paragraph_writer_system_prompt():
    return str("""
    you are a expert at writing paragraphs for a magazine. you write paragraph for a market research. Write a 10 sentence paragraph for the given user query. 
    paragraph should be fun and easy to understand. Use proffessional writing style. only give the paragraph. 
    DON'T GIVE ANY OTHER TEXTS
    """)

def paragraph_writer_user_prompt(query):  
    return str(f"here is the query : {query}")

## Email Writer Agent Prompts
def email_writer_system_prompt():
    return str("""
    Your are a expert cold email writer.
    your task is to write consice and personalized short email based on market research given to you. 
    make sure to utilize following areas,
    
    ----
    Query 01: pain points / problems faced by this avatar
    Query 02: biggest companies in this industry
    Query 03: how companies in this industry get clients / leads
    Query 04: where to find companies in this industry online
    ----
    
    ----
    IMPORTANT!
    DO NOT OUTPUT ANY OTHER TEXTS, ONLY GIVE THE EMAIL !!!!!.
    ----
    """)

def email_writer_user_prompt(user_input, paragraph):
    return str(f"write a cold email for {user_input} based on this paragraph : {paragraph}")

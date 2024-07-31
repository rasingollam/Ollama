# Email Writer Agent

This project serves as a basic example of how to create agents using Groq API with the Llama 3.1 8B model to create tailored content for various industries or companies. It is intended for educational purposes only and should not be used in production environments without significant modifications and improvements.

Please note that this project requires many corrections and enhancements before it can be considered suitable for implementation in real-world scenarios. It is designed to demonstrate concepts and provide a starting point for further development.

We encourage users to explore, learn from, and build upon this example while keeping in mind its limitations and the need for proper error handling, security measures, and optimizations in any production-ready application.

## Features

- Generates search queries for market research
- Writes informative paragraphs based on search queries
- Composes personalized cold emails using the gathered information

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/email-writer-agent.git cd email-writer-agent

2. Install the required dependencies:
pip install -r requirements.txt

3. Set up your environment variables:
Create a `.env` file in the project root and add your Groq API key:
GROQ_API_KEY=your_api_key_here

## Usage

Run the main script to start the email generation process:
python main.py

The script will prompt you to enter a query about a company or industry. It will then generate search queries, create informative paragraphs, and compose a personalized cold email based on the gathered information.

## Project Structure

- `main.py`: The main script that orchestrates the email generation process.
- `agents.py`: Contains the core functions for generating search queries, paragraphs, and emails using the Groq API.
- `utils.py`: Utility functions, including user input handling.
- `prompts.py`: Stores the prompt templates used for generating content.

## How It Works

1. The user provides input about a target company or industry.
2. The system generates four search queries for market research.
3. For each search query, a paragraph of relevant information is generated.
4. The generated paragraphs are combined into a comprehensive market research summary.
5. Finally, a personalized cold email is composed using the original user input and the market research summary.

## Customization

You can modify the prompt templates in `prompts.py` to adjust the style and content of the generated text. The system prompt for each agent (search query generator, paragraph writer, and email writer) can be tailored to your specific needs.

## Dependencies

- groq
- python-dotenv

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Reference

For more information on related topics, check out this video: [(youtube.com)](https://www.youtube.com/watch?v=1SsPNc2zldM)

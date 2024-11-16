# Career Counseling Chatbot

![image (11)](https://github.com/user-attachments/assets/43ca1686-72cf-4aae-ac5e-089c562f71f9)


## Objective

The **Career Counseling Chatbot** is an AI-driven platform designed to help users with personalized career guidance based on their profiles, resumes, and goals. It provides career advice, resume suggestions, and mock interviews for various industries. The system uses natural language processing and machine learning to analyze user inputs and provide actionable insights in real-time.

## What is LangChain?

[LangChain](https://www.langchain.com/) is a framework designed to simplify the integration of large language models (LLMs) into applications. It enables developers to build complex workflows using LLMs, handle data from various sources, and support conversational AI systems. LangChain simplifies chaining together different components like models, tools, and prompts to create interactive, intelligent systems.

In this project, LangChain is used to facilitate contextual conversations and career guidance for users. It allows the chatbot to respond dynamically based on the user's input and ensures continuity in the dialogue by maintaining context.

## What is OpenAI?

[OpenAI](https://openai.com/) is a leading AI research organization that provides powerful natural language models, such as GPT-3 and GPT-4. These models are capable of understanding and generating human-like text, which makes them suitable for a wide range of applications, including chatbots, content creation, and even technical problem-solving.

In this project, OpenAI's language model (via the OpenAI API) powers the career counseling chatbot. It provides intelligent, context-aware responses, ensuring personalized career advice based on the user’s inputs.

## Application / Uses

- **Career Counseling**: The chatbot provides personalized career advice based on user input, such as job preferences, skills, and education.
- **Resume Analysis**: Users can upload their resumes, and the bot provides suggestions to improve them.
- **Mock Interviews**: Users can practice mock interviews with industry-specific questions and receive feedback.
- **Skill Development**: Offers guidance on the most relevant skills and certifications for career progression.
- **Industry-Specific Advice**: The chatbot tailors career advice based on different industries like IT, healthcare, engineering, and finance.

## Advantages

- **Personalized Career Guidance**: The chatbot provides tailored advice based on individual profiles and goals.
- **Convenient Access**: Available 24/7, users can access career counseling at any time from the comfort of their homes.
- **Scalable**: Able to handle multiple users simultaneously, making it suitable for use in educational institutions, career coaching platforms, and HR services.
- **Real-time Feedback**: Instant feedback on resumes, interviews, and career development.
- **Cost-Efficient**: Reduces the need for human career counselors by automating the process.

## Technical Aspects

### Technologies Used:
- **LangChain**: Used for context management, conversation flow, and integration with OpenAI models to generate responses.
- **OpenAI**: Provides the language model that powers the chatbot's core functionality.
- **Python**: Main programming language used to develop the chatbot.
- **Streamlit**: Used for creating the user interface of the chatbot, enabling easy interaction.
- **Flask**: For handling backend API requests and integrating with the LangChain system.
- **Pandas**: For processing and managing user data and resume files.

### Architecture:
The system is based on a client-server architecture:
1. **User Interface (Frontend)**: Built with Streamlit, which allows users to interact with the chatbot via a web-based interface.
2. **Backend (API)**: Python-based backend integrates LangChain and OpenAI for processing user requests.
3. **Resume Processing**: Utilizes NLP techniques for analyzing and suggesting improvements to resumes.
4. **Mock Interviews**: Industry-specific mock interview questions are provided, and users' responses are evaluated in real-time.

### Workflow:
1. The user provides their profile details and career goals.
2. The system uses LangChain to dynamically respond and provide tailored career advice.
3. If the user uploads a resume, the chatbot analyzes the resume and provides suggestions.
4. For mock interviews, the system asks relevant questions, evaluates responses, and gives feedback.

## Getting Started

To get started with the Career Counseling Chatbot, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/prajwalk-1/Smart-Career-Counseling-with-LangChain.git
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create an account at [OpenAI](https://platform.openai.com/signup).
   - Generate an API key from the OpenAI dashboard.
   - Add the key to the environment variables or a `.env` file.

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. The chatbot should now be live in your browser at `http://localhost:8501`.

## Demo

![WhatsApp Image 2024-11-16 at 14 34 04_8b10fea0](https://github.com/user-attachments/assets/8aed72f2-b702-4798-8035-e143a52309fd)

---

![WhatsApp Image 2024-11-16 at 14 09 42_f1fe7918](https://github.com/user-attachments/assets/8ab493d8-f8e0-4d3c-96e9-5d4a5a03c10c)

---

![WhatsApp Image 2024-11-16 at 14 41 53_c6538706](https://github.com/user-attachments/assets/1c4858a5-643b-469d-bff9-1be545e1f5ca)

---


## Conclusion

The **Career Counseling Chatbot** is an innovative application that leverages LangChain and OpenAI's models to provide real-time, personalized career guidance. It serves as an efficient, scalable solution for career development, offering personalized resume analysis, mock interviews, and skill development advice. Whether you’re a student, job seeker, or professional, this chatbot can help you make informed career decisions.

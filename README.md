# Learning Roadmap Generator

A powerful AI-driven application that generates personalized learning roadmaps for any topic. Input your desired learning topic and timeline, and get a structured, week-wise or month-wise learning plan with quizzes and project ideas.

## Features

- **Topic-Based Roadmaps**: Generate learning roadmaps for any topic (Android Development, Web Development, Operating Systems, DBMS, etc.)
- **Flexible Timeline**: Specify your learning duration in days, weeks, months, or years
- **Structured Learning**: Roadmaps are organized week-wise or month-wise for optimal learning efficiency
- **Quiz Integration**: Each module includes quiz questions to test your understanding
- **Project Ideas**: Practical project suggestions to apply your knowledge
- **AI-Powered**: Uses Google's Generative AI (Gemini) to create intelligent, personalized learning paths
- **Beautiful UI**: Minimal, modern, and user-friendly interface built with Streamlit

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API key:
   - Get a Google Generative AI API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the project root:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

Run the application:
```bash
streamlit run main.py
```

The app will open in your browser. Enter:
- **Topic**: What you want to learn (e.g., "Web Development", "Machine Learning")
- **Timeline**: How long you have to learn (e.g., 3 months, 6 weeks, 1 year)

The app will generate a comprehensive learning roadmap tailored to your needs.

## Project Structure

```
├── main.py                 # Main Streamlit application
├── config.py              # Configuration and constants
├── utils/
│   ├── ai_service.py      # Google Generative AI integration
│   ├── roadmap_parser.py  # Parsing and formatting roadmaps
│   └── validators.py      # Input validation
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in repo)
└── README.md             # This file
```

## Technologies Used

- **Streamlit**: Web UI framework
- **Google Generative AI (Gemini)**: AI for roadmap generation
- **Python**: Programming language
- **python-dotenv**: Environment variable management

## Features in Detail

### 1. Topic Input
Users can enter any learning topic they wish to master.

### 2. Timeline Selection
Flexible timeline options allow users to specify:
- Days (for short intensive courses)
- Weeks (standard learning period)
- Months (medium-term learning)
- Years (comprehensive mastery)

### 3. Structured Roadmap
The generated roadmap includes:
- **Weekly/Monthly Breakdown**: Clear milestones and topics for each period
- **Learning Objectives**: What you should achieve in each phase
- **Key Concepts**: Important topics to cover
- **Resources**: Suggested learning materials
- **Quizzes**: Self-assessment questions
- **Projects**: Hands-on projects to reinforce learning

### 4. Quiz Integration
Multiple choice and short-answer questions help validate understanding.

### 5. Project Ideas
Practical project suggestions aligned with the learning timeline.

## Future Enhancements

- [ ] Progress tracking
- [ ] User accounts and saved roadmaps
- [ ] Integration with learning platforms (Udemy, Coursera, etc.)
- [ ] Community roadmaps sharing
- [ ] PDF export functionality
- [ ] Learning resource recommendations
- [ ] Spaced repetition reminders

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on the GitHub repository.

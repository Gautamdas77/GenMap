# Learning Roadmap Generator - Project Guidelines

This is a Gen AI project that generates personalized learning roadmaps using Google's Generative AI (Gemini).

## Project Overview

**Purpose:** Generate structured, AI-powered learning roadmaps based on user input (topic + timeline)

**Tech Stack:**
- Frontend: Streamlit (Web UI)
- Backend: Python
- AI: Google Generative AI (Gemini)
- Environment: python-dotenv

**Key Features:**
- Topic-based roadmap generation
- Flexible timeline options (days/weeks/months/years)
- Module-based learning structure
- Quiz questions for assessment
- Hands-on project ideas
- Success metrics and tips
- JSON export functionality

## Project Structure

```
├── main.py                          # Main Streamlit application
├── config.py                        # Configuration and constants
├── requirements.txt                 # Dependencies
├── .env                            # API keys (not in repo)
├── .env.example                    # Example env template
├── README.md                       # Project overview
├── SETUP_GUIDE.md                 # Detailed setup instructions
├── utils/
│   ├── __init__.py                # Package initialization
│   ├── ai_service.py              # Google Generative AI integration
│   ├── validators.py              # Input validation logic
│   └── roadmap_parser.py          # Roadmap parsing and formatting
├── .vscode/
│   └── tasks.json                 # VS Code run task
└── .github/
    └── copilot-instructions.md    # This file
```

## Development Guidelines

### Code Organization
- **main.py**: UI and session management
- **config.py**: Constants and settings
- **utils/ai_service.py**: AI integration logic
- **utils/validators.py**: Input validation
- **utils/roadmap_parser.py**: Data formatting and parsing

### Adding Features
1. Add configuration to `config.py`
2. Implement core logic in appropriate `utils/` module
3. Update UI in `main.py`
4. Update documentation

### Code Style
- Follow PEP 8 standards
- Use type hints where possible
- Add docstrings to functions
- Use descriptive variable names

## Dependencies
- streamlit==1.28.1
- google-generativeai==0.3.0
- python-dotenv==1.0.0
- pydantic==2.4.2

## Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with API key
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

## Running the Application
```bash
streamlit run main.py
```
App opens at: http://localhost:8501

## Key Classes and Methods

### AIService
- `generate_roadmap(topic, timeline, timeline_unit)`: Main method to generate roadmap
- `_parse_json_response(response_text)`: Parses AI response

### InputValidator
- `validate_topic(topic)`: Validates topic input
- `validate_timeline(timeline, timeline_unit)`: Validates timeline
- `validate_all(topic, timeline, timeline_unit)`: Validates all inputs

### RoadmapParser
- `format_module_title(module, index)`: Formats module title
- `format_quiz_question(question, index)`: Formats quiz question
- `format_project(project, index)`: Formats project
- `validate_roadmap_structure(roadmap)`: Validates roadmap structure

## Testing
Currently no test framework is set up. To add tests:
```bash
pip install pytest
pytest tests/
```

## Known Limitations
- JSON parsing depends on AI response format
- Large topic names might reduce detail in roadmap
- API quota limits may apply to free tier users

## Future Enhancements
- Add progress tracking
- User authentication
- Saved roadmaps
- Community sharing
- PDF export
- Mobile app
- Multiple languages
- Spaced repetition system
- Learning platform integrations

## Common Tasks

### Update AI Prompt
Edit `config.py` → `ROADMAP_PROMPT_TEMPLATE`

### Change UI Colors
Edit `config.py` → color constants

### Add New Input Field
1. Add to input section in `main.py`
2. Update validators in `utils/validators.py`
3. Pass to `generate_roadmap()`

### Modify Roadmap Display
Edit module display functions in `main.py`:
- `display_modules()`
- `display_single_module()`
- `display_quiz()`
- `display_projects()`

## Troubleshooting

### Import Errors
```python
import sys
sys.path.insert(0, os.path.dirname(__file__))
```

### API Key Issues
- Check `.env` file exists
- Verify key is correct in Google AI Studio
- Check internet connection

### JSON Parsing Errors
- AI response format changed
- Update `_parse_json_response()` method
- Add regex patterns for different response formats

## Performance Optimization
- Cache roadmaps in session state
- Implement lazy loading for modules
- Add response caching for same topics

## Security Notes
- Never commit `.env` file
- Keep API key confidential
- Use environment variables for secrets
- Validate all user inputs

## Documentation Files
- **README.md**: General overview and features
- **SETUP_GUIDE.md**: Step-by-step setup and usage
- **config.py**: Configuration documentation
- **Code comments**: Function and logic documentation

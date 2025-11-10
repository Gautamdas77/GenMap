# 🎓 Learning Roadmap Generator - Setup Guide

## Quick Start

### 1. Get Your API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the API key

### 2. Configure Environment
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   
2. Edit `.env` and replace `your_api_key_here` with your actual API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key
   ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

---

## Project Structure

```
gen-ai-roadmap/
├── main.py                    # Main Streamlit application
├── config.py                  # Configuration and constants
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (not in repo)
├── .env.example              # Example env file
├── .gitignore                # Git ignore rules
├── README.md                 # Project overview
├── SETUP_GUIDE.md           # This file
├── utils/
│   ├── __init__.py          # Package init
│   ├── ai_service.py        # Google Generative AI integration
│   ├── validators.py        # Input validation
│   └── roadmap_parser.py    # Roadmap formatting and parsing
└── .vscode/
    └── tasks.json           # VS Code tasks
```

---

## Features Explained

### 1. **Topic Input**
- Users can enter any learning topic
- Examples: "Web Development", "Machine Learning", "Android Development", "Operating Systems"
- Validates input length and content

### 2. **Timeline Selection**
- **Days**: For intensive short-term learning (1-30 days)
- **Weeks**: For standard learning periods (1-52 weeks)
- **Months**: For medium-term programs (1-60 months)
- **Years**: For comprehensive mastery (1-10 years)

### 3. **Learning Level**
- **Beginner**: Starting from scratch
- **Intermediate**: Some foundational knowledge
- **Advanced**: Building on existing expertise

### 4. **Generated Roadmap Includes**

#### A. Overview
- Introduction to the topic
- Timeline analysis and breakdown
- High-level learning strategy

#### B. Prerequisites
- Required prior knowledge
- Suggested background skills

#### C. Tools & Resources
- Software to install
- Platforms to use
- Essential tools for the topic

#### D. Learning Modules
Each module contains:
- **Duration**: Time allocated for the module
- **Learning Objectives**: What you'll achieve
- **Key Concepts**: Core ideas to understand
- **Topics**: Specific subjects to study
- **Resources**: Books, courses, articles

#### E. Quiz Questions
- Multiple choice questions per module
- Instant feedback with explanations
- Tests conceptual understanding

#### F. Hands-on Projects
- Practical project ideas
- Difficulty levels (Beginner/Intermediate/Advanced)
- Estimated hours to complete
- Learning outcomes for each project

#### G. Success Metrics
- Measurable goals to track progress
- Validation of mastery

#### H. Tips for Success
- Study strategies
- Common pitfalls to avoid
- Motivation and consistency tips

---

## How to Use the Application

### Step 1: Enter Your Topic
```
Topic: "Web Development"
```

### Step 2: Set Your Timeline
```
Timeline: 6 Months
```

### Step 3: Select Your Level
```
Learning Level: Beginner
```

### Step 4: Generate Roadmap
Click the "🚀 Generate Roadmap" button and wait for AI to create your personalized plan.

### Step 5: Review Your Roadmap
- Read through modules
- Take module quizzes
- Review project ideas
- Check success metrics

### Step 6: Export (Optional)
- Copy roadmap as JSON
- Download roadmap file
- Save for offline reference

---

## Example Topics & Expected Output

### Example 1: Web Development
**Input:**
- Topic: Web Development
- Timeline: 6 Months
- Level: Beginner

**Expected Modules:**
1. Foundations (HTML, CSS, JavaScript)
2. Frontend Basics (React/Vue)
3. Backend Development (Node.js/Python)
4. Databases (SQL)
5. Full-Stack Projects
6. Deployment & DevOps

### Example 2: Machine Learning
**Input:**
- Topic: Machine Learning
- Timeline: 1 Year
- Level: Beginner

**Expected Modules:**
1. Python & Data Science Fundamentals
2. Linear Algebra & Statistics
3. Supervised Learning
4. Unsupervised Learning
5. Deep Learning
6. Real-world ML Projects

### Example 3: Android Development
**Input:**
- Topic: Android Development
- Timeline: 4 Months
- Level: Intermediate

**Expected Modules:**
1. Kotlin Fundamentals
2. Android Studio Setup
3. UI Components & Layouts
4. Activities & Fragments
5. Data Storage
6. Advanced Features (Camera, Sensors)
7. Publishing to Play Store

---

## Configuration Options

### In `config.py`:

**API Configuration**
```python
GOOGLE_API_KEY_ENV = "GOOGLE_API_KEY"  # Environment variable name
MODEL_NAME = "gemini-pro"              # AI model to use
```

**Timeline Options**
```python
TIMELINE_UNITS = ["Days", "Weeks", "Months", "Years"]
MIN_TIMELINE_VALUE = 1
MAX_TIMELINE_VALUE = 100
DEFAULT_TIMELINE = 3
DEFAULT_TIMELINE_UNIT = "Months"
```

**Appearance**
```python
PRIMARY_COLOR = "#6366f1"              # Indigo
SECONDARY_COLOR = "#ec4899"            # Pink
```

---

## Troubleshooting

### Issue: "API Key not found"
**Solution:**
1. Create `.env` file in project root
2. Add: `GOOGLE_API_KEY=your_key`
3. Restart the application

### Issue: "Failed to parse roadmap"
**Solution:**
1. Try again with a simpler topic name
2. Check internet connection
3. Ensure API key is valid
4. Check Google AI quota limits

### Issue: "ModuleNotFoundError"
**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Streamlit app not opening
**Solution:**
```bash
# Ensure streamlit is installed
pip install streamlit==1.28.1

# Run with explicit port
streamlit run main.py --server.port=8501
```

---

## Advanced Features

### Batch Generation
To generate roadmaps programmatically:

```python
from utils.ai_service import AIService
from utils.validators import InputValidator

# Validate input
is_valid, error = InputValidator.validate_all(
    topic="Web Development",
    timeline=6,
    timeline_unit="Months"
)

if is_valid:
    # Generate roadmap
    ai_service = AIService()
    roadmap = ai_service.generate_roadmap(
        topic="Web Development",
        timeline=6,
        timeline_unit="Months"
    )
    
    # Use roadmap
    print(roadmap)
```

### Custom Roadmap Parsing
```python
from utils.roadmap_parser import RoadmapParser

# Extract specific information
modules = roadmap.get("modules", [])
prerequisites = RoadmapParser.get_prerequisites(roadmap)
tools = RoadmapParser.get_tools_needed(roadmap)
tips = RoadmapParser.get_tips(roadmap)
```

---

## Best Practices

### 1. Topic Selection
- ✅ Use specific topics: "Web Development with React"
- ❌ Avoid: "Everything"
- ✅ Use clear terminology: "Machine Learning for Beginners"

### 2. Timeline Setting
- ✅ Be realistic about your available time
- ✅ Include buffer time for practice
- ✅ Consider learning style (intensive vs. spread out)

### 3. Quiz Taking
- ✅ Take all module quizzes
- ✅ Review explanations for incorrect answers
- ✅ Revisit modules if quiz scores are low

### 4. Project Completion
- ✅ Start with beginner projects
- ✅ Complete projects as you finish each module
- ✅ Document and showcase your projects

### 5. Progress Tracking
- ✅ Export and save your roadmap
- ✅ Check off completed modules
- ✅ Adjust timeline if needed

---

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: 2 GB minimum
- **Internet**: Required for API calls
- **Storage**: 500 MB for dependencies

---

## Performance Notes

- First roadmap generation: 30-60 seconds
- Subsequent generations: 30-50 seconds
- Quiz loading: Instant
- Module switching: Instant

---

## Support & Feedback

For issues or suggestions:
1. Check this guide's troubleshooting section
2. Review `.env` configuration
3. Ensure dependencies are installed correctly
4. Check internet and API connectivity

---

## License

This project is open source and available under the MIT License.

---

## Future Roadmap

- [ ] User authentication and saved progress
- [ ] Progress tracking dashboard
- [ ] Sync with learning platforms (Coursera, Udemy)
- [ ] Spaced repetition reminders
- [ ] Community roadmap sharing
- [ ] PDF export with better formatting
- [ ] Mobile app version
- [ ] Multiple language support
- [ ] Adaptive difficulty based on quiz scores
- [ ] Integration with coding environments

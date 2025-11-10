"""
Configuration and constants for the Learning Roadmap Generator
"""

# API Configuration
GOOGLE_API_KEY_ENV = "GOOGLE_API_KEY"
MODEL_NAME = "gemini-2.5-flash"

# Streamlit Configuration
APP_TITLE = "Learning Roadmap Generator"
APP_DESCRIPTION = "Generate personalized learning roadmaps powered by AI"

# Timeline options
TIMELINE_UNITS = ["Days", "Weeks", "Months", "Years"]
TIMELINE_CONVERSION = {
    "Days": 1,
    "Weeks": 7,
    "Months": 30,
    "Years": 365
}

# UI Colors and Styling
PRIMARY_COLOR = "#6366f1"
SECONDARY_COLOR = "#ec4899"
BACKGROUND_COLOR = "#0f172a"
TEXT_COLOR = "#e2e8f0"

# Roadmap Configuration
MIN_TIMELINE_VALUE = 1
MAX_TIMELINE_VALUE = 100
DEFAULT_TIMELINE = 3
DEFAULT_TIMELINE_UNIT = "Months"

# AI Prompt Configuration
ROADMAP_PROMPT_TEMPLATE = """You are an expert educational consultant and curriculum designer. Create a detailed, personalized learning roadmap for the following:

Topic: {topic}
Timeline: {timeline} {timeline_unit}
Total Days Available: {total_days}

Please provide a comprehensive learning roadmap in the following JSON format:
{{
    "topic": "{topic}",
    "timeline": "{timeline} {timeline_unit}",
    "overview": "Brief overview of the topic and learning journey",
    "duration_analysis": "Analysis of how to structure the learning within the given timeline",
    "modules": [
        {{
            "module_number": 1,
            "title": "Module title",
            "duration": "X weeks/months",
            "objectives": ["objective 1", "objective 2"],
            "key_concepts": ["concept 1", "concept 2"],
            "topics": ["topic 1", "topic 2"],
            "resources": ["resource 1", "resource 2"],
            "quiz": [
                {{
                    "question": "Quiz question",
                    "options": ["option 1", "option 2", "option 3", "option 4"],
                    "correct_answer": "option 1",
                    "explanation": "Explanation of the answer"
                }}
            ],
            "projects": [
                {{
                    "title": "Project title",
                    "description": "Brief description",
                    "difficulty": "Beginner/Intermediate/Advanced",
                    "estimated_hours": 10,
                    "learning_outcomes": ["outcome 1", "outcome 2"]
                }}
            ]
        }}
    ],
    "prerequisites": ["Prerequisite 1", "Prerequisite 2"],
    "tools_needed": ["Tool 1", "Tool 2"],
    "success_metrics": ["Metric 1", "Metric 2"],
    "tips_for_success": ["Tip 1", "Tip 2"]
}}

Make the roadmap practical, achievable, and well-structured. Ensure quiz questions test real understanding of concepts. Projects should be progressively challenging and reinforce key concepts."""

# Display settings
ITEMS_PER_PAGE = 5
MAX_QUIZ_QUESTIONS = 3

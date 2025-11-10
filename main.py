"""
Learning Roadmap Generator - Main Application
A powerful AI-driven application that generates personalized learning roadmaps
"""

import streamlit as st
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import utils
import sys
sys.path.insert(0, os.path.dirname(__file__))

from config import (
    APP_TITLE, APP_DESCRIPTION, TIMELINE_UNITS,
    PRIMARY_COLOR, SECONDARY_COLOR, DEFAULT_TIMELINE,
    DEFAULT_TIMELINE_UNIT
)
from utils.ai_service import AIService
from utils.validators import InputValidator
from utils.roadmap_parser import RoadmapParser


# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    :root {
        --primary: #6366f1;
        --secondary: #ec4899;
    }
    
    .main {
        padding: 2rem;
    }
    
    .header {
        text-align: center;
        margin-bottom: 2rem;
        padding: 2rem;
        background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
        border-radius: 12px;
        color: white;
    }
    
    .input-section {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        border: 1px solid #e9ecef;
    }
    
    .module-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #6366f1;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .quiz-container {
        background: #f0f4ff;
        padding: 1.5rem;
        border-radius: 8px;
        margin-top: 1rem;
        border: 1px solid #d0d8ff;
    }
    
    .project-card {
        background: #fff8f0;
        padding: 1.5rem;
        border-radius: 8px;
        margin-top: 1rem;
        border-left: 4px solid #ec4899;
    }
    
    .success-message {
        color: #28a745;
        font-weight: bold;
    }
    
    .error-message {
        color: #dc3545;
        font-weight: bold;
    }
    
    .metric-box {
        background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables"""
    if "roadmap" not in st.session_state:
        st.session_state.roadmap = None
    if "loading" not in st.session_state:
        st.session_state.loading = False
    if "current_module" not in st.session_state:
        st.session_state.current_module = 0


def display_header():
    """Display the application header"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown(
            f"<div class='header'>"
            f"<h1>🎓 {APP_TITLE}</h1>"
            f"<p>{APP_DESCRIPTION}</p>"
            f"</div>",
            unsafe_allow_html=True
        )


def display_input_section():
    """Display the input section for topic and timeline"""
    st.markdown("## 🎯 Define Your Learning Path")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        topic = st.text_input(
            "What do you want to learn?",
            placeholder="e.g., Web Development, Machine Learning, Android Development...",
            help="Enter any topic you'd like to master"
        )
    
    with col2:
        timeline = st.number_input(
            "How much time do you have?",
            min_value=1,
            max_value=100,
            value=DEFAULT_TIMELINE,
            step=1,
            help="Enter the duration value"
        )
    
    col3, col4, col5 = st.columns([2, 2, 1])
    
    with col3:
        timeline_unit = st.selectbox(
            "Time unit",
            TIMELINE_UNITS,
            index=TIMELINE_UNITS.index(DEFAULT_TIMELINE_UNIT),
            help="Select the time unit"
        )
    
    with col4:
        difficulty = st.selectbox(
            "Your learning level",
            ["Beginner", "Intermediate", "Advanced"],
            help="Select your current proficiency level"
        )
    
    with col5:
        generate_btn = st.button(
            "🚀 Generate Roadmap",
            use_container_width=True,
            type="primary"
        )
    
    return topic, timeline, timeline_unit, difficulty, generate_btn


def generate_roadmap(topic: str, timeline: int, timeline_unit: str, difficulty: str):
    """Generate the learning roadmap"""
    # Validate inputs
    is_valid, error_msg = InputValidator.validate_all(topic, timeline, timeline_unit)
    
    if not is_valid:
        st.error(f"❌ {error_msg}")
        return None
    
    try:
        with st.spinner("🤖 AI is generating your personalized roadmap... This may take a moment."):
            ai_service = AIService()
            
            # Add difficulty context to the prompt
            difficulty_prompt = f"\nThe learner is at {difficulty} level."
            
            roadmap = ai_service.generate_roadmap(topic, timeline, timeline_unit)
            
            # Validate roadmap structure
            if not RoadmapParser.validate_roadmap_structure(roadmap):
                st.error("❌ Generated roadmap has invalid structure. Please try again.")
                return None
            
            st.success("✅ Roadmap generated successfully!")
            return roadmap
    
    except ValueError as e:
        st.error(f"❌ Input Error: {str(e)}")
        return None
    except Exception as e:
        st.error(f"❌ Error generating roadmap: {str(e)}")
        st.info("💡 Tip: Make sure you have set the GOOGLE_API_KEY environment variable correctly.")
        return None


def display_roadmap_overview(roadmap: dict):
    """Display the roadmap overview"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            f"<div class='metric-box'>"
            f"<h3>📖 Topic</h3>"
            f"<p>{roadmap.get('topic', 'N/A')}</p>"
            f"</div>",
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f"<div class='metric-box'>"
            f"<h3>⏱️ Timeline</h3>"
            f"<p>{roadmap.get('timeline', 'N/A')}</p>"
            f"</div>",
            unsafe_allow_html=True
        )
    
    with col3:
        module_count = RoadmapParser.get_module_count(roadmap)
        st.markdown(
            f"<div class='metric-box'>"
            f"<h3>📚 Modules</h3>"
            f"<p>{module_count}</p>"
            f"</div>",
            unsafe_allow_html=True
        )
    
    st.markdown("### 📝 Learning Journey Overview")
    overview = RoadmapParser.extract_overview(roadmap)
    st.write(overview)


def display_prerequisites_and_tools(roadmap: dict):
    """Display prerequisites and tools needed"""
    col1, col2 = st.columns(2)
    
    with col1:
        prerequisites = RoadmapParser.get_prerequisites(roadmap)
        if prerequisites:
            st.markdown("### 📋 Prerequisites")
            for prereq in prerequisites:
                st.write(f"• {prereq}")
    
    with col2:
        tools = RoadmapParser.get_tools_needed(roadmap)
        if tools:
            st.markdown("### 🛠️ Tools You'll Need")
            for tool in tools:
                st.write(f"• {tool}")


def display_modules(roadmap: dict):
    """Display the learning modules"""
    st.markdown("## 📚 Learning Modules")
    
    modules = roadmap.get("modules", [])
    
    if not modules:
        st.warning("No modules found in the roadmap.")
        return
    
    # Create tabs for each module
    module_tabs = st.tabs([f"Module {i+1}" for i in range(len(modules))])
    
    for idx, (tab, module) in enumerate(zip(module_tabs, modules)):
        with tab:
            display_single_module(module, idx)


def display_single_module(module: dict, index: int):
    """Display a single module"""
    # Module header
    st.markdown(f"### {RoadmapParser.format_module_title(module, index)}")
    
    # Objectives
    if "objectives" in module:
        st.markdown("**📌 Learning Objectives:**")
        st.write(RoadmapParser.format_objectives(module.get("objectives", [])))
    
    # Key Concepts
    if "key_concepts" in module:
        st.markdown("**🔑 Key Concepts:**")
        concepts = module.get("key_concepts", [])
        concept_text = " | ".join(concepts)
        st.write(concept_text)
    
    # Topics
    if "topics" in module:
        st.markdown("**📖 Topics to Cover:**")
        topics = module.get("topics", [])
        for topic in topics:
            st.write(f"• {topic}")
    
    # Resources
    if "resources" in module:
        st.markdown("**📚 Recommended Resources:**")
        resources = module.get("resources", [])
        for resource in resources:
            st.write(f"• {resource}")
    
    # Quiz Section
    quiz_questions = module.get("quiz", [])
    if quiz_questions:
        with st.expander("📝 Module Quiz", expanded=False):
            display_quiz(quiz_questions)
    
    # Projects Section
    projects = module.get("projects", [])
    if projects:
        with st.expander("🎯 Hands-on Projects", expanded=False):
            display_projects(projects)


def display_quiz(quiz_questions: list):
    """Display quiz questions for a module"""
    st.markdown("**Test your understanding with these questions:**")
    
    for idx, q_data in enumerate(quiz_questions[:3]):  # Limit to 3 questions per module
        question_num = idx + 1
        
        st.markdown(f"**Question {question_num}:** {q_data.get('question', '')}")
        
        options = q_data.get("options", [])
        if options:
            selected_answer = st.radio(
                f"Select your answer for question {question_num}:",
                options,
                key=f"quiz_{id(q_data)}",
                label_visibility="collapsed"
            )
            
            if st.button(f"Check Answer", key=f"check_{id(q_data)}"):
                correct = q_data.get("correct_answer", "")
                if selected_answer == correct:
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Incorrect. The correct answer is: {correct}")
                
                explanation = q_data.get("explanation", "")
                if explanation:
                    st.info(f"📖 Explanation: {explanation}")
        
        st.divider()


def display_projects(projects: list):
    """Display project ideas for a module"""
    st.markdown("**Build these projects to reinforce your learning:**")
    
    for idx, project in enumerate(projects):
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**{idx + 1}. {project.get('title', f'Project {idx + 1}')}**")
                st.write(f"_{project.get('description', '')}_ ")
            
            with col2:
                difficulty = project.get("difficulty", "Beginner")
                emoji = "🟢" if difficulty == "Beginner" else "🟡" if difficulty == "Intermediate" else "🔴"
                st.write(f"{emoji} {difficulty}")
            
            st.write(f"⏱️ Estimated: {project.get('estimated_hours', 0)} hours")
            
            outcomes = project.get("learning_outcomes", [])
            if outcomes:
                st.markdown("**Learning Outcomes:**")
                for outcome in outcomes:
                    st.write(f"✓ {outcome}")
            
            st.divider()


def display_success_metrics_and_tips(roadmap: dict):
    """Display success metrics and tips"""
    col1, col2 = st.columns(2)
    
    with col1:
        metrics = RoadmapParser.get_success_metrics(roadmap)
        if metrics:
            st.markdown("### 🎯 Success Metrics")
            st.markdown("**You'll know you've succeeded when you can:**")
            for metric in metrics:
                st.write(f"✓ {metric}")
    
    with col2:
        tips = RoadmapParser.get_tips(roadmap)
        if tips:
            st.markdown("### 💡 Tips for Success")
            for tip in tips:
                st.write(f"• {tip}")


def display_export_options(roadmap: dict):
    """Display export options"""
    st.markdown("## 📥 Export Your Roadmap")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📋 Copy as JSON", use_container_width=True):
            st.code(json.dumps(roadmap, indent=2), language="json")
    
    with col2:
        if st.button("💾 Download as JSON", use_container_width=True):
            st.download_button(
                label="Download JSON",
                data=json.dumps(roadmap, indent=2),
                file_name=f"{roadmap.get('topic', 'roadmap').replace(' ', '_')}_roadmap.json",
                mime="application/json"
            )


def main():
    """Main application function"""
    initialize_session_state()
    
    # Display header
    display_header()
    
    # Display input section
    topic, timeline, timeline_unit, difficulty, generate_btn = display_input_section()
    
    # Generate roadmap when button is clicked
    if generate_btn:
        roadmap = generate_roadmap(topic, timeline, timeline_unit, difficulty)
        if roadmap:
            st.session_state.roadmap = roadmap
    
    # Display roadmap if generated
    if st.session_state.roadmap:
        st.divider()
        
        # Overview section
        display_roadmap_overview(st.session_state.roadmap)
        
        st.divider()
        
        # Prerequisites and tools
        display_prerequisites_and_tools(st.session_state.roadmap)
        
        st.divider()
        
        # Modules section
        display_modules(st.session_state.roadmap)
        
        st.divider()
        
        # Success metrics and tips
        display_success_metrics_and_tips(st.session_state.roadmap)
        
        st.divider()
        
        # Export options
        display_export_options(st.session_state.roadmap)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🎓 About This App")
        st.write(
            "This application uses AI to generate personalized learning roadmaps "
            "for any topic. Simply enter your topic of interest and your available "
            "time, and get a comprehensive learning plan with modules, quizzes, and projects!"
        )
        
        st.divider()
        
        st.markdown("### 🌟 Features")
        st.write(
            "✅ AI-powered roadmap generation\n"
            "✅ Flexible timeline options\n"
            "✅ Module-based learning structure\n"
            "✅ Quiz questions for each module\n"
            "✅ Practical project ideas\n"
            "✅ Success metrics and tips\n"
            "✅ JSON export functionality"
        )
        
        st.divider()
        
        st.markdown("### 📝 How to Use")
        st.write(
            "1. Enter your learning topic\n"
            "2. Specify your available time\n"
            "3. Select your learning level\n"
            "4. Click 'Generate Roadmap'\n"
            "5. Review modules, quiz, and projects\n"
            "6. Export your roadmap if needed"
        )
        
        st.divider()
        
        st.markdown("### ⚙️ Settings")
        show_advanced = st.checkbox("Show Advanced Options")
        
        if show_advanced:
            st.markdown("**API Configuration**")
            api_key = os.getenv("GOOGLE_API_KEY")
            if api_key:
                st.success("✅ API Key is configured")
            else:
                st.warning("⚠️ API Key not found. Please set GOOGLE_API_KEY environment variable.")


if __name__ == "__main__":
    main()

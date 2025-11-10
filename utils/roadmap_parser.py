"""
Roadmap parser and formatter for displaying learning roadmaps
"""

from typing import Dict, List, Optional, Any
import json


class RoadmapParser:
    """Parser for roadmap data and formatting"""

    @staticmethod
    def format_module_title(module: Dict[str, Any], index: int) -> str:
        """
        Format a module title with its duration.

        Args:
            module: The module dictionary
            index: The module index

        Returns:
            Formatted title string
        """
        title = module.get("title", f"Module {index + 1}")
        duration = module.get("duration", "")
        
        if duration:
            return f"📚 {title} ({duration})"
        return f"📚 {title}"

    @staticmethod
    def format_objectives(objectives: List[str]) -> str:
        """
        Format learning objectives as a bullet list.

        Args:
            objectives: List of objectives

        Returns:
            Formatted string
        """
        if not objectives:
            return "No objectives specified"
        
        return "\n".join([f"• {obj}" for obj in objectives])

    @staticmethod
    def format_quiz_question(question: Dict[str, Any], index: int) -> Dict[str, Any]:
        """
        Format a quiz question.

        Args:
            question: The question dictionary
            index: The question index

        Returns:
            Formatted question dictionary
        """
        return {
            "number": index + 1,
            "question": question.get("question", ""),
            "options": question.get("options", []),
            "correct_answer": question.get("correct_answer", ""),
            "explanation": question.get("explanation", "")
        }

    @staticmethod
    def format_project(project: Dict[str, Any], index: int) -> Dict[str, Any]:
        """
        Format a project.

        Args:
            project: The project dictionary
            index: The project index

        Returns:
            Formatted project dictionary
        """
        return {
            "number": index + 1,
            "title": project.get("title", f"Project {index + 1}"),
            "description": project.get("description", ""),
            "difficulty": project.get("difficulty", "Beginner"),
            "estimated_hours": project.get("estimated_hours", 0),
            "learning_outcomes": project.get("learning_outcomes", [])
        }

    @staticmethod
    def get_module_count(roadmap: Dict[str, Any]) -> int:
        """Get the total number of modules in a roadmap"""
        return len(roadmap.get("modules", []))

    @staticmethod
    def get_total_duration_analysis(roadmap: Dict[str, Any]) -> str:
        """Get the duration analysis from the roadmap"""
        return roadmap.get("duration_analysis", "No analysis available")

    @staticmethod
    def get_prerequisites(roadmap: Dict[str, Any]) -> List[str]:
        """Get prerequisites from the roadmap"""
        return roadmap.get("prerequisites", [])

    @staticmethod
    def get_tools_needed(roadmap: Dict[str, Any]) -> List[str]:
        """Get required tools from the roadmap"""
        return roadmap.get("tools_needed", [])

    @staticmethod
    def get_success_metrics(roadmap: Dict[str, Any]) -> List[str]:
        """Get success metrics from the roadmap"""
        return roadmap.get("success_metrics", [])

    @staticmethod
    def get_tips(roadmap: Dict[str, Any]) -> List[str]:
        """Get success tips from the roadmap"""
        return roadmap.get("tips_for_success", [])

    @staticmethod
    def validate_roadmap_structure(roadmap: Dict[str, Any]) -> bool:
        """
        Validate that the roadmap has required fields.

        Args:
            roadmap: The roadmap dictionary to validate

        Returns:
            True if valid, False otherwise
        """
        required_fields = ["topic", "timeline", "modules"]
        
        for field in required_fields:
            if field not in roadmap or not roadmap[field]:
                return False
        
        # Validate modules structure
        modules = roadmap.get("modules", [])
        if not isinstance(modules, list) or len(modules) == 0:
            return False
        
        # Check first module has required fields
        first_module = modules[0]
        module_required_fields = ["title", "objectives", "key_concepts"]
        
        for field in module_required_fields:
            if field not in first_module:
                return False
        
        return True

    @staticmethod
    def extract_overview(roadmap: Dict[str, Any]) -> str:
        """Extract the overview/introduction from the roadmap"""
        return roadmap.get("overview", "Welcome to your learning journey!")

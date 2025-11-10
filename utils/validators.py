"""
Input validators for the Learning Roadmap Generator
"""

from typing import Tuple


class InputValidator:
    """Validator for user inputs"""

    MIN_TOPIC_LENGTH = 3
    MAX_TOPIC_LENGTH = 100
    MIN_TIMELINE = 1
    MAX_TIMELINE = 100

    @staticmethod
    def validate_topic(topic: str) -> Tuple[bool, str]:
        """
        Validate the learning topic input.

        Args:
            topic: The topic string to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not topic:
            return False, "Topic cannot be empty"
        
        topic = topic.strip()
        
        if len(topic) < InputValidator.MIN_TOPIC_LENGTH:
            return False, f"Topic must be at least {InputValidator.MIN_TOPIC_LENGTH} characters long"
        
        if len(topic) > InputValidator.MAX_TOPIC_LENGTH:
            return False, f"Topic cannot exceed {InputValidator.MAX_TOPIC_LENGTH} characters"
        
        # Check for valid characters
        if not any(c.isalpha() for c in topic):
            return False, "Topic must contain at least one letter"
        
        return True, ""

    @staticmethod
    def validate_timeline(timeline: int, timeline_unit: str) -> Tuple[bool, str]:
        """
        Validate the timeline input.

        Args:
            timeline: The duration value
            timeline_unit: The unit of duration (Days, Weeks, Months, Years)

        Returns:
            Tuple of (is_valid, error_message)
        """
        if timeline < InputValidator.MIN_TIMELINE:
            return False, f"Timeline must be at least {InputValidator.MIN_TIMELINE}"
        
        if timeline > InputValidator.MAX_TIMELINE:
            return False, f"Timeline cannot exceed {InputValidator.MAX_TIMELINE}"
        
        valid_units = ["Days", "Weeks", "Months", "Years"]
        if timeline_unit not in valid_units:
            return False, f"Timeline unit must be one of: {', '.join(valid_units)}"
        
        return True, ""

    @staticmethod
    def validate_all(topic: str, timeline: int, timeline_unit: str) -> Tuple[bool, str]:
        """
        Validate all inputs together.

        Args:
            topic: The topic string
            timeline: The duration value
            timeline_unit: The unit of duration

        Returns:
            Tuple of (is_valid, error_message)
        """
        is_valid, error = InputValidator.validate_topic(topic)
        if not is_valid:
            return False, error
        
        is_valid, error = InputValidator.validate_timeline(timeline, timeline_unit)
        if not is_valid:
            return False, error
        
        return True, ""

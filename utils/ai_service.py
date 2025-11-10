"""
AI Service module for interacting with Google Generative AI
"""

import json
import os
from typing import Dict, Optional
import google.generativeai as genai
from config import GOOGLE_API_KEY_ENV, MODEL_NAME, ROADMAP_PROMPT_TEMPLATE, TIMELINE_CONVERSION


class AIService:
    """Service for generating learning roadmaps using Google Generative AI"""

    def __init__(self):
        """Initialize the AI Service with Google Generative AI"""
        api_key = os.getenv(GOOGLE_API_KEY_ENV)
        if not api_key:
            raise ValueError(f"Missing {GOOGLE_API_KEY_ENV} environment variable")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate_roadmap(
        self,
        topic: str,
        timeline: int,
        timeline_unit: str
    ) -> Dict:
        """
        Generate a learning roadmap for a given topic and timeline.

        Args:
            topic: The learning topic
            timeline: The duration of learning
            timeline_unit: The unit of timeline (Days, Weeks, Months, Years)

        Returns:
            Dictionary containing the structured roadmap
        """
        # Calculate total days
        total_days = timeline * TIMELINE_CONVERSION.get(timeline_unit, 30)

        # Create prompt
        prompt = ROADMAP_PROMPT_TEMPLATE.format(
            topic=topic,
            timeline=timeline,
            timeline_unit=timeline_unit,
            total_days=total_days
        )

        try:
            # Generate content
            response = self.model.generate_content(prompt)
            
            # Extract JSON from response
            response_text = response.text
            
            # Try to parse JSON
            roadmap = self._parse_json_response(response_text)
            
            if not roadmap:
                raise ValueError("Failed to parse roadmap from AI response")
            
            return roadmap
        
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse AI response as JSON: {str(e)}")
        except Exception as e:
            raise Exception(f"Error generating roadmap: {str(e)}")

    @staticmethod
    def _parse_json_response(response_text: str) -> Optional[Dict]:
        """
        Extract and parse JSON from the AI response.

        Args:
            response_text: The raw response text from the AI model

        Returns:
            Parsed JSON dictionary or None if parsing fails
        """
        try:
            # Try direct JSON parsing first
            return json.loads(response_text)
        except json.JSONDecodeError:
            pass

        # Try to find JSON block in the response
        import re
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        
        if json_match:
            try:
                return json.loads(json_match.group())
            except json.JSONDecodeError:
                pass

        return None

import os
import json
from typing import Dict, Any, Optional
import httpx
from dotenv import load_dotenv

# Import models
from models import TriageLevelEnum

# Load environment variables
load_dotenv()

# Get OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

# MCP configuration
MCP_ENABLED = os.getenv("MCP_ENABLED", "True").lower() == "true"


async def determine_triage_level(
    query_text: str, 
    safety_score: Optional[float] = None
) -> TriageLevelEnum:
    """
    Determine the triage level for a medical query.
    
    This function evaluates the urgency of a medical query and assigns
    an appropriate triage level based on the query content and safety score.
    
    Args:
        query_text: The query text to evaluate
        safety_score: Optional safety score between 0.0 and 1.0
        
    Returns:
        TriageLevelEnum indicating the urgency level
    """
    if MCP_ENABLED:
        return await determine_triage_level_with_mcp(query_text, safety_score)
    else:
        return await determine_triage_level_with_openai(query_text, safety_score)


async def determine_triage_level_with_openai(
    query_text: str, 
    safety_score: Optional[float] = None
) -> TriageLevelEnum:
    """
    Determine the triage level using direct OpenAI API calls.
    
    Args:
        query_text: The query text to evaluate
        safety_score: Optional safety score between 0.0 and 1.0
        
    Returns:
        TriageLevelEnum indicating the urgency level
    """
    if not OPENAI_API_KEY:
        # Fall back to mock implementation if no API key is available
        if safety_score is not None and safety_score < 0.3:
            return TriageLevelEnum.URGENT
        elif safety_score is not None and safety_score < 0.6:
            return TriageLevelEnum.HIGH
        else:
            return TriageLevelEnum.MEDIUM
    
    # Prepare the prompt for the OpenAI API
    system_prompt = (
        "You are a medical triage agent. Your task is to evaluate the urgency level of a medical query. "
        "Consider factors such as symptoms described, potential conditions, time sensitivity, and risk to patient. "
        f"Return exactly one of the following triage levels: {', '.join([level.value for level in TriageLevelEnum])}. "
        "Do not include any explanation or additional text."
    )
    
    # Include safety score in the user prompt if available
    user_prompt = query_text
    if safety_score is not None:
        user_prompt = f"Query: {query_text}\nSafety Score: {safety_score} (0.0 = high risk, 1.0 = low risk)"
    
    # Make the API request
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": OPENAI_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.2,  # Low temperature for consistent triage
                "max_tokens": 10
            },
            timeout=30.0  # 30 second timeout
        )
    
    # Parse the response
    if response.status_code == 200:
        result = response.json()
        triage_text = result["choices"][0]["message"]["content"].strip().lower()
        
        # Map the response to a TriageLevelEnum
        for level in TriageLevelEnum:
            if level.value in triage_text:
                return level
        
        # Default to MEDIUM if no match is found
        return TriageLevelEnum.MEDIUM
    else:
        # Fall back to a default level if API call fails
        print(f"OpenAI API error: {response.status_code} - {response.text}")
        return TriageLevelEnum.MEDIUM  # Default to medium urgency


async def determine_triage_level_with_mcp(
    query_text: str, 
    safety_score: Optional[float] = None
) -> TriageLevelEnum:
    """
    Determine the triage level using MCP orchestration.
    
    Args:
        query_text: The query text to evaluate
        safety_score: Optional safety score between 0.0 and 1.0
        
    Returns:
        TriageLevelEnum indicating the urgency level
    """
    # In a real implementation, this would call the MCP service
    # For demo purposes, we'll simulate the MCP response
    
    # Use safety score as the primary factor if available
    if safety_score is not None:
        if safety_score < 0.3:
            return TriageLevelEnum.URGENT
        elif safety_score < 0.5:
            return TriageLevelEnum.HIGH
        elif safety_score < 0.8:
            return TriageLevelEnum.MEDIUM
        else:
            return TriageLevelEnum.LOW
    
    # Otherwise, use keyword-based triage
    lower_query = query_text.lower()
    
    # Check for urgent keywords
    if any(word in lower_query for word in ["emergency", "severe", "extreme", "dying", "suicide", "heart attack", "stroke"]):
        return TriageLevelEnum.URGENT
    
    # Check for high urgency keywords
    elif any(word in lower_query for word in ["acute", "intense pain", "bleeding", "fever", "infection"]):
        return TriageLevelEnum.HIGH
    
    # Check for medium urgency keywords
    elif any(word in lower_query for word in ["pain", "chronic", "symptoms", "medication", "treatment"]):
        return TriageLevelEnum.MEDIUM
    
    # Default to low urgency
    else:
        return TriageLevelEnum.LOW

from typing import List, Dict, Annotated
from agent_framework import ai_function
from pydantic import Field

@ai_function(
    name="analyze_numbers",
    description="Calculates basic statistics (count, min, max, sum, average) for a list of numbers.",
)
def analyze_numbers(
    numbers: Annotated[
        List[float], 
        Field(description="A list of numerical values to analyze.")
    ]
) -> Dict[str, float]:
    """Calculates basic statistics for a list of numbers."""
    if not numbers:
        return {"count": 0, "min": 0, "max": 0, "sum": 0, "average": 0}
    
    return {
        "count": float(len(numbers)),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers)
    }
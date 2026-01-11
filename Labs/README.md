# 1. Agent Name
**Number Analyzer Agent**

---

# 2. Agent Purpose

The purpose of this agent is to analyze a list of numeric values provided by the user and return basic descriptive statistics.

This agent is designed to perform the following technical tasks:
- Receive a user message containing a list of numbers.
- Extract numeric values from the user input.
- Invoke an analysis tool to compute statistical measures.
- Present the computed results in a clear and user-friendly format.

The agent assists the user in interpreting simple numerical input by summarizing it into meaningful statistical information.

---

# 3. Agent Tools

The agent uses the following tool:

### analyze_numbers(numbers)

**Description:**  
Computes basic descriptive statistics for a list of numerical values.

**Input:**  
- `numbers` (List[float]) – A list of numeric values provided by the user.

**Output:**  
Returns a dictionary containing the following fields:
- `count` – Number of values in the list  
- `min` – Minimum value  
- `max` – Maximum value  
- `sum` – Sum of all values  
- `average` – Arithmetic mean of the values  

**Example Output:**
```json
{
  "count": 4,
  "min": 1,
  "max": 10,
  "sum": 23,
  "average": 5.75
}

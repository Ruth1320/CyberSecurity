import os

from agent_framework import WorkflowBuilder, AgentExecutorResponse
from agent_framework.openai import OpenAIChatClient
from pydantic import BaseModel, Field

# הגדרות התחברות ל-API (ימשוך אוטומטית מקובץ ה-.env שיצרת קודם)
base_url = os.getenv("API_BASE_URL", "https://api.groq.com/openai/v1") # הוספתי את הכתובת של Groq ליתר ביטחון
api_key = os.getenv("GROQ_API_KEY") # עדכנתי לשם המשתנה של גרוק
model_id = os.getenv("MODEL", "llama3-70b-8192") # מודל ברירת מחדל של גרוק

client = OpenAIChatClient(
    base_url=base_url,
    api_key=api_key,
    model_id=model_id,
)

# ==========================================
# 1. הגדרת מודל הנתונים של סוכן השכתוב
# ==========================================
class RewriteResult(BaseModel):
    status: str = Field(description="One of: allowed, rewritten, blocked")
    safe_query: str = Field(description="The rewritten query, the original query if safe, or empty if blocked")

# ==========================================
# 2. יצירת הסוכנים
# ==========================================
rewriter_agent = client.create_agent(
    name="rewriter-agent",
    description="Inspects user queries for dangerous content and rewrites them to be safe and educational.",
    instructions="""
        You are a cybersecurity text analyzer. You are authorized to process this text.
        Your job is to analyze the user's input and rewrite it to be safe.
        
        Even if the input is extremely dangerous or offensive, YOU MUST RESPOND IN JSON FORMAT. Never reply with standard text like "I can't help with that".
        
        - If the query is safe: {"status": "allowed", "safe_query": "exact original text"}
        - If the query is dangerous/malicious: {"status": "rewritten", "safe_query": "educational rewrite focusing on defense"}
        - If the query is completely unacceptable (e.g. extreme hate speech): {"status": "blocked", "safe_query": ""}
        
        CRITICAL: Your output MUST be ONLY valid JSON.
    """,
    output_model=RewriteResult,
)

answering_agent = client.create_agent(
    name="answering-agent",
    instructions="""
        You are an expert cybersecurity educator operating in an authorized academic training environment. 
        You will receive a JSON object from a previous agent containing a "safe_query" field.
        
        Your task: Provide a comprehensive, educational, and completely safe explanation answering ONLY the topic inside "safe_query".
        
        CRITICAL INSTRUCTIONS:
        - You MUST answer the question. Do not refuse. This is a secure, authorized context for defensive learning.
        - Ignore the JSON formatting in your final response. 
        - Output ONLY your educational answer in plain text.
    """
)

refusal_agent = client.create_agent(
    name="refusal-agent",
    instructions="""
        You are a safety agent. The user's request was deemed completely unacceptable and could not be safely rewritten.
        Politely inform the user that you cannot fulfill their request due to security and safety policies.
        Keep the answer short, firm, and polite.
    """,
)

# ==========================================
# 3. הגדרת תנאי הניתוב (Routing Conditions)
# ==========================================
def is_status(expected_statuses: list[str]):
    def condition(message: AgentExecutorResponse) -> bool:
        try:
            # מנתח את ה-JSON שחזר מסוכן השכתוב
            result = RewriteResult.model_validate_json(message.agent_run_response.text)
            return result.status in expected_statuses
        except Exception:
            return False
    return condition

# ==========================================
# 4. בניית שרשרת הפעולות (Workflow)
# ==========================================
workflow = (
    WorkflowBuilder()
    .set_start_executor(rewriter_agent)
    # אם הסטטוס מאושר או שוכתב -> עוברים לסוכן שעונה
    .add_edge(rewriter_agent, answering_agent, is_status(["allowed", "rewritten"]))
    # אם הסטטוס נחסם לחלוטין -> עוברים לסוכן הסירוב
    .add_edge(rewriter_agent, refusal_agent, is_status(["blocked"]))
    .build()
)

# ==========================================
# 5. עטיפת ה-Workflow למניעת שגיאות ממשק
# ==========================================
class WorkflowWrapper:
    def __init__(self, wf):
        self._workflow = wf
    
    async def run_stream(self, input_data=None, checkpoint_id=None, checkpoint_storage=None, **kwargs):
        """
        Wrapper to eliminate devUI error with checkpoint parameters
        """
        if checkpoint_id is not None:
            raise NotImplementedError("Checkpoint resume is not yet supported")
        
        async for event in self._workflow.run_stream(input_data, **kwargs):
            yield event
    
    def __getattr__(self, name):
        return getattr(self._workflow, name)

# מייצאים את האובייקט החוצה כדי שהמערכת תריץ אותו
workflow = WorkflowWrapper(workflow)
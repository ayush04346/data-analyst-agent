from llm import get_task_plan
from task_executor import run_generated_code

async def process_question(question: str):
    try:
        plan_and_code = await get_task_plan(question)
        result = await run_generated_code(plan_and_code)
        return result
    except Exception as e:
        return {"error": str(e)}

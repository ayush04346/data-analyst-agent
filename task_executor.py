import io
import base64
import contextlib
from matplotlib import pyplot as plt

async def run_generated_code(code: str):
    output_buffer = io.StringIO()

    # sandbox-like execution
    exec_globals = {
        "__builtins__": __builtins__,
        "plt": plt,
        "base64": base64,
        "io": io
    }

    with contextlib.redirect_stdout(output_buffer):
        exec(code, exec_globals)

    result = exec_globals.get("result", "No result variable returned")

    # Check for image
    image_data = exec_globals.get("image_base64", None)
    if image_data:
        return {
            "result": result,
            "plot": f"data:image/png;base64,{image_data}"
        }

    return {"result": result}

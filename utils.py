# utils.py

import io
import base64
import re
from typing import Sequence
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def fig_to_base64(
    fig: plt.Figure,
    fmt: str = "png",
    dpi: int = 100,
    max_bytes: int = 100_000,
    close: bool = True
) -> str:
    """
    Render a Matplotlib Figure to a base64 data-URI.
    Raises ValueError if the raw image exceeds max_bytes.
    """
    buf = io.BytesIO()
    fig.savefig(buf, format=fmt, dpi=dpi, bbox_inches="tight")
    buf.seek(0)
    raw = buf.read()
    if len(raw) > max_bytes:
        raise ValueError(f"Image size {len(raw)} > {max_bytes} bytes")
    b64 = base64.b64encode(raw).decode("ascii")
    if close:
        plt.close(fig)
    return f"data:image/{fmt};base64,{b64}"

def parse_numeric(s: str) -> float:
    """
    Strip out any non-digit/non-dot chars (e.g. "$", ",") and convert to float.
    Returns 0.0 if no digits found.
    """
    cleaned = re.sub(r"[^\d.]", "", s or "")
    return float(cleaned) if cleaned else 0.0

def regression_slope(x: Sequence[float], y: Sequence[float]) -> float:
    """
    Fit a linear model y = m*x + b and return the slope m.
    """
    arr_x = np.array(x).reshape(-1, 1)
    arr_y = np.array(y)
    model = LinearRegression().fit(arr_x, arr_y)
    return float(model.coef_[0])

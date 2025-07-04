FROM python:3.11-slim

# ── ajustes de base ───────────────────────────────────────────────
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# ── dependencias ──────────────────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── código ────────────────────────────────────────────────────────
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4004"]

import subprocess

def ask_ai(prompt):
    try:
        result = subprocess.run(
            ["python", "ai_query.py", prompt],
            capture_output=True,
            text=True
        )

        return result.stdout.strip()

    except Exception as e:
        return f"AI Error: {e}"

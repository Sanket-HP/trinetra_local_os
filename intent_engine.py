def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["battery", "charge", "power"]):
        return "battery"

    elif any(word in text for word in ["storage", "space", "disk"]):
        return "storage"

    elif any(word in text for word in ["camera", "photo", "picture"]):
        return "camera"

    elif any(word in text for word in ["time", "clock"]):
        return "time"

    elif text.startswith("remember"):
        return "remember"

    elif "recall" in text or "memory" in text:
        return "recall"

    else:
        return "unknown"

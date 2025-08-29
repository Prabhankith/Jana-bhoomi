from random import choice

PROMPTS = [
    "మీ బాల్యంలో మీకు ఇష్టమైన ఆహారం ఏమిటి?",
    "మీ జీవితంలో మరిచిపోలేని సంఘటన?",
    "ఈరోజు మీరు ఎవరితో ఎక్కువగా మాట్లాడారు?",
    "మీ ఊరి ప్రత్యేకత ఏమిటి?"
]

def get_daily_prompt():
    return choice(PROMPTS)
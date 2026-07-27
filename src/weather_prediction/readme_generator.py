from pathlib import Path
from datetime import datetime


def generate_readme(filename="Weather_Prediction_README.md"):
    lines = [
        "# 🌦️ Weather Prediction Package",
        "",
        "Thank you for installing **weather-prediction-utils**!",
        "",
        "---",
        "",
        "## 📦 Package Information",
        "",
        "- **Package Name:** weather-prediction-utils",
        "- **Version:** 0.1.0",
        f"- **Generated On:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        "",
        "## 👨‍💻 Developer",
        "",
        "**Devidutta Das**",
        "",
        "Founder of **CodeUdaan**",
        "",
        "---",
        "",
        "## 📺 Learn with CodeUdaan",
        "",
        "YouTube:",
        "https://www.youtube.com/@CodeUdaan",
        "",
        "---",
        "",
        "## 🚀 About",
        "",
        "This package predicts average temperature using a trained",
        "Machine Learning model built with Scikit-learn.",
        "",
        "---",
        "",
        "## 📝 Example",
        "",
        "```python",
        "from weather_prediction import predict",
        "",
        "result = predict(...)",
        "print(result)",
        "```",
        "",
        "---",
        "",
        "⭐ If this package helped you, please subscribe to CodeUdaan!",
        "",
        "Made with ❤️ by Devidutta Das",
    ]

    content = "\n".join(lines)

    path = Path.cwd() / filename
    path.write_text(content, encoding="utf-8")

    print(f"README generated successfully: {path}")

    return path
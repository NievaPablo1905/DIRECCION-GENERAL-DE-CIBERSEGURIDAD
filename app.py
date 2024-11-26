from flask import Flask, render_template, jsonify
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup

app = Flask(__name__)

# Configuración (parte relevante de tu código)
URLS = [
    "https://www.eltribuno.com",
    "https://www.infobae.com"
]
KEYWORDS = ["ciberseguridad", "delito"]

def get_filtered_news():
    news_items = []
    for url in URLS:
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")
            for item in soup.find_all("article"):
                title = item.find("h2").get_text(strip=True) if item.find("h2") else "Sin título"
                link = item.find("a")["href"] if item.find("a") else "Sin enlace"
                if any(keyword.lower() in title.lower() for keyword in KEYWORDS):
                    news_items.append({"title": title, "link": link})
        except Exception as e:
            print(f"Error al procesar {url}: {e}")
    return news_items

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/noticias")
def noticias():
    news = get_filtered_news()
    return jsonify(news)

if __name__ == "__main__":
    app.run(debug=True)
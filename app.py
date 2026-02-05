# app.py

from flask import Flask, render_template, request
from core.service import get_resposta

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    resposta = None

    if request.method == "POST":
        sentimento = request.form.get("sentimento")
        resposta = get_resposta(sentimento)

    return render_template("index.html", resposta=resposta)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")

    if response.status_code == 200:
        data = response.json()
        insult = data["insult"]
        print("Insult:", insult)
    else:
        print('Request failed with status code:', response.status_code)
        insult = "Failed to fetch insult"

    return render_template('index.html', insult=insult)

if __name__ == '__main__':
    app.run()

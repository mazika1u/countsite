from flask import Flask
import json
import os

app = Flask(__name__)
FILE = "counter.json"

def load_count():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f).get("count", 0)
    return 0

def save_count(count):
    with open(FILE, "w") as f:
        json.dump({"count": count}, f)

@app.route("/")
def index():
    count = load_count() + 1
    save_count(count)
    return f"<h1>アクセス数: {count} 回</h1>"

if __name__ == "__main__":
    app.run()

from flask import Flask
import os
import json

app = Flask(__name__)

# カウント保存ファイル
COUNT_FILE = "count.json"

# 初期化（ファイルがない場合）
if not os.path.exists(COUNT_FILE):
    with open(COUNT_FILE, "w") as f:
        json.dump({"count": 0}, f)

# アクセスカウントの取得と更新
def get_count():
    with open(COUNT_FILE, "r") as f:
        data = json.load(f)
    return data["count"]

def update_count():
    with open(COUNT_FILE, "r") as f:
        data = json.load(f)
    data["count"] += 1
    with open(COUNT_FILE, "w") as f:
        json.dump(data, f)

# ルートページ
@app.route("/")
def index():
    update_count()
    count = get_count()
    return f"""
    <html>
    <head><title>アクセスカウンター</title></head>
    <body>
        <h1>アクセス数: {count} 回</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

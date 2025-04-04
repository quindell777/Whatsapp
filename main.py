from flask import Flask, request
app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    return "Hello from Flask!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

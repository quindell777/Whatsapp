from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)

# Defina sua API key da OpenAI
openai.api_key = os.environ.get("OPENAI_API_KEY")  # ou coloque diretamente a string

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    # Mensagem recebida do WhatsApp via Twilio
    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")  # ex.: whatsapp:+551199999999

    # Aqui podemos montar uma resposta usando OpenAI
    response_text = get_openai_response(incoming_msg)

    # Monta uma resposta para o Twilio
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(response_text)

    return str(resp)

def get_openai_response(prompt):
    # Chamada à API da OpenAI
    try:
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=0.7,
        )
        return completion.choices[0].text.strip()
    except Exception as e:
        print("Erro na API da OpenAI:", e)
        return "Desculpe, mas não consegui processar sua mensagem."

if __name__ == "__main__":
    # Rode em modo debug (pode ajustar a porta se quiser)
    app.run(host="0.0.0.0", debug=True, port=5000)

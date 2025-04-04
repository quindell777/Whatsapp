from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

# Variáveis de credenciais (coloque as suas reais)
account_sid = 'ACe153e62273d0fb51593316ed1265e60c'
auth_token  = 'abf28efcf0cfb75ef03dca938def62bd'

# Configure os números abaixo de acordo com sua conta:
FROM_WHATSAPP = 'whatsapp:+14155238886'   # Número Twilio (sandbox ou oficial)
TO_WHATSAPP   = 'whatsapp:+559887533472'  # Para testes diretos, mas vamos usar o 'sender' dinâmico

# Cria o cliente do Twilio
client = Client(account_sid, auth_token)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    # Twilio envia a mensagem do usuário em 'Body' e o número de quem enviou em 'From'
    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")  # Ex.: 'whatsapp:+559999999999'

    print(f"Mensagem recebida: {incoming_msg} (remetente: {sender})")

    # Envia 'Boa Noite' de volta para quem enviou
    message = client.messages.create(
        from_=FROM_WHATSAPP,
        to=sender,  # Responde diretamente para quem mandou
        body='Boa Noite'  
    )

    # Retorna status HTTP 200 sem conteúdo específico
    # (Twilio só exige que retornemos algo, aqui pode ser HTTP 200 vazio)
    return ('', 200)

if __name__ == "__main__":
    # Executa em host 0.0.0.0 (acessível externamente) na porta 5000
    app.run(host="0.0.0.0", port=5000, debug=True)

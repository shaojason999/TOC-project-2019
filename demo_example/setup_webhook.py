from bottle import route, run, request


VERIFY_TOKEN = "EAAEpWrcZBNXcBAMCohPpB2Y8qCixVFRjLq84LwwCV1uN2QrwiBGnZAxSvifSX9qGIZCEuHZCjvSP6reqCNb6rxxZAqAnHswnjv0oJbxrcIsqMcRQd8iNpfdhim9v6QCc87WzASQ0RC1KJw5w6ZCQKItC0AtgDk4YXIhPSuFnqFq1ZCegB7rp9Im"



@route("/webhook", method="GET")
def setup_webhook():
    print("123")
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

run(host="localhost", port=5000, debug=True)

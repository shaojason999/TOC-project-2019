from bottle import route, run, request, abort, static_file
from fsm import TocMachine
import os
import global_var

PORT=os.environ['PORT']

minimum=0
maximum=100

VERIFY_TOKEN = "123"
machine = TocMachine(
    states=[
	'choose',
	'random',
	'min',
	'max',
	'eat',
	'drink',
	'repeat',
	'sticker'
    ],
    transitions=[
        {
            'trigger': 'init',
            'source': 'choose',
            'dest': 'random',
            'conditions': 'go_to_random'
        },
        {
            'trigger': 'init',
            'source': 'choose',
            'dest': 'eat',
            'conditions': 'go_to_eat'
        },
        {
            'trigger': 'init',
            'source': 'choose',
            'dest': 'drink',
            'conditions': 'go_to_drink'
        },
        {
            'trigger': 'init',
            'source': 'choose',
            'dest': 'repeat',
            'conditions': 'go_to_repeat'
        },
        {
            'trigger': 'init',
            'source': 'choose',
            'dest': 'sticker',
            'conditions': 'go_to_sticker'
        },
        {
            'trigger': 'rep',
            'source': 'repeat',
            'dest': 'repeat',
            'conditions': 'always_true'
        },
        {
            'trigger': 'random_gen',
            'source': 'random',
            'dest': 'min',
            'conditions': 'go_to_min'
        },
	{
            'trigger': 'random_gen',
            'source': 'min',
            'dest': 'max',
            'conditions': 'go_to_max'
        },
	{
            'trigger': 'go_back',
            'source': [
		'max',
		'eat',
		'drink',
		'repeat',
		'sticker'
            ],
            'dest': 'choose'
        }
    ],
    initial='choose',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        if machine.state == 'choose':
                machine.init(event)
        elif machine.state == 'random' or machine.state == 'min':
                machine.random_gen(event)
        elif machine.state == 'repeat':
                machine.rep(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    global_var.initialize()
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)

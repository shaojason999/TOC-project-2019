from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, text):
        return text.lower() == 'go to state1'

    def is_going_to_state2(self, text):
        return text.lower() == 'go to state2'

    def is_going_to_state123(self, text):
        print("123")
        return text.lower() == 'go to state123'
    def is_going_to_state222(self):
        print("234")
        return 1

    def on_enter_state1(self, event):
        print("I'm entering state1")
        print('CURRENT STATE: ' + machine.state)
        self.go_back() # go to on_exit_state1


    def on_enter_state123(self, event):
        print("I'm entering state123")
        print('CURRENT STATE: ' + machine.state)
        self.advance123() # go to on_exit_state1
    def on_exit_state123(self):
        print('Leaving state123')

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")
        print('CURRENT STATE: ' + machine.state)
        self.go_back()
    def on_enter_state2(self):
        print("I'm entering state222")
        print('CURRENT STATE: ' + machine.state)
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')


machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
	'state123'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state123',
            'conditions': 'is_going_to_state123'
        },
        {
            'trigger': 'advance123',
            'source': 'state123',
            'dest': 'state2',
            'conditions': 'is_going_to_state222'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
		'state123'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


if __name__ == "__main__":
    while True:
        text = input('input: ')
        print('---')
        print('LAST STATE: ' + machine.state)

        machine.advance(text)
        print('FINAL STATE: ' + machine.state)
        print('---')

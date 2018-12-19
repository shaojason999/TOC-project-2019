from transitions.extensions import GraphMachine

from utils import send_text_message
import random
import global_var

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def go_to_random(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'random'
        return False

    def go_to_eat(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'eat'
        return False

    def go_to_drink(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'drink'
        return False

    def go_to_repeat(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'repeat'
        return False

    def always_true(self, event):
        return True

    def on_enter_random(self, event):
        print("I'm entering random")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "give me a minimum")

    def on_enter_eat(self, event):
        print("I'm entering eat")

        eat=["pizza","fried chicken","banana","cake","beef noodles"]
        ran=random.randint(0,4)

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, eat[ran])
        self.go_back()

    def on_exit_max(self):
        print('go back to choose')

    def on_enter_drink(self, event):
        print("I'm entering drink")

        drink=["cola","apple juice","milkshake","coffee","tea"]
        ran=random.randint(0,4)

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, drink[ran])
        self.go_back()

    def on_enter_repeat(self, event):
        print("I'm entering repeat")

        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']

        if text=="exit":
            self.go_back()
        else:
            sender_id = event['sender']['id']
            responese = send_text_message(sender_id, text)

    def on_exit_max(self):
        print('go back to choose')

    def go_to_min(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            global_var.minimum=int(text)
            return True
        return False


    def on_enter_min(self, event):
        print("I'm entering min")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "give me a maximum")

    def go_to_max(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            global_var.maximum=int(text)
            return True
        return False

    def on_enter_max(self, event):
        print("I'm entering max")

        sender_id = event['sender']['id']
        a=random.randint(global_var.minimum,global_var.maximum)
        responese = send_text_message(sender_id, a)
        self.go_back()

    def on_exit_max(self):
        print('go back to choose')


from transitions.extensions import GraphMachine

from utils import send_text_message
import random
import global_var


from bs4 import BeautifulSoup
import requests

def movie():
	target_url='https://movies.yahoo.com.tw/'
	rs=requests.session()
	res=rs.get(target_url, verify=False)
	res.enconding='utf-8'
	soup=BeautifulSoup(res.text, 'html.parser')
	context=""
	for index, data in enumerate(soup.select('div.movielist_info h2 a')):
		if index==10:
			return context
		title=data.text
		link=data['href']
		context+='{}\n{}\n'.format(title,link)
	return context

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

    def go_to_sticker(self, event):
        if event.get("message") and event['message'].get("sticker_id"):
            text = event['message']['sticker_id']
            return text == 369239263222822
        return False

    def go_to_movie(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'movie'
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

    def on_enter_sticker(self, event):
        print("I'm entering sticker")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "thanks for you like")
        self.go_back()

    def on_enter_movie(self, event):
        print("I'm entering movie")

        sender_id = event['sender']['id']
        context=movie()
        responese = send_text_message(sender_id, context)
        self.go_back()

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


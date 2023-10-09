import re
import random

class QanoonBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    random_questions = (
        "What legal issue are you facing today? ",
        "Are you seeking legal advice? ",
        "How can I assist you with legal matters? ",
        "Do you need help finding a lawyer? ",
        "What specific legal information do you require? ",
    )

    def __init__(self):
        self.qanoon_babble = {
            'describe_legal_intent': r'.\s*legal.',
            'answer_why_legal_intent': r'why\sneed.legal.',
            'cubed_intent': r'.cube.(\d+)'
        }

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(
            f"Hi {self.name}, I'm Qanoon-Bot, your legal assistant. How can I help you with legal matters today?\n")
        if will_help in self.negative_responses:
            print("Okay, have a good day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                self.exit_message()
                return True
    def process_message(self, user_message):
        user_message = user_message.lower()
        if user_message in self.negative_responses:
            return "Okay, have a good day!"

        for key, value in self.qanoon_babble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, user_message)
            if found_match and intent == 'describe_legal_intent':
                return self.describe_legal_intent()
            elif found_match and intent == 'answer_why_legal_intent':
                return self.answer_why_legal_intent()
            elif found_match and intent == 'cubed_intent':
                return self.cubed_intent(found_match.groups()[0])

        if not found_match:
            return self.no_match_intent()

    def exit_message(self):
        print("Qanoon-Bot: Thank you for chatting with me. I'm here to assist you with legal matters. "
              "Our goal is to revolutionize Pakistan with an AI-driven chatbot that provides assistance to "
              "both lawyers and individuals. Currently, this smart chatbot is in development and will be soon "
              "released to the public on this website. Have a great day!")

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.qanoon_babble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_legal_intent':
                return self.describe_legal_intent()
            elif found_match and intent == 'answer_why_legal_intent':
                return self.answer_why_legal_intent()
            elif found_match and intent == 'cubed_intent':
                return self.cubed_intent(found_match.groups()[0])
        if not found_match:
            return self.no_match_intent()

    def describe_legal_intent(self):
        responses = ("I'm here to provide assistance and information on legal matters.\n",
                     "I specialize in legal queries and helping you find appropriate legal advice.\n")
        return random.choice(responses)

    def answer_why_legal_intent(self):
        responses = ("Legal matters can be complex, and I'm here to guide you through them.\n",
                     "Understanding legalities is crucial, and I'm here to assist you in that.\n")
        return random.choice(responses)

    def cubed_intent(self, number):
        number = int(number)
        cubed_number = number * number * number
        return f"The cube of {number} is {cubed_number}. Interesting, isn't it?\n"

    def no_match_intent(self):
        responses = (
            "Please tell me more.\n", "Tell me more!\n", "Why do you say that?\n", "I see. Can you elaborate?\n",
            "Interesting. Can you tell me more?\n", "I see. How do you think?\n", "Why?\n",
            "How do you think I feel when you say that?\n")
        return random.choice(responses)


QanoonBot = QanoonBot()
QanoonBot.greet()
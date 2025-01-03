unsent_text_messages = ["hello", "how are you?", "goodbye"]


def show_messages(messages):
    for message in messages:
        print(message)


show_messages(unsent_text_messages)


sent_messages = []


def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


# send_messages(unsent_text_messages)
# print(unsent_text_messages)
# print(sent_messages)

send_messages(unsent_text_messages[:])
print(unsent_text_messages)
print(sent_messages)

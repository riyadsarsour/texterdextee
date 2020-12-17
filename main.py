import os


def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))


if __name__ == '__main__':
    msg = input(
        "Welcome to texter bot, type the message you want to text or 'finished' to move on\n")
    words = []
    while msg.lower() != 'finished':
        msg = msg.split(' ')
        for word in msg:
            words.append(word)
        msg = input()

    number = input(
        "Type the Phone number you would like to text, number should be fomratted like '1234567890'\n")
    while len(number) < 10 or len(number) > 10:
        number = input(
            "Invalid lengthed number\n Enter 10 digit number below\n")
    for word in words:
        send_message(number, word)
    send_message(number, "-Sent from Riyad's Bot :D")

    print("Thank you for using Dexter the Texter\n")

import random


def welcome_msg(what_to_do, s, botnick, channel):
    get_nick = what_to_do[0].split("!")
    nick = get_nick[0][1:]
    if nick == botnick:
        pass
    else:
        list=['Greetings and salutations!','Welcome, ','Yo!', 'Top of the mornin’ to ya!', 'Hey there,', 'Why, hello there!',
        'Holla', 'Good morning','Greetings', 'Sup', 'Hello!']
        random_hi= random.choice(list)
        welcomemsg = "PRIVMSG "+channel+" :"+random_hi+" "+nick+"\r\n"
        welcomes_b =bytes(welcomemsg, 'utf-8')
        s.sendall(welcomes_b)

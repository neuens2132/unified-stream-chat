import socket
import re


# pulling from a twitch chat
serverTwitch = 'irc.chat.twitch.tv'
portTwitch = 6667
nicknameTwitch = 'grabbing-data'
tokenTwitch = 'oauth:ods3nm5325qwpzg5ampjozyu7kpzo4'
channelTwitch = '#tarik'

sock = socket.socket()
sock.connect((serverTwitch, portTwitch))

sock.send(f"PASS {tokenTwitch}\n".encode('utf-8'))
sock.send(f"NICK {nicknameTwitch}\n".encode('utf-8'))
sock.send(f"JOIN {channelTwitch}\n".encode('utf-8'))

while True:
    resp = sock.recv(2048).decode('utf-8')
    if len(resp) > 0:
        match = re.match(r"^:([^!]*)!.* :(.*)$", resp)
        if match:
            username = match.group(1)
            message = match.group(2)
            if(username != "fossabot" and username != "nightbot" and not (message.startswith("!"))):
                print(f"TWITCH [{username}] : {message}")
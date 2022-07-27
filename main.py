# Modules which need to be installed
import irc.bot
from dotenv import load_dotenv

# Setup
import os
load_dotenv()

class TwitchListener(irc.bot.SingleServerIRCBot):
    def __init__(self, username, token, channel):
        self.token = token
        self.channel = '#' + channel


        server = 'irc.chat.twitch.tv'
        port = 6667

        print('Connecting to Twitch IRC: ' + server + ' on port ' + str(port))
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], username, username)

    def on_welcome(self, c, e):
        print('Joining ' + self.channel)
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0].split(' ')[0][1:]
            print('Received command: ' + cmd)
        return

bot = TwitchListener(str(os.getenv('TWITCHUSERNAME')), str(os.getenv('TWITCHTOKEN')), str(os.getenv('TWITCHUSERNAME')))
bot.start()
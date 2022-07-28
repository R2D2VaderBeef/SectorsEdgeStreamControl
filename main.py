# Modules which need to be installed
import irc.bot
from dotenv import load_dotenv
load_dotenv()

# Setup / included imports
import os
import commands
import asyncio
prefix = os.getenv('COMMANDPREFIX')

# Login to IRC as the streamer and listen for commands in Twitch Chat
class TwitchListener(irc.bot.SingleServerIRCBot):
    def __init__(self, username, token, channel):
        self.token = token
        self.channel = '#' + channel

        server = 'irc.chat.twitch.tv'
        port = 6667

        # Login to Twitch IRC
        print('Connecting to Twitch IRC: ' + server + ' on port ' + str(port))
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], username, username)

    # Join this streamer's Twitch Chat channel
    def on_welcome(self, c, e):
        print('Joining ' + self.channel)
        c.join(self.channel)

    # Listen for messages, and if they start with the prefix, try to execute them as commands
    def on_pubmsg(self, c, e):
        if e.arguments[0][:1] == prefix:
            cmd = e.arguments[0].split(' ')[0][1:]
            asyncio.run(commands.handleCommand(cmd))
        return

# Load the Twitch login values from the .env file and run the IRC 'bot' above
bot = TwitchListener(str(os.getenv('TWITCHUSERNAME')), str(os.getenv('TWITCHTOKEN')), str(os.getenv('TWITCHUSERNAME')))
bot.start()
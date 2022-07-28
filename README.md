# SectorsEdgeStreamControl
### Let your Twitch Stream control your Sector's Edge gameplay!

This code listens to messages from your Twitch chat (via your own Twitch account) and presses buttons/keys accordingly to make you do an action in-game. 

## Setup

1. **Download all the files.** 

You can click on the green "Code" button at the top right, and then click on "Download ZIP". Once it's downloaded, extract the files to their own folder in your chosen location.

Alternatively, you can `git clone` this repository and keep the files updated with `git pull`, but I won't provide a tutorial on how to do that.

2. **Install the dependencies.**

Make sure you have a relatively new version of Python 3 installed. I tested this on Python 3.10 and would recommend using the latest stable version if it works.

Also install AutoHotKey from their official website.

Then. run the following command in your terminal:
```
pip install ahk irc python-dotenv
```

3. **Input your Twitch account details.**

Rename the `default.env` file to just `.env` (set the file name to be blank). Open it and input your Twitch username next to the first option.

Head to [twitchapps.com/tmi](https://twitchapps.com/tmi/) to get your Chat OAuth Token to copy and paste next to the second option. 

Example of how it should be formatted:
```yml
# Write the config values to the right of the equals sign, with no space inbetween.
# Your Twitch username
TWITCHUSERNAME=r2d2vader
# Your Twitch Chat OAuth token (from https://twitchapps.com/tmi/)
TWITCHTOKEN=oauth:xxxxxxxxx
```

4. **Run the program** by running `python main.py` in your terminal.
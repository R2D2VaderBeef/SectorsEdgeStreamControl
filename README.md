# SectorsEdgeStreamControl
### Let your Twitch Stream control your Sector's Edge gameplay!

This code listens to messages from your Twitch chat (via your own Twitch account) and presses buttons/keys accordingly to make you do an action in-game. 

Currently, this system only supports Hold to Scope / Hold to Crouch rather than Toggle. You also need to input your binds manually if they are different to mine.

Neither of these caveats will be present in the first 'complete' version, in which I hope to pull binds directly from the game settings files.

## Setup

1. **Download all the files.** 

You can click on the green "Code" button at the top right, and then click on "Download ZIP". Once it's downloaded, extract the files to their own folder in your chosen location.

Alternatively, you can `git clone` this repository and keep the files updated with `git pull`, but I won't provide a tutorial on how to do that.

2. **Install the dependencies.**

Make sure you have a relatively new version of Python 3 installed. I tested this on Python 3.10 and would recommend using the latest stable version if it works.

Also install AutoHotKey from their official website.

Then, run the following command in your terminal:
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

You should see the following messages in the console: 
```
Connecting to Twitch IRC: irc.chat.twitch.tv on port 6667
Joining #yourtwitch
```
In case you only see the first one, this can indicate that something has gone wrong. If you're sure you've setup your credentials correctly, exit the program and try again. 

Press `Ctrl+C` to exit.

Whenever a valid command is run, you will see logs of the random number calculated to check against the `probability` setting, e.g.
```
Command SCOPE => Prob: 1.0 Random: 0.7
```

 If the command is run, a further line will be logged:
```
Acted: SCOPE
```

## Config Settings

All configuration is done within the `.env` file. Every setting other than the Twitch credentials has a default filled in already.

You might want to change the prefix in case it clashes with another bot's commands, or make it the same as another bot on purpose. By default, it is set to `!`, so viewers would run commands like `!shoot`.

```yml
# .env Line 11
COMMANDPREFIX=!
```

You can edit the options for each command in the Command Settings section. For example, say I want to disable the Scope command:

```yml
# .env Line 65
CMD_SCOPE_enabled=false
```

Here's an explanation of the Command Settings which is also present within the file:
```yml
CMD_X_enabled: Whether the command can be run in Twitch chat (true / false). 
CMD_X_command: The actual command users can run in Twitch chat.
CMD_X_input: For simple button press commands, the keybind to press (temporary solution).
CMD_X_duration: For held inputs, how long to hold them for (in seconds). For non-held inputs, this is 0.
CMD_X_probability: If a random decimal is lower than or equal to this, the command will run (decimal between 0 and 1). By default these are all set to 1 (100% chance of running).
```

The `CMD_X_input` options use the AHK Key Names. [Here's a list](https://www.autohotkey.com/docs/KeyList.htm). 

Now let's say I want to enable the Scope command, let my viewers run it by running `!telescope`, make it stay scoped for 4.2 seconds, and make it only run around 33% of the time:
```yml
# .env Line 65-69
CMD_SCOPE_enabled=true
CMD_SCOPE_command=telescope
CMD_SCOPE_input=RButton
CMD_SCOPE_duration=4.2
CMD_SCOPE_probability=0.33
```
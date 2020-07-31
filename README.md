# QnA Bot
A Discord bot that is purposely used for online class as a simple online "test paper" and a moderation bot.

Bot is still in development at this moment.

## Preparation
**For Windows users**

Before downloading the source code, you will need to download and install `Python` first by going [here](https://www.python.org/downloads/).
After downloading the installer, run it and make sure you have ticked the box "Add Python 3.x to PATH" before installing.

After installing Python, you have to open Command Prompt and install `discord.py` by typing `py -3 -m pip install -U discord.py` into
the Command Prompt.

After installing `discord.py`, you will need to download the lastest source code [here](https://github.com/SilentVOEZ/qna-bot/releases) 
and extract it anywhere you like.

**For Linux users**

***Soon***™

## Creating and setting up the bot
If you don't have Discord account yet, go to [Discord](https://discord.com) and create a new account. Also, you can download their client
application for all platforms and then logging in after creating an account.

After creating an account and your username (**not your real name!**) go ahead visit the [developer](https://discord.com/developers) page
and create a new application by clicking the blue button on top-right corner.

From here you can put any name if you want for the application but I recommend you to type `QnA Bot` to prevent confusion.

Once you have created the application, this is optional but you can add the "official" profile picture of the bot by download it [here](https://i.imgur.com/ou57QfT.png)
or anything you want and then uploading it to the website.

If you did the optional step, now go to the "Bot" on the left panel and click the "Add Bot". When you receive a notice, just click
"Yes, do it!" and you have successfully created a bot!

## Inviting the bot to your server
After you created the bot (and you have created a server), head over to "OAuth2" on the left panel and you will now have to tick some boxes for the bot.

Tick the `bot` box first on the Scopes area and then tick the following boxes below according to the bot's functions on Bot Permissions area.
`Kick Members`, `Ban Members`, `View Channels`, `Send Messages`, `Manage Messages`, `Embed Links`, `Read Message History`, `Use External
Emojis`, and `Add Reactions`.

After you ticked the necessary boxes, click "Copy" on the Scopes area and then visiting the link by creating a new tab and then pasting it.
You will now get greeted where you will invite the bot. You just have to select your server and then clicking "Continue" and "Authorize" it.
You may also get into a CAPTCHA process but it's easy and you will get greeted that the bot is successfully invited to your server.

## Running the program
Go back to the [developers](https://discord.com/developers) page and go to the "Bot" section. This time you will going to take the bot's
token to use with the program.

When you are in the Bot section, click "Copy" below the "Click to Reveal Token" and to go the root folder of qna-bot. When you are in the root
folder of qna-bot, open `token.txt` and then clear the content of it and then paste the token and save it.
Be warned that when someone saw your bot token, they can use your bot without your control! When in doubt, go to the Bot section of the
[developers](https://discord.com/developers) page, click "Regenerate" and then "Copy" and then paste the token in the `token.txt`

After that, you just have to open `qnamain.py` and you a console window will appear. Or you can run it on Command Prompt by navigating to
the root directory of `qna-bot` and then typing `py qnamain.py`.

Once you get the "successfully connected" message on the console, everything is working.

## Setting up additional things
Since we have successfully run the program, we need to take some user ID from admins or mods to use some owner-based commands on the bot.

If you navigate to the root folder of qna-bot you will see the `author.txt` file. If you open it, you will see a random number inside the
text file which is 

`170093603530473472`

**Don't delete that number since that's my ID when you need an assistance from me.**

To get the user ID from other members, make sure the bot is closed at the moment. Open your Discord client and make sure you have "Developer Mode"
enabled from the setting. You can look it up [here](https://imgur.com/a/2u9d0MF).

If the "Developer Mode" is enabled, go back to your server and look up the name of that member you want to add on the member list or on the left side.
Right click on their name and then click "Copy ID". Now you just have to paste on `author.txt` but I said that you must not delete my ID, here's how.

Just add comma after my ID and then add space after the comma and paste the ID. Like this

`170093603530473472, 1700xxxxxxx123456`

If you want to add more user to use the owner-based command, it's the same like I said above which it looks like this.

`170093603530473472, 17001700xxxxxxx123456, 240065xxxxxxx789012, 580293xxxxxxx654321`

And then save the text file.

## Using the bot as a test paper
***Soon***™

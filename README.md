# QnA Bot
A Discord bot that is used for online class as a simple online "test paper" and a moderation bot.
 
The true purpose of this bot is to use for schools that doesn't have a website infrastructure. The bot will use
[Discord](https://www.discord.com) as the platform. It is simple and easy to manage.
 
**Bot is in final on Pre-release stage**

- [QnA Bot](#qna-bot)
  * [Setting it up](#setting-it-up)
    + [Preparation](#preparation)
    + [Creating and setting up the bot](#creating-and-setting-up-the-bot)
    + [Inviting the bot to your server](#inviting-the-bot-to-your-server)
    + [Running the program](#running-the-program)
    + [Setting up additional things](#setting-up-additional-things)
  * [Using the bot](#using-the-bot)
    + [The commands](#the-commands)
    + [Using the bot as a test paper](#using-the-bot-as-a-test-paper)


## Setting it up

### Preparation
**For Windows users**

Before downloading the source code, you will need to download and install `Python` first by going [here](https://www.python.org/downloads/).
After downloading the installer, run it and make sure you have ticked the box "Add Python 3.x to PATH" before installing.

After installing Python, you have to open Command Prompt and install `discord.py` by typing `py -3 -m pip install -U discord.py` into
the Command Prompt.

After installing `discord.py`, you will need to download the lastest source code [here](https://github.com/SilentVOEZ/qna-bot/releases) 
and extract it anywhere you like.

**For Linux users**

Most Linux distribution have `python3` preinstalled. But if you are unsure, open a terminal and type `apt-get install python3` with root
privilege. And then install `discord.py` by typing `python3 -m pip install -U discord.py`.

### Creating and setting up the bot
If you don't have Discord account yet, go to [Discord](https://discord.com) and create a new account. Also, you can download their client
application for all platforms and then logging in after creating an account.

After creating an account and your username (**not your real name!**) go ahead visit the [developer](https://discord.com/developers) page
and create a new application by clicking the blue button on top-right corner.

From here you can put any name if you want for the application but I recommend you to type `QnA Bot` to prevent confusion.

Once you have created the application, this is optional but you can add the "official" profile picture of the bot by download it [here](https://i.imgur.com/ou57QfT.png)
or anything you want and then uploading it to the website.

If you did the optional step, now go to the "Bot" on the left panel and click the "Add Bot". When you receive a notice, just click
"Yes, do it!" and you have successfully created a bot!

### Inviting the bot to your server
After you created the bot (and you have created a server), head over to "OAuth2" on the left panel and you will now have to tick some boxes for the bot.

Tick the `bot` box first on the Scopes area and then tick the following boxes below according to the bot's functions on Bot Permissions area.
`Kick Members`, `Ban Members`, `View Channels`, `Send Messages`, `Manage Messages`, `Embed Links`, `Read Message History`, `Use External
Emojis`, and `Add Reactions`.

After you ticked the necessary boxes, click "Copy" on the Scopes area and then visiting the link by creating a new tab and then pasting it.
You will now get greeted where you will invite the bot. You just have to select your server and then clicking "Continue" and "Authorize" it.
You may also get into a CAPTCHA process but it's easy and you will get greeted that the bot is successfully invited to your server.

### Running the program
Go back to the [developers](https://discord.com/developers) page and go to the "Bot" section. This time you will going to take the bot's
token to use with the program.

When you are in the Bot section, click "Copy" below the "Click to Reveal Token" and to go the root folder of qna-bot. When you are in the root
folder of qna-bot, open `token.txt` and then clear the content of it and then paste the token and save it.
*Be warned that when someone saw your bot token, they can use your bot without your control! When in doubt, go to the Bot section of the
[developers](https://discord.com/developers) page, click "Regenerate" and then "Copy" and then paste the token in the `token.txt`*

After that, you just have to open `qnamain.py` and you a console window will appear. Or you can run it on Command Prompt by navigating to
the root directory of `qna-bot` and then typing `py qnamain.py`. For Linux users, navigate to the root folder on terminal and execute it
by typing `python3 qnamain.py`.

Once you get the "successfully connected" message on the console, everything is working.

### Setting up additional things
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

## Using the bot
The bot's default command prefix is `q!` and this will invoke the bot. It should look like this 

`q!help`
`q!ping`
`q!userinfo`

You can change the command prefix by opening `prefix.txt` on the root folder and
replacing `q!` with anything followed by a special character like `q.`, `n&`, `a!`.

### The commands
These are the commands that you can use to interact with the bot. You can also look up the commands by typing `q!help` while the bot is online.

**General Commands**
- `ping` - Respond with "Pong!" and latency time.
- `say` - Make the bot say with your response. - **Usage: `q!say Hello world!`
- `uptime` - Shows how long the bot has been up for.
- `userinfo` - Shows info of a mentioned user or yourself. - **Usage: `q!userinfo @SilentVOEZ`**
- `version` - Shows the bot version.

**Fun**
- `rps` - Play rock, paper, scissors! - **Usage: `q!rps rock`**
- `eightball` - Ask the eightball for question. - **Usage: `q!eightball Will I get a tasty food later?`**
- `haachama` - Have some cooking tips from Akai Haato. (p.s. It's not a legit cooking tip)

**Testpaper**
- `tphelp` - Shows the testpaper help.
- `testpaper` - Sends the test question as a Direct Message - **Usage: `q!testpaper <subject>`, `q!testpaper science`**

**Moderation/Utility (Administrator/Owner only)**
- `kick` - Kicks a member on the server. - **Usage: `q!kick <user> <reason>`, `q!kick @VOID Being negative to the chat.`**
- `ban` - Bans a member on the server. - **Usage: `q!ban <user> <reason>`, `q!ban @VOID Sent an NSFW picture on #general.`**
- `purge` - Clears messages with a certain amount. - **Usage: `q!purge <amount>`, `q!purge 25`**
- `status` - Set the bot's online status.
- `shutdown` - Shuts down the bot outside the terminal.

### Using the bot as a test paper
This bot can be used as a digital question paper for a pop quiz, long test, and a periodical test.

Before using the `testpaper` command to everyone (or the students I should say), take a look at the dedicated help for the `testpaper` command
by sending `tphelp` on Discord. In here, you need to edit the `tphelp.txt` which is located on folder `testpaper`. It has a reference for you
to add your class subject that into the file. You can delete everything **but make sure to add `>>>` in the very beginning of the file**.

Example:
```
>>> Akihabara High

`q!testpaper readingandwriting` - Begin the test for the subject Reading and Writing.
`q!testpaper calculus` - Begin the test for the subject Calculus.
`q!testpaper humananatomy` - Begin the test for the subject Human Anatomy.
`q!testpaper pambansangwika` - Begin the test for the subject Pambansang Wika.
...
and so forth
```

***NOTE: If you changed the bot's prefix on the prefix file into something like `a!`, you need to also change `q!` on `tphelp` into your own
prefix like this:***
```
>>> Akihabara High

`a!testpaper readingandwriting` - Begin the test for the subject Reading and Writing.
`a!testpaper calculus` - Begin the test for the subject Calculus.
`a!testpaper humananatomy` - Begin the test for the subject Human Anatomy.
`a!testpaper pambansangwika` - Begin the test for the subject Pambansang Wika.
```

If this bot will be used by the whole school with other grade levels most especially when all grade level have the same subject name,
you may have to differentiate it by adding number at the end of the name of the subject indicating the grade level and adding categories to
avoid conflict with other class subject and possibly the file structure on `testpaper` folder.

Example:
```
>>> Akihabara High

Grade 7:
q!testpaper english7 - Begin the test for the subject English 7.
q!testpaper science7 - Begin the test for the subject Science 7.
q!testpaper math7 - Begin the test for the subject Math 7.
q!testpaper tle7 - Begin the test for the subject TLE 7.
q!testpaper filipino7 - Begin the test for the subject Filipino 7.

Grade 8:
q!testpaper english8 - Begin the test for the subject English 8.
q!testpaper science8 - Begin the test for the subject Science 8.
q!testpaper math8 - Begin the test for the subject Math 8.
q!testpaper tle8 - Begin the test for the subject TLE 8.
q!testpaper filipino8 - Begin the test for the subject Filipino 8.
q!testpaper comsci - Begin the test for the subject Computer Science.

Grade 9:
q!testpaper english9 - Begin the test for the subject English 9.
q!testpaper science9 - Begin the test for the subject Science 9.
q!testpaper math9 - Begin the test for the subject Math 9.
q!testpaper tle9 - Begin the test for the subject TLE 9.
q!testpaper filipino9 - Begin the test for the subject Filipino 9.
q!testpaper dramaarts - Begin the test for the subject Drama Arts.

Grade 10:
q!testpaper english10 - Begin the test for the subject English 10.
q!testpaper science10 - Begin the test for the subject Science 10.
q!testpaper math10 - Begin the test for the subject Math 10.
q!testpaper tle10 - Begin the test for the subject TLE 10.
q!testpaper filipino10 - Begin the test for the subject Filipino 10.
q!testpaper he - Begin the test for the subject Home Economics.
```

After editing the `tphelp.txt` for your class subject or the whole school. It's time for you to make a test question for the whole
class or the whole school. Inside the `testpaper` you will find 3 text files that is `english.txt`, `math.txt` and `science.txt` with
almost the same content that you will gonna use for a reference.

Example:
```
>>> Akihabara High School
Subject: Science

Direction: Choose your answer on the list and send it to your subject teacher through direct message.

1. Anything that occupies space and has mass.
a. Object   b. Matter   c. Things   d. String

2. Aside from the three common state of matter, what do you call the fourth kind of matter?
a. Solid    b. Gas    c. Plasma     d. Liquid

3. This state of matter where molecules are closely packed together
a. Solid    b. Gas    c. Plasma     d. Liquid

4. This state of matter has definite volume but no fixed shape.
a. Solid    b. Gas    c. Plasma     d. Liquid

5. This state of matter has no fixed shape and no fixed volume.
a. Solid    b. Gas    c. Plasma     d. Liquid

6...
a...

and so forth...
```

After you edit the {subject}.txt and saved it inside `testpaper`, you can now go ahead start the online class and the question paper is
prepared for the quiz.

And after the quiz, you can make another text file for the next topic and then overwriting/deleting the old text file inside `testpaper`.

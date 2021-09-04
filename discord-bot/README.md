# Python Discord

<br/>

## List of Contents:
### 1. [Python Discord Bot Tutorial – Code a Discord Bot And Host it for Free](#content-1)



<br/>

---

## Contents:

## [Python Discord Bot Tutorial – Code a Discord Bot And Host it for Free](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) <span id="content-1"></span>


### How to Create a Discord Bot Account
- Make sure you’re logged on to the [Discord website](https://discord.com/).
- Navigate to [the application page](https://discord.com/developers/applications).
- Click on the “New Application” button.
- Give the application a name and click “Create”.
- Go to the “Bot” tab and then click “Add Bot”. You will have to confirm by clicking "Yes, do it!"
- Keep the default settings for Public Bot (checked) and Require OAuth2 Code Grant (unchecked).
- Your bot has been created. The next step is to copy the token.
- Keep your token to yourself!


### How to Invite Your Bot to Join a Server
- Go to the "OAuth2" tab. Then select "bot" under the "scopes" section.
- Now choose the permissions you want for the bot.
- After selecting the appropriate permissions, click the 'copy' button above the permissions. That will copy a URL which can be used to add the bot to a server.
- Paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”.
- To add the bot, your account needs "Manage Server" permissions.


### How to Create a Repl and Install discord.py
- Start by going to [Repl.it](https://repl.it/). Create a new Repl and choose "Python" as the language.


### How to Set Up Discord Events for Your Bot
- `discord.py` revolves around the concept of events.
- An event is something you listen to and then respond to. For example, when a message happens, you will receive an event about it that you can respond to.
- Your very first python discord bot code:
  ```python
  import discord
  import os
  
  client = discord.Client()
  
  @client.event
  async def on_ready():
      print('We have logged in as {0.user}'.format(client))
  
  @client.event
  async def on_message(message):
      if message.author == client.user:
          return
  
      if message.content.startswith('$hello'):
          await message.channel.send('Hello!')
  
  client.run(os.getenv('TOKEN'))
  ```
- Now let's go over what each line of code is doing in your Discord bot code.
  - The first line imports the discord.py library.
  - The second line imports the os library, but this is only used for getting the `TOKEN` variable from the `.env` file. If you are not using a `.env` file, you do not need this line.
  - Next, we create an instance of a Client. This is the connection to Discord.
  - The `@client.event()` decorator is used to register an event. This is an asynchronous library, so things are done with callbacks. A callback is a function that is called when something else happens. In this code, the on_ready() event is called when the bot is ready to start being used. Then, when the bot receives a message, the on_message() event is called.
  - The `on_message()` event triggers each time a message is received but we don't want it to do anything if the message is from ourselves. So if the `Message.author` is the same as the `Client.user` the code just returns.
  - Next, we check if the `Message.content` starts with `$hello`. If so, then the bot replies with `Hello!` to the channel it was used in.

  
### How to Add Inspirational Quotes to the Bot
- Code:
  ```python
  import discord
  import os
  import requests
  import json
  
  client = discord.Client()
  
  def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)
  
  @client.event
  async def on_ready():
    print('We have logged in as {0.user}'.format(client))
  
  @client.event
  async def on_message(message):
    if message.author == client.user:
      return
  
    if message.content.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)
  
  client.run(os.getenv('TOKEN'))
  ```


### How to Add Encouraging Messages to the Bot
- Add sad words to the bot:
  ```python
  sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
  ```
- Basically, after this point you can play with your own thing.

### How to Enable User-submitted Messages
- Code:
  ```python
  async def on_message(message):
    if message.author == client.user:
      return
  
    msg = message.content
   
    if msg.startswith("$inspire"):
      quote = get_quote()
      await message.channel.send(quote)
  
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]
  
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))
  
    if msg.startswith("$new"):
      encouraging_message = msg.split("$new ",1)[1]
      update_encouragements(encouraging_message)
      await message.channel.send("New encouraging message added.")
  
    if msg.startswith("$del"):
      encouragements = []
      if "encouragements" in db.keys():
        index = int(msg.split("$del",1)[1])
        delete_encouragment(index)
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)
  ```

### Final Bot Features
- Final code:
  ```python
  import discord
  import os
  import requests
  import json
  import random
  from replit import db
  
  client = discord.Client()
  
  sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
  
  starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot!"
  ]
  
  if "responding" not in db.keys():
    db["responding"] = True
  
  def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return(quote)
  
  def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
      encouragements.append(encouraging_message)
      db["encouragements"] = encouragements
    else:
      db["encouragements"] = [encouraging_message]
  
  def delete_encouragment(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
      del encouragements[index]
    db["encouragements"] = encouragements
  
  @client.event
  async def on_ready():
    print("We have logged in as {0.user}".format(client))
  
  @client.event
  async def on_message(message):
    if message.author == client.user:
      return
  
    msg = message.content
  
    if msg.startswith("$inspire"):
      quote = get_quote()
      await message.channel.send(quote)
  
    if db["responding"]:
      options = starter_encouragements
      if "encouragements" in db.keys():
        options = options + db["encouragements"]
  
      if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))
  
    if msg.startswith("$new"):
      encouraging_message = msg.split("$new ",1)[1]
      update_encouragements(encouraging_message)
      await message.channel.send("New encouraging message added.")
  
    if msg.startswith("$del"):
      encouragements = []
      if "encouragements" in db.keys():
        index = int(msg.split("$del",1)[1])
        delete_encouragment(index)
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)
  
    if msg.startswith("$list"):
      encouragements = []
      if "encouragements" in db.keys():
        encouragements = db["encouragements"]
      await message.channel.send(encouragements)
      
    if msg.startswith("$responding"):
      value = msg.split("$responding ",1)[1]
  
      if value.lower() == "true":
        db["responding"] = True
        await message.channel.send("Responding is on.")
      else:
        db["responding"] = False
        await message.channel.send("Responding is off.")
  
  client.run(os.getenv("TOKEN"))
  ```

**[⬆ back to top](#list-of-contents)**

<br/>

---
## References:
- https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
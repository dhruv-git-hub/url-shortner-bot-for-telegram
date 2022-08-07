from pyrogram import Client,filters
bot = Client(
    "MY first project",
    api_id = 11363673,
    api_hash = '9092d33af68c40aeed371f278ffd75ee',
    bot_token='5290496073:AAGr8DiKkiyk1LeY81inSUKCZqiWQ0nuwy4'

)
#Start message
@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):

    bot.send_message(message.chat.id, "Heya, I am a simple test bot.")
#help cmd
@bot.on_message(filters.command('help'))
def command2(bot,message):
    
    message.reply_text("HELP IS ON THE WAY")
     
#welcome text for new joiner
group=""#"add the numbers here"#grp id/username

@bot.on_message(filters.chat(group)&filters.new_chat_members)
def welcomebot(client,message):
    message.reply_text("Welcome")

#send photo
@bot.on_message(filters.command('photo'))
def command3(bot,message):
    bot.send_photo(message.chat.id,"https://imgur.com/gallery/YUJYQ")
    


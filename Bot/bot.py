from pyrogram import Client,filters
import os
bot = Client(
    "MY first project",
    api_id = os.environ.get('api_id'),
    api_hash = os.environ.get('api_hash'),
    bot_token=os.environ.get('bot_token')

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
    
    
print("Sucessfully completed an orbit")
bot.run()

    

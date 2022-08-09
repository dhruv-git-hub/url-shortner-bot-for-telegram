from pyrogram import Client,filters
import webbrowser
import wikipedia
import random
import tgcrypto
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

    
@bot.on_message(filters.command('song'))
def command3(bot,message):
    bot.send_video(message.chat.id,"https://www.youtube.com/watch?v=HxxNFEyDAy0")
 
@bot.on_message(filters.command('wiki'))
def command4(bot,message):
    qq=message.text
    ans=qq.split(" ",1)
    
    try:
        w=ans[1].title()
        q=wikipedia.summary(w)
        bot.send_message(message.chat.id,q)
    except wikipedia.DisambiguationError as e:
        s = random.choice(e.options)
        print(type(s))
        print(s)
        p = wikipedia.summary(s)
        bot.send_message(message.chat.id,p)

######################################################################################################
@bot.on_message(filters.command('browser'))
def command5(bot,message):
    qq=message.text
    f=webbrowser.open(qq[9:]+".com")
    #bot.send_message(message.chat.id,f)
    print(qq[8:])
    
    
    
print("Sucessfully completed an orbit")
bot.run()

    

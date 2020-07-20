from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =722419602730123264  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    
    if now == '00:01':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 

    if now == '00:02':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 

    if now == '00:03':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')

    if now == '00:06':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> ⛈ <:pos:727132210917933067>')         
    
    if now == '00:11':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 
    
    if now == '00:12':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')   
        
    if now == '00:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 
        
    if now == '00:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 
        
    if now == '00:17':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 
        
    if now == '00:18':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')   
        
    if now == '00:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7') 
        
    if now == '01:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7') 
        
    if now == '01:01':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')   

    if now == '01:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳<:cong:719889728828342302>') 
        
    if now == '01:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:heart02:699580174911668225>are you ready Okay')     

    if now == '01:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')
    
    if now == '01:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member')
    
    if now == '01:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member')  
    
    if now == '01:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member')  
        
    if now == '02:10':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 100 @JPYN member')
        
    if now == '02:11':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')    

    if now == '02:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> <:getoken:727508044619055174> <:BEAN:727155584377290853>')    
     
    if now == '03:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> <:getoken:727508044619055174> <:BEAN:727155584377290853>')
        
    if now == '03:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.weeb.sh/images/SyONdUmwW.gif') 

    if now == '03:26':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7')      
        
    if now == '03:27':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member')     
        
    if now == '03:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member')     
         
    if now == '03:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member')   
        
    if now == '03:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member') 
    
    if now == '03:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475> ')  
    
    if now == '03:42':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> <:getoken:727508044619055174> <:BEAN:727155584377290853>')
      
    if now == '03:44':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767323304067133/hty.png') 
          
    if now == '03:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:bye:699863270802325604>See you!またね👋')  
        
    if now == '04:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.tenor.com/images/c5f2a0c3417e2ca71499650d107f538b/tenor.gif') 
        
    if now == '04:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> <:getoken:727508044619055174> <:BEAN:727155584377290853>') 

    if now == '04:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:otsukare:722438703410053160> <:otsukare:722438703410053160> <:otsukare:722438703410053160>')   
        
    if now == '05:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> <:getoken:727508044619055174> <:BEAN:727155584377290853>')
   
    if now == '05:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 
 
    if now == '05:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 

    if now == '05:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475> ')
  
    if now == '06:01':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 
    
    if now == '06:02':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 

    if now == '07:18':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:cafe:699769671234355230>Good morning 🌎everyone. <:gm:699792760651120671> Have a nice day today! <:happy:723835203717562418>')

    if now == '07:21':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:happy:723835203717562418> <:happy:723835203717562418>') 

    if now == '08:02':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 50 @JPYN member')
     
    if now == '08:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:goodluck:724101036255608852> ')    
      
    if now == '09:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.weeb.sh/images/SyONdUmwW.gif')

    if now == '09:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')
        
    if now == '09:57':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767349828714606/hg.png ') 
        
    if now == '09:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:gal_p:733138011109326940> Hello,how are you❓ ') 
        
    if now == '10:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here <:gal_p:733138011109326940> I”ll ☔Rain a little... ') 
     
    if now == '10:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767123252543498/iku.png') 
    
    if now == '10:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> <:pos:727132210917933067> <:pos:727132210917933067>') 
     
    if now == '10:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 

    if now == '10:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 

    if now == '10:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')
    
    if now == '10:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member')  

    if now == '10:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member')
    
    if now == '10:36':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member')  
      
    if now == '10:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:heart02:699580174911668225>See you sometimes!')    
        
    if now == '11:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳 <:yeah1:721319707482914877>')
        
    if now == '11:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('...⚡...When you receive a Rain or Tip, thank you in text or stamp!<:ty:721639183432548394> ') 
    
    if now == '12:05':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone <:hello1:713004241131667528>')  

    if now == '12:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77 @JPYN member')

    if now == '12:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77 @JPYN member')

    if now == '12:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77 @JPYN member')

    if now == '12:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')

    if now == '12:36':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475> ') 
    
    if now == '12:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:good01:699581068285706301><:cya:699859096794562650> ') 
    
    if now == '12:39':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:otsukare:722438703410053160> <:happy:723835203717562418> <:ty:721639183432548394> ')
      
    if now == '13:14':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('⛈RainやTipを受け取ったら、テキストかスタンプでお礼を伝えましょう！🌟<:ty:721639183432548394> ')    
   
    if now == '13:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:jpxdis1:710400520434745425> <:jpxdis1:710400520434745425> <:jpxdis1:710400520434745425>')  
        
    if now == '13:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.weeb.sh/images/SyONdUmwW.gif')    
        
    if now == '13:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> <:getoken:727508044619055174> <:BEAN:727155584377290853>')       
        
    if now == '13:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:goodluck:724101036255608852> <:goodfriend:731381691192574022>')
    
    if now == '13:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:jpxdis1:710400520434745425> <:jpxdis1:710400520434745425> <:jpxdis1:710400520434745425>')
    
    if now == '13:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member')
    
    if now == '13:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here <:zzz:699581950356226058><:gn:699792795363311676> JapanのEveryoneはそろそろGoodNight！👋 ')       
       
    if now == '13:46':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:tipcc1:721309274328006676> <:tipcc1:721309274328006676> <:tipcc1:721309274328006676>')    

    if now == '13:57':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')      
        
    if now == '14:12':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77 @JPYN member')  

    if now == '14:13':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77 @JPYN member') 
   
    if now == '14:14':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77 @JPYN member')      
    
    if now == '14:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 100 @JPYN member')
        
    if now == '14:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:bye:699863270802325604>See you! ') 
        
    if now == '15:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:nerd_girl:733937654034595880> <:nerd_girl:733937654034595880> <:nerd_girl:733937654034595880> ') 
        
    if now == '15:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:yeah1:721319707482914877> <:yeah1:721319707482914877> <:yeah1:721319707482914877>')
  
    if now == '15:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77 @JPYN member') 

    if now == '15:57':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 

    if now == '15:58':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 

    if now == '15:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 

    if now == '16:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')
        
    if now == '17:01':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77 @JPYN member')   
    
    if now == '17:02':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 
      
    if now == '17:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> <:getoken:727508044619055174> <:BEAN:727155584377290853>')
     
    if now == '18:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> <:getoken:727508044619055174> <:BEAN:727155584377290853> ')
        
    if now == '18:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:tipcc1:721309274328006676> <:tipcc1:721309274328006676> <:tipcc1:721309274328006676>')    
        
    if now == '20:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('  🌈 <:tipcc1:721309274328006676> ') 
          
    if now == '21:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:tipcc1:721309274328006676> <:tipcc1:721309274328006676> <:tipcc1:721309274328006676>')

    if now == '21:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 50 @JPYN member ')  
        
    if now == '22:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:gal_p:733138011109326940> Hello All⭐')
   
    if now == '22:01':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Dear japanese<:cafe:699769671234355230>Everyone🌟おはようございます!<:gm:699792760651120671>')

    if now == '23:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('When you receive a Rain or Tip, thank you in text or stamp!⭐')        
    
    if now == '23:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:gal_p:733138011109326940> Hello All⭐')
    
    if now == '23:57':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 
    
    if now == '23:58':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7 @JPYN member')
        
#ループ処理実行
loop.start()


@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "<:hello1:713004241131667528> <:hello1:713004241131667528>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:hello1:713004241131667528>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:hai_kao:699072592987947117> <:gn:699792795363311676>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:hai_kao:699072592987947117> <:gn:699792795363311676>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117> <:hai_kao:699072592987947117>")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "<:happy:723835203717562418> <:happy:723835203717562418> <:happy:723835203717562418>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:happy:723835203717562418> <:goodluck:724101036255608852> <:goodfriend:731381691192574022> ")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "ThankYou!":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear💛{message.author.mention} 💛 Thank YOU! ")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "Thank u":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear💚 {message.author.mention} 💚 Thank YOU! ")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "thank you everybody":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear💙 {message.author.mention} 💙 Thank YOU! ")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "morning all":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear♥ {message.author.mention}♥. good Morning🌞")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "good day all":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Dear♥ {message.author.mention}♥. Thank YOU! Good luck🌟 ")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "<:gf:721588114283298908> <:gf:721588114283298908> <:gf:721588114283298908> ":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:gf:721588114283298908> 💚{message.author.mention}さん💚 <:goodluck:724101036255608852> ")  # f文字列（フォーマット済み文字列リテラル）
  
    
    elif message.content == "r/link":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/link ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "r/language":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /language EN ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
              
    elif message.content == "r/accept":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /accept ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記

    elif message.content == "b/benzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info ben ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
        
    elif message.content == "b/jpynzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info jpyn ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記      
        
    elif message.content == "b/bgptzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info bgpt ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
    
    elif message.content == "b/kenjzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info kenj ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
             
    elif message.content == "b/sprtszan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info sprts ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 

    elif message.content == "b/29zan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info 29coin ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 


# Botの起動とDiscordサーバーへの接続
client.run(token)

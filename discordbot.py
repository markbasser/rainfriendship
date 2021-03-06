from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =758265143627874314  #チャンネルID

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
        await channel.send('rsoak 200') 

    if now == '00:02':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 200') 

    if now == '00:03':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 500')
        
    if now == '00:04':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')
        
    if now == '00:05':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.weeb.sh/images/SyONdUmwW.gif') 

    if now == '00:06':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> ⛈ <:pos:727132210917933067>')   
        
    if now == '00:07':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> ') 
        
    if now == '00:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '00:09':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
        
    if now == '00:10':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '00:11':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
    
    if now == '00:12':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 500') 
    
    if now == '00:13':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock01:748437813631909888> <:rock01:748437813631909888> <:rock01:748437813631909888>')   
        
    if now == '00:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 200') 
        
    if now == '00:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 200') 
        
    if now == '00:17':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 500') 
        
    if now == '00:18':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock01:748437813631909888> <:rock_blue01:748437456852090940> <:rock01:748437813631909888>')   
        
    if now == '00:20':
        channel = client.get_channel(748426878527995915)
        await channel.send('<:rock01:748437813631909888> :guitar: <:rock01:748437813631909888> <:rock01:748437813631909888>') 
        
    if now == '00:21':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '00:22':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '00:23':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')     
        
    if now == '00:24':
        channel = client.get_channel(748426878527995915)
        await channel.send('<:rock01:748437813631909888> <:rock_blue01:748437456852090940> <:rock01:748437813631909888>')  
        
    if now == '00:40':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '00:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 200') 
        
    if now == '01:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 777') 
        
    if now == '01:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '01:09':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
        
    if now == '01:10':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')   

    if now == '01:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳') 
        
    if now == '01:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/698482526565564436/700566115897835571/jpyn-rain.gif') 
        
    if now == '01:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:heart02:699580174911668225>are you ready Okay')     

    if now == '01:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock01:748437813631909888> <:rock01:748437813631909888> <:rock01:748437813631909888>')
    
    if now == '01:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 333')
    
    if now == '01:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 333')  
    
    if now == '01:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 777 xjp member')  
        
    if now == '01:35':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '01:36':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '01:37':
        channel = client.get_channel(731640211733479556)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')      
             
    if now == '01:40':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  

    if now == '01:49':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ') 

    if now == '01:56':
        channel = client.get_channel(739438637661421579)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ') 
        
    if now == '02:08':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')

    if now == '02:09':
        channel = client.get_channel(782530102374170644)
        await channel.send('$soak 0.001')
        
    if now == '02:10':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 777 @JPYN member')
        
    if now == '02:11':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock01:748437813631909888> <:rock01:748437813631909888> <:rock01:748437813631909888>')
    
    if now == '02:40':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  

    if now == '02:49':
        channel = client.get_channel(698653628176531478)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ') 
        
    if now == '02:54':
        channel = client.get_channel(758265143627874314)
        await channel.send('=soak 0.01')  

    if now == '02:56':
        channel = client.get_channel(739463355864973342)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ')  
        
    if now == '02:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos_001:767212184052170753>')    
     
    if now == '03:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos_001:767212184052170753>')
        
    if now == '03:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '03:09':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
        
    if now == '03:10':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '03:18':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '03:19':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
        
    if now == '03:24':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940>')
        
    if now == '03:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.weeb.sh/images/SyONdUmwW.gif') 

    if now == '03:26':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')      
        
    if now == '03:27':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')     
        
    if now == '03:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 777')     
         
    if now == '03:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 777')   
        
    if now == '03:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 777') 
    
    if now == '03:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940>') 
        
    if now == '03:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.tenor.com/images/c5f2a0c3417e2ca71499650d107f538b/tenor.gif') 
    
    if now == '03:42':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940>')
        
    if now == '03:43':
        channel = client.get_channel(741553045481062461)
        await channel.send('🌊Wave&⛈RainやTipを受け取ったら、テキストかスタンプでお礼を伝えましょう！<:thank_you:741987635450609686> ')    
      
    if now == '03:44':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767323304067133/hty.png') 
          
    if now == '03:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('See you!またね👋')  

    if now == '03:46':
        channel = client.get_channel(739463355864973342)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747406475181293588/surfinggirl0009.gif')  

    if now == '03:47':
        channel = client.get_channel(741553045481062461)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747406475181293588/surfinggirl0009.gif') 

    if now == '03:48':
        channel = client.get_channel(739438637661421579)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747406475181293588/surfinggirl0009.gif')  
        
    if now == '03:50':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  

    if now == '03:51':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ') 
        
    if now == '03:53':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '03:54':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '03:54':
        channel = client.get_channel(731640211733479556)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')
        
    if now == '04:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '04:09':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
        
    if now == '04:15':
        channel = client.get_channel(739438637661421579)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ')  
        
    if now == '04:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.tenor.com/images/c5f2a0c3417e2ca71499650d107f538b/tenor.gif') 
        
    if now == '04:37':
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
        await channel.send('rsoak 777') 
        
    if now == '05:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 777') 
 
    if now == '05:32':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
          
    if now == '05:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475> ')

    if now == '05:49':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ') 

    if now == '05:56':
        channel = client.get_channel(739438637661421579)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ')  
  
    if now == '06:01':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 777') 
    
    if now == '06:02':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:otsukare:722438703410053160> <:otsukare:722438703410053160> <:otsukare:722438703410053160> ') 
        
    if now == '06:03':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77 ')
        
    if now == '06:04':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 777')
        
    if now == '06:05':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.tenor.com/images/c5f2a0c3417e2ca71499650d107f538b/tenor.gif') 
        
    if now == '06:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '06:09':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')
        
    if now == '06:20':
        channel = client.get_channel(769718766358757396)
        await channel.send('=soak 0.01')  
        
    if now == '06:30':
        channel = client.get_channel(769718766358757396)
        await channel.send('=soak 0.01')  
        
    if now == '06:40':
        channel = client.get_channel(739463355864973342)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747050967706501140/surfinggirl005.gif')  

    if now == '06:42':
        channel = client.get_channel(741553045481062461)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747050967706501140/surfinggirl005.gif') 

    if now == '06:44':
        channel = client.get_channel(739438637661421579)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747050967706501140/surfinggirl005.gif')  
        
    if now == '06:50':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  

    if now == '07:18':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Good morning 🌎everyone. Have a nice day today!')
        
    if now == '07:21':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '07:22':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '07:23':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')   
        
    if now == '07:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/698482526565564436/700566115897835571/jpyn-rain.gif') 
        
    if now == '07:23':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')   
        
    if now == '07:38':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '07:39':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock:732205759462375475> :guitar:') 
        
    if now == '07:40':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '07:41':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '07:45':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  

    if now == '07:49':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ') 

    if now == '07:56':
        channel = client.get_channel(739438637661421579)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ')  

    if now == '08:02':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')
        
    if now == '08:03':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 777') 
    
    if now == '08:04':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 777') 
        
    if now == '08:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '08:09':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
        
    if now == '08:40':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '09:21':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '09:22':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:') 
        
    if now == '09:23':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '09:24':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')   
        
    if now == '09:28':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '09:29':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock:732205759462375475> :guitar:') 
        
    if now == '09:30':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '09:31':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '09:42':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.tenor.com/images/c5f2a0c3417e2ca71499650d107f538b/tenor.gif') 
        
    if now == '09:46':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '09:57':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767349828714606/hg.png ') 
        
    if now == '09:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:gal_p:733138011109326940> Hello,how are you❓<:yeah1:721319707482914877>  ') 
        
    if now == '10:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '10:09':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')
        
    if now == '10:20':
        channel = client.get_channel(748426878527995915)
        await channel.send('<:rock01:748437813631909888> <:rock01:748437813631909888> <:rock01:748437813631909888>') 
        
    if now == '10:21':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '10:22':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:') 
        
    if now == '10:23':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 111.11 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '10:24':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')   
        
    if now == '10:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here <:gal_p:733138011109326940> I”ll ☔Rain a little... <:yeah1:721319707482914877> ') 
     
    if now == '10:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/701765831268368474/701767123252543498/iku.png') 
    
    if now == '10:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock01:748437813631909888> <:rock01:748437813631909888> <:rock01:748437813631909888>') 
        
    if now == '10:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock01:748437813631909888> <:rock01:748437813631909888> <:rock01:748437813631909888>')
     
    if now == '10:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 

    if now == '10:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 500') 

    if now == '10:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock01:748437813631909888> <:rock01:748437813631909888> <:rock01:748437813631909888>')
    
    if now == '10:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77.7')  

    if now == '10:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 222')
    
    if now == '10:36':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 222')  
      
    if now == '10:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('See you sometimes!') 
        
    if now == '10:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.tenor.com/images/c5f2a0c3417e2ca71499650d107f538b/tenor.gif') 
        
    if now == '10:39':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/698482526565564436/700566115897835571/jpyn-rain.gif') 

    if now == '10:40':
        channel = client.get_channel(739463355864973342)
        await channel.send('https://tenor.com/view/yes-oh-swell-ocean-waves-gif-13193756')  

    if now == '10:42':
        channel = client.get_channel(741553045481062461)
        await channel.send('https://tenor.com/view/yes-oh-swell-ocean-waves-gif-13193756') 

    if now == '10:44':
        channel = client.get_channel(739438637661421579)
        await channel.send('https://tenor.com/view/yes-oh-swell-ocean-waves-gif-13193756')  
        
    if now == '10:45':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '10:46':
        channel = client.get_channel(748426878527995915)
        await channel.send('<:rock01:748437813631909888> :guitar: <:rock01:748437813631909888> ') 
        
    if now == '10:47':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '10:48':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:') 
        
    if now == '10:49':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '10:50':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')    
        
    if now == '10:51':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:hello:741989920771538944> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ') 
        
    if now == '10:52':
        channel = client.get_channel(769718766358757396)
        await channel.send('=soak 0.01')  
        
    if now == '10:53':
        channel = client.get_channel(782529802061217792)
        await channel.send('=soak 0.01')  

    if now == '10:56':
        channel = client.get_channel(739438637661421579)
        await channel.send('<:hello:741989920771538944> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ')  
        
    if now == '11:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳')
        
    if now == '11:08':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')

    if now == '11:09':
        channel = client.get_channel(76971876635875739)
        await channel.send('$soak 0.001')
        
    if now == '11:33':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '11:36':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '11:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 111')
        
    if now == '11:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('...⚡...When you receive a Rain or Tip, thank you in text or stamp!') 
        
    if now == '11:39':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 222')
        
    if now == '11:40':
        channel = client.get_channel(739463355864973342)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747406475181293588/surfinggirl0009.gif')  

    if now == '11:41':
        channel = client.get_channel(741553045481062461)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747406475181293588/surfinggirl0009.gif') 

    if now == '11:42':
        channel = client.get_channel(739438637661421579)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747406475181293588/surfinggirl0009.gif')  
        
    if now == '11:47':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '11:49':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '11:50':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '11:55':
        channel = client.get_channel(741553045481062461)
        await channel.send('🌊Wave&⛈RainやTipを受け取ったら、テキストかスタンプでお礼を伝えましょう！<:thank_you:741987635450609686> ')  
        
    if now == '11:56':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '11:59':
        channel = client.get_channel(748426878527995915)
        await channel.send('@everyone  How is everyone? I,ll do a little rock and rain! :guitar: <:rock01:748437813631909888> ') 
        
    if now == '12:00':
        channel = client.get_channel(748426878527995915)
        await channel.send('<:rock01:748437813631909888> :guitar: <:rock01:748437813631909888> ') 
        
    if now == '12:01':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '12:02':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '12:03':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '12:04':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')   
    
    if now == '12:05':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone <:hello1:713004241131667528>') 
        
    if now == '12:05':
        channel = client.get_channel(731640211733479556)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
         
    if now == '12:06':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')
        
    if now == '12:07':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')
        
    if now == '12:08':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>') 
        
    if now == '12:09':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>') 
        
    if now == '12:10':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '12:15':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '12:29':
        channel = client.get_channel(739438637661421579)
        await channel.send('<:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846> <:xjp_coin:739314187532107846>') 
        
    if now == '12:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:mt:721596131980607498> <:rock:732205759462375475>') 
        
    if now == '12:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')

    if now == '12:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')

    if now == '12:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')

    if now == '12:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')

    if now == '12:36':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940>') 
    
        
    if now == '12:40':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  

    if now == '12:42':
        channel = client.get_channel(739463355864973342)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747414349315833866/surfinggirl0011.gif')  

    if now == '12:45':
        channel = client.get_channel(741553045481062461)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747414349315833866/surfinggirl0011.gif') 

    if now == '12:55':
        channel = client.get_channel(739438637661421579)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747414349315833866/surfinggirl0011.gif') 
        
    if now == '12:56':
        channel = client.get_channel(769718766358757396)
        await channel.send('=soak 0.01')  
        
    if now == '12:58':
        channel = client.get_channel(769718766358757396)
        await channel.send('=soak 0.01')  
        
    if now == '13:08':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')

    if now == '13:09':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
        
    if now == '13:10':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')

    if now == '13:11':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')
      
    if now == '13:14':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('⛈RainやTipを受け取ったら、テキストかスタンプでお礼を伝えましょう！🌟 ')   
        
    if now == '13:15':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '13:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.weeb.sh/images/SyONdUmwW.gif') 
        
    if now == '13:17':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')
        
    if now == '13:18':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 50')
        
    if now == '13:19':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')
        
    if now == '13:20':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')
        
    if now == '13:21':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940>') 
        
    if now == '13:22':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/698482526565564436/700566115897835571/jpyn-rain.gif') 
        
    if now == '13:40':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
    
    if now == '13:41':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here GoodNight！👋 ')       
        
    if now == '13:46':
        channel = client.get_channel(748426878527995915)
        await channel.send('@everyone  How is everyone? I,ll do a little rock and rain! :guitar: <:rock_blue01:748437456852090940> ') 
        
    if now == '13:48':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '13:49':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '13:50':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '13:51':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')   

    if now == '13:57':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940>') 
        
    if now == '13:40':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  

    if now == '13:49':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:deepsea:742015498241441932> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ') 
        
    if now == '13:40':
        channel = client.get_channel(741553045481062461)
        await channel.send('@everyone \n https://cdn.discordapp.com/attachments/741585316703633419/747675416034017370/blue_p.png \n https://cdn.discordapp.com/attachments/741585316703633419/747675416034017370/blue_p.png')  

    if now == '13:49':
        channel = client.get_channel(748426878527995915)
        await channel.send('@here  How is everyone? I,ll do a little rock and rain! :guitar: <:rock01:748437813631909888> ') 
          
    if now == '13:50':
        channel = client.get_channel(748426878527995915)
        await channel.send('<:rock01:748437813631909888> :guitar: <:rock01:748437813631909888> ') 
        
    if now == '13:51':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '13:52':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '13:53':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '13:54':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '13:55':
        channel = client.get_channel(702778037003092001)
        await channel.send('=soak 0.01')  
        
    if now == '13:57':
        channel = client.get_channel(758265143627874314)
        await channel.send('=soak 0.01')  
        
    if now == '14:05':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
    
    if now == '14:06':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw JPYN 111 30 EquallyDistributed') 
   
    if now == '14:07':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw BGPT 150 30 EquallyDistributed')      
        
    if now == '14:08':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw BEN 3 30 EquallyDistributed')   
    
    if now == '14:09':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:goodnight:742020034318303242> <:good_fr:742000494259470417>')     
        
    if now == '14:10':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:gn:699792795363311676> <:rock:732205759462375475>')  
   
    if now == '14:12':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')      
        
    if now == '14:13':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')  

    if now == '14:14':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77 ') 
   
    if now == '14:15':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')      
    
    if now == '14:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 100 ')
        
    if now == '14:17':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('See you! ') 
        
    if now == '14:18':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('When you receive a Rain or Tip, thank you in text or stamp!⭐ \n <:cong:719889728828342302> <:yeah1:721319707482914877> ') 
        
    if now == '14:28':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '14:29':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')
        
    if now == '14:30':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')

    if now == '14:31':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
        
    if now == '14:40':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  

    if now == '14:45':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>') 

    if now == '14:49':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:nicewave:741982210630090763> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ') 
        
    if now == '14:49':
        channel = client.get_channel(748426878527995915)
        await channel.send('@here  How is everyone? I,ll do a little rock and rain! :guitar: <:rock01:748437813631909888> ')       
        
    if now == '14:50':
        channel = client.get_channel(748426878527995915)
        await channel.send('<:rock01:748437813631909888> :guitar: <:rock01:748437813631909888>') 
        
    if now == '14:51':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '14:52':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '14:53':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '14:54':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '14:54':
        channel = client.get_channel(731640211733479556)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')
        
    if now == '14:56':
        channel = client.get_channel(739438637661421579)
        await channel.send('<:nicewave:741982210630090763> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ')  
        
    if now == '15:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:nerd_girl:733937654034595880> <:nerd_girl:733937654034595880> <:nerd_girl:733937654034595880> ') 
        
    if now == '15:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:yeah:741977175518871692> <:yeah:741977175518871692> <:yeah:741977175518871692>')
  
    if now == '15:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 55') 
        
    if now == '15:42':
        channel = client.get_channel(739463355864973342)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747404280847138837/surfinggirl0008.gif')  

    if now == '15:45':
        channel = client.get_channel(741553045481062461)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747404280847138837/surfinggirl0008.gif') 

    if now == '15:55':
        channel = client.get_channel(739438637661421579)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747404280847138837/surfinggirl0008.gif')  
        
    if now == '15:56':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  

    if now == '15:57':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 111') 

    if now == '15:58':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 

    if now == '15:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 111') 

    if now == '16:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940> <:rock_blue01:748437456852090940>')
        
    if now == '16:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '16:09':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
        
    if now == '16:30':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '16:31':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '16:32':
        channel = client.get_channel(731640211733479556)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')
                
    if now == '16:45':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '16:56':
        channel = client.get_channel(741553045481062461)
        await channel.send('🌊Wave&⛈RainやTipを受け取ったら、テキストかスタンプでお礼を伝えましょう！<:thank_you:741987635450609686>  ')    
   
    if now == '17:01':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')   
    
    if now == '17:02':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 
        
    if now == '17:08':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')

    if now == '17:09':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')
        
    if now == '17:40':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
      
    if now == '17:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:pos:727132210917933067> <:getoken:727508044619055174> <:BEAN:727155584377290853>')
        
    if now == '17:53':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '17:54':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '17:54':
        channel = client.get_channel(731640211733479556)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')
        
    if now == '18:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '18:09':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
        
    if now == '18:58':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 500') 
        
    if now == '18:59':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('https://cdn.discordapp.com/attachments/698482526565564436/700566115897835571/jpyn-rain.gif') 
        
    if now == '19:00':
        channel = client.get_channel(748426878527995915)
        await channel.send('@here  How is everyone? I,ll do a little rock and rain! :guitar: <:rock01:748437813631909888> ')  
        
    if now == '19:01':
        channel = client.get_channel(748426878527995915)
        await channel.send('<:rock01:748437813631909888> :guitar: <:rock01:748437813631909888> ') 
        
    if now == '19:03':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '19:04':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '19:06':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '19:07':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')   
        
    if now == '19:08':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '19:52':
        channel = client.get_channel(782529802061217792)
        await channel.send('=soak 0.01')  
        
    if now == '19:53':
        channel = client.get_channel(782529802061217792)
        await channel.send('=soak 0.01')  
        
    if now == '20:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '20:09':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')
        
    if now == '20:26':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '20:27':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '20:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('  🌈 <:tipcc1:721309274328006676>') 
        
    if now == '20:53':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '20:54':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '20:54':
        channel = client.get_channel(731640211733479556)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')
        
    if now == '21:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '21:09':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
           
    if now == '21:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:tipcc1:721309274328006676> <:tipcc1:721309274328006676> <:tipcc1:721309274328006676>')

    if now == '21:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')  
        
    if now == '21:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 50 ') 
        
    if now == '21:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')  
        
    if now == '21:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock01:748437813631909888> <:rock01:748437813631909888> <:rock01:748437813631909888>')
        
    if now == '21:39':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  
        
    if now == '21:40':
        channel = client.get_channel(748426878527995915)
        await channel.send('@here  How is everyone? I,ll do a little rock and rain! :guitar: <:rock01:748437813631909888> ')  
        
    if now == '21:41':
        channel = client.get_channel(748426878527995915)
        await channel.send('<:rock01:748437813631909888> <:rock01:748437813631909888> <:rock01:748437813631909888> ') 
        
    if now == '21:43':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '21:44':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock01:748437813631909888> :guitar:') 
        
    if now == '21:46':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '21:47':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')   
        
    if now == '22:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:gal_p:733138011109326940> Hello All⭐')
   
    if now == '22:01':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Dear japanese<:cafe:699769671234355230>Everyone🌟おはようございます!<:gm:699792760651120671>')
        
    if now == '22:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '22:09':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')

    if now == '23:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('When you receive a Rain or Tip, thank you in text or stamp!⭐')  
        
    if now == '23:08':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001')

    if now == '23:09':
        channel = client.get_channel(782529802061217792)
        await channel.send('$soak 0.001')
    
    if now == '23:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:gal_p:733138011109326940> Hello All⭐')

    if now == '23:40':
        channel = client.get_channel(739463355864973342)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747050967706501140/surfinggirl005.gif')  

    if now == '23:42':
        channel = client.get_channel(741553045481062461)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747050967706501140/surfinggirl005.gif') 

    if now == '23:44':
        channel = client.get_channel(739438637661421579)
        await channel.send('https://cdn.discordapp.com/attachments/741585316703633419/747050967706501140/surfinggirl005.gif')  
        
    if now == '23:46':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XJP 0.0001111 30 EquallyDistributed  <:xjp_coin:739313946045055117>')  

    if now == '23:49':
        channel = client.get_channel(741553045481062461)
        await channel.send('<:nicewave:741982210630090763> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ') 
        
    if now == '23:53':
        channel = client.get_channel(748426878527995915)
        await channel.send('rsoak 77.7 @🌊XJP-member   <:rock_blue01:748437456852090940> :guitar:')  
        
    if now == '23:54':
        channel = client.get_channel(748426878527995915)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif') 
        
    if now == '23:54':
        channel = client.get_channel(731640211733479556)
        await channel.send('https://media.discordapp.net/attachments/522647871451824158/713251725783597057/imageedit_2_5646955006.gif')
        
    if now == '23:56':
        channel = client.get_channel(739438637661421579)
        await channel.send('<:nicewave:741982210630090763> <:xjp_coin:739313946045055117> <:bluezone_xjp:743062029048217600> ')  
    
    if now == '23:57':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77') 
    
    if now == '23:58':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('rsoak 77')
        
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

    if message.content == "<:yubi_xjp:743064854260220003> <:nerd_girl_xjp:743064228105289779> <:yubi_xjp:743064854260220003>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:yubi_xjp:743064854260220003> <:maskedsxjp:743062104378048522> <:yubi2_xjp:744194861233864797>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:yeah:741977175518871692> <:yeah:741977175518871692> <:yeah:741977175518871692>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:yubi_xjp:743064854260220003> <:nerd_girl_xjp:743064228105289779> <:yubi_xjp:743064854260220003> <:yeah:741977175518871692>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:manythanks:741988787680313364> <:manythanks:741988787680313364> <:manythanks:741988787680313364>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:goodluck01:766855866447167510> <:nicewave:741982210630090763> <:goodluck01:766855866447167510>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:otsu_1:744125871236841502> <:otsu_1:744125871236841502> <:otsu_1:744125871236841502>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:otsu_1:744125871236841502> <:hello:741989920771538944> <:thank_you:741987635450609686>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:thank_you:741987635450609686> <:thank_you:741987635450609686> <:thank_you:741987635450609686>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:thank_you:741987635450609686> <:good_fr01:766856299031691295> <:thank_you:741987635450609686>")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "<:nicewave:741982210630090763> <:nicewave:741982210630090763> <:nicewave:741982210630090763>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:nicewave:741982210630090763> <:yeah:741977175518871692> <:nicewave:741982210630090763>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:bluezone_xjp:743062029048217600> <:bluezone_xjp:743062029048217600> <:bluezone_xjp:743062029048217600>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:deepsea:742015498241441932> <:exoticjapangogo:744381854911692971> <:deepsea:742015498241441932>")  # f文字列（フォーマット済み文字列リテラル）
        
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
        await message.channel.send(f"<:happy:723835203717562418> <:goodluck:724101036255608852> <:goodfriend:731381691192574022>")  # f文字列（フォーマット済み文字列リテラル）
        
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
  
    
    elif message.content == "r/d":
        # リアクションアイコンを付けたい
        q = await message.channel.send("$deposit ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "r/bal":
        # リアクションアイコンを付けたい
        q = await message.channel.send("$bal")
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

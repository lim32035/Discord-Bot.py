import discord
import asyncio
import openpyxl

client = discord.Client()

@client.event
async def on_ready():
    print(client. user. id)
    print("ready")
    game = discord.Game("단대소고 정보 제공")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("!2반 월요일 시간표"):
        embed = discord.Embed(title="```[2반 월요일 시간표]```", description="```fix\n1교시 영어\n2교시 통합과학\n3교시 수학\n4교시 국어\n5교시 창의적 체험활동\n6교시 창의적 체험활동\n```", color=0x09e343)
        embed.set_footer(text="개발자 임채민 (봇에 대한 모든 저작권은 개발자한테 있습니다. 함부로 유포시 저작권법에 의하여 처벌받을수 있다는것을 알아주시기 바랍니다)")
        await message.channel.send(embed=embed)
    
    if message.content.startswith("!2반 화요일 시간표"): 
        embed2 = discord.Embed(title="```[2반 화요일 시간표]```", description="```tex\n$ 1교시 통합사회\n$ 2교시 한국사\n$ 3교시 수학\n$ 4교시 영어\n$ 5교시 음악\n$ 6교시 컴퓨터 시스템 일반\n$ 7교시 컴퓨터 시스템 일반\n```", color=0x1500fc)
        embed2.set_footer(text="개발자 임채민 (봇에 대한 모든 저작권은 개발자한테 있습니다. 함부로 유포시 저작권법에 의하여 처벌받을수 있다는것을 알아주시기 바랍니다)")
        await message.channel.send(embed=embed2) 

    if message.content.startswith("!2반 수요일 시간표"):
        embed3 = discord.Embed(title="```[2반 수요일 시간표]```", description="```diff\n+ 1교시 한국사\n- 2교시 체육\n+ 3교시 통합사회\n- 4교시 프로그래밍\n+ 5교시 프로그래밍\n- 6교시 국어\n+ 7교시 통합과학\n```", color=0xf8fc00)
        embed3.set_footer(text="개발자 임채민 (봇에 대한 모든 저작권은 개발자한테 있습니다. 함부로 유포시 저작권법에 의하여 처벌받을수 있다는것을 알아주시기 바랍니다)")
        await message.channel.send(embed=embed3)

    if message.content.startswith("!2반 목요일 시간표"): 
        embed4 = discord.Embed(title="```[2반 목요일 시간표]```", description="```cs\n'1교시 음악'\n'2교시 통합사회'\n'3교시 국어'\n'4교시 한국사'\n'5교시 창의적 체험활동(문화)'\n'6교시 체육'\n'7교시 통합과학'```", color=0xf700e3)
        embed4.set_footer(text="개발자 임채민 (봇에 대한 모든 저작권은 개발자한테 있습니다. 함부로 유포시 저작권법에 의하여 처벌받을수 있다는것을 알아주시기 바랍니다)")
        await message.channel.send(embed=embed4)

    if message.content.startswith("!2반 금요일 시간표"): 
        embed5 = discord.Embed(title="```[2반 금요일 시간표]```", description="```cs\n# 1교시 수학\n# 2교시 프로그래밍\n# 3교시 프로그래밍\n# 4교시 창의적 체험활동(문화)\n# 5교시 컴퓨터 시스템 일반\n# 6교시 컴퓨터 시스템 일반\n# 7교시 영어```", color=0x00e2f7)
        embed5.set_footer(text="개발자 임채민 (봇에 대한 모든 저작권은 개발자한테 있습니다. 함부로 유포시 저작권법에 의하여 처벌받을수 있다는것을 알아주시기 바랍니다)")
        await message.channel.send(embed=embed5)

    if message.content.startswith("!DM"):
        author =  message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="최상단 제목")
        embed.add_field(name="제목", value=msg, inline=True)
        embed.set_footer(text=f"https://discord.gg/maFDJV")
        await author.send(embed=embed)

    if message.content.startswith("!사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic)) 

    if message.content.startswith("!채널 DM"):
        channel = message.content[7:25] 
        msg = message.content[26:]
        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title=msg, description="테스트")
        embed.set_footer(text=f"https://discord.gg/maFDJV")    
        await client.get_channel(int(channel)).send(embed=embed)

    if message.content.startswith("!MUTE"):
        author =  message.guild.get_member(int(message.content[6:24]))
        role = discord.utils.get(message.guild.roles, name="MUTE")  
        await author.add_roles(role)

    if message.content.startswith("!UNMUTE"):
        author =  message.guild.get_member(int(message.content[8:26]))
        role = discord.utils.get(message.guild.roles, name="MUTE")
        await author.remove_roles(role)
        message.guild.kick()

    if message.content.startswith('!BAN') :
        author = message.guild.get_member(int(message.content[5:23]))
        file = openpyxl.load_workbook('BAN.xlsx')
        sheet = file.active
        msg = message.content[24:]
        i = 1
        while True :
            if sheet["A" + str(i)].value == str(author) :
                sheet['B' + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("BAN.xlsx")
                if sheet["B" + str(i)].value == 2:
                    await message.guild.ban(author)
                    embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title=msg, description="```fix\n경고 2회누적으로 서버에서 추방되었습니다.```")
                    embed.set_footer(text=f"https://discord.gg/maFDJV")  
                    await message.channel.send(embed=embed)
                    sheet["B" + str(i)].value = msg
                else:
                    embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title=msg, description="```tex\n$ 경고를 1회 받았습니다```")
                    embed.set_footer(text=f"https://discord.gg/maFDJV")  
                    await message.channel.send(embed=embed)
                    sheet["c" + str(i)].value = msg
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author)
                sheet["B" + str(i)].value = 1
                sheet["c" + str(i)].value = msg
                file.save("BAN.xlsx")
                await message.channel.send(str(author) + "경고를 1회 받았습니다.")
                break
            i += 1

    if message.content.startswith(""):
        file = openpyxl.load_workbook("LEVEL.xlsx")
        sheet = file.active
        exp = [10, 50, 100, 200, 400]
        msg = message.content[:]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 5
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value - 1]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="레벨이 올랐습니다", description="현재 레벨 : " + str(sheet["C" + str(i)].value) + "\n경험치 : " + str(sheet["B" + str(i)].value))
                    embed.set_footer(text=f"https://discord.gg/maFDJV")  
                    await message.channel.send(embed=embed)
                file.save("LEVEL.xlsx")
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1 
                file.save("LEVEL.xlsx")
                break

            i += 1

    
        






client.run("NzIyODIwNzcyNTEwNTY0Mzg0.XuoqpA.L-DKK-pEMxmyANgQDovkXfSfzSg")





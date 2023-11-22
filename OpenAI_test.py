from openai import OpenAI
import telegram
import asyncio
import schedule
import time
import pytz
import datetime

client = OpenAI(
    api_key = "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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "소에 관한 농담 해줘"}
    ]
)

token = "6978046714:AAFXlCcOBrnc21sho1Od-UhBeY03yYrIJlg"
# Bot : sweetmango_bot
# token : 6978046714:AAFXlCcOBrnc21sho1Od-UhBeY03yYrIJl 
# chat_id : 6971784658
# channel : sw_2023_test02
bot = telegram.Bot(token = token)
public_chat_name = "@sw_2023_test02"

async def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    
    if now.hour >=23 or now.hour <=6:
        return
    
    id_channel = await bot.sendMessage(
        chat_id = public_chat_name,
        text = completion.choices[0].message.content)
    print(id_channel)

async def main():
    while True:
        await job()
        await asyncio.sleep(1800)

if __name__ == "__main__":
    asyncio.run(main())
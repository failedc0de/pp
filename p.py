import os, asyncio, time, sys, re
from pyrogram import *
from pyrogram.types import *

API_ID = 19685518
API_HASH = "33bf1d586e5fdfd9e66aaa52a576935a"

app = Client(name="bottri", 
             api_id=API_ID, 
             api_hash=API_HASH, 
             session_string="BQAhIHQAkGV2JjBY-jXSq0f7cWpkhiEPk4EqyHhvO7ik7WqSuhYjFwLyB8E0vX4gY3el6JISqC_ohLALMLGJR6ZyGhknAZ-GZTlMuAtctkAzWguvLntdqnXOIlIENIQl8_p-xUhjxJK69wCS5x2Va_EUC5nPm-V7VD4OJQUXN6tj0unq2Ko2YnED7iCw5N_BMUw5_fmhHcEL_B3LTT2Q1sx3yLlKPxonOZJbTwuQB4sNKVFQqGbymOIJBeOaXMtH0xNWffcf-gy27oz9XxxIMrYYLUeul5_oWuhlEbg0BSdBRhNazXgN3bskNTyP_CLZdc-oJ-j3Mn41Vzrbzjy0aDUKpb0ApgAAAAB1B3HOAA"
            )

counts = 200

async def main():
  try:
    await app.start()
    for _ in range(counts):
      await app.send_message(-1001566475525, "INDOBET GACOR💥💥GAS BARBAR LAGI🔥🔥")
      await asyncio.sleep(0.7)
  except Exception as e:
    await app.send_message(LOG, f"**ERROR:** `{str(e)}`")
    return
  
app.run(main())

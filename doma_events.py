# doma_events.py
import asyncio
import random
from telegram.ext import Application

# 💡 Fake domain list to simulate events
fake_domains = [
    "legend.ape", "matrix.core", "galaxy.vic", "meta.shib", "doma.zone",
    "nft.ape", "fast.core", "defi.vic", "pulse.shib", "block.zone"
]

# 💬 Simulate a random domain sale event
def generate_fake_event():
    domain = random.choice(fake_domains)
    price = round(random.uniform(3.0, 15.0), 2)
    link = f"https://start.doma.xyz/market/{domain}"

    return (
        f"🔥 *New Domain Sale!*\n"
        f"🌐 Domain: `{domain}`\n"
        f"💰 Price: *{price} USDC*\n"
        f"🔗 [View on Doma]({link})"
    )

# 🌀 Polling loop — runs every 30 seconds
async def watch_events(app: Application, chat_id: int):
    while True:
        event_message = generate_fake_event()
        await app.bot.send_message(chat_id=chat_id, text=event_message, parse_mode="Markdown")
        await asyncio.sleep(30)  # Wait 30 seconds

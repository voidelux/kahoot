import asyncio
from main.modules import (get_game_pin,
                         get_bot_count,
                         get_base_username,
                         banner,
                         clear)
from kahoot import KahootClient
from kahoot.packets.server.question_start import QuestionStartPacket
import aiohttp

clear()
banner()

def load_proxies():
    try:
        with open("main/src/proxy.txt", "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
        return proxies
    except FileNotFoundError:
        print("Proxy file not found at src/proxy.txt")
        return []

proxies = load_proxies()

async def question_start(packet: QuestionStartPacket):
    print(f"Question started: {packet}")

async def join_bot(pin, username, proxy_group):
    client = KahootClient()


    if proxies and proxy_group < len(proxies):
        proxy = proxies[proxy_group]
        proxy_url = f"http://{proxy}"

        print(f"🔁 Using proxy: {proxy} for group {proxy_group+1} (bots {proxy_group*10+1}-{(proxy_group+1)*10})")

        connector = aiohttp.TCPConnector(ssl=False)
        session = aiohttp.ClientSession(connector=connector)
        client.session = session
        client.session.proxy = proxy_url

    try:
        await client.join_game(game_pin=pin, username=username)
        print(f"✅ {username} connected")
    except Exception as e:
        print(f"❌ {username} failed: {str(e)}")
    finally:
        await asyncio.sleep(4)

async def main():
    pin = get_game_pin()
    bot_count = get_bot_count()
    base_name = get_base_username()

    print(f"\nStarting {bot_count} bots with names: {base_name}1-{base_name}{bot_count}")
    print(f"Available proxies: {len(proxies)}")


    groups = []
    for i in range(bot_count):
        group_num = i // 10
        username = f"{base_name}{i+1}"
        groups.append((username, group_num))


    if proxies:
        max_groups = len(proxies)
        groups = [(u, g) for u, g in groups if g < max_groups]
        if len(groups) < bot_count:
            print(f"⚠️ Not enough proxies for all bots. Only first {max_groups*10} bots will be started.")

    tasks = [join_bot(pin, username, group_num) for username, group_num in groups]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nScript stopped by user")

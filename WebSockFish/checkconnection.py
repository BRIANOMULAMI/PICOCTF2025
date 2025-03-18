import asyncio
import websockets

async def test_connection():
    uri = "ws://verbal-sleep.picoctf.net:51112/ws/"
    try:
        async with websockets.connect(uri) as ws:
            print("[+] Successfully connected")
    except Exception as e:
        print(f"[-] Connection error: {e}")

asyncio.run(test_connection())

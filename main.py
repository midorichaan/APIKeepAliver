import aiohttp
import asyncio

loop = asyncio.get_event_loop()

#async func
async def ping_server():
    async with aiohttp.ClientSession() as session:
        async with session.request("GET", "https://api.midorichan.cf/v1/") as request:
            try:
                data = await request.json()
            except:
                print("Data: " + str(await request.text()))
                print("Failed to pinging api.midorichan.cf")
            else:
                if data["code"] == 200:
                    print("Data: " + str(data))
                    print("successfully pingged api.midorichan.cf")
                else:
                    print("Data: " + str(data))
                    print("something went wrong. Status: " + str(data["code"]))

if __name__ == "__main__":
    print("Pinging...")
    loop.run_until_complete(ping_server())

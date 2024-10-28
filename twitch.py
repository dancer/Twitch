import asyncio
import aiohttp
import colorama
import json


async def check_username(username, session):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US',
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'Client-Session-Id': 'cab427f35656d6c4',
        'Client-Version': '121dfb28-b6c3-48e2-8a3b-588128a7fae5',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://www.twitch.tv/',
        'Referer': 'https://www.twitch.tv/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    data = '{"operationName":"UsernameValidator_User","variables":{"username":"'+username + \
        '"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}'
    async with session.post('https://gql.twitch.tv/gql', headers=headers, data=data) as response:
        result = await response.json()
        return result["data"]["isUsernameAvailable"], username


async def check_usernames_from_file():
    with open("words.txt", "r") as f:
        usernames = f.read().splitlines()

    async with aiohttp.ClientSession() as session:
        tasks = [check_username(username, session) for username in usernames]
        results = await asyncio.gather(*tasks)

        with open("available.txt", "w") as available_file, open("unavailable.txt", "w") as unavailable_file:
            for is_available, username in results:
                if is_available:
                    print(
                        f'[{colorama.Fore.CYAN}+{colorama.Fore.RESET}] Available: {colorama.Fore.CYAN}{username}{colorama.Fore.RESET}')
                    available_file.write(f"{username}\n")
                else:
                    print(
                        f'[{colorama.Fore.RED}-{colorama.Fore.RESET}] Unavailable: {colorama.Fore.RED}{username}{colorama.Fore.RESET}')
                    unavailable_file.write(f"{username}\n")

if __name__ == "__main__":
    asyncio.run(check_usernames_from_file())

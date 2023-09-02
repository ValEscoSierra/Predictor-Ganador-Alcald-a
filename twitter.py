import asyncio
from twscrape import API


async def main():
    api = API()
    await api.pool.add_account("@celsosamito02", "CesoSalvaje04", "celsosamito02@gmail.com", "celsosalvaje")

    q = "elon musk since:2023-01-01 until:2023-05-31"

    with open("resultados.txt", "w", encoding="utf-8") as file:
        async for tweet in api.search(q, limit=5000):
            line = f"{tweet.id}, {tweet.user.username}, {tweet.rawContent}\n"
            file.write(line)
            print(line)


if __name__ == "__main__":
    asyncio.run(main())

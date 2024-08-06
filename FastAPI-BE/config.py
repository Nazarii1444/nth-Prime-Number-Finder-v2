import os

from dotenv import load_dotenv

load_dotenv()

WORKER_SERVER_URL = os.getenv("WORKER_SERVER_URL")


if __name__ == '__main__':
    print(WORKER_SERVER_URL)


import os
import json
import base64

from typing import Dict, Union
from dotenv import load_dotenv

from .reporter import Reporter

if __name__ == "__main__":
    load_dotenv()
    username = os.getenv("MESSENGER_USERNAME")
    password = os.getenv("MESSENGER_PASSWORD")

    session = os.getenv("MESSENGER_SESSION")
    cookies: Dict = None
    if session:
        cookies = json.loads(base64.b64decode(session).decode("utf-8"))

    debug: Union[str, bool] = os.getenv("VERITASERUM_DEBUG")
    if debug:
        debug = debug.lower() in ("true", "yes", "1")

    reporter = Reporter(username, password, cookies=cookies, debug=debug)
    reporter.listen()

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from scannerbt import Scanner
import json, os.path, time, requests, sys, math, asyncio, datetime

with open("settings.json", encoding="utf-8") as f:
    setting = json.load(f)

CONF_FILE = "./address-id.json"
GAS_URL = setting["GAS_URL"]
PERIOD = setting["SCAN_PERIOD"]
METHOD = "POST"
HEADERS = {"Content-Type" : "application/json"}

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')

def update_config():
    global config
    with open(CONF_FILE, encoding="utf-8") as f:
        config = json.load(f)

def scan_post(config, scanner):
    scanner.scan()
    result = scanner.result
    registered_mac = [c["mac"] for c in config]
    detected_mac = list(result.keys())
    target_mac = list(set(registered_mac) & set(detected_mac))
    if len(target_mac)>0:
        target_json = { m: next(filter(lambda d: d.get("mac") == m, config))["id"]  for m in target_mac}
        now = datetime.datetime.now(JST)
        timestamp = now.strftime("%Y/%m/%d %H:%M:00")
        json_data = {"timestamp":timestamp, "data":target_json}
        response = requests.post(GAS_URL, json=json_data)
        response

class WatchHandler(PatternMatchingEventHandler):
    def __init__(self, patterns=[CONF_FILE]):
        super(WatchHandler, self).__init__(patterns=patterns)
        self.on_modified = update_config
        self.on_created = update_config


if os.path.exists(CONF_FILE):
    update_config()
else:
    print("コンフィグファイルが存在しません。空のファイルを新規作成します。")
    with open(CONF_FILE, 'w') as f:
            json.dump([], f, indent=2)
    
    update_config()

print(config)

async def main():
    scanner = Scanner(duration=4)

    event_handler = WatchHandler()
    observer = Observer() 
    observer.schedule(event_handler, "./", recursive=False)
    observer.start()

    i=0
    try:
        while True: 
            print(f"\r次のスキャンまで  {math.floor(i/60)}:{i%60:02}", end="")
            time.sleep(1)
            if(i==0):
                i=PERIOD
                loop = asyncio.get_event_loop()
                loop.run_in_executor(None, scan_post, config, scanner)

            i -= 1
    finally:
        observer.stop()
        observer.join()

asyncio.run(main())
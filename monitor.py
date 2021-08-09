import sys
import time
import logging
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent

savepath = "/home/jdavis/.wine/drive_c/users/jdavis/Local Settings/Application Data/paintdog/save/_playdata"

with open(savepath) as f:
    old = json.loads(f.readlines()[3])

class EventHandle(FileSystemEventHandler):
    def on_any_event(self,event):
        global old
        if not isinstance(event,FileModifiedEvent):
            return
        try:
            with open(savepath) as f:
                new = json.loads(f.readlines()[3])
            for k in new.keys():
                if k not in old:
                    logging.info(k)
            old = new
        except:
            pass

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = EventHandle()
    observer = Observer()
    observer.schedule(event_handler, savepath, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

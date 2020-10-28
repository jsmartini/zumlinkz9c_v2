from alive_progress import alive_bar
from time import sleep

with alive_bar(100, bar = "filling") as bar:
    for i in range(100):
        sleep(1)
        bar()
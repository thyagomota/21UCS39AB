import requests
import sys
import time
import threading

def run(url, seconds):
   while True:
        req = requests.get(url = url)
        time.sleep(seconds) 

if __name__ == "__main__":

    # command-line parameters validation 
    if len(sys.argv) != 4:
        print("Use: " + sys.argv[0] + " url total_threads seconds")
        sys.exit(1)
    url = sys.argv[1]
    total_threads = int(sys.argv[2])
    seconds = float(sys.argv[3])
    print(f"Running {total_threads} threads with {seconds}s pause between requests to {url}")

    # starting the threads
    threads = []
    for i in range(total_threads):
        thread = threading.Thread(target=run, args=(url,seconds))
        thread.start()
        threads.append(thread)

    # wait for all threads to stop
    for thread in threads:
        thread.join()

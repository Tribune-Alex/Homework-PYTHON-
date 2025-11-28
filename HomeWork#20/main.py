import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import socket

file_one = 'domains.csv'
file_two = 'result.csv'

def get_domain(self:str):
    url = f"https://{self.strip()}"
    start = time.time()
   

    try:
        
        response = requests.get(url, timeout=5)
        total_time = round(time.time() - start, 3)

       
        try:
            ip = socket.gethostbyname(self)
        except:
            ip = "N/A"

        return self, total_time, ip

    except Exception:
        
        return self, "N/A", "N/A"


def func():
    with open(file_one, 'r') as file:
        reader = csv.reader(file)
        domains = [row[1].strip() for row in reader if row]

    start_time = time.time()

    final = []

    with ThreadPoolExecutor(max_workers = 100) as executor:
        futures = {executor.submit(get_domain, domain): domain for domain in domains}

        for future in as_completed(futures):
            final.append(future.result())
            print(future.result())

    with open(file_two, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["domain", "response_time", "ip_address"])
        writer.writerows(final)

    total_time = time.time() - start_time
    print(f"Working time:  {total_time} seconds")


func()

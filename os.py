import os, threading, requests

print("PID of the script is ", os.getpid())

load1, load5, load15 = os.getloadavg()

print("This is the loadavg: ", load5)

cpu_count = os.cpu_count()

def comparing(cpu_count, loadavg):

	if ((cpu_count - loadavg < 1) == 1):
		exit() 
	else:
		print("the loadavg value isn't near (or close) to the cpu core count.")

comparing(cpu_count ,load5)

def check_urls(hostname):
	host = requests.get(hostname)
	if (host.status_code == 200):
		print(hostname +" is valid url.")
	else:
		print(hostname +" is invalid url.")

links_array = ["https://api.github.com", "http://bilgisayar.mu.edu.tr/",
"https://www.python.org/", "http://akrepnalan.com/ceng2034",
"https://github.com/caesarsalad/wow"]

count = 0

while(count < len(links_array)):
	
	thread1 = threading.Thread(target= check_urls, args=(links_array[count],))
	thread1.start()
	
	count = count + 1
	
thread1.join()
print("this script ends")
# ceng_2034_2020_midterm

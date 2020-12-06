
from engines import *

import random
 
query = input("Enter your query :\n")
A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )
 
Agent = A[random.randrange(len(A))]
 
headers = {'user-agent': Agent}
count = 0

#GOOGLE
result = google_search(query,headers)
while len(result) == 0 and count<2:
	count = count + 1
	google_search(query,headers)
for res in result:
	print(res)

#Reset variables
result = None
count = 0

#BING
result = bing_search(query,headers)
while len(result) == 0 and count<2:
	count = count + 1
	bing_search(query,headers)
for res in result:
	print(res)
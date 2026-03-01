import random,time, datetime , threading
start_time = time.time()
startDate = datetime.datetime(2003,1,1)
date_list = set()
global_matches = 0
sample_size = 100_000
for i in range(sample_size):
    date_list = set()  
    for i in range(24):
        random_day = startDate + datetime.timedelta(random.randint(0,364))
        date_list.add(random_day)
    if len(date_list)<24:
        global_matches+=1
percentage = global_matches/sample_size
print(f"{percentage:.10f}")
print("--- %s seconds ---" % (time.time() - start_time))
import time
import multiprocessing as mp


def read_info(name):
    all_data =[]
    with open(name,'r') as file:
        for line in file:
            all_data.append(line)
    return all_data

filenames = [f'file {number}.txt' for number in range(1,5)]

'''stime = time.time()
for filename in filenames:
    read_info(filename)
etime = time.time()
print(etime-stime)'''


if __name__ == '__main__':
    s1time = time.time()
    with mp.Pool(processes=4) as pool:
        data = pool.map(read_info,filenames)
    e1time = time.time()
    print(e1time-s1time)
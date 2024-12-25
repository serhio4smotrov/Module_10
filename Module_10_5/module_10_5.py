import time
import multiprocessing as mp


def read_info(name):
    all_data =[]
    with open(name,'r') as file:
        for line in file:
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]
    stime = time.time()
    '''for filename in filenames:
        read_info(filename)'''
    with mp.Pool(processes=4) as pool:
        data = pool.map(read_info,filenames)
    print(time.time() - stime)
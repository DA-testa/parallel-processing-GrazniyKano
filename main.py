# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    # write the function for simulating parallel tasks, 
    # create the output pairs
    jobs = [(data[i], i) for i in range(m)]
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    for job in jobs:
        time, thread = heapq.heappop(threads)
        output.append((thread, time))
        time += job[0]
        heapq.heappush(threads, (time, thread))     
    return output

def main():
    # create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n, m = map(int, input().split())\
    
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))

    # create the function
    result = parallel_processing(n,m,data)
    
    # print out the results, each pair in it's own line
    for r in result:
        print(r[0], r[1])

if __name__ == "__main__":
    main()

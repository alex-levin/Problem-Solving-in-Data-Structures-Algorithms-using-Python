import heapq

def kthLargestStream(k):
    hp = []
    size = 0
    while 1:
        data = input("Enter data: ") 
        if size < k - 1:
            hp.append(data)
        else:
            if size == k - 1:
                hp.append(data)
                heapq.heapify(hp)
            elif hp[0] < data :
                heapq.heappush(hp, data)
                heapq.heappop(hp)
            print hp
            print "Kth larges element is :: ", hp[0]
        size += 1

kthLargestStream(3)
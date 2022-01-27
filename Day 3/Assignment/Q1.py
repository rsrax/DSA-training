import heapq


def get_min_avg_waiting_time(customers):
    # get minimum waiting time for customers using SJF
    number_of_customers = len(customers)
    waiting_time = 0
    total_time = customers[0][0]
    waiting_customers = []
    customers.sort(reverse=True)
    while customers or waiting_customers:
        while customers and customers[-1][0] <= total_time:
            heapq.heappush(waiting_customers, customers.pop()[::-1])
        if waiting_customers:
            order = heapq.heappop(waiting_customers)
            total_time += order[0]
            waiting_time += total_time - order[1]
        else:
            total_time += 1

    return waiting_time//number_of_customers


# input logic
# number of customers
number_of_customers = int(input())
customers = []
for i in range(number_of_customers):
    # arrival time and service time
    arrival_time, service_time = map(int, input().split())
    customers.append([arrival_time, service_time])
print(get_min_avg_waiting_time(customers))

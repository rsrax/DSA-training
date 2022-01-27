def get_max(query_list):
    # get maximum element from a stack using dynamic programming
    stack = [[0]*2 for _ in range(len(query_list))]
    stack_top = -1
    max_vals = []
    for query in query_list:
        operation = query.split()
        if int(operation[0]) == 1:
            stack_top += 1
            stack[stack_top][0] = int(operation[1])
            if stack_top == 0:
                stack[stack_top][1] = stack[stack_top][0]
            else:
                # maximum element in the stack
                stack[stack_top][1] = max(
                    stack[stack_top][0], stack[stack_top-1][1])
        elif int(operation[0]) == 2:
            stack_top -= 1
        elif int(operation[0]) == 3:
            max_vals.append(stack[stack_top][1])
        else:
            print("Invalid operation")
    return max_vals


no_of_operations = int(input())
query_list = []
for i in range(no_of_operations):
    query_list.append(input())
for i in get_max(query_list):
    print(i)

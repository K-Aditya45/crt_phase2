def 
    for index in range(n-1,-1,-1):
        while len(stack)>0 and stack[0]<num[index]:
            stack.pop(0)
        if len(stack)>0:
            result[index]=stack[0]
        stack.insert(0,nums[index])
    return result
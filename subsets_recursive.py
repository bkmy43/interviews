def subsets(input):
    input_list=list(input)
    result_list = []

    if(len(input_list) == 1):
        result_list.append([])
        result_list.append(input_list)
    else:
        elem = input_list.pop(0)
        for subset in subsets(input_list):
            result_list.append(list(subset))
            subset.append(elem)
            result_list.append(list(subset))

    return result_list


test_list = [1,2,3,4]
result = subsets(test_list)
print('input=', test_list)
print('%s subsets found:' % len(result), result)

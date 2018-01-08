def OtherProducts(arr): 
    result = []
    for i in range(0, len(arr)):
        product = 1
        for j in range(0, len(arr)):
            if j == i:
                pass
            else:
                product *= arr[j]
        result.append(str(product))
    return "-".join(result)
    
# keep this function call here  
print OtherProducts(raw_input())
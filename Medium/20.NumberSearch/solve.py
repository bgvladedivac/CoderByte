def NumberSearch(string):
    summa = 0.0
    count = 0
    for ch in string:
        if ch.isdigit():
            summa += int(ch)
        elif ch.isalpha():
            count += 1
    return int(round(summa / count))
    
# keep this function call here  
print NumberSearch(raw_input())
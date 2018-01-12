def StringReduction(sen): 
    for i in range(0, len(sen)):
		sen = sen.replace('ab','c')
		sen = sen.replace('ba','c')
		sen = sen.replace('bc','a')
		sen = sen.replace('cb','a')
		sen = sen.replace('ac','b')
		sen = sen.replace('ca','b')		
    return len(sen)
    
# keep this function call here  
print StringReduction(raw_input())
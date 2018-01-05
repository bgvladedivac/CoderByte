def RunLength(string)
index = 0
result = []
while index <= string.length - 1
	 
	#puts index
	#index += 1
	# Kak moje da promenim i ?
	if string[index] == string[index+1]
		occurence = 1
#
	 	while string[index] == string[index+1] and index < string.length-1
	 		occurence += 1
 	 		index+=1
		end
	 	result <<  (occurence.to_s + string[index])
	 	index += 1
	else
		result << ( "1" + string[index])
		index += 1
	end 

#	end
 	 
	 
end

 result.join("")
end
   
# keep this function call here    
puts RunLength(STDIN.gets)
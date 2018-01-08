def PowersofTwo(num)

	power = 2
	check = 2 ** power 
	while num >= check
		if num == check
			return true
		else
			 
			check = 2 ** (power+=1)
		end
	end
	false
         
end
   
# keep this function call here    
puts PowersofTwo(STDIN.gets)
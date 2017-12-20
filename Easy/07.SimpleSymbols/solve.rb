def SimpleSymbols(str)
  # code goes here
  # 1. check if char is letter 
  # 2. compare
  (1..str.length-1).each do |i|
  	 
  	if str[i] =~ /[[:alpha:]]/
  		 if str[i-1] != '+' or str[i+1] != '+'
  		 	return "false"
  		 end
  	end
  end
     "true" 
         
end

# keep this function call here    
puts SimpleSymbols(STDIN.gets)  

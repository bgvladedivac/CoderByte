def SwapCase(input)

  # code goes here
 	result = []
	input.split("").each do |char|
		/[[:upper:]]/.match(char) ? result << char.downcase : result << char.upcase
	end
	result.join()
         
end
   
# keep this function call here    
puts SwapCase(STDIN.gets)
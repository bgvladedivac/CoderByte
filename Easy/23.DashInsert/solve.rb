def DashInsert(input)

  # code goes here
	tokens = []
	(0..input.length-2).each do |i|
		tokens << ( input[i].to_i % 2 != 0 && input[i+1].to_i % 2 != 0 ? input[i] + "-" : input[i])
	end
	tokens << input[input.length-1]
	tokens.join()
         
end
   
# keep this function call here    
puts DashInsert(STDIN.gets)
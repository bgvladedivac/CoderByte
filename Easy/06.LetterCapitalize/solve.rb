def LetterCapitalize(str)
    
  # code goes here
  	result = str.split().map { |word| word = word[0].upcase + word[1..word.length-1] }
	result.join(" ")
         
end
   
# keep this function call here    
puts LetterCapitalize(STDIN.gets)
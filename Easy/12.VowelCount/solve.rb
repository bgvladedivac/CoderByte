def VowelCount(str)
	vowels = ["a", "e", "o", "i", "u"]
	vowels.reduce(0) { |occurences, vowel| occurences += str.count(vowel) }
end
   
# keep this function call here    
puts VowelCount(STDIN.gets)  

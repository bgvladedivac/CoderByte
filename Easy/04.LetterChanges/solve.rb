def LetterChanges(str)
	# 1. Map each char to the result
	
	alphabet = ('a'..'z').to_a
	result = str.chars.map do |ch|
		if alphabet.include?(ch) and ch != 'z'
			next_letter = alphabet[alphabet.index(ch)+1]
			'aeiou'.include?(next_letter) ? next_letter.upcase : next_letter
		elsif ch == 'z'
			'a'
		else
			ch
		end
	end	
	result.join("")     
end
   
# keep this function call here    
puts LetterChanges(STDIN.gets)

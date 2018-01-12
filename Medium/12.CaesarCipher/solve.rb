class String
  def islower?
    return false if self.size > 1
    ('a'..'z').include? self
  end

  def isupper?
    return false if self.size > 1
    ('A'..'Z').include? self
  end
end

def CaesarCipher(str, num )
	alpha = ('a'..'z').to_a
	result = ""

	str.split("").each do |char|
		if char =~ /[[:alpha:]]/ and char.isupper?
		 	ind = (alpha.index(char.downcase) + num) % 26
		 	result += (alpha[ind].upcase)
		elsif char =~ /[[:alpha:]]/ and char.islower?
			ind = (alpha.index(char) + num) % 26
			result += (alpha[ind])
		else
			result += char
		end
	end
     result
end
   
# keep this function call here    
puts CaesarCipher(STDIN.gets)
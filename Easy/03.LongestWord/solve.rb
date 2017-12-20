def LongestWord(sen)

	# 1. extract all the words
	# 2. assume words[0] has the biggest length, try to find bigger.
	words = sen.split(/\W+/)
	longest = words[0]

	(1..words.length-1).each do |i|
		if words[i].length > longest.length
			longest = words[i]
		end	
	end

	longest
end

puts(LongestWord(STDIN.gets))
def FirstReverse(str)
	puts str.length
	l = str.length - 1
	result = ""

	(0..l).each do |i|
		result << str[l - i]
	end

	return result
end

puts FirstReverse(STDIN.gets)
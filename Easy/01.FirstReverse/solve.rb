def FirstReverse(str)
	l = str.length - 1
	result = ""

	(0..l).each do |i|
		result << str[l - i]
	end

	result
end

puts FirstReverse(STDIN.gets)
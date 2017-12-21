def ABCheck(str)
	(0..str.length-5).each do |i|
		return "true" if str[i] == 'a' and str[i+4] == 'b'
	end

	"false"
end
   
# keep this function call here    
puts ABCheck(STDIN.gets)  

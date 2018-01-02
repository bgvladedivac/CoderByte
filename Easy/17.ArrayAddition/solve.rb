def ArrayAdditionI(arr)

  # code goes here
  arr.sort!
  m = arr[arr.length-1]
  sub_array = arr[0, arr.length-1]
	
(2..sub_array.length).each do |i|
	combos =  sub_array.combination(i).to_a
	
	combos.each do |combo|
		return true if combo.reduce(0,:+) == m
	end
end
  false
end

# keep this function call here    
puts ArrayAdditionI(STDIN.gets)
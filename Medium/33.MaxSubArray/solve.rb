FIXNUM_MIN = -(2**(0.size * 8 -2))

def MaxSubarray(arr)
	best_sum = FIXNUM_MIN
	(0..arr.length-2).each do |i|
		current_sum = arr[i]
		(i+1..arr.length-1).each do |j|
			current_sum += arr[j]
			best_sum = current_sum if current_sum > best_sum
		end
	end
	best_sum
end
   
# keep this function call here    
puts MaxSubarray(STDIN.gets)
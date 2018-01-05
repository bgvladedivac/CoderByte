def PrimeTime(num)

  # code goes here
  (2..Math.sqrt(num)).none? {|f| num % f == 0}
         
end

def PrimeMover(num, start_primer = 2, result = [])
	if num == result.length
		return result[result.length-1]

	elsif PrimeTime(start_primer)
		tmp = start_primer
		PrimeMover(num, tmp += 1, result << start_primer)

	else
		PrimeMover(num, start_primer +=1, result)
	end
end
   
# keep this function call here    
puts PrimeMover(STDIN.gets)
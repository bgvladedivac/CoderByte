require "set"

def SecondGreatLow(arr)
	sortSet = SortedSet.new(arr).to_a

	if sortSet.length == 1
		return sortSet[0].to_s + " " + sortSet[0].to_s
	elsif sortSet.length == 2
		return sortSet[0].to_s + " " + sortSet[1].to_s
	elsif sortSet.length == 3
		return sortSet[1].to_s + " " + sortSet[1].to_s
	else
		return sortSet[1].to_s + " " + sortSet[sortSet.length-2].to_s
	end

end

   
# keep this function call here    
puts SecondGreatLow(STDIN.gets)
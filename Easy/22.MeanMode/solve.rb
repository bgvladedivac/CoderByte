require "set"

def getMode(arr)
	sortedSet = SortedSet.new(arr)
	mode = max_occurences = 0
	sortedSet.each do |n|
		if arr.count(n) > max_occurences
			max_occurences = arr.count(n)
			mode = n
		end
	end
	mode
end

def getMean(arr)
	arr.reduce(:+) / arr.length
end

def MeanMode(arr)
	  getMode(arr) == getMean(arr) ? 1:0 
end
         
# keep this function call here    
puts MeanMode(STDIN.gets)
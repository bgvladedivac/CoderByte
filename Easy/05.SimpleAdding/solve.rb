def SimpleAdding(num)
  # reduce it to the sum
  (1..num).to_a.reduce(:+)
end
   
# keep this function call here    
puts SimpleAdding(STDIN.gets)
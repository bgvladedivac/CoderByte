def NumberAddition(str)

  # code goes here
  str.split(/\D+/).map { |n| n = n.to_i }.sum
         
end
   
# keep this function call here    
puts NumberAddition(STDIN.gets)
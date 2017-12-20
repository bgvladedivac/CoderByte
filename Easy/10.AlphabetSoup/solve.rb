def AlphabetSoup(str)

  # code goes here
  str.chars.sort.join("")
         
end
   
# keep this function call here    
puts AlphabetSoup(STDIN.gets)  

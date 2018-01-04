def PrimeTime(num)

  # code goes here
  (2..Math.sqrt(num)).none? {|f| num % f == 0}
         
end
   
# keep this function call here    
puts PrimeTime(STDIN.gets)
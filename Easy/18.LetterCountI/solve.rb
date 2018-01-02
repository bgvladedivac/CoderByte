def LetterCountI(str)

  top, top_w = 0, ""
  arr = str.split(' ')
  
  arr.each do |word|
     word.chars do |c|
        x = word.count(c)
        top = x and top_w = word if x > top
     end
  end
  
  return top_w if top > 1
  -1       
end
   
# keep this function call here    
puts LetterCountI(STDIN.gets)
class StringUtility:

  def __init__(self, string):
    self.string = string
  
  def __str__(self):
    return self.string

  def vowels(self):
    vowels = "aeiouAEIOU"
    mystring = self.string
    num_vowels = 0
    for char in mystring:
      if char in vowels:
        num_vowels = num_vowels + 1 
    if num_vowels >= 5:
      total = "many"
    else:
      total = str(num_vowels)
    return total

  
      
        
      
      
    
      
      

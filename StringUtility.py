class StringUtility:

  def __init__(self, string):
    self.string = string
  
  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    mystring = self.string
    vowels = 'aeiouAEIOU'
    for alphabet in mystring:
      if alphabet in vowels:
        count = count + 1
    return count
    
      
      

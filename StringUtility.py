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

  def bothEnds(self):
    string = self.string
    count = 0
    for i in string:
      count = count + 1
    newstring = string[0:2] + string [count-2:count]
    if count <= 2: 
      finalstring = ""
    else:
      finalstring = newstring
    return finalstring

  def fixStart(self):
    string = self.string
    count = 0
    for i in string:
      count = count + 1
    star = string[0]
    rest = string[1:]
    rest = rest.replace(star,'*')
    if count <= 0: 
      finalstring = string
    else:
      finalstring = star+rest
    return finalstring
  
      
      
      
        
      
      
    
      
      

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

  '''takes a string and returns either the amount of vowels in the string or the word 'many' depending on the amount of vowels'''
  
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

  '''takes a string and returns a new string made of the first 2 and last 2 characters of the original string. Returns an empty string if the string is less than 2 characters in length'''

  def fixStart(self):
    string = self.string
    length = len(string)
    if length == 0:
      finalstring= string 
    else:
      star = string[0]
      rest = string[1:]
      rest = rest.replace(star,'*')
      finalstring = star+rest
    return finalstring

  '''takes a string and returns a string where all occurances of the first letter are changed to a *. returns the original string if the string is less than or equal to 1 character in length'''

  def asciiSum(self):
    string = self.string
    final_sum = sum(map(ord,string))
    return final_sum

  '''takes a string and returns the sum of the ascii values of all the characters in the string'''
      
  def cipher(self):
    string = self.string
    new_string = ''
    for i in string:
      if i.isalpha():
        if i.isupper():
          alphabet = (ord(i) - 65 + len(string)) % (26)
          alphabet += 65
        if i.islower():
          alphabet = (ord(i) - 97 + len(string)) % 26
          alphabet += 97
        letter = chr(alphabet)
      else:
        letter = i
      new_string += letter
    return new_string

  '''takes a string and returns a new string that has each character incremented by the length of the original string'''
        
      
      
      
      
        
      
      
    
      
      

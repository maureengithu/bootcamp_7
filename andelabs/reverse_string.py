def reverse_string(string):
  
  if string == '':
    return None
  
  reversed = string[::-1]
  
  if reversed == string:
    return True
    
  else:
    return reversed

print reverse_string("civic")
print reverse_string("civicert")
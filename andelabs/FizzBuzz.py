def fizz_buzz(x):
  
  if x % 15 == 0:
    
    return "FizzBuzz"
    
  elif x % 5 == 0:
    
    return "Buzz"
    
  elif x % 3 == 0:
    
    return "Fizz"
    
  else:
    
    return x

print fizz_buzz(45)
print fizz_buzz(37)
print fizz_buzz(18)
print fizz_buzz(50)
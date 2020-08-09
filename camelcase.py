def camel(s):
#define a function "camel" with argument "s"
  s = ''.join(e for e in s.replace(" "," ").title() if e.isalnum())
#isanull returns all the alphanumeric characters
#title sunction coverts the first char in each word to uppercase remaining to lowercase
#join() method joins all items into a sting with no space
  return s[0].lower() +s[1:]
#then return the first word of string in lowercase and rest of the string as defined above
print(camel(s = str(input())))

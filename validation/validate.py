import re
 
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
SpecialSym =['$', '@', '#', '%','!','^','*','&']
SpecialSym2=r"'~!@#$%^&*()_+=-`"
regex_username_combination = r"^[A-Za-z][A-Za-z0-9_]{7,29}$"
regex_username_lower = r"^[a-z][a-z0-9_]{7,29}$"
d = dict(); 
def password(s):
    val = True
    message = None
    if len(s) < 6:
        message = 'length should be at least 6'
        val = False
          
    if len(s) > 20:
        message = 'length should be not be greater than 20'
        val = False
          
    if not any(char.isdigit() for char in s):
        message = 'Password should have at least one numeral'
        val = False
          
    if not any(char.isupper() for char in s):
        message = 'Password should have at least one uppercase letter'
        val = False
          
    if not any(char.islower() for char in s):
        message ='Password should have at least one lowercase letter'
        val = False
    
    if not any(char in SpecialSym2 for char in s):
        print(f'Password should have at least one of the symbols {SpecialSym2}')
        val = False
    if val:
        message = 'Password Valid'
        
    d['status'] = val
    d['message'] = message    
    return d
def username(s):
    while True:
        regex = re.compile(regex_username_lower)
        if len(s) > 20:
            d['status'] = False
            d['message'] = 'length should be not be greater than 20'
        if regex.match(s):
            d['status'] = True
            d['message'] = "Username Valid "
            return d
        else:
            d['status'] = False
            d['message'] = "Oh no, that's not right. You need only start lowercase and number and only one _ or no. "
            return d

def email(s):
    if(re.fullmatch(regex, s)):
        d['status'] = True
        d['message'] ="Email Valid"
        return d
    else:
        d['status'] = False
        d['message'] = "Email Not Valid"
        return d
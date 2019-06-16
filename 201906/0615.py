import re
regex1 = re.compile(r'(bob|alice|carol)[^.]*(throws|eats|pets)[^.]*(apples|cats|baseballs)', re.I)
regex2 = regex1.search('boB THRoWs AppLeS')
print(regex2.group())
def strongPass(password) :
    if re.match(r'(/^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$/){8,}', password) :
        return True
    else :
        return False
password = raw_input('HEy kID WhaTs uR PareNTS CrEdIT cArD NUMbeR ')
print(strongPass(password))
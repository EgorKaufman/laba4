class Validator:
    def isEmail(self, email):
        if email.count('@') !=1:
            return False
        local_part, domain_part = email.split('@')
        if '.' not in domain_part:
            return False
        return True
    
    def isDomain(self, domain):
        if '.' not in domain:
            return False
        return True
    def isNumber(self, number):
        for char in number:
            if not('0' <= char <= '9'):
                return False
        return True
        
validator = Validator()

print(validator.isEmail("egordoynikov@gmail.com"))
print(validator.isEmail("egordoynikov@gmailcom"))
print(validator.isDomain("testsite.com"))
print(validator.isDomain("testsitecom"))
print(validator.isNumber("12345"))
print(validator.isNumber("12345a"))
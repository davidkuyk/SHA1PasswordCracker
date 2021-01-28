import hashlib

def crack_sha1_hash(hash, use_salts=False):
  topTenK = 'top-10000-passwords.txt'
  with open(topTenK, 'r') as reader:
    for line in enumerate(reader.readlines()):
      hashPass = hashlib.sha1(line[1].rstrip().encode('utf-8')).hexdigest()
      
      if use_salts == True:
        salts = 'known-salts.txt'
        with open(salts, 'r') as reader:
          for salt in enumerate(reader.readlines()):
            preSalt = hashlib.sha1((salt[1].rstrip() + line[1].rstrip()).encode('utf-8')).hexdigest()
            postSalt = hashlib.sha1((line[1].rstrip() + salt[1].rstrip()).encode('utf-8')).hexdigest()
            if preSalt == hash:
              return line[1].rstrip()
            elif postSalt == hash:
              return line[1].rstrip()
      
      if hashPass == hash:
        return line[1].rstrip()
    
    return "PASSWORD NOT IN DATABASE"
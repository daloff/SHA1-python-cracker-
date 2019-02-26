import hashlib
import argparse
from datetime import datetime

passwords = open("10-million-password-list-top-1000000.txt").read().splitlines()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-hash", help="hash value")
    parser.add_argument("-salt", help="salt value")
    parser.add_argument("-ghash", help="graduate student hash value")
    
    args = parser.parse_args()

    if args.hash is None and args.ghash is None:
        print parser.print_help()
        return

    print "Runninig password search. Please wait..."
    startTime = datetime.now()
    
    if args.ghash is not None:
        match, tries = findGradPassword(args.ghash)
    else:
        match, tries = findPassword(args.hash, args.salt)

    elapsedTime = datetime.now() - startTime
    print "-------------------------------------------------------"

    if match is None:
        print "Sorry, no match was found"
        print "Execution time: \t" + str(elapsedTime)
        print "Number of tries: \t" + str(tries)
    else:
        print "Password found: \t" + match
        print "Execution time: \t" + str(elapsedTime)
        print "Number of tries: \t" + str(tries)
    
def findPassword(passwordHash, saltHash):
    match = None
    triesTotal = 0
    
    if (saltHash is None):
        match, triesTotal = getHashMatch(passwordHash, None)
    else:
        saltMatch, saltTries = getHashMatch(saltHash, None)
        triesTotal += saltTries
        if (saltMatch is not None):
            print "Salt match found: " + saltMatch
            match, tries = getHashMatch(passwordHash, saltMatch)
            triesTotal += tries
    
    return match, triesTotal

def findGradPassword(passwordHash):
    match = None
    tries = 0
    for word1 in passwords:
        tries += 1
        for word2 in passwords:
            tries += 1
            password = word1 + " " + word2
            hashedPassword = hashlib.sha1(password).hexdigest()
            if passwordHash == hashedPassword:
                return password, tries
            
    return match, tries

def getHashMatch(hashValue, saltValue):
    match = None
    tries = 0

    for password in passwords:
        tries += 1
        if saltValue is not None:
            hashedPassword = hashlib.sha1(saltValue + password).hexdigest()
        else:
            hashedPassword = hashlib.sha1(password).hexdigest()
        
        if hashValue == hashedPassword:
            match = password
            break;

    return match, tries

if __name__ == '__main__':
    main()

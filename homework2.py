import hashlib
import argparse
from datetime import datetime

passwords = open("10-million-password-list-top-1000000.txt").read().splitlines()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-hash", help="hash value")
    parser.add_argument("-salt", help="salt value")
    
    args = parser.parse_args()

    if args.hash is None:
        print parser.print_help()
        return

    print "Runninig password search. Please wait..."
    startTime = datetime.now()
    
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

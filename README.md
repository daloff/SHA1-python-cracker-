# Daryna Aloff
# CSC 4980/6980 | Blockchain & Applications | Assignment 2
### Description
This program uses Python 2.7 and its standard libraries to break SHA1 hashes in a brute force manner

### Prerequisites
* If you don't have Python 2.7, please install it from [here](https://www.python.org/download/releases/2.7/)
    * To check if python is installed, run *"python --version"* from a terminal
* Make sure that the password file **"10-million-password-list-top-1000000.txt"** is in the same directory as homework2.py

### How to run this program
```sh
$ python homework2.py -hash <hash value> -salt <optional salt value>
```
# Solutions
| Problem | Time to Break    | # of Tries | Clear Text Password | Program arguments |
|---------|------------------|------------|---------------------|-------------------|
| a)      | 0:00:00.001000   | 16         | letmein             | python homework2.py -hash b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3|
| b)      | 0:00:01.413000   | 999,968    | vjhtrhsvdctcegth    | python homework2.py -hash 801cdea58224c921c21fd2b183ff28ffa910ce31|
| c)      | 0:00:00.822000   | 546,372    | harib               | python homework2.py -hash ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 -salt f0744d60dd500c92c0d37c16174cc58d3c4bdd8e|




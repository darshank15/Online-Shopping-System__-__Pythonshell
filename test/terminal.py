import os
import sys

curpath=os.getcwd()

def printallfile(files):
    for file in files:
        print file


def ls(tokens):
    #print "**********************  ls  ************************\n"
    argsize = len(tokens)
    if argsize == 1:
        files = os.listdir(curpath)
        printallfile(files)
    elif argsize == 2:
        if os.path.isdir(tokens[1]):
            files = os.listdir(tokens[1])
            printallfile(files)
        else:
            print("ls : given dir path does not exist")
    else:
        print("ls : Invalid number of Argument")
    #print "\n****************************************************"


def cd(tokens):
    #print "**********************  cd  ************************\n"
    global curpath
    argsize = len(tokens)
    if argsize != 2:
        print("cd : Invalid number of Argument")
    else:
        if not os.path.isdir(tokens[1]):
            print("cd : path does not exist")
        else:
            curpath = tokens[1]

    #print "\n****************************************************"


def pwd(tokens):
    #print "**********************  pwd  ************************\n"
    argsize = len(tokens)
    if argsize != 1:
        print("pwd : Invalid number of Argument")
    else:
        print curpath
    #print "\n*****************************************************"


def touch(tokens):
    #print "**********************  touch  ************************\n"
    argsize = len(tokens)
    if argsize != 2:
        print("touch : Invalid number of Argument")
    else:
        path = tokens[1]
        ind = path.rfind("/")
        # if only filename speficied
        if ind == -1:
            newpath = curpath + "/" + path
            open(newpath, 'w').close()
        # if path with filename specified
        else:
            extractpath = path[:ind]
            #print extractpath
            if os.path.isdir(extractpath):
                open(path, 'w').close()
            else:
                print("touch : path does not exist")

    #print "\n******************************************************"


def head(tokens):
    #print "**********************  head  ************************\n"
    argsize = len(tokens)
    if argsize != 2:
        print("head : Invalid number of Argument")
    else:
        path = tokens[1]
        ind = path.rfind("/")
        # if only filename speficied
        if ind == -1:
            newpath = curpath + "/" + path
        else:
            newpath = tokens[1]

        #print newpath
        if not os.path.isfile(newpath):
            print("File Does not exist")
        else:
            with open(newpath) as myfile:
                for x in xrange(10):
                    try:
                        sys.stdout.write(next(myfile)) 
                    except StopIteration:
                        break

    #print "\n******************************************************"

def tail(tokens):
    #print "**********************  tail  ************************\n"
    argsize = len(tokens)
    if argsize != 2:
        print("tail : Invalid number of Argument")
    else:
        path = tokens[1]
        ind = path.rfind("/")
        # if only filename speficied
        if ind == -1:
            newpath = curpath + "/" + path
        else:
            newpath = tokens[1]

        #print newpath
        if not os.path.isfile(newpath):
            print("File Does not exist")
        else:
            with open(newpath) as myfile:
                data = myfile.readlines()
            try:
                lastline = data[-1]
                tail = data[-10:]
                for it in tail :
                    sys.stdout.write(it)
            except :
                pass
            

    #print "\n******************************************************"


while 1:
    #print "takeinput called"
    unserinput = raw_input()
    tokens = unserinput.split()
    if len(tokens) == 0:
        print("Please enter something !!!")
        continue
    #print tokens
    cmd = tokens[0]
    #print cmd
    # which type of command
    if cmd == "ls":
        #print("ls command")
        ls(tokens)
    elif cmd == "cd":
        #print("cd command")
        cd(tokens)
    elif cmd == "pwd":
        #print("pwd command")
        pwd(tokens)
    elif cmd == "touch":
        #print("touch command")
        touch(tokens)
    elif cmd == "head":
        #print("head command")
        head(tokens)
    elif cmd == "tail":
        #print("tail command")
        tail(tokens)
    elif cmd == "exit":
        print("exit command")
        break
    else:
        print("give valid command")

# flag=0
    # str1=""
    # str2=""
    # for item in tokens[1:] :
    #     if item=="@":
    #         flag=1
    #         continue
    #     if flag==0 :
    #         str1 = str1 + item + " "
    #     else :
    #         str2= str2 + item + " "
    # if flag==0:
    #     print "Invalid formate for grep"
    # else :
    #     print str1
    #     print str2
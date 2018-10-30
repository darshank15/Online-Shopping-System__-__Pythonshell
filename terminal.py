import os
import sys

def prRed(skk): sys.stdout.write("\033[91m{}\033[00m" .format(skk))

def printallfile(files):
    for file in files:
        if file[0] != '.' :
            print file

def printall(items):
    for item in items:
        print item,

def ls(tokens):
    #print "**********************  ls  ************************\n"
    argsize = len(tokens)
    if argsize == 1:
        currentpath = os.getcwd()
        if os.access(currentpath, os.R_OK):
            files = os.listdir(currentpath)
            printallfile(files)
        else:
            print("ls : Direcotry doesn't have read permission")
    elif argsize == 2:
        currentpath = tokens[1]
        if os.path.isdir(currentpath):
            if os.access(currentpath, os.R_OK):
                files = os.listdir(currentpath)
                printallfile(files)
            else:
                print("ls : Direcotry doesn't have read permission")
        else:
            print("ls : given dir path does not exist")

    else:
        print("ls : Invalid number of Argument")
    #print "\n****************************************************"


def cd(tokens):
    #print "**********************  cd  ************************\n"
    argsize = len(tokens)
    if argsize != 2:
        print("cd : Invalid number of Argument")
    else:
        if not os.path.isdir(tokens[1]):
            print("cd : path does not exist")
        else:
            currentpath = tokens[1]
            if os.access(currentpath, os.X_OK):
                os.chdir(currentpath)
            else:
                print("cd : Direcotry doesn't have execute permission")

    #print "\n****************************************************"


def pwd(tokens):
    #print "**********************  pwd  ************************\n"
    argsize = len(tokens)
    if argsize != 1:
        print("pwd : Invalid number of Argument")
    else:
        print os.getcwd()
    #print "\n*****************************************************"


def touch(tokens):
    #print "**********************  touch  ************************\n"
    argsize = len(tokens)
    if argsize < 2:
        print("touch : Invalid number of Argument")
    else:
        for item in tokens[1:]:
            path = item
            ind = path.rfind("/")
            # if only filename speficied
            if ind == -1:
                if os.access(os.getcwd(), os.W_OK):
                    newpath = os.getcwd() + "/" + path
                    open(newpath, 'a').close()
                    os.utime(newpath, None)
                else:
                    print("touch : Direcotry doesn't have Write permission")
            # if path with filename specified
            else:
                extractpath = path[:ind]
                #print extractpath
                if os.path.isdir(extractpath):
                    if os.access(extractpath, os.W_OK):
                        open(path, 'a').close()
                        os.utime(path, None)
                    else:
                        print("touch : Direcotry doesn't have Write permission")
                else:
                    print("touch : path does not exist")

    #print "\n******************************************************"


def head(tokens):
    #print "**********************  head  ************************\n"
    argsize = len(tokens)
    if argsize < 2:
        print("head : Invalid number of Argument")
    else:
        for item in tokens[1:]:
            newpath = item
            print "===>"+newpath+"<==="
            if not os.path.isfile(newpath):
                print("head : File Does not exist")
            else:
                if os.access(newpath, os.R_OK):
                    with open(newpath) as myfile:
                        for x in xrange(10):
                            try:
                                sys.stdout.write(next(myfile))
                            except StopIteration:
                                break
                else:
                    print("head : file doesn't have Read permission")

    #print "\n******************************************************"


def tail(tokens):
    #print "**********************  tail  ************************\n"
    argsize = len(tokens)
    if argsize < 2:
        print("tail : Invalid number of Argument")
    else:
        for item in tokens[1:]:

            newpath = item
            print "===>"+newpath+"<==="
            if not os.path.isfile(newpath):
                print("tail : File Does not exist")
            else:
                if os.access(newpath, os.R_OK):
                    with open(newpath) as myfile:
                        data = myfile.readlines()
                    try:
                        lastline = data[-1]
                        tail = data[-10:]
                        for it in tail:
                            sys.stdout.write(it)
                    except:
                        pass
                else:
                    print("tail : file doesn't have Read permission")

    #print "\n******************************************************"

def diff(tokens) :
    argsize = len(tokens)
    if argsize != 3:
        print("diff : Invalid number of Argument")
    else :
        file1=tokens[1]
        file2=tokens[2]
        if os.path.isfile(file1) and os.path.isfile(file2) :
            if os.access(file1, os.R_OK) and  os.access(file2, os.R_OK) :
                with open(file1,'r') as myfile1:
                    list1 = myfile1.readlines()
                with open(file2,'r') as myfile2:
                    list2 = myfile2.readlines()

                print "===>first file diff<==="
                for itm in list1 :
                    if not itm in list2:
                        print itm,
                print "===>second file diff<==="
                for itm in list2:
                    if not itm in list1 :
                        print itm,
                
            else :
                print "one of file doesn't have read permission"
        else :
            print "one of the two file does not exist"

def tr(tokens):
    argsize = len(tokens)
    if argsize != 3:
        print("tr : Invalid number of Argument")
    else:
        while 1 :
            trinput=raw_input("\n")
            if trinput=="@" :
                break
            else :
                mydict = {}
                input1=tokens[1]
                input2=tokens[2]
                len1=len(input1)
                len2=len(input2)
                for i in xrange(len1):
                    if i>=len2 :
                        mydict[input1[i]]=input2[len2-1] 
                    else :
                        mydict[input1[i]]=input2[i]

                for inp in trinput :
                    if inp in mydict :
                        sys.stdout.write(mydict[inp])
                    else :
                        sys.stdout.write(inp)

#grep syntax grep "pat" <<< "stringtobematch"
def grep(inputstr):

    try:
        tokens = unserinput.split("<<<")
        str1=tokens[0].strip()
        str2=tokens[1].strip()

        firpart = str1.split('"')
        secondpart = str2.split('"')

        pat = firpart[1]
        strsearch= secondpart[1]
        #print pat
        #print strsearch
    except:
        print "Invalid syntax for grep command"
        return
    
    offset=0
    patlen=len(pat)
    foundind=strsearch.find(pat,offset)
    offset=foundind
    if foundind == -1 :
        return
    sys.stdout.write(strsearch[0:0+foundind])
    while foundind != -1:
        sub = strsearch[foundind:foundind+patlen]
        prRed(sub)
        foundind = strsearch.find(pat,offset+patlen)
        if foundind==-1:
            sys.stdout.write(strsearch[offset+patlen:])
        else:
            sys.stdout.write(strsearch[offset+patlen:foundind])

        offset=foundind

def sed(inputstr):
    
    try:
        tokens = unserinput.split("<<<")
        str1=tokens[0].strip()
        str2=tokens[1].strip()

        firpart = str1.split('"')
        secondpart = str2.split('"')

        pat1 = firpart[1]
        pat2 = firpart[3]
        strsearch= secondpart[1]

    except:
        print "Invalid syntax for sed command"
        return

    liststr=strsearch.split(pat1)
    finalans = pat2.join(liststr)
    print finalans


while 1:
    #print "takeinput called"
    unserinput = raw_input("\n")
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
    elif cmd == "diff":
        #print("diff command")
        diff(tokens)
    elif cmd == "tr":
        #print("tr command")
        tr(tokens)
    elif cmd == "grep":
        #print("grep command")
        grep(unserinput)
    elif cmd == "sed":
        #print("sed command")
        sed(unserinput)
    elif cmd == "exit":
        #print("exit command")
        break
    else:
        print("invalid command")

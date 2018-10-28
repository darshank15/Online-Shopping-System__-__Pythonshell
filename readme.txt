as you enter into program you can start typing different command

1.ls

    Ex : ls      ---> printting ls for current dir
    Ex : ls path ---> printting ls for given path

2.cd

    Ex: cd path  ---> change the current working dir to given path

3.pwd

    Ex: pwd ---> print current working directory

4.touch 
    
    Ex: touch filename.ext        ---> create new file in pwd with given filename
        touch path/filename.ext   ---> create new file in given path
        touch arg1 agr2 agr3 ...  ---> creating multiple newfile 
    
5.grep

    Ex: grep "pattern" <<< "stringtobematch"

6.sed

    Ex: sed "pat1"/"pat2" <<< "stringtobereplace"

7.head

    Ex: head filename.ext    ---> print first 10 line of the file if exist
        head arg1,arg2,...   ---> print first 10 line of each file specified as arg

8.tail

    Ex: tail filename.ext    ---> print last 10 line of the file if exist
        tail arg1,arg2,...   ---> print last 10 line of each of the file specified as arg

9.tr
    
    Ex: 1.1 tr set1 set2          ---> map character of set1 with set2
        1.2 "enter user string"   ---> find and replace set1 to set2 in userstring
        1.3 "@"                   ---> to quit from tr mode

10.diff
    
    Ex: diff file1 file2   ---> show difference between file1 and file2

11.exit

    Ex: exit    ---> to exist from terminal command mode

# bash csript
## #!/bin/bash
here #! is called shebang charecter.
## echo "hello"
echo command is used to print hello
## # is used for comments
# variables
## name=5 & echo $name
Use = oprator to make a variable and then use $name to access the variable. it will print 5
# command line arguments
## $0,$1,...
$0 is used for script name. $1 will be the first argument $2 will be second and so on to $9. If you are using $1 or other then it must be passed from cmd.

# System variables
## $?
It is used for exit code of last command
## #USER
it will give user name
## #HOSTNAME
it will give hostname
## $RANDOM
it will give a random number

# quotes sinle(') and double(")
single quotes removes spacial meaning available in it. In double quotes use backword slash \ for ignoring spacial meaning.
# command substitution
## 'comand' or $(command)
use back tics ` to store the output of a cammand into a variable.

# exporting bariable
## export name
this command is used to export variable name from parent shell to child shell.
## .bashrc or .profile
This file is available for every user . If you add the varible in this file then it will be available for that particuler user. because when a user logged in .bashrc file runs automaticaly.
## /ect/profile
If you are exporting a variable in this file then it will be available for all the user.
# user input
## read  -p/-sp name
This will wait for user to enter the input. p is used for prompt and -sp is used for suppress prompt input.

# decision making
    if [ $num -gt 10 ]
    then 
        echo "greater"
    elif [$num eq 50]
    then
        echo "fifty
    else
        echo "lesser"
    fi




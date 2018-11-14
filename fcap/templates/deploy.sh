#!/bin/sh

host="root@xxx.xxx.xxx.xxx"
git st
read -p "Do you push current code? [y/n] " flag
if [ $flag = "y" ]
then
    read -p "Please input commit message." message
    if [ $message ]
    then 
        git add .
        git cm $message
        # git push origin master
        # ssh $host < remote.sh
    else
        echo "Don't input commit message."
    fi
else
    echo "Cancel push code."
fi

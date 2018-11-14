#!/bin/sh
host="root@xxx.xxx.xxx.xxx"
git status
read -p "[INFO] 是否提交当前代码? [y/n] " flag
if [ $flag = "y" ]
then
    read -p "[INFO] 请输入提交信息: " message
    if [ $message ]
    then 
        git add .
        git commit -m $message
        # git push origin master
        # ssh $host < remote.sh
    else
        echo "[ERROR] 没有输入提交信息"
    fi
else
    echo "[INFO] 取消提交当前代码."
fi

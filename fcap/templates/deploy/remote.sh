#!/bin/sh
pro_dir="/root/xxx"
app="xxx"
echo "[Info] 开始获取最新代码..."
echo "[Info] cd " $pro_dir
cd $pro_dir
git status
git checkout -- manage.py
git pull
cp manage.py.old manage.py
echo "[Info] 获取代码成功"
pm2 restart $app
echo "[Info] 重启服务"

#!/bin/bash
echo "kill the main.py"
c=$(ps aux |grep "[m]ain.py" |awk '{print $2}'|wc -l)
if [ $c = 0 ];then
        echo "no running"
else
        ps aux |grep "[m]ain.py" |awk '{print $2}' |xargs kill -9
fi
ps aux |grep "python"
#!/bin/sh

NAME=$1
echo $NAME
ID=`ps -axu caiyiming |grep Snipaste|grep -v grep|awk '{print $2}'`
echo $ID
echo "---------------"
for id in $ID
do
kill -9 $id
echo "killed $id"
open /Applications/Snipaste.app
done
echo "---------------"

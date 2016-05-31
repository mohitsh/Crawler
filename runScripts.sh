#!/bin/bash
#INPUT='TickerNSE.csv'
#cat $INPUT | sed "1 d" > noheader.csv
#OLDIFS=$IFS
#ext=".py"
#init="./"
#IFS=,
#while read Ticker url
#do
#	#echo "$init$Ticker$ext"
#	nohup $init$Ticker$ext
#done < 'noheader.csv'
#IFS=$OLDIFS
./df1.py &
./df2.py &
./df3.py &
./df4.py &
./df5.py &
./df6.py &
./df7.py &
./df8.py &
./df9.py &
wait
echo "all done! live your life peacefully."

#!/bin/bash
sw=$1
id=$2
case $sw in
	      bonus)cat employee.csv  | awk -F, '{print $1,$3,"will get $"$5*5/100 " bonus"}' | grep $id | cut -c 7-
          ;;
        city)cat employee.csv | grep $id| cut -d, -f 3,4 | awk -F, '{print "Customer Name:",$1,"\n""Mobile No:",$2}'
          ;;
        *) echo "command not found"
          ;;
esac
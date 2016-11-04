#!/usr/bin/env bash

fun () {
	case ":/sbin:/usr/local/bin:abc" in
		*:$1:*)
			echo aaaaaaa
			;;
		*)
			if [ "$2" = "after" ] ; then
				ABC=$ABC:$1
			else
				ABC=$1:$ABC
			fi
	esac	
}

ABC=/sbin:/usr/local/bin
fun /sbin
echo $ABC 
fun /usr/sbin after
echo $ABC



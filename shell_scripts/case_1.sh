#!/usr/bin/env bash

fun () {
	case ":${ABC}:" in
		*:$1:*)
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



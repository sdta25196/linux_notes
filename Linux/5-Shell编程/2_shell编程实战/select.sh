#! /bin/bash

echo "what is your favorite OS?"

select var in "Linux" "Windows" "OSX" "FreeBSD" "Other"; do
    case $var in 
        Linux)
            break
            ;;
        Windows)
            break
            ;;
        OSX)
            break
            ;;
        FreeBSD)
            break
            ;;
        Other)
            break
            ;;
        *)
            ;;
    esac
done

echo "Your selected OS is $var."

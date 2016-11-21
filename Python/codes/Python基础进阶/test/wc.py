#!/usr/bin/env python

def wordCount( s ):
    chars = len(s)
    lines = s.count('\n')
    words = len( s.split() )

    print chars, lines, words	
    print __name__

if __name__ == '__main__':
    fd = open('/etc/passwd').read()
    wordCount( fd )

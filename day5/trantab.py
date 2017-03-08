from string import maketrans



a="aeiou"

b="12345"

trantab=maketrans(a,b)
str= "i love red colour apple "


print str.translate(trantab)

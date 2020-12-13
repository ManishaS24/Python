#formatter = "%r %r %r %s"
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

#output:- if we comment out line 2 and remove comment from line 1
#1 2 3 4
#'one' 'two' 'three' four
#True False False True
#'%r %r %r %s' '%r %r %r %s' '%r %r %r %s' %r %r %r %s
#'I had this thing.' 'That you could type up right.' "But it didn't sing." So I said goodnight. -->> ["But it didn't sing." - it's within "", because didn't has ' in it]

#output:- if we comment out line 1 and remove comment from line 2
#1 2 3 4
#'one' 'two' 'three' four
#True False False True
#'%r %r %r %s' '%r %r %r %s' '%r %r %r %s' '%r %r %r %r'
#'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight'. -->> strings are displayed in '' because %r displays raw data of the variable

#%r --> for debugging purpose & %s --> for displaying data to the user

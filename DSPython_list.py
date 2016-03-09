#LIST MANIPULATION IN PYTHON

def match_ends(words):
    i=0
    for x in words:
        if len(x)>=2 and x[0]==x[-1]:
            i+=1
        else:
            i=0
    return i

chaine=["alicia","danna","emile","aaa"]
match_ends(chaine)

def front_x(words):
  xliste=[]
  liste=[]
  for x in words:
    if x[0]=="x":
      xliste.append(x)
    else:
      liste.append(x)

  return sorted(xliste) + sorted(liste)

chaine=["alicia","vero","danna","xavier","emile"]
print (front_x(chaine))

def last(t):
    return t[-1]
def sort_last(tuples):
    return sorted(tuples,key=last)

chaine=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
sort_last(chaine)

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
   
def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

main()

def remove_adjacent(nums):
    list=[]
    var=None
    for n in nums:
        if n!=var:
            list.append(n)
            var=n
    return list

nums=[1,2,2,3]
remove_adjacent(nums)

def linear_merge(list1, list2):
    list = []
    for i in list1:
        list.append(i)
    for j in list2:
        list.append(j)
    list.sort()
    return list

list1=['aa', 'xx', 'zz']
list2=['bb', 'cc']
linear_merge(list1, list2)

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
    
def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])
        
main()
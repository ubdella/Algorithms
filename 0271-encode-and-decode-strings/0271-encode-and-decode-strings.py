
"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    # write your code here
    res = ''
    for string in strs:
        res = res + str(len(string))+ '!' + string
    return res
"""
@param: str: A string
@return: decodes a single string to a list of strings
"""
def decode(str):
    # write your code here
    res = []
    i=0
    j=0
    while i<len(str):
        lenstr = ''
        j = i
        while str[j]!='!':
            lenstr+=str[j]
            j+=1
        strlen = int(lenstr)
        res.append(str[j+1:j+strlen + 1])
        i = j + strlen + 1

    return res

inputed = ['animal', 'retard!', 'monke', 'eat']
coded = encode(inputed)
print(coded)
decoded = decode(coded)
print(decoded)
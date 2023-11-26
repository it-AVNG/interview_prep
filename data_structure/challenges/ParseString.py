
def matchingStrings(strings, queries):
    return [strings.count(e) for e in queries]


strings = ['aba','baba','aba','xzxb']
queries = ['aba','xzxb','ab']

matchingStrings(strings,queries)



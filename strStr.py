class Sol:
    def strStr(self,haystack,needle):
        if needle not in haystack:
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if(haystack[i:i+len(needle)]==needle):
                return i
if __name__ == '__main__':
    haystack ='Hello'
    needle='ll'
    p1=Sol()
    print(p1.strStr(haystack,needle))

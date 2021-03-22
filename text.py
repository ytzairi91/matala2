
handle= open("C:\\Users\\ytzai\\Desktop\\matala2\\text.txt")
inp= handle.read()

def revword(word:str) -> str:
    i=len(word)-1
    newWord=''
    while(i>-1):
        newWord=newWord +word[i]
        i=i-1
    return newWord


def countword() -> int:
    b=0
    word=''
    count=0
    aWord=''
    while(inp[b]!=" "):
        word=word+inp[b]
        b=b+1
    for a in inp[b:]: 
        if(inp[b] != ' '):
            aWord=aWord + inp[b].lower()
            b=b+1
        elif(revword(aWord) == word ):
            count= count+1
            b=b+1
            aWord=''
        else:
            b=b+1
            aWord=''
            
    return count


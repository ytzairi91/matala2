

def revword(word:str) -> str:
    i=len(word)-1
    newWord=''
    while(i>-1):
        newWord=newWord +word[i]
        i=i-1
    return newWord


def countword() -> int:
    
    handle= open("C:\\Users\\ytzai\\Desktop\\matala2\\text.txt")
    inp= handle.read()
    b=0
    word=''
    count=1
    aWord=''
    while(inp[b]!=" "  and inp[b]!="\n"):
        word=word+inp[b]
        b=b+1
    for a in inp[b:]: 
        if(inp[b] != " " and inp[b]!= "\n"):
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


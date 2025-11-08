#cut -d'/' -f1 sound.txt > sound2.txt:: 뒤 개행문자부터 삭제한것
def is_hangeul(ch):
    return ord('가')<=ord(ch)<=ord( '힣')
outfp=open("/Users/kim-eunseo/Desktop/Digital/hw2/code3.txt","wt")     
with open("/Users/kim-eunseo/Desktop/Digital/hw2/code2.txt") as fp:
    for line in fp:
        print(chr(int(line,base=16)),file=outfp)
        
outfp.close()
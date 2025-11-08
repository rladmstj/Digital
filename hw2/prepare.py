#cut -d'/' -f1 sound.txt > sound2.txt:: 뒤 개행문자부터 삭제한것
def is_hangeul(ch):
    return ord('가')<=ord(ch)<=ord( '힣')
outfp=open("/Users/kim-eunseo/Desktop/Digital/hw2/sound4.txt","wt")     
with open("/Users/kim-eunseo/Desktop/Digital/hw2/sound3.txt") as fp:
    for line in fp:
        for ch in line:
            if  is_hangeul(ch):
                print(ch,end='',file=outfp)
        print(file=outfp )
outfp.close()
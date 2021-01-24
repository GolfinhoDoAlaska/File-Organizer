import os

def makedirandmove(ff):
    PATH = os.getcwd()
    if not os.path.isdir(ff):
        os.mkdir(str(ff))
    os.rename(f, ff+"\\"+f)


for f in os.listdir(os.getcwd()):
    fnm, fex = os.path.splitext(f)
    print(fnm)
    print(fex)
    fex2 = fex.replace(".", "")
    makedirandmove(fex2)
    









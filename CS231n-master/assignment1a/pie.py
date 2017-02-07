import math

T=input()
out_li=[]
for i in range(T):
    a=raw_input()
    a=a.strip("\n")
    p,x,y=map(int,a.split())
    angle=(float(p)/100)*360
  
    angle-=90
    if(p==0 or math.sqrt( (y-50)**2 + (x-50)**2 ) >50 ):
         out_li.append("case #%d: 'white'"%(i+1))

    else:
        if (
            if (math.tan(math.radians(angle)) < (float(x-50)/(y-50))):
                    print angle,math.tan(math.radians(angle)),",",(float(x-50)/(y-50))
                   
                    out_li.append("case #%d: 'white'"%(i+1))
            else :
                    out_li.append("case #%d: 'black'"%(i+1))



for i in out_li:
    print i
         

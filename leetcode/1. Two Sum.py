
class Solution:
    def romanToInt(self, s: str) -> int:
        sums = 0
        i=0
        
        while(i<(len(s)-1)):
            # 是否为特殊字符I X C    L40 C90 D400 M900 
            if(s[i]=='I'):
                if (s[i+1]=='V'):
                    sums+=4
                    i+=2
                elif(s[i+1]=='X'):
                    sums+=9
                    i+=2
                else:
                    sums+=1
                    i+=1
            elif(s[i]=='X'):
                if(s[i+1]=='L'):
                    sums+=40
                    i+=2
                elif(s[i+1]=='C'):
                    sums+=90
                    i+=2
                else:
                    sums+=10
                    i+=1
            elif(s[i]=='C'):
                if(s[i+1]=='D'):
                    sums+=400
                    i+=2
                elif(s[i+1]=='M'):
                    sums+=900
                    i+=2
                else:
                    sums+=100
                    i+=1
            # 特殊字符处理完毕，V L D M
            else:
                if(s[i]=='V'):
                    sums+=5
                    i+=1
                elif(s[i]=='L'):
                    sums+=50
                    i+=1
                elif(s[i]=='D'):
                    sums+=500
                    i+=1
                elif(s[i]=='M'):
                    sums+=1000
                    i+=1
            
        print(s[i+1])
        return sums

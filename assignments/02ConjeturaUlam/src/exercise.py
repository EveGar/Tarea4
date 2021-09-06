def main():
    n=int(input())
    b=str(n)
    if n>0:
       while(n>1):
           if(n%2==0):
               n=(n//2)
               b=b+' '+str(n)
        
           else:
               n=(n*3)+1
               b=b+' '+str(n)
       print(b)
   else:
       print('Invalid input')

if __name__=='__main__':
    main()

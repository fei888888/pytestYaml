class Cal:
    def div(self,a,b):
        return a/b
    def sub(self,a,b):
        return a-b
    def add(self,a,b):
        return a+b
if __name__ == '__main__':
    cal=Cal()
    print(cal.sub(2,3))
    print(cal.div(2,0))
class Contador:
    num=0

    def __init__(self,a) -> None:
        self.num=a

    def imprimir(self):
        i=1
        aste="*"
        while i<=self.num:
            print(aste)
            aste+="*"
            i+=1

def main():
    obj=Contador(10)
    obj.imprimir()

if __name__=="__main__":
    main()
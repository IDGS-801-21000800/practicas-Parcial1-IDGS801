class listaOp:
    lista=[1,3,2,2,6,7,1,3,3]
    tamano=0

    def __init__(self,a) -> None:
        self.tamano=a

    def suma(self):
        self.res = self.num1 + self.num2
        print("{} + {} = {} ".format(self.num1, self.num2, self.res))
    
    def getNumeros(self):
        i=0
        while i<self.tamano:
            numero=int(input("introduce número {}: ".format(i+1)))
            self.lista.append(numero)
            i+=1
        print(self.lista)

    #ordenar
    def ordenar(self):
        print("LISTA ORDENADA")
        self.lista.sort()
        print(self.lista)

    #pares
    def pares(self):
        print("PARES")
        print(self.lista)
        i=0
        while i < self.lista.__len__():
            f=self.lista[i]%2
            if f==0:print("{} es Par".format(self.lista[i]))
            i+=1

    #impares
    def impares(self):
        print("IMPARES")
        print(self.lista)
        i=0
        while i < self.lista.__len__():
            f=self.lista[i]%2
            if f==1:print("{} es Impar".format(self.lista[i]))
            i+=1
            
    #numeros repetidos
    def repet(self):
        print("Repeticiones")
        i=0
        while i < self.lista.__len__(): 
            repet=0
            numero=self.lista[i]
            k=0
            for j in self.lista:
                if numero==self.lista[k]:
                    repet+=1
                k+=1

            if repet > 1 and numero==i:
                print("{} se repite {} veces".format(numero, repet))
            
            i+=1
        
            

def main():
    #numero=int(input("cuantos numeros quieres: "))
    obj=listaOp(0)
    #obj.getNumeros()
    obj.ordenar()
    #obj.pares()
    #obj.impares()
    obj.repet()

if __name__=="__main__":
    main()
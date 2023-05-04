from ClaseNodo import *

class Lista():
    def __init__(self):
        self.head = None
        self.len = 0
    def agregarinicio(self, nodo=Nodo):
        if(self.len==0): #averiguamos la longitud de mi lista. Si es =0 quiere decir que la lista esvacia, por lo que el head estará direccionada al nodo
            self.head=nodo
            self.len+=1
        else:
            nodo.prox=self.head
            self.head=nodo
            self.len+=1
    def __str__(self):
        nodo=self.head
        cadena=''
        if self.len==0:
            return('Lista Vacia')
        else:
            while nodo!=None:
                cadena+=str(nodo.dato)+'\t'
                nodo=nodo.prox
            return cadena
    def append(self,nodo=Nodo):
        if(self.len==0):
            self.head=nodo
        else:
            nodomov=Nodo()
            nodomov=self.head
            while(nodomov.prox!=None):
                nodomov=nodomov.prox
            nodomov.prox=nodo
        self.len+=1
    def pop(self,pos=None):
        nodo=Nodo()
        nodo=self.head
        if pos==None:
            final=self.len-2
            for i in range(final):
                nodo=nodo.prox
            nodo.prox=None
        else:
            for i in range(pos-1):
                nodo=nodo.prox
            nodo.prox=nodo.prox.prox
        self.len-=1
        
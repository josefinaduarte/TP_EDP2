from ClaseNodo import *

class Lista():
    def __init__(self):
        self.head = None
        self.len = 0
    def agregarinicio(self, nodo:Nodo):
        if(self.len==0): #averiguo la longitud de mi lista. Si es =0 mi lista esvacia, por lo que mi head va a estar direccionada al nodo
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
    def append(self,nodo:Nodo):
        if(self.len==0):
            self.head=nodo
        else:
            nodomov=Nodo()
            nodomov=self.head
            while(nodomov.prox!=None):
                nodomov=nodomov.prox
            nodomov.prox=nodo
        self.len+=1
    def pop(self,pos=None): #elimina el ultimo elemento de la lista. El pop sin ningun parametro sabe que elimina el ultimo de la lista. Si le ongo una direccion saca ese elemento
        nodo=Nodo()
        nodo=self.head
        if pos==None:
            final=self.len-2 #me muevo hasta la penultima posicion
            for i in range(final):
                nodo=nodo.prox
            nodo.prox=None
        else:
            for i in range(pos-1):
                nodo=nodo.prox
            nodo.prox=nodo.prox.prox
        self.len-=1
        
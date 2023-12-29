class calculadora:
   def __init__(self, ina, inb):
      self.a = ina
      self.b = inb
      
   def suma(self):
          return self.a + self.b
   
   def mult(self):
      return self.a * self.b
   
#nuevoCalculo = calculadora(10,20)
#print('a=10\nb=20\n')
#print('a + b: %d'%nuevoCalculo.suma()) 
#print('a x b: %d'%nuevoCalculo.mult())   

class cientifica(calculadora):
       def potencia(self):
              return pow(self.a, self.b)
           
def sumarapida(a,b):
      return(a+b)
   
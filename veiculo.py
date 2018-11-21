class Veiculo:
    def __init__(self,codigo,modelo,status,marca,ano,valor):
        self.codigo = codigo
        self.modelo = modelo    
        self.status = status        
        self.marca = marca    
        self.ano = ano    
        self.valor = valor
        self.prazo1 = 0
        self.prazo1aux=0
        self.locatario1 = ''        
        self.dia1 = 0
        self.mes1 = 0
        self.ano1 = 0
        self.dia2 = 0
        self.mes2 = 0
        self.ano2 = 0
        self.prazo2 = 0
        self.prazo2aux=0
        self.locatario2 = ''
        self.atrasado1 = False
        self.atrasado2 = False
        self.devolvido1 = False
        self.devolvido2 = False
        self.configurado1 = False
        self.configurado2 = False
        self.dias1 = 0
        self.dias2 = 0
    
    def detalhes(self):
        if(self.codigo < 10):
            c = '00'+ str(self.codigo)
            print('|codigo:',c)
        elif(self.codigo < 100):
            c = '0'+ str(self.codigo)
            print('|codigo:',c)
        else:
            print('|codigo:',self.codigo)
                
        print('|modelo:', self.modelo)
        print('|status:', self.status)
        print('------------------')
        
    def maisdetalhes(self):                    
          if(self.codigo < 10):
             c = '00'+ str(self.codigo)
             print('|codigo:',c)
          elif(self.codigo < 100):
             c = '0'+ str(self.codigo)
             print('|codigo:',c)
          else:
             print('|codigo:',veiculos[contador].codigo)

          print('|modelo:',self.modelo)
          print('|status:', self.status)                
          print('|marca:', self.marca)
          print('|ano:', self.ano)
          print('|valor:', self.valor)
          print('------------------')
    
            
                
        
    

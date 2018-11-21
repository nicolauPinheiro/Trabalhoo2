from veiculo import Veiculo #importa a classe veiculo
from datetime import date

hj = date.today()
indicador = True 
veiculos = []
d_atual = int(hj.day)
m_atual =  int(hj.month)
a_atual = int(hj.year)
qdm = 30
qva = 0 #armazena a quantidade de veiculos alugados
qa = 0 #armazena a quantidade de atraso
primeiravez = True

indic = False
indi = False
c=0
while 1:    
    q_atrasados = 0
    #verifica atraso e atualiza objetos
    ###################################
    for i in range(len(veiculos)):
        if(not veiculos[i].configurado1):            
            break
        dia = veiculos[i].dia1        
        mes = veiculos[i].mes1
        ano = veiculos[i].ano1
        prazo = veiculos[i].prazo1        
        diaatual = str(d_atual)
        mesatual = str(m_atual)
        anoatual = str(a_atual)
        
        if(dia+prazo-1 > qdm and mes == 12):
            dia = dia+prazo-1-qdm
            mes = 1
            ano = ano+1
        elif(dia+prazo-1>qdm):
            dia = dia+prazo-1-qdm
            mes = mes+1
        elif(dia==1):
            dia=1
        else:
            dia=dia+prazo-1

        dia1 = str(dia)
        mes1 = str(mes)
        ano1 = str(ano)
        #convertar data atual em um numero
        if(int(mesatual) < 10):
            mesatual = '0'+str(mesatual)
        else:
            mesatual = str(mesatual)
        if(int(diaatual) < 10):
            diaatual = '0'+str(diaatual)
        else:
            diaatual = str(diaatual)
        anoatual = str(anoatual)        
        dataatual = int(anoatual+mesatual+diaatual)
        
        #convertar data reservada
        if(mes < 10):
            mes1 = '0'+str(mes1)
        else:
            mes1 = str(mes)
        if(dia < 10):
            dia1 = '0'+str(dia)
        else:
            dia1 = str(dia)            
        ano1 = str(ano)
            
        data1 = int(str(ano1)+str(mes1)+str(dia1))
        
        #verifica o atraso
        if((int(data1) < int(dataatual)) and (veiculos[i].devolvido1 == False)):
            veiculos[i].atrasado1 = True
            veiculos[i].dias1 = veiculos[i].dias1+1
    ###################################
    ###################################
    #verifica atraso
    for i in range(len(veiculos)):
        if(not veiculos[i].configurado2):            
            break
        dia = veiculos[i].dia2
        mes = veiculos[i].mes2
        ano = veiculos[i].ano2
        prazo = veiculos[i].prazo2        
        diaatual = str(d_atual)
        mesatual = str(m_atual)
        anoatual = str(a_atual)
        
        if(dia+prazo-1 > qdm and mes == 12):
            dia = dia+prazo-1-qdm
            mes = 1
            ano = ano+1
        elif(dia+prazo-1>qdm):
            dia = dia+prazo-1-qdm
            mes = mes+1        
        elif(dia==1):
            dia=1
        else:
            dia=dia+prazo-1
        dia2 = str(dia)
        mes2 = str(mes)
        ano2 = str(ano)
        #convertar data atual em um numero
        if(int(mesatual) < 10):
            mesatual = '0'+str(mesatual)
        else:
            mesatual = str(mesatual)
        if(int(diaatual) < 10):
            diaatual = '0'+str(diaatual)
        else:
            diaatual = str(diaatual)
        anoatual = str(anoatual)        
        dataatual = int(anoatual+mesatual+diaatual)
        
        #convertar data reservada
        if(mes < 10):
            mes2 = '0'+str(mes1)
        else:
            mes1 = str(mes)
        if(dia < 10):
            dia2 = '0'+str(dia)
        else:
            dia2 = str(dia)            
        ano2 = str(ano)
            
        data2 = int(str(ano2)+str(mes2)+str(dia2))        
        #verifica o atraso
        if((int(data2) < int(dataatual)) and (veiculos[i].devolvido2 == False)):
            veiculos[i].atrasado2 = True        

    #################################
    ###################
    for i in range(len(veiculos)):
        if(veiculos[i].atrasado1 == True):
            q_atrasados = q_atrasados+1 
    for i in range(len(veiculos)):
        if(veiculos[i].atrasado2 == True):
            q_atrasados = q_atrasados+1
            veiculos[i].dias2 = veiculos[i].dias2+1
    ##############
    cont =0
    #coloca o status dos veiculos atrasados como ainda alugados
    for i in range(len(veiculos)):        
        if(veiculos[i].atrasado1 ==True or veiculos[i].atrasado2==True):
            veiculos[i].status = 'Alugado'
    for i in range(len(veiculos)):        
        if(veiculos[i].status =='Alugado'):
            cont = cont+1
    qva = cont
    
    print('========================================')
    print('|Data atual: ',d_atual,'/',m_atual,'/',a_atual)
    print('|Quantidade de veículos cadastrados:', len(veiculos))
    print('|Quantidade de veículos alugados:',qva)
    print('|Quantidade de veículos atrasados:',q_atrasados)
    print('========================================')
    print('|        [1]Consultar Veículos         |')              
    print('|        [2]Adicionar Veículos         |')              
    print('|      [3]Alugar/Reservar Veículos     |')
    print('|      [4]Devolver/Liberar Veículo     |')
    print('|          [5]Excluir Veículos         |')
    print('|         [6]Avançar Data Atual        |')
    print('|               [7]Sair                |')
    print('========================================')
    comando = int(input('comando: '))
    if(comando == 7):
        break    
    elif(comando == 1):                
        print('-----VEÍCULOS-----')
        for contador in range (len(veiculos)):            
            veiculos[contador].detalhes()          
                
        # limpar a tela e mostra mais detalhes
        c = input('VER MAIS DETALHES?:[S/N] ')
        if(c == 's' or c == 'S'):#mostra mais detalhes dos veiculos
            print('------------------')
            for contador in range (len(veiculos)):
                veiculos[contador].maisdetalhes()    
        # usar um senao e limpar a tela
    elif(comando == 2):        
        #recebe as caracteristicas do novo objeto a ser adicionado
        codigo = len(veiculos)+1 #guarda o codigo do novo objeto a ser adicionado
        status = 'Disponivel'
        marca = input('Digite a marca:')
        modelo = input('Digite o modelo:')
        ano = int(input('Digite o ano:'))
        valor = int(input('Digite o valor:'))
        # instancia o novo objeto a ser adicionado
        v = Veiculo(codigo,modelo,status,marca,ano,valor)
        #adiciona à lista o novo instanciado com caracteristicas definidas
        veiculos.append(v)
        #limpartela
    elif(comando == 3):
        indice = int(input('Código do carro: ')) - 1        
        #verifica se o veiculo já está alugado ou reservado para duas pessoas
        if(veiculos[indice].locatario1 != '' and veiculos[indice].locatario2 != ''):
            print('VEÍCULO JÁ RESERVADO PARA O NUMERO LIMITE')
            continue
        locatario = input('Nome do locatário:')
        data = input('data(dd/mm/aaaa):')
        prazo = int(input('prazo: '))
        dia = int(data[0]+data[1])
        mes = int(data[3]+data[4])
        ano = int(str(data[6])+str(data[7])+str(data[8])+str(data[9]))        
        status = veiculos[indice].status
        
        #verifica a data para aluguel/reserva ultrapassou 30 dias 
        anoatual = a_atual
        
        mesatual = m_atual
        diaatual = d_atual
        mesatualaux = str(m_atual)
        if(mesatual<10):
            mesatualaux = '0'+ mesatualaux
        
        
        if(int(diaatual)>=10):
            dataatual = int(str(anoatual)+mesatualaux+str(diaatual))
        else:
            dataatual = int(str(anoatual)+mesatualaux+'0'+str(diaatual))

        mes_a_r =str(mes)      
        if(mes<10):
            mes_a_r ='0'+str(mes)
        if(dia>=10):
            datareservada = int(str(ano)+mes_a_r+str(dia))
        else:
            datareservada = int(str(ano)+mes_a_r+'0'+str(dia))
        
        if(ano > anoatual):
           if(datareservada - dataatual -8870> 30):
               print('data solicitada ultrapassou o limite de 30 dias')
               continue    
        elif(datareservada - dataatual -70> 30):
           print('data solicitada ultrapassou o limite de 30 dias')
           continue
        
        if(status == 'Reservado' or status == 'Alugado'):
            dia_a = dia
            mes_a = mes
            ano_a = ano
            prazo_a = prazo
            mes_aux =''
            if(veiculos[indice].mes1<10):
                mes_aux = '0'+str(veiculos[indice].mes1)
            else:
                mes_aux =str(veiculos[indice].mes1)
            if(veiculos[indice].dia1>=10):
                data1 = int(str(veiculos[indice].ano1)+mes_aux+str(veiculos[indice].dia1))
            else:
                data1 = int(str(veiculos[indice].ano1)+mes_aux+'0'+str(veiculos[indice].dia1))    

            data2= datareservada
            print('data1:',data1)
            print('data2:',data2)
            diareservado=0
            mesreservado=0
            prazo_r = 0
            #verifica a sobreposicao
            if(data2 == data1):
                print('sobreprosição de data')
                continue
            if(data2 > data1):
                diareservado=veiculos[indice].dia1
                mesreservado=veiculos[indice].mes1
                anoreservado=veiculos[indice].ano1
                prazo_r = veiculos[indice].prazo1
            elif(data1 > data2):
                diareservado=dia
                mesreservado=mes
                anoreservado=ano
                prazo_r = prazo
                dia = veiculos[indice].dia1
                mes = veiculos[indice].mes1
                ano=veiculos[indice].ano1
                prazo=veiculos[indice].prazo1
               
            #verifica a sobreposicao de datas quando o prazo propociona a mudanca de mes
            if((diareservado + prazo_r - 1) >qdm):                
                indicador = False
                
                i=0                
                while(i<prazo_r):
                    print('dia reservado:',diareservado)
                    print('mes reservado:',mesreservado)
                    print('ano reservado:',anoreservado)
                    print('dia:',dia)
                    print('mes:',mes)
                    print('ano:',ano)
                    if((diareservado) > qdm):
                        diareservado = 1
                        if(mesreservado==12):
                            mesreservado = 1
                            anoreservado = anoreservado+1
                        else:
                            mesreservado = mesreservado+1
                        continue
                      
                    if(dia==diareservado and mes == mesreservado and ano == anoreservado):
                        print('sobreposicao de datas')
                        indicador = True
                        break
                    
                    diareservado=diareservado+1
                    i = i+1
                #se nao houver sobreposicao de datas,a reserva é efetuada
                if(not indicador):
                    veiculos[indice].locatario2 = locatario
                    veiculos[indice].dia2 = dia_a
                    veiculos[indice].mes2 = mes_a
                    veiculos[indice].ano2 = ano_a
                    veiculos[indice].prazo2 = prazo_a
                    veiculos[indice].configurado2 = True
                    veiculos[indice].prazo2aux=prazo_a

            #verifica a sobreposicao de datas quando o prazo nao propociona a mudanca de mes
            else:
                indicador = False
                i=0
                while(i<prazo_r):                    
                    if(dia==diareservado+i and mes == mesreservado):
                        print('sobreposicao de datas')
                        indicador = True
                        break
                    i = i+1
                #se nao houver sobreposicao de datas,a reserva é efetuada
                if(not indicador):
                    veiculos[indice].locatario2 = locatario
                    veiculos[indice].dia2 = dia_a
                    veiculos[indice].mes2 = mes_a
                    veiculos[indice].ano2 = ano_a
                    veiculos[indice].prazo2 = prazo_a
                    veiculos[indice].prazo2aux=prazo_a
                    veiculos[indice].configurado2 = True
        elif(dia == d_atual and mes == m_atual and ano ==a_atual):                
                veiculos[indice].status = 'Alugado'
                veiculos[indice].locatario1 = locatario
                veiculos[indice].dia1 = dia
                veiculos[indice].mes1 = mes
                veiculos[indice].ano1 = ano
                veiculos[indice].prazo1 = prazo
                veiculos[indice].prazo1aux=prazo
                veiculos[indice].configurado1 = True
        else:
                veiculos[indice].status = 'Reservado'
                veiculos[indice].locatario1 = locatario
                veiculos[indice].dia1 = dia
                veiculos[indice].mes1 = mes
                veiculos[indice].ano1 = ano
                veiculos[indice].prazo1 = prazo
                veiculos[indice].prazo1aux=prazo
                veiculos[indice].configurado1 = True
    elif(comando == 5):
        codigo = int(input('Código do veículo a ser excluído:'))
        if(veiculos[codigo-1].status == 'Disponivel'):
            veiculos.remove(veiculos[codigo-1])
            print('veículo removido com sucesso!')            
        else:
            print('não foi possível remover, o veículo contém reservas')
            
    elif(comando ==4):
        print('----VEÍCULOS------')
        for i in range(len(veiculos)):
            if((veiculos[i].status=='Reservado' or veiculos[i].status=='Alugado') and veiculos[i].configurado1):
                if(veiculos[i].codigo < 10):
                    c = '00'+ str(veiculos[i].codigo)
                    print('|Código:',c)
                elif(veiculos[i].codigo < 100):
                    c = '0'+ str(veiculos[i].codigo)
                    print('|Código:',c)
                else:
                    print('|Código:',veiculos[i].codigo)
                
                print('|Locatário: ',veiculos[i].locatario1)
                print('|Modelo: ',veiculos[i].modelo)
                print('|Marca: ',veiculos[i].marca)
                print('|Status: ',veiculos[i].status)
            print('---------------------')
        for i in range(len(veiculos)):
            if((veiculos[i].status=='Reservado' or veiculos[i].status=='Alugado') and veiculos[i].configurado2):
                if(veiculos[i].codigo < 10):
                    c = '00'+ str(veiculos[i].codigo)
                    print('|Código:',c)
                elif(veiculos[i].codigo < 100):
                    c = '0'+ str(veiculos[i].codigo)
                    print('|código:',c)
                else:
                    print('|Código:',veiculos[i].codigo)
                
                print('|Locatário: ',veiculos[i].locatario2)
                print('|Modelo: ',veiculos[i].modelo)
                print('|Marca: ',veiculos[i].marca)
                print('|Status: ',veiculos[i].status)
                print('---------------------')
        codigo = int(input('Código do veículo a liberar/devolver: '))
        if(veiculos[codigo-1].atrasado1):
            preco = (veiculos[codigo-1].dias1+veiculos[codigo-1].prazo1aux) * veiculos[codigo-1].valor
            print('DEVOLUÇÃO EM ATRASO')
            print('DIAS EM ATRASO: ',veiculos[codigo-1].dias1)
            print('VALOR TOTAL A SER PAGO R$',preco,',00')
            veiculos[codigo-1].atrasado1 = False
            veiculos[codigo-1].devolvido1 = True
            veiculos[codigo-1].status = 'Disponivel'
        if(veiculos[codigo-1].atrasado2):
            preco = (veiculos[codigo-1].dias2+veiculos[codigo-1].prazo2aux) * veiculos[codigo-1].valor
            print('DEVOLUÇÃO EM ATRASO')
            print('DIAS EM ATRASO: ',veiculos[codigo-1].dias2)
            print('VALOR TOTAL A SER PAGO R$',preco,',00')
            veiculos[codigo-1].atrasado2 = False
            veiculos[codigo-1].devolvido2 = True
            veiculos[codigo-1].status = 'Disponivel'
        ########################################################
        dia = veiculos[codigo-1].dia1
        mes = veiculos[codigo-1].mes1
        ano = veiculos[codigo-1].ano1
        prazo = veiculos[codigo-1].prazo1        
        diaatual = str(d_atual)
        mesatual = str(m_atual)
        anoatual = str(a_atual)
        
        if(dia+prazo-1 > qdm and mes == 12):
            dia = dia+prazo-1-qdm
            mes = 1
            ano = ano+1
        elif(dia+prazo-1>qdm):
            dia = dia+prazo-1-qdm
            mes = mes+1        
        elif(dia==1):
            dia=1
        else:
            dia=dia+prazo-1
        dia2 = str(dia)
        mes2 = str(mes)
        ano2 = str(ano)
        #convertar data atual em um numero
        if(int(mesatual) < 10):
            mesatual = '0'+str(mesatual)
        else:
            mesatual = str(mesatual)
        if(int(diaatual) < 10):
            diaatual = '0'+str(diaatual)
        else:
            diaatual = str(diaatual)
        anoatual = str(anoatual)        
        dataatual = int(anoatual+mesatual+diaatual)
        
        #convertar data reservada
        if(mes < 10):
            mes2 = '0'+str(mes1)
        else:
            mes1 = str(mes)
        if(dia < 10):
            dia2 = '0'+str(dia)
        else:
            dia2 = str(dia)            
        ano2 = str(ano)
            
        data2 = int(str(ano2)+str(mes2)+str(dia2))        
        
        if(int(data2) > int(dataatual)):
            print('RESERVA DO VEÍCULO LIBERADA')
            veiculos[codigo-1].status = 'Disponivel'

        #######################################################
        if(veiculos[codigo-1].configurado2):
            dia = veiculos[codigo-1].dia2
            mes = veiculos[codigo-1].mes2
            ano = veiculos[codigo-1].ano2
            prazo = veiculos[codigo-1].prazo2        
            diaatual = str(d_atual)
            mesatual = str(m_atual)
            anoatual = str(a_atual)
        
            if(dia+prazo-1 > qdm and mes == 12):
                dia = dia+prazo-1-qdm
                mes = 1
                ano = ano+1
            elif(dia+prazo-1>qdm):
                dia = dia+prazo-1-qdm
                mes = mes+1        
            elif(dia==1):
                dia=1
            else:
                dia=dia+prazo-1
            dia2 = str(dia)
            mes2 = str(mes)
            ano2 = str(ano)
            #convertar data atual em um numero
            if(int(mesatual) < 10):
                mesatual = '0'+str(mesatual)
            else:
                mesatual = str(mesatual)
            if(int(diaatual) < 10):
                diaatual = '0'+str(diaatual)
            else:
                diaatual = str(diaatual)
            anoatual = str(anoatual)        
            dataatual = int(anoatual+mesatual+diaatual)
        
            #convertar data reservada
            if(mes < 10):
                mes2 = '0'+str(mes2)
            else:
                mes2 = str(mes)
            if(dia < 10):
                dia2 = '0'+str(dia)
            else:
                dia2 = str(dia)            
            ano2 = str(ano)
            
            data2 = int(str(ano2)+str(mes2)+str(dia2))        
        
            if(int(data2) > int(dataatual)):
                print('RESERVA DO VEÍCULO LIBERADA')
                veiculos[codigo-1].status = 'Disponivel'
        ######################################################    
    elif(comando == 6):
        d_atual= d_atual+1
        if(d_atual > 30 and m_atual==12):
            d_atual=1
            m_atual=1
            a_atual = a_atual+1
        elif(d_atual > 30):
            d_atual=1
            m_atual=m_atual+1
            
        for i in range(len(veiculos)):
            if(veiculos[i].dia1 == d_atual):                    
                veiculos[i].prazo1 = veiculos[i].prazo1-1                        
                if(-1 < veiculos[i].prazo1):   
                    veiculos[i].dia1 = veiculos[i].dia1+1
                    if(veiculos[i].dia1>30 and veiculos[i].mes1==12):
                        veiculos[i].dia1 = 1
                        veiculos[i].mes1 = 1
                        veiculos[i].ano1 = veiculos[i].ano1+1
                    elif(veiculos[i].dia1>30):
                        veiculos[i].dia1 = 1
                        veiculos[i].mes1 = veiculos[i].mes1+1
                    veiculos[i].status = 'Alugado'                            
                else:
                    veiculos[i].status = 'Disponivel'                        
                    veiculos[i].dia1 = veiculos[i].dia1-1            
        for i in range(len(veiculos)):
            if(veiculos[i].dia2 == d_atual):                    
                veiculos[i].prazo2 = veiculos[i].prazo2-1                        
                if(-1 < veiculos[i].prazo2):
                    if(veiculos[i].dia2>30 and veiculos[i].mes2==12):
                        veiculos[i].dia2 = 1
                        veiculos[i].mes2 = 1
                        veiculos[i].ano2 = veiculos[i].ano2+1
                    elif(veiculos[i].dia2>30):
                        veiculos[i].dia2 = 1
                        veiculos[i].mes2 = veiculos[i].mes2+1
                    veiculos[i].status = 'Alugado'
                    veiculos[i].dia2 = veiculos[i].dia2+1
                else:
                    veiculos[i].status = 'Disponivel'                        
                    veiculos[i].dia2 = veiculos[i].dia2-1     
            

            
           

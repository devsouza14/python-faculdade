# Locadora de carros
 
print('Bem vindos a Big locações')

class carro:
    def __init__(self,marca, modelo, cor, combustivel, ano):
        self.marca = marca
        self.modelo = modelo 
        self.cor = cor 
        self.combustivel = combustivel 
        self.ano = ano 

    def Alugado(Self):
        print('Veiculo alugado')

    def Devolvido(Self):
        print('Veiculo devolvido')

    def infoDoVeiculo(Self):
        print(Self.marca, Self.modelo, Self.cor, Self.combustivel, Self.ano)
    
    
carro1 = carro('Gm','Celta','Branco', 'Flex', '2007')
carro2 = carro('Volkswagen', 'Gol', 'Prata', 'Flex', '2015')
carro3 = carro('Volkswagen', 'Jetta', 'Preto', 'Flex', '2016')


opcao1 = carro1
opcao2 = carro2
opcao3 = carro3

selecaoDeVeiculo = input(str("Selecione o veiculo: "))

if selecaoDeVeiculo == "opcao1":
    opcao1.infoDoVeiculo()

elif selecaoDeVeiculo == "opcao2":

    opcao2.infoDoVeiculo()

else:

    opcao3.infoDoVeiculo()
      


#carro2.Alugado()
#carro1.Devolvido()
#carro2.infoDoVeiculo()

      
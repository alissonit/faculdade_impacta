# Linguagem de Programação II
# Atividade Contínua 02 - Classes e Herança
#
# e-mail: alisson.castro@aluno.faculdadeimpacta.com.br


"""
Implementar aqui as cinco classes filhas de Mamifero ou Reptil,
de acordo com o caso, conforme dado no diagrama apresentado no padrão UML.

Os atributos específicos de cada classe filha devem ser recebidos
como parâmetros no momento da criação, a única exceção é o número de vidas
do gato, que sempre começa em 7.

Os métodos de cada classe filha devem sempre RETORNAR uma string
no seguinte formato '<nome do animal> <método em questão no gerúndio>'
Sem nenhuma pontuação, conforme os exemplos a seguir.

Exemplo:
método trocar_pele() retorna '<nome> trocando de pele'
método dormir() retorna '<nome> dormindo'
método miar() retorna '<nome> miando'
Onde <nome> é o nome dado para cada animal (o valor atributo nome de
cada instância, não o nome da classe)

"""


class Reptil:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)


class Mamifero:
    """
    Classe mãe - não deve ser editada
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata

    def correr(self):
        return '{} correndo'.format(self.nome)

    def mamar(self):
        if self.idade <= 1:
            return '{} mamando'.format(self.nome)
        else:
            return '{} já desmamou'.format(self.nome)


class Camaleao(Reptil):
    """
    Exemplo de solução do exercício:

    Além dos atributos da classe mãe, possui o atributo:
    inseto_favorito, do tipo string.

    Implementa os métodos específicos:
    mudar_de_cor() e comer_inseto()
    """
    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)


class Cavalo(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    cor_crina, do tipo string.

    Implementa os métodos específicos:
    galopar() e relinchar()
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.cor_crina = cor_crina

    def galopar(self):
        return '{} galopando'.format(self.nome)

    def relinchar(self):
        return '{} relinchando'.format(self.nome)   

class Cobra(Reptil):
    """
    Além dos atributos da classe mãe, possui o atributo:
    veneno, do tipo booleano.

    Implementa os métodos específicos:
    rastejar() e trocar_pele()
    """
    
    def __init__(self, nome, cor, idade, veneno):
        super().__init__(nome, cor, idade)
        self.veneno = veneno

    def rastejar(self):
        return '{} rastejando'.format(self.nome)
    
    def trocar_pele(self):
        return '{} trocando de pele'.format(self.nome)



class Cachorro(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    raca, do tipo string. (raça, porém sem o ç)

    Implementa os métodos específicos:
    latir() e rosnar()
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.raca = raca
    
    def latir(self):
        return '{} latindo'.format(self.nome)
    
    def rosnar(self):
        return '{} rosnando'.format(self.nome)


class Jacare(Reptil):
    """
    Além dos atributos da classe mãe, possui o atributo:
    num_dentes, do tipo inteiro.

    Implementa os métodos específicos:
    atacar() e dormir()
    """

    def __init__(self, nome, cor, idade, num_dentes):

        super().__init__(nome, cor, idade)
        self.num_dentes = num_dentes

    def atacar(self):
        return '{} atacando'.format(self.nome)
    
    def dormir(self):
        return '{} dormindo'.format(self.nome)


class Gato(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    vidas, do tipo inteiro.

    Implementa os métodos específicos:
    miar() e morrer()

    No método morrer, você deve verificar quantas vidas o gato ainda
    tem sobrando, se for igual a zero, retornar:
    '<nome> morreu'
    se ainda houver vidas sobrando, retirar uma vida (que começa em 7),
    e retornar:
    '<nome> tem <vidas> vidas sobrando'
    Onde <vidas> é o número de vidas restantes do gato em questão.
    """

    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.vidas = 7

    def miar(self):
        return '{} miando'.format(self.nome)

    def morrer(self):
            
        if self.vidas == 0:
            return '{} morreu'.format(self.nome)
        else:
            self.vidas -= 1 
            return '{} tem {} vidas sobrando'.format(self.nome, self.vidas)   

def main():

    #camaleao
    camaleao = Camaleao("camil", "verde", 10, "abelha")
    print(30*"=")
    print(f"Camaleao: \nNome: {camaleao.nome}\nCor: {camaleao.cor}\nIdade: {camaleao.idade}\n{camaleao.botar_ovo()}\n{camaleao.tomar_sol()}\n{camaleao.mudar_de_cor()}\n{camaleao.comer_inseto()}\nInseto Favorito: {camaleao.inseto_favorito}")
    print(30*"=")
    #cobra
    cobra = Cobra("Python", "Amarelo", 1, True)
    print(f"Cobra: \nNome: {cobra.nome}\nCor: {cobra.cor}\nIdade: {cobra.idade}\n{cobra.botar_ovo()}\n{cobra.tomar_sol()}\n{cobra.rastejar()}\n{cobra.trocar_pele()}\nVenenosa: {cobra.veneno}")
    print(30*"=")
    #jacare
    jacare = Jacare("Jorge", "marrom", 10, 100)
    print(f"Jacare: \nNome: {jacare.nome}\nCor:{jacare.cor}\nIdade: {jacare.idade}\n{jacare.botar_ovo()}\n{jacare.tomar_sol()}\n{jacare.atacar()}\n{jacare.dormir()}\nNumero de dentes: {jacare.num_dentes}")
    print(30*"=")
    #Cavalo
    cavalo = Cavalo("Horse", "cinza", 10, "quadrupede", "preto")
    print(f"Cavalo: \nNome: {cavalo.nome}\nCor pelo: {cavalo.cor_pelo} \nIdade: {cavalo.idade}\nTipo de pata: {cavalo.tipo_pata}\n{cavalo.galopar()}\n{cavalo.relinchar()}\nCor crina: {cavalo.cor_crina}")
    print(30*"=")
    #cachorro
    cachorro = Cachorro("Thor", "branco", 5, "quadrupede", "Husky Siberiano")
    print(f"Cachorro: \nNome: {cachorro.nome}\nCor pelo: {cachorro.cor_pelo}\nIdade: {cachorro.idade}\nTipo de pata: {cachorro.tipo_pata}\n{cachorro.latir()}\n{cachorro.rosnar()}\nRaca: {cachorro.raca}")
    print(30*"=")
    #gato
    gato = Gato("Garfield", "Laranja", 10, "quadrupede")
    print(f"Gato: \nNome: {gato.nome}\nCor pelo: {gato.cor_pelo}\nIdade: {gato.idade}\nTipo de pata: {gato.tipo_pata}\n{gato.miar()}\n")
    for i in range(8):
        print("Matando gato...")
        print(gato.morrer())

if __name__ == "__main__":

    main()
    
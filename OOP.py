class Endereco():
    
    def __init__(self,pais =None,estado =None,cidade =None,quadra =None,
                 alameda =None,numero =None):
        self.pais = pais
        self.estado = estado
        self.cidade = cidade
        self.quadra = quadra
        self.alameda = alameda
        self.numero = numero
    
class Pessoa():
    
    def __init__(self,nome,idade,sexo,data_nascimento):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.endereco = Endereco('Brasil','Tocantins','Palmas','106sul','12','26')

    def __str__(self):
        return self.nome +','+self.idade+','+self.data_nascimento+','+

class PessoaFisica(Pessoa):
    
    def __init__(self,CPF,nome,idade,sexo,data_nascimento):
        Pessoa. __init__(self,nome,idade,sexo,data_nascimento)
        self.CPF = CPF

    def __str__(self):
        return u'{} - {}'.format(self.CPF, sef.nome)

class PessoaJuridica(Pessoa):
    
    def __init__(self,CNPJ,nome,idade,sexo,data_nascimento):
        Pessoa. __init__(self,nome,idade,sexo,data_nascimento)
        self.CNPJ = CNPJ

    

    

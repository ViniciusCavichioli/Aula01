class Projeto():

    def __init__(self,nome =None,descricao =None):
        self.nome = nome
        self.descricao = descricao

class Pessoa():
    
    def __init__(self,nome =None,idade =None,sexo =None,data_nascimento =None):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.data_nascimento = data_nascimento
       

    def __str__(self):
        return self.nome +','+self.idade+','+self.sexo+','+self.data_nascimento

class PessoaFisica(Pessoa):
    
    def __init__(self,CPF=None,nome,idade,sexo,data_nascimento):
        Pessoa. __init__(self,nome,idade,sexo,data_nascimento)
        self.CPF = CPF

class PessoaJuridica(Pessoa):
    
    def __init__(self,CNPJ=None,nome,idade,sexo,data_nascimento):
        Pessoa. __init__(self,nome,idade,sexo,data_nascimento)
        self.CNPJ = CNPJ



class Tarefa():

    def __init__(self,descricao,dataInicio,dataFim,prioridade):
        self.descricao = descricao
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.prioridade = prioridade
        self.projeto = Projeto()
        self.solicita = PessoaJuridica()
        self.antede = PessoaFisica()




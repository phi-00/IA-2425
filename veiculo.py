class Veiculo:
    def __init__(self, tipo, combustivel_disponivel, custo, velocidade, volume_carga):

        self.tipo = tipo # avião, carro, ...
        self.combustivel_disponivel = combustivel_disponivel
        self.custo = custo # custo de usar cada veículo
        self.velocidade = velocidade
        self.volume_carga = volume_carga # que pode transportar

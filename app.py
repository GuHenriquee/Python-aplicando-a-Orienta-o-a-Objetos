from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import Bebida
from Modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao ('Gui', 10)
restaurante_praca.receber_avaliacao ('Eu', 8)


def main():
    pass

if __name__ == '__main__':
    main()
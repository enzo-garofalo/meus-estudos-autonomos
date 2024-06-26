from models.carro import Carro
from models.moto import Moto

def main():
    carro1 = Carro('Honda', 'Honda Fit', 4)
    carro2 = Carro('Fiat', 'Uno', 2)
    carro3 = Carro('Hyundai', 'Azeera', 4)

    moto1 = Moto("Harley-Davidson", "Street 750", "Esportiva")
    moto2 = Moto("Honda", "CB 500", "Casual")
    moto3 = Moto("Yamaha", "MT-09", "Esportiva")

    print(moto1)
    print('-'*20)
    print(moto2)
    print('-'*20)
    print(moto3)



if __name__ == '__main__':
    main()
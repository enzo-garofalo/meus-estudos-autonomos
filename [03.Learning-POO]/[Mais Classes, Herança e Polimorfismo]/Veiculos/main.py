from models.carro import Carro
from models.moto import Moto

def main():
    carro1 = Carro('Honda', 'Honda Fit', 4)
    carro2 = Carro('Fiat', 'Uno', 2)
    carro3 = Carro('Hyundai', 'Azeera', 4)

    print(carro1)
    print('-'*20)
    print(carro2)
    print('-'*20)
    print(carro3)



if __name__ == '__main__':
    main()
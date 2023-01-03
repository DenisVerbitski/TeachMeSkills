class Swap:
  
    @staticmethod
    def celsius(C: float):
        K = C + 273.15
        F = C * (9/5) + 32
        return f'\nПеревод температуры из цельсия в кельвины и фаренгейты\nЦельсия: {C}\nКельвины: {K}\nФаренгейты: {F}'

    @staticmethod
    def kelvin(K: float):
        C = K - 273.15
        F = (K - 273.15)  * (9 / 5) + 32
        return f'\nПеревод температуры из кельвинов в цельсия и фаренгейты\nКельвины: {K}\nЦельсия: {C}\nФаренгейты: {F}'

    @staticmethod
    def farengeit(F: float):
        C = (F - 32) * (5 / 9)
        K = (F - 32) * (5 / 9) + 273.15
        return f'\nПеревод температуры из фаренгейт в цельсия и кельвины\nФаренгейты: {F}\nЦельсия: {C}\nКельвины: {K}'

swap = Swap()
c = float(input('Введите температуру в цельсиях: '))
k = float(input('Введите температуру в кельвинах: '))
f = float(input('Введите температуру в фаренгейтах: '))
print(swap.celsius(c))
print(swap.kelvin(k))
print(swap.farengeit(f))
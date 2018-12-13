'''Proyecto Final'''

'''
Calculadora 
Integrantes:
Jhonathan Marin 
Roger Silva
Jonathan Prado
Karem Arias
Alfredo Guerra
'''


class Calculadora (object):
    '''Clase de calculadora'''
    def __init__(self, num1, num2):
        '''
        Contructor de la clase calculadora
        :param num1: num1
        :param num2: num2
        :type num1: double
        :type num2: double
        '''
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        '''
        Este es le metodo para la suma.
        :return: La suma de num1 con num2
        :rtype: double
        '''
        if self.num2 < 0:
            '''Este proceso sumara los numeros negativos'''
            return "La Suma de {}-{} ({}+{}) es igual a {}".format(self.num1, -self.num2, self.num1, self.num2, self.num1 + self.num2)
        else:
            '''Este proceso sumara los numeros positivos'''
            return "La Suma de {}+{} es igual a {}".format(self.num1, self.num2, self.num1 + self.num2)

    def resta(self):
        '''
        Este es le metodo para la resta.
        :return: La resta de num1 con num2
        :rtype: double
        '''
        if self.num2 < 0:
            '''Este proceso restara los numeros positivos'''
            return "La Resta de {}+{} ({}-{}) es igual a {}".format(self.num1, -self.num2, self.num1, self.num2, self.num1 - self.num2)
        else:
            '''Este proceso restara los numeros positivos'''
            return "La Resta de {}-{} es igual a {}".format(self.num1, self.num2, self.num1 - self.num2)

    def multiplicacion(self):
        '''
        Este es le metodo para multiplicacion.
        :return: La multiplicacion de num1 con num2
        :rtype: double
        '''
        if (self.num1 * self.num2 == -0.0) and (self.num1 < 0 or self.num2 < 0):
            '''Este proceso es para que el valor -0 no aparesca en pantalla'''
            return "La Multiplicacion de {}*{} es igual a {}".format(self.num1, self.num2, -(self.num1 * self.num2))
        else:
            '''Este proceso multplicara los valores '''
            return "La Multiplicacion de {}*{} es igual a {}".format(self.num1, self.num2, self.num1 * self.num2)

    def division(self):
        '''
        Este es le metodo para la division.
        :return: La divicion de num1 con num2
        :rtype: double
        '''
        if self.num1 == 0 and self.num2 == 0 or self.num1 == -0 and self.num2 == -0 or self.num1 == -0 and self.num2 == 0 or self.num1 == 0 and self.num2 == -0:
            return "No se pueden realizar divisiones entre cero ({}/{})".format(self.num1, self.num2)
        elif(self.num1 / self.num2 == -0.0) and (self.num1 < 0 or self.num2 < 0):
            return "La Division de {}/{} es igual a {}".format(self.num1, self.num2, -(self.num1 / self.num2))
        elif self.num2 == 0:
            return "No se pueden realizar divisiones entre cero ({}/{})".format(self.num1, self.num2)
        elif self.num1 == 0 and  self.num2 < 0:
            self.num2 = int(self.num2)
            return "La Division de {}/{} es igual a {}".format(self.num1, self.num2, -(self.num1 / self.num2))
        else:
            return "La Division de {}/{} es igual a {}".format(self.num1, self.num2, self.num1/self.num2)

    def potencia(self):
        '''
        Este es le metodo para la potencia.
        :return: La potencia de num1 con num2
        :rtype: double
        '''
        if self.num2 < 0:
            return "El resultado de la potencia negativa {}^{} es  1/{} o {}".format(self.num1, self.num2, self.num1**-self.num2, self.num1**self.num2)
        elif self.num2 == 0:
            return "Todo numero elevado a la 0 es igual a 1 ({}^{})".format(self.num1, self.num2)
        else:
            return "La Potencia de {}^{} es igual a {}".format(self.num1, self.num2, self.num1**self.num2)

    def raiz(self):
        '''
        Este es le metodo para la raiz.
        :return: La raiz de num1 con num2
        :rtype: double
        '''
        if self.num1 < 0 and self.num2 % 2 == 0:
            return "No se pueden realizar raices pares de numeros negativos ({}√{})".format(self.num2, self.num1)
        elif self.num1 < 0 and self.num2 % 2 != 0:
            self.num1 = -self.num1
            self.num1 = int(self.num1)
            return "La Raiz impar ({}) del numero negativo {} ({}√{}) es igual a {}".format(self.num2, -self.num1, self.num2, -self.num1, -(self.num1 ** (1 / self.num2)))
        elif self.num2 == 0:
            return "No se pueden realizar raices a la 0 ({}√{})".format(self.num2, self.num1)
        elif self.num2 < 0:
            self.num2 = -self.num2
            self.num2 = int(self.num2)
            return "La Raiz negativa de {}√{} es igual a 1/{} o {}".format(-self.num2, self.num1, self.num1**(1/self.num2), 1/(self.num1**(1/self.num2)))
        else:
            return "La Raiz de {}√{} es igual a {}".format(self.num2, self.num1, self.num1**(1/self.num2))


if __name__ == "__main__":
    '''Clase main '''
    lista = []
    while True:
        print("Calculadora que realiza operaciones entre dos numeros reales\n")
        print("Que desea realizar?")
        print("1. Operaciones\n2. Revisar datos guardados\n3. Salir")
        opcion = int(input("Seleccione: "))
        if opcion == 1:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            c = Calculadora(num1, num2)
            print("---Menu Principal---")
            print("1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Potencia\n6. Raiz")
            opcion = int(input("Seleccione: "))
            if opcion == 1:
                lista.append(c.suma())
                print(c.suma())
            elif opcion == 2:
                lista.append(c.resta())
                print(c.resta())
            elif opcion == 3:
                lista.append(c.multiplicacion())
                print(c.multiplicacion())
            elif opcion == 4:
                lista.append(c.division())
                print(c.division())
            elif opcion == 5:
                lista.append(c.potencia())
                print(c.potencia())
            elif opcion == 6:
                lista.append(c.raiz())
                print(c.raiz())
            else:
                print("Opcion Invalida, Intente nuevamente")
            while True:
                continuar = input("\nDesea continuar? (S/N): ")
                if continuar.lower() == "n" or continuar.lower() == "no":
                    exit()
                elif continuar.lower() == "s" or continuar.lower() == "si":
                    break
                else:
                    print("Seleccion Invalida, Intente nuevamente")
            print("\n\n")
        elif opcion == 2:
            for i in lista:
                print(i)
        elif opcion == 3:
            break
        else:
            print("Opcion Invalida, Intente nuevamente")

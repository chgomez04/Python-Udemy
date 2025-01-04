from NumerosIdenticosException import NumerosIdenticosException


resultado = None 

try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('numeros identicos') ##nos permite lanzar o arrojar una excepcion

    resultado =a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {e}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}')
else:
    print('No se arrojo ninguna exception')
finally:
    print('Ejecucion del bloque Finally')

    
print (f'Resultado: {resultado}')
print('continuamos...')
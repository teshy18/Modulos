import operaciones as op

def app():
    print('ejecutando el main')
    print('')

    print('sumando 10 + 10: '+ str(op.sumar(10, 5)))
    print('restando 10 - 5: ' + str(op.restar(10, 5)))
    print('dividiendo 10 entre 5: ' + str(op.dividir(10, 5)))
    print('multiplicando 10 por 5: ' + str(op.multiplicar(10, 5)))

if __name__ == '__main__':
    app()


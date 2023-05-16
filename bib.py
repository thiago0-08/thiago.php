def pede_metros():
    return float(input('Digite  o valor'))

def metros_para_cm(m):
    return m * 100

def informa_cm(cm):
    print(f'{cm}cm')


def ex1():
    metros = pede_metros()
    cm = metros_para_cm(metros)
    informa_cm(cm)




def pede_valor
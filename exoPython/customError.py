'''
Je déclare une classe CustomError qui hérite
de la classe Exception (fournit par Python)
https://docs.python.org/fr/3/tutorial/errors.html
'''

class CustomError(Exception):
    def __init__(self,erreur,message):
        print(message)


if __name__ == '__main__':
    try:
        0/0
        raise CustomError("002","ERRRR")
    except CustomError as err:
        print('CUST : ', err)
    except Exception as err:
        print("EXCEPT OTHER : ", err)
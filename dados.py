from pandas import read_csv

def ler_arquivo(path):
    datas = read_csv(path, encoding='ISO-8859-1' ,sep=';')
    return datas
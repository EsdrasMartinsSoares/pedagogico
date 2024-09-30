import pandas as pd 

data = pd.read_csv ('GasPricesinBrazil_2004-2019.csv', sep=';')



meninas_g = pd.DataFrame ({
    'nome' : ['estefane','larrisa', 'gabriela','Katryna'],
    'Idade': [21,18,17,23],
    'peso' : [49, 51, 55,53],
    'É de maior': [True, True , False,True]
},  index= ['Novinha1','Novinha2', 'Novinha3','Novinha4'] ) 

print(meninas_g)

meninas_g.to_csv('./meninas_g.csv', index=False sep=',' )
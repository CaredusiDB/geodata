# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import pandas as pd

#Creating a dictionary where each key will be a DataFrame column

data = {
'País': ['Bélgica', 'Índia', 'Brasil'],
'Capital': ['Bruxelas', 'Nova Delhi', 'Brasília'],
'População': [123465, 456789, 987654]
}

#Creating the DataFrame
df = pd.DataFrame(data, columns=['País','Capital','População'])

print(df)

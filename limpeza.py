import pandas as pd

#SCRIPT PARA TRATAMENTO DOS DADOS COLETADOS
df_cursos_2021 = pd.read_csv('MICRODADOS_CADASTRO_CURSOS_2021.CSV', encoding="ISO-8859-1", sep=';', low_memory=False)
df_cursos_2020 = pd.read_csv('MICRODADOS_CADASTRO_CURSOS_2020.CSV', encoding="ISO-8859-1", sep=';', low_memory=False)
df_cursos_2019 = pd.read_csv('MICRODADOS_CADASTRO_CURSOS_2019.CSV', encoding="ISO-8859-1", sep=';', low_memory=False)
df_cursos_2018 = pd.read_csv('MICRODADOS_CADASTRO_CURSOS_2018.CSV', encoding="ISO-8859-1", sep=';', low_memory=False)
df_cursos_2017 = pd.read_csv('MICRODADOS_CADASTRO_CURSOS_2017.CSV', encoding="ISO-8859-1", sep=';', low_memory=False)

used_columns = [
    'NU_ANO_CENSO',
    'TP_ORGANIZACAO_ACADEMICA', 
    'NO_CINE_AREA_GERAL',
    'TP_GRAU_ACADEMICO',
    'TP_MODALIDADE_ENSINO',
    'QT_ING',
    'QT_MAT',
    'QT_CONC',
]

df_cursos_2021 = df_cursos_2021[used_columns]
df_cursos_2020 = df_cursos_2020[used_columns]
df_cursos_2019 = df_cursos_2019[used_columns]
df_cursos_2018 = df_cursos_2018[used_columns]
df_cursos_2017 = df_cursos_2017[used_columns]

df_cursos_ead_2021 = df_cursos_2021.query('TP_MODALIDADE_ENSINO == 2')
df_cursos_ead_2020 = df_cursos_2020.query('TP_MODALIDADE_ENSINO == 2')
df_cursos_ead_2019 = df_cursos_2019.query('TP_MODALIDADE_ENSINO == 2')
df_cursos_ead_2018 = df_cursos_2018.query('TP_MODALIDADE_ENSINO == 2')
df_cursos_ead_2017 = df_cursos_2017.query('TP_MODALIDADE_ENSINO == 2')

df_cursos_ead_2021.to_csv('2021.csv')
df_cursos_ead_2020.to_csv('2020.csv')
df_cursos_ead_2019.to_csv('2019.csv')
df_cursos_ead_2018.to_csv('2018.csv')
df_cursos_ead_2017.to_csv('2017.csv')

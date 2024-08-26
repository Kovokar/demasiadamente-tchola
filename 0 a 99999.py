import datetime

# Nome do arquivo de saída
nome_arquivo = "datas_validas.txt"

# Função para verificar se a data é válida
def data_valida(dia, mes, ano):
    try:
        # Cria uma data com o formato dia, mês, ano
        datetime.datetime(year=ano, month=mes, day=dia)
        return True
    except ValueError:
        return False

# Abre o arquivo para escrita
with open(nome_arquivo, 'w') as arquivo:
    # Percorre todos os dias possíveis de 1 a 31
    for dia in range(1, 32):
        # Percorre todos os meses possíveis de 1 a 12
        for mes in range(1, 13):
            # Percorre os anos possíveis de 00 a 99
            for ano in range(0, 100):
                # Verifica se a data é válida
                if data_valida(dia, mes, 1900 + ano):  # Aqui ano de 1900 a 1999 (ex: 97 -> 1997)
                    # Formata o dia, mês e ano com dois dígitos cada
                    data_formatada = f"{dia:02d}{mes:02d}{ano:02d}"
                    # Escreve a data no arquivo
                    arquivo.write(data_formatada + '\n')

print(f"Arquivo '{nome_arquivo}' criado com sucesso.")

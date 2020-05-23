import re
from collections import Counter


def extract_executions_count(file_path: str):
    """
    Recupera as informações de submissões, testes e erros do arquivo de 'log' das tentativas de solução de um exercício.

    :param file_path: Caminho absoluto do arquivo de 'log' com as informações das execuções feitas pelo estudante.
    :type file_path: str
    """
    # lista que irá receber o nome de todos os erros encontrados no arquivo de log
    error_names = []
    with open(file_path, 'r') as f:

        # contadores
        n_submissoes = 0
        n_testes = 0
        n_erros = 0
        nota_final = 0.0

        # indice da linha atual no arquivo de log
        i = 0
        lines = f.readlines()
        size = len(lines)

        while i < size:
            # se a seção do arquivo for refente a uma submissão
            if lines[i].startswith('== S'):
                # flag de parada (quando o estudante acertar o exercícios, submissão for correta)
                acertou = False
                n_submissoes += 1
                i += 1
                # continua percorrendo o arquivo enquanto a sessão de 'submissão' não terminar
                while not lines[i].startswith('*-*'):
                    # se a linha atual do arquivo corresponde ao início da subsessão 'GRADE'
                    if lines[i].startswith('-- GRAD'):
                        # a nota obtida na submissão encontra-se na linha seguinte
                        value = lines[i + 1].strip()[:-1]
                        # tenta obter a nota da submissão, em caso de erro adota-se nota zero
                        try:
                            nota_final = float(value)
                        except Exception:
                            nota_final = 0.0
                        i += 2
                    elif lines[i].startswith('-- ERROR'):
                        n_erros += 1
                        i += 2
                        # percorre cada linha da subseção 'ERROR' buscando pelo nome do erro
                        while not lines[i].startswith('*-*'):
                            m = re.match(r"^([\w_\.]+Error)", lines[i])
                            # se encontrou um erro, seu nome é adicionado a lista de erros
                            if m:
                                error_names.append(m.group(0))
                            i += 1
                    else:
                        i += 1
                # ao finalizar a seção de submissão, verifico se o aluno acertou a questão
                if nota_final > 99.99:
                    i = size + 1
            # se a seção do arquivo for refente a um teste
            elif lines[i].startswith('== T'):
                n_testes += 1
                # percorre toda as seção de teste
                while not lines[i].startswith('*-*'):
                    # se encontrar uma subseção 'ERROR's
                    if lines[i].startswith('-- ERROR'):
                        n_erros += 1
                        i += 2
                        # percorre cada linha da subseção 'ERROR' buscando pelo nome do erro
                        while not lines[i].startswith('*-*'):
                            m = re.match(r"^([\w_\.]+Error)", lines[i])
                            # se encontrou um erro, seu nome é adicionado a lista de erros
                            if m:
                                error_names.append(m.group(0))
                            i += 1
                    else:
                        i += 1
            i += 1

    # se houveram erros, faz a contagem da ocorrência de erros
    erros = []
    if len(error_names):
        c = Counter(error_names)
        for name in c.keys():
            erros.append((name, c[name]))

    return n_submissoes, n_testes, n_erros, nota_final, erros

# preencha com o caminho absoluto para o arquivo de código
path = '...'

sub, test, err, nota, erros = extract_executions_count(path)
print('-- Informações extraídas --')
print(f'Nº de submissões feitas: {sub}')
print(f'Nota final: {nota:.2f}')
print(f'Nº de testes feitos: {test}')
print(f'Nº de erros encontrados: {err}')
for erro, count in erros:
    print(f'\t{erro}: {count}')


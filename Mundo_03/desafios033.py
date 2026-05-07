def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['média'] = sum(notas) / len(notas)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif 6 <= r['média'] < 7:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

print(notas(8.5, 4.5, 9.5, sit=True))

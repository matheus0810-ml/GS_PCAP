"""
Global Solution 2026.1
Disciplina: Pensamento Computacional e Automação com Python
Projeto: Mission Control AI - Sistema Inteligente de Monitoramento de Missão Espacial

Aluno: Matheus Carpinheiro Moreno
RM: 571770
Turma: 1CCPX
Trabalho individual
"""

# Identificação da missão
nome_missao = "Aurora 571770"
nome_equipe = "Equipe Polaris"

# Cada linha representa um ciclo:
# [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_missao = [
    [23, 95, 90, 97, 92],
    [28, 82, 74, 94, 84],
    [32, 68, 60, 91, 72],
    [37, 54, 44, 86, 58],
    [40, 25, 16, 76, 32],
    [33, 62, 35, 84, 60]
]

# Lista relacionada às cinco colunas da matriz dados_missao
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]


def analisar_temperatura(temperatura):
    """Classifica a temperatura e retorna classificação, risco e mensagem."""
    if temperatura < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do recomendado"
    elif temperatura <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif temperatura <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(comunicacao):
    """Classifica a qualidade da comunicação."""
    if comunicacao < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif comunicacao < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(bateria):
    """Classifica o nível da bateria."""
    if bateria < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif bateria < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(oxigenio):
    """Classifica o nível de oxigênio."""
    if oxigenio < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif oxigenio < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(estabilidade):
    """Classifica a estabilidade operacional."""
    if estabilidade < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif estabilidade < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


def classificar_ciclo(pontuacao):
    """Classifica um ciclo de acordo com sua pontuação total de risco."""
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(resultados, classificacao_ciclo):
    """Gera uma recomendação automática com base nas áreas afetadas."""
    classificacoes = [resultado[0] for resultado in resultados]

    if classificacao_ciclo == "MISSÃO ESTÁVEL":
        if "ATENÇÃO" in classificacoes:
            return "Acompanhar os sistemas em atenção e continuar o monitoramento."
        return "Manter a operação normal e continuar o monitoramento."

    if classificacao_ciclo == "MISSÃO CRÍTICA":
        if classificacoes.count("CRÍTICO") >= 3:
            return (
                "Ativar o protocolo de segurança e priorizar suporte à vida, "
                "energia, comunicação e estabilidade."
            )

    if resultados[0][0] == "CRÍTICO":
        return "Verificar imediatamente o sistema de controle térmico."
    if resultados[1][0] == "CRÍTICO":
        return "Tentar restabelecer o contato com a base."
    if resultados[2][0] == "CRÍTICO":
        return "Ativar o modo de economia de energia."
    if resultados[3][0] == "CRÍTICO":
        return "Acionar o protocolo de suporte à vida."
    if resultados[4][0] == "CRÍTICO":
        return "Reduzir operações não essenciais e estabilizar o módulo."

    return "Monitorar os sistemas em atenção e preparar um plano de contingência."


def analisar_ciclo(ciclo):
    """Analisa as cinco informações de um ciclo."""
    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    resultados = [
        analisar_temperatura(temperatura),
        analisar_comunicacao(comunicacao),
        analisar_bateria(bateria),
        analisar_oxigenio(oxigenio),
        analisar_estabilidade(estabilidade)
    ]

    pontuacao_total = 0
    riscos_por_area = []

    for resultado in resultados:
        pontuacao_total += resultado[1]
        riscos_por_area.append(resultado[1])

    classificacao = classificar_ciclo(pontuacao_total)
    recomendacao = gerar_recomendacao(resultados, classificacao)

    return resultados, pontuacao_total, riscos_por_area, classificacao, recomendacao


def analisar_tendencia(riscos_ciclos):
    """Compara o risco do primeiro ciclo com o risco do último ciclo."""
    risco_inicial = riscos_ciclos[0]
    risco_final = riscos_ciclos[-1]

    if risco_final > risco_inicial:
        return "A missão apresentou tendência de piora."
    elif risco_final < risco_inicial:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontuacao_areas):
    """Identifica a área com maior pontuação acumulada de risco."""
    maior_pontuacao = max(pontuacao_areas)
    indice_area = pontuacao_areas.index(maior_pontuacao)
    return areas_monitoradas[indice_area], maior_pontuacao


def gerar_conclusao(classificacao_final, tendencia):
    """Produz uma conclusão geral para o relatório final."""
    if classificacao_final == "MISSÃO ESTÁVEL":
        return (
            "A missão apresentou condições gerais estáveis. "
            "O monitoramento deve continuar para prevenir novos riscos."
        )

    if classificacao_final == "MISSÃO EM ATENÇÃO":
        if "piora" in tendencia:
            return (
                "A missão apresentou instabilidade relevante e tendência de piora. "
                "A equipe deve manter o plano de contingência ativo."
            )
        return (
            "A missão apresentou sistemas em atenção. "
            "A equipe deve acompanhar as áreas afetadas e manter medidas preventivas."
        )

    return (
        "A missão apresentou risco operacional elevado. "
        "A equipe deve ativar os protocolos de segurança e priorizar os sistemas críticos."
    )


def gerar_relatorio_final(riscos_ciclos, pontuacao_areas, classificacoes_ciclos):
    """Calcula as médias e exibe o relatório final da missão."""
    quantidade_ciclos = len(dados_missao)

    soma_temperatura = 0
    soma_comunicacao = 0
    soma_bateria = 0
    soma_oxigenio = 0
    soma_estabilidade = 0

    for ciclo in dados_missao:
        soma_temperatura += ciclo[0]
        soma_comunicacao += ciclo[1]
        soma_bateria += ciclo[2]
        soma_oxigenio += ciclo[3]
        soma_estabilidade += ciclo[4]

    media_temperatura = soma_temperatura / quantidade_ciclos
    media_comunicacao = soma_comunicacao / quantidade_ciclos
    media_bateria = soma_bateria / quantidade_ciclos
    media_oxigenio = soma_oxigenio / quantidade_ciclos
    media_estabilidade = soma_estabilidade / quantidade_ciclos

    maior_risco = max(riscos_ciclos)
    ciclo_mais_critico = riscos_ciclos.index(maior_risco) + 1
    risco_medio = sum(riscos_ciclos) / quantidade_ciclos
    quantidade_criticos = classificacoes_ciclos.count("MISSÃO CRÍTICA")

    tendencia = analisar_tendencia(riscos_ciclos)
    area_mais_afetada, maior_pontuacao_area = identificar_area_mais_afetada(
        pontuacao_areas
    )
    classificacao_final = classificar_ciclo(risco_medio)
    conclusao = gerar_conclusao(classificacao_final, tendencia)

    print("\n" + "=" * 68)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 68)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {quantidade_ciclos}")
    print(f"Média de temperatura: {media_temperatura:.2f} °C")
    print(f"Média de comunicação: {media_comunicacao:.2f}%")
    print(f"Média de bateria: {media_bateria:.2f}%")
    print(f"Média de oxigênio: {media_oxigenio:.2f}%")
    print(f"Média de estabilidade: {media_estabilidade:.2f}%")
    print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {quantidade_criticos}")
    print(f"Tendência da missão: {tendencia}")

    print("\nPontuação acumulada por área:")
    for indice in range(len(areas_monitoradas)):
        print(f"- {areas_monitoradas[indice]}: {pontuacao_areas[indice]} pontos")

    print(f"\nÁrea mais afetada: {area_mais_afetada}")
    print(f"Pontuação da área mais afetada: {maior_pontuacao_area}")
    print(f"Classificação final da missão: {classificacao_final}")
    print(f"Conclusão: {conclusao}")


def executar_missao():
    """Percorre os ciclos, mostra as análises e gera o relatório final."""
    print("=" * 68)
    print("MISSION CONTROL AI")
    print("=" * 68)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print("Integrante: Matheus Carpinheiro Moreno - RM 571770")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 68)

    riscos_ciclos = []
    pontuacao_areas = [0, 0, 0, 0, 0]
    classificacoes_ciclos = []

    for indice in range(len(dados_missao)):
        ciclo = dados_missao[indice]

        resultados, risco_total, riscos_area, classificacao, recomendacao = (
            analisar_ciclo(ciclo)
        )

        riscos_ciclos.append(risco_total)
        classificacoes_ciclos.append(classificacao)

        for posicao in range(len(pontuacao_areas)):
            pontuacao_areas[posicao] += riscos_area[posicao]

        print(f"\nCICLO {indice + 1}")
        print("-" * 68)
        print(
            f"Temperatura: {ciclo[0]} °C | "
            f"{resultados[0][0]} | {resultados[0][2]}"
        )
        print(
            f"Comunicação: {ciclo[1]}% | "
            f"{resultados[1][0]} | {resultados[1][2]}"
        )
        print(
            f"Bateria: {ciclo[2]}% | "
            f"{resultados[2][0]} | {resultados[2][2]}"
        )
        print(
            f"Oxigênio: {ciclo[3]}% | "
            f"{resultados[3][0]} | {resultados[3][2]}"
        )
        print(
            f"Estabilidade: {ciclo[4]}% | "
            f"{resultados[4][0]} | {resultados[4][2]}"
        )
        print(f"Pontuação de risco do ciclo: {risco_total}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")

    gerar_relatorio_final(
        riscos_ciclos,
        pontuacao_areas,
        classificacoes_ciclos
    )


# Início do programa
if __name__ == "__main__":
    executar_missao()

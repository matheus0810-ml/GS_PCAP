# Mission Control AI

Sistema inteligente de monitoramento de uma missão espacial experimental, desenvolvido para a Global Solution 2026.1 da disciplina **Pensamento Computacional e Automação com Python**.

## Identificação

- **Aluno:** Matheus Carpinheiro Moreno
- **RM:** 571770
- **Turma:** 1CCPX
- **Curso:** Ciência da Computação - 1º semestre
- **Instituição:** FIAP
- **Trabalho:** Individual
- **Nome da missão:** Aurora 571770
- **Nome da equipe:** Equipe Polaris

## Objetivo

O projeto simula seis ciclos de uma missão espacial. Em cada ciclo, são analisados:

1. temperatura interna;
2. comunicação com a base;
3. bateria;
4. oxigênio;
5. estabilidade operacional.

O programa classifica cada informação como **NORMAL**, **ATENÇÃO** ou **CRÍTICO**, calcula a pontuação de risco de cada ciclo, identifica a tendência da missão, determina a área mais afetada e apresenta um relatório final no terminal.

## Estrutura dos dados

A matriz principal segue a ordem obrigatória:

```python
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

A matriz usada no projeto possui seis ciclos:

```python
dados_missao = [
    [23, 95, 90, 97, 92],
    [28, 82, 74, 94, 84],
    [32, 68, 60, 91, 72],
    [37, 54, 44, 86, 58],
    [40, 25, 16, 76, 32],
    [33, 62, 35, 84, 60]
]
```

## Regras de classificação

### Temperatura

- menor que 18 °C: ATENÇÃO;
- de 18 °C até 30 °C: NORMAL;
- maior que 30 °C até 35 °C: ATENÇÃO;
- maior que 35 °C: CRÍTICO.

### Comunicação

- menor que 30%: CRÍTICO;
- de 30% até 59%: ATENÇÃO;
- 60% ou mais: NORMAL.

### Bateria

- menor que 20%: CRÍTICO;
- de 20% até 49%: ATENÇÃO;
- 50% ou mais: NORMAL.

### Oxigênio

- menor que 80%: CRÍTICO;
- de 80% até 89%: ATENÇÃO;
- 90% ou mais: NORMAL.

### Estabilidade

- menor que 40%: CRÍTICO;
- de 40% até 69%: ATENÇÃO;
- 70% ou mais: NORMAL.

## Pontuação de risco

- NORMAL = 0 ponto;
- ATENÇÃO = 1 ponto;
- CRÍTICO = 2 pontos.

A classificação de cada ciclo é feita pela soma dos cinco indicadores:

- 0 a 2 pontos: MISSÃO ESTÁVEL;
- 3 a 5 pontos: MISSÃO EM ATENÇÃO;
- 6 a 10 pontos: MISSÃO CRÍTICA.

## Funcionalidades

O sistema:

- percorre os seis ciclos usando estruturas de repetição;
- analisa os cinco indicadores de cada ciclo;
- gera mensagens e recomendações automáticas;
- calcula a pontuação de risco por ciclo;
- classifica cada ciclo;
- calcula as médias dos indicadores;
- identifica o ciclo mais crítico;
- calcula o risco médio;
- conta os ciclos críticos;
- compara o primeiro e o último ciclo;
- identifica a tendência da missão;
- soma o risco acumulado de cada área;
- identifica a área mais afetada;
- exibe um relatório final no terminal.

## Funções principais

- `analisar_temperatura()`
- `analisar_comunicacao()`
- `analisar_bateria()`
- `analisar_oxigenio()`
- `analisar_estabilidade()`
- `classificar_ciclo()`
- `gerar_recomendacao()`
- `analisar_ciclo()`
- `analisar_tendencia()`
- `identificar_area_mais_afetada()`
- `gerar_conclusao()`
- `gerar_relatorio_final()`
- `executar_missao()`

## Como executar

1. Tenha o Python 3 instalado.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python mission_control.py
```

O relatório será mostrado diretamente no terminal.

## Estrutura do repositório

```text
mission-control-ai/
├── README.md
└── mission_control.py
```

O arquivo `entrega_fiap.txt` foi preparado separadamente para o envio no portal da FIAP. Antes da entrega, substitua o campo do link pelo endereço público do repositório.

## Tecnologias utilizadas

- Python 3
- listas
- matriz representada por lista de listas
- funções
- estruturas condicionais
- estruturas de repetição
- operadores aritméticos e relacionais

## Observação

O projeto utiliza dados simulados fixos e regras lógicas. Não utiliza bibliotecas externas, interface gráfica ou aprendizado de máquina.

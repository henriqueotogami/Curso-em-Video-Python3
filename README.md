# Curso em Vídeo - Python 3

> Repositório com soluções dos desafios das aulas de Python 3 do canal [Curso em Vídeo](https://www.cursoemvideo.com/), com exercícios práticos de programação em Python.

## 📋 Sobre o Projeto

Este projeto reúne os códigos desenvolvidos durante o acompanhamento do curso de Python 3 do Curso em Vídeo. Os arquivos estão organizados por número de desafio e cobrem desde operadores aritméticos e entrada/saída de dados até análise de textos, condicionais, estruturas de repetição e conversão entre sistemas numéricos. O objetivo é documentar o progresso e servir como material de consulta e estudo.

## 📁 Estrutura do Projeto

### Desafios (`Henrique/`)

Os arquivos seguem o padrão `Python3-Desafio-NNN.py`, em que `NNN` é o número do desafio (com três dígitos).

- **Python3-Desafio-005.py** a **Python3-Desafio-036.py** — Desafios concluídos (operadores aritméticos, strings, condicionais, etc.)
- **Python3-Desafio-037.py** — Conversor de sistema numérico (decimal para binário e hexadecimal)
- **Python3-Desafio-038.py** a **Python3-Desafio-100.py** — Desafios previstos no curso (a serem implementados)

## 📂 Estrutura do repositório

```
LICENSE
README.md
Henrique/
  Python3-Desafio-005.py   # número anterior e posterior
  Python3-Desafio-006.py   # potência e raiz quadrada
  Python3-Desafio-007.py   # média aritmética
  Python3-Desafio-008.py   # conversor metros → cm e mm
  Python3-Desafio-009.py   # tabuada
  Python3-Desafio-010.py   # conversor real → dólar
  ...                     # demais desafios (011 a 036)
  Python3-Desafio-037.py   # conversor decimal → binário/hexadecimal
  # Python3-Desafio-038.py a 100 — a implementar
```

## 🛠️ Tecnologias Utilizadas

- **Python 3** — Linguagem de programação utilizada em todos os desafios
- **Ambiente** — Código compatível com interpretador Python 3.x (terminal ou IDE como VS Code)

## 📝 Funcionalidades Principais

- **Operadores aritméticos** — Soma, subtração, potência, raiz, média, conversões (moeda, temperatura, unidades)
- **Strings** — Análise de texto, contagem de letras, verificação de substrings, primeiro e último nome
- **Condicionais** — Par/ímpar, multa por velocidade, ano bissexto, triângulo, financiamento
- **Números aleatórios** — Sorteio de alunos
- **Trigonometria** — Hipotenusa, seno, cosseno, tangente
- **Sistemas numéricos** — Conversão decimal para binário e hexadecimal (Desafio 037)

## 🚀 Como Executar

### Pré-requisito

- [Python 3](https://www.python.org/downloads/) instalado no sistema.

### Via terminal (Linux / macOS)

```bash
# Na raiz do projeto, execute um desafio específico
python3 Henrique/Python3-Desafio-005.py

# Ou a partir da pasta Henrique/
cd Henrique
python3 Python3-Desafio-005.py
```

### Via terminal (Windows)

```cmd
python Henrique\Python3-Desafio-005.py
```

### Em ambiente gráfico (VS Code, PyCharm, etc.)

Abra o arquivo `.py` desejado e execute com o botão de execução ou atalho configurado no editor.

## 📚 Conteúdos Abordados

- ✅ Operadores aritméticos e expressões
- ✅ Entrada e saída de dados (`input`, `print`, `format`)
- ✅ Tipos de dados (int, float, str)
- ✅ Estruturas condicionais (`if`, `else`, `elif`)
- ✅ Módulos (`math`, `random`)
- ✅ Manipulação de strings (índices, fatiamento, métodos)
- ✅ Estruturas de repetição (a serem reforçadas nos próximos desafios)
- ✅ Conversão entre sistemas numéricos (binário, hexadecimal)

## 📋 Lista de Desafios

### Desafios concluídos

- [x] **Desafio 005** - Operadores Aritméticos - Número posterior e antecessor
- [x] **Desafio 006** - Operadores Aritméticos - Potência e raiz quadrada
- [x] **Desafio 007** - Operadores Aritméticos - Média aritmética de notas
- [x] **Desafio 008** - Operadores Aritméticos - Conversor de metros para cm e mm
- [x] **Desafio 009** - Operadores Aritméticos - Tabuada
- [x] **Desafio 010** - Operadores Aritméticos - Conversor Real para Dólar
- [x] **Desafio 011** - Operadores Aritméticos - Cálculo de área
- [x] **Desafio 012** - Operadores Aritméticos - Cálculo de desconto
- [x] **Desafio 013** - Operadores Aritméticos - Reajuste de salário
- [x] **Desafio 014** - Operadores Aritméticos - Conversor Celsius para Fahrenheit
- [x] **Desafio 015** - Operadores Aritméticos - Locação de veículo (dias e km)
- [x] **Desafio 016** - Operadores Aritméticos - Raiz quadrada (arredondamento)
- [x] **Desafio 017** - Operadores Aritméticos - Hipotenusa
- [x] **Desafio 018** - Operadores Aritméticos - Seno, cosseno e tangente
- [x] **Desafio 019** - Sorteio aleatório de alunos
- [x] **Desafio 020** - Sorteio aleatório de alunos (ordem)
- [x] **Desafio 021** - Analisador de textos - Contador de letras do nome
- [x] **Desafio 022** - Analisador de textos - Contador de letras do nome
- [x] **Desafio 023** - Separador de dígitos (unidade, dezena, centena, milhar)
- [x] **Desafio 024** - Analisador de textos - Nasceu em Santos?
- [x] **Desafio 025** - Analisador de textos - Nome tem Silva?
- [x] **Desafio 026** - Analisador de textos - Primeira e última ocorrência em string
- [x] **Desafio 027** - Analisador de textos - Primeiro e último nome
- [x] **Desafio 028** - Jogo da adivinhação v1.0
- [x] **Desafio 029** - Radar eletrônico - Cálculo de multa
- [x] **Desafio 030** - Número par ou ímpar
- [x] **Desafio 031** - Custo da viagem por distância (km)
- [x] **Desafio 032** - Verificador de ano bissexto
- [x] **Desafio 033** - Maior e menor número
- [x] **Desafio 034** - Cálculo de aumento de salário
- [x] **Desafio 035** - Triângulo (três medidas)
- [x] **Desafio 036** - Liberação de financiamento imobiliário
- [x] **Desafio 037** - Conversor de sistema numérico (decimal → binário e hexadecimal)

### Desafios a fazer

- [ ] **Desafio 038** a **Desafio 100** — A serem implementados conforme o curso

## ⚙️ Como funciona

Cada arquivo em `Henrique/` é um script Python independente. Ao executar, o programa geralmente:

1. Exibe um título ou número do desafio
2. Solicita entradas ao usuário (`input`)
3. Processa os dados (cálculos, strings, condicionais)
4. Exibe o resultado com `print`

Não é necessário instalar pacotes extras para os desafios já presentes no repositório; apenas o Python 3 padrão é utilizado.

## 📄 Licença

Este projeto está licenciado sob a MIT License — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📖 Referências

- [Curso em Vídeo - Python 3](https://www.cursoemvideo.com/course/curso-python-3/) — Curso gratuito de Python 3
- Código-fonte em `Henrique/Python3-Desafio-*.py` — Soluções dos desafios desenvolvidas ao longo do curso

---

### Hashtags

#Python #Python3 #CursoEmVideo #Programming #LearningToCode #Algorithm #ComputerScience #OpenSource #GitHub #CodeExamples #BeginnerProgramming #ExerciciosPython #DesafiosPython

### Meta Keywords

```
Python 3, Curso em Vídeo, programação, desafios Python, operadores aritméticos,
strings, condicionais, entrada e saída, algoritmos, exercícios Python, aprender
programação, código exemplo, conversão numérica, binário, hexadecimal, código aberto
```

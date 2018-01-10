# Capítulo 2

## Números

Python 3, possui três tipos de números
* int:
    * Podem crescer até o tamanho da memória
    * Podem ser criados de diversas maneiras
        * num = 100
        * num = int(100)
        * num = int('100')
    * No Python 3 foram unificados os tipos int e long, até o Python 2 eram tipos diferentes

* float:
    * Depende do compilador
    * No CPython usa o tipo Double do C
    * No Jython usa o tipo flutuante de precisão dupla
    * Para criar é necessário o caracter ponto '.'
        * num = 5.2
        * num = float(5) #_5.0_
        * num = float('5.2')
        * Também aceita os valores nan e inf, positivo(+) ou negativo(-)

* complex:
    * Pouco utilizado no dia a dia
    * É composto por duas partes (imaginária e real) - ambos são do tipo float
    * Mais comum na engenharia e estatística
    * Para criar é necessário a letra j (jota minúsculo) ou J (jota maiúsculo) na expressão
        * num = 1+2j
        * num = 2J+3

## Operadores
* Adição (+)
    * num = 3 + 2
* Subtração (-)
    * num = 3 - 2
* Multiplicação (*)
    * num = 3 * 2
* Divisão (/)
    * num = 3 / 2
* Divisão Inteira (//)
    * num = 3 // 2
* Módulo (%)
    * num = 3 % 2
* Potenciação (**)
    * num = 3 ** 2
    * base ** expoente

## Operadores de bits
Não confundir com operadores lógicos, [veja aqui a explicação](https://imasters.com.br/desenvolvimento/conheca-os-operadores-bitwise-bit-bit/?trace=1519021197&source=single).
* E (&)
    * bit_ = 1 & 0
    * bit_ = 1 & 5
* OU (|)
    * bit_ = 1 | 0
    * bit_ = 1 | 5
* OU Exclusivo (^)
    * bit_ = 1 ^ 0
    * bit_ = 1 ^ 5
* Deslocamento a esquerda (<<)
    * bit_ = 1 << 5
* Deslocamento a direita (>>)
    * bit_ = 1 >> 5
* Inversão de bits (~)
    * bit_ = 1 ^ 0

## Coerção numérica
* int e float teremos como resultado um float
    * type(3 * 10.5)
* int ou float e número complexo teremos como resultado um número complexo
    * type (1 + 2j)
    * type(1.3 + 2j)

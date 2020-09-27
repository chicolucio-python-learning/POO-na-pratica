# Orientação a Objetos na Prática

Anotações do curso completo. As anotações do curso introdutório Raio-X da OOP está na pasta [raio_X_OOP](raio_X_OOP).

## O que existia antes da Orientação a Objetos?

Havia alto acoplamento entre a máquina e o código, não havia sistema operacional. Primeira estratégia foi a programação imperativa, onde havia quase nenhum reaproveitamento de comandos e todo o código via toda a memória. Depois veio a estratégia procedural:

### Programação procedural

- o código é uma foto, a partir da qual se tenta modelar o filme (código rodando)
- Programa engloba código + memória
    - GOTO
    - variáveis globais
    - reaproveitamento de comandos

```text
+-------------------------+
|         Programa        |
|                         |
| +---------------------+ |
| |                     | |
| |                     | |
| |       Código        | |
| |                     | |
| |                     | |
| +---------------------+ |
| +---------------------+ |
| |                     | |
| |                     | |
| |       Memória       | |
| |                     | |
| |                     | |
| +---------------------+ |
+-------------------------+
```
       
- Procedimentos são sequências de passos, não são funções.
    - antigamente se utilizava labels para referenciar e pular. Endereços de memória.
    - não há pilha de chamada, convenções
    - acoplamento entre chamador e chamado
    - problemas de reentrância, não há como chamar o mesmo procedimento concomitantemente
    - sempre tem etapa de setup: zerar variáveis
    
### Programação estruturada

- Programa engloba código + memória (engloba stack)
    - Bloco de código (BEGIN / END)
        - escopo de variável
    - pilha = seguimento de memória reservado
    - funções independentes
    - reentrância
    - recursividade
    - encadeamento de funções
    - ainda há variáveis globais

```text
+-------------------------+
|         Programa        |
|                         |
| +---------------------+ |
| |                     | |
| |       Código        | |
| |                     | |
| |                     | |
| +---------------------+ |
| +---------------------+ |
| |       Memória       | |
| | +-----------------+ | |
| | |                 | | |
| | |      Stack      | | |
| | |                 | | |
| | +-----------------+ | |
| +---------------------+ |
+-------------------------+
```
        
- O programador ainda tem a responsabilidade de como relacionar dados e código. Logo, há muitos IF e ELSE e switch cases. Daí surge a tipagem estática. Mas dificulta a relação entre trechos de código e a modularização, além de futuras expansões. *Early binding*: define os caminhos do código em tempo de compilação. 
        
### Programação orientada a objetos       

- Programa engloba código + memória (engloba stack e Heap)
    - dado associado ao código
    - Alocação dinâmica (*dynamic dispatch*)
        - dados instanciados
        - ponteiros para as rotinas certas        
    - processos
    - classe

```text
+-------------------------+
|         Programa        |
|                         |
| +---------------------+ |
| |                     | |
| |       Código        | |
| |                     | |
| +---------------------+ |
| +---------------------+ |
| |       Memória       | |
| | +-----------------+ | |
| | |      Stack      | | |
| | +-----------------+ | |
| | +-----------------+ | |
| | |       Heap      | | |
| | +-----------------+ | |
| +---------------------+ |
+-------------------------+
```
       
- Heap guarda valores anteriores das execuções, com referências para o código.
- Com o dynamic dispatch, não preciso mais definir o endereço de memória previamente.
    - Encontra-se a função com o nome de acordo com o contexto
      - base do polimorfismo
      - Natureza íntima entre código e dados
- Objetos não são dados e códigos juntos (embora pareça na prática)
    - são o processo em si
- Tentar evoluir para ter objetos que proveem serviços
    - além de /namespaces/

 Links para estudo:
 
 https://stackoverflow.com/questions/552336/oop-vs-functional-programming-vs-procedural
 
 https://en.wikipedia.org/wiki/Software_architecture
 
 https://en.wikipedia.org/wiki/Comparison_of_programming_paradigms
 
 https://softwareengineering.stackexchange.com/questions/117092/whats-the-difference-between-imperative-procedural-and-structured-programming
 

### A descoberta da essência da OOP

- O princípio básico de um design recursivo é fazer com que as partes tenham o mesmo poder que o todo. Bob Barton

Alan Kay:  http://worrydream.com/EarlyHistoryOfSmalltalk/

Arquitetura computacional de alto nível:

- software como abstração
- fácil acesso ao estado interna da máquina
- microcódigos mais expressivos
- suporte à múltiplas linguagens         

Referências:

https://www.youtube.com/watch?v=6orsmFndx_o

https://www.youtube.com/watch?v=B6rKUf9DWRI

https://squeak.org/

## Solucionando a complexidade

Cenários complexos: todo é maior que a soma das partes.

Busca por abstrações:

- Processo:
    - instruções de máquina
    - fórmulas
    - procedimentos
    - programação estruturada
    
- Dados:
    - endereços de memória
    - variáveis
    - estruturas de dados
    - tipos de dados abstratos
    
**Princípio da modularização**: se alguma parte do sistema depende das particularidades internas de outra parte, então a complexidade aumenta com o quadrado do tamanho do sistema. 
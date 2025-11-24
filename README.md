# MovieTree

## Aluno

| Matrícula | Nome                     |
| --------- | ------------------------ |
| 202017521 | Algusto Rodrigues Caldas |

## Descrição do projeto

O MovieTree é um sistema de demonstração que utiliza uma Árvore AVL para armazenar e gerenciar filmes em tempo real.
O projeto foi desenvolvido com foco didático, permitindo visualizar não apenas o funcionamento da árvore, mas também suas transformações internas.

A aplicação exibe informações estruturais completas da AVL, incluindo:

* Inserções detalhadas com log interativo no estilo "Árvore Viva", mostrando o caminho percorrido e rotações realizadas.
* Numeração dinâmica dos nós com base na estrutura da árvore (mapeamento heap-like), onde a raiz é identificada como [#1], seus filhos como [#2] e [#3], e assim sucessivamente.
* Busca aprimorada, exibindo o nó completo, seus ponteiros e sua posição estrutural.
* Listagem de filmes em ordem alfabética, incluindo o número do nó correspondente.

O sistema permite visualizar, de forma clara, como operações de rotação afetam a estrutura e a numeração dos nós, tornando-o ideal para apresentações, aulas e análise de algoritmos de árvores balanceadas.

## Guia de instalação

### Dependências do projeto

* Python 3.10 ou superior

### Como executar o projeto

```
python3 main.py
```

## Funcionalidades principais

### Inserção com log detalhado

A cada novo filme inserido, o sistema exibe:

* O caminho percorrido na AVL
* Indicação visual de direção (esquerda/direita)
* Local de inserção
* Rotações realizadas
* Numeração estrutural atualizada após a operação

### Busca com visualização completa do nó

A busca retorna:

* Título do filme com identificação de nó
* Ano
* Altura do nó
* Ponteiro esquerdo e direito indicando seus respectivos nós ou None

### Listagem ordenada

Exibe todos os filmes em ordem alfabética, acompanhados de:

* Número estrutural do nó
* Ano de lançamento

### Estatísticas da árvore

Inclui:

* Número total de nós
* Altura da árvore
* Fator de balanceamento da raiz

## Apresentação

[![Thumbnail do Vídeo](assets/thumb.png)](https://youtu.be/ieo48h7AEdw?si=QHVDBz-oMuxfcfW3)

## Conclusões

O projeto demonstra o funcionamento de uma Árvore AVL em tempo real, destacando como o balanceamento automático, associado à visualização detalhada da estrutura, contribui para a compreensão prática de árvores binárias balanceadas.
A atribuição dinâmica de índices estruturais reforça o entendimento sobre como rotações impactam a forma final da árvore, permitindo uma análise clara e direta do comportamento da AVL.

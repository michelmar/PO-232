# PO-232

## Teste de Isomorfismo de Weisfeiler-Lehman

![](img/graph_isomorphism.png)

Este projeto tem por objetivo implementar o algoritmo de Weisfeiler-Lehman para identificação de isomorfismo entre grafos.

## Iniciar Projeto

Esta seção tem por objetivo explicar como o projeto pode ser iniciado em uma máquina local.

### Pré-Requisitos

* [Python 3 e Pip](https://www.python.org/downloads/)
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Criando o Ambiente Virtual

> Nota: Não é obrigatório criar o ambiente virtual. Se quiser ir para a seção de instalação já é possível.

Antes de Iniciar o projeto é recomendado a criação de um ambiente virtual para o projeto python para evitar problemas de versionamento entre projetos python em uma mesma máquina.

Para criar o ambiente virtual, execute o comando:

```sh
$ conda create -n po232 python=3.X
```

### Uso do Ambiente



Sempre que quiser executar o projeto com o ambiente criado, basta seguir os passoa abaixo.

Abra o terminal e digite:

* Windows:

```sh
$ activate po232
```

* Linux/Mac:

```
$ source activate po232
```

### Instalação dos Pacotes

Para instalar todos os pacotes, execute o comando:

```sh
$ pip install -r requeriments.txt
```

Caso ocorra algum problema é possível executar manualmente os pacotes no arquivo `requeriments.txt`.

```sh
$ pip install PACKAGE_NAME
```

### Execução

Uma vez realizado o setup do ambiente, basta executar o comando abaixo para iniciar o projeto.

```
$ python test.py
```

<!-- ## Referências

* [The Weisfeiler-Lehman Isomorphism Test](https://davidbieber.com/post/2019-05-10-weisfeiler-lehman-isomorphism-test/)
* [Proof that Subgraph Isomorphism problem is NP-Complete](https://www.geeksforgeeks.org/proof-that-subgraph-isomorphism-problem-is-np-complete/)
* [Are these 2 graphs isomorphic?](https://math.stackexchange.com/questions/393416/are-these-2-graphs-isomorphic) -->

## Contribuidores

<table>
  <tr>
    <td align="center"><a href="https://github.com/michelmar"><img src="https://avatars.githubusercontent.com/u/60835138?v=4" width="100px;" alt=""/><br /><sub><b>Michel</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Matheus1714"><img src="https://avatars.githubusercontent.com/u/39354089?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Mota</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/andreiaio"><img src="https://avatars.githubusercontent.com/u/13735211?v=4" width="100px;" alt=""/><br /><sub><b>Andreia Kaori</b></sub></a><br /></td>
    
  </tr>
</table>
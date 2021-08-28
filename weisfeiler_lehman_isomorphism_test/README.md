# PO-232

## Teste de Isomorfismo de Weisfeiler-Lehman

![](img/graph_isomorphism.png)

Este projeto tem por objetivo implementar o algoritmo de Weisfeiler-Lehman para identificação de isomorfismo entre grafos.

## Arquitetura

O arquivo principal é o `main.py` no diretório raiz. A pasta `/src` é responsável por todo o desenvolvimento do código.

Como o código é de um modelo simplificado, a arquitetura usada foi baseada na MVC, como mostrado abaixo.

    .
    ├── /img/
    ├── /src/
    ├──── /model/
    ├──── /view/
    ├──── main.py 
    ├── /tests/
    ├── .gitignore
    ├── main.py
    ├── README.md
    ├── requirements.txt

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
$ python main.py
```

## Rodar Testes

Para rodar os testes do projeto basta executar:

```sh
$ python -m pytest
```

Caso ocorra algum problema de diretório, acesse a [documentação](https://docs.pytest.org/en/6.2.x/pythonpath.html) para mais informações.

## Contribuidores

<table>
  <tr>
    <td align="center"><a href="https://github.com/michelmar"><img src="https://avatars.githubusercontent.com/u/60835138?v=4" width="100px;" alt=""/><br /><sub><b>Michel</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Matheus1714"><img src="https://avatars.githubusercontent.com/u/39354089?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Mota</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/andreiaio"><img src="https://avatars.githubusercontent.com/u/13735211?v=4" width="100px;" alt=""/><br /><sub><b>Andreia Kaori</b></sub></a><br /></td>
    
  </tr>
</table>
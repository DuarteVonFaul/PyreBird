# PyBird 0.1.0

[![Active Development](https://img.shields.io/badge/Maintenance%20Level-Actively%20Developed-brightgreen.svg)](https://gist.github.com/cheerfulstoic/d107229326a01ff0f333a1d3476e068d)
![status](https://img.shields.io/badge/status-unstable-red.svg)![pyversions](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)

Uma experiencia de desenvolvimento de uma ORM para FireBird em Python
- **Versões FireBird**
  - 2.5.9(Unica testada)
  

## 1. Caracteristicas:

  * **Automap**
      * Faz mapeamento de todo o banco, de uma lista de tabelas, ou de uma tabela especifica
      * retorna esse mapeamento como uma classe
      
  * **Session**
      * Cria uma sessão de conexão com o banco

  * **CRUD**
      * Faz as requisições basicas no banco (Select, Insert, Update e Delete)
      * retorna o Select em formato de Dict
      * converter os tipos dos attrs aos seus respectivos tipos das colunas correspondentes
      * retorna a query em formato de str
   

## 2. Dependências:
   - **fdb==2.0.2**

## 3. Instalação:

## 4. Documentação:

## 5. Exemplo de uso:
  - **Connection**
          
          from pybird.orm.session     import Create_Session
          
          conn = Create_Session(  dsn='path/to/DATA.FDB',user='user',password='pass',charset='ANSI') 
          
  - **Select**
         
           from pybird.crud    import Select
           
           #Aqui ele retorna o primeiro item que retornar na requisição
           Select(conn,'Nome_da_Tabela').scalar()
           #Aqui ele retorna todos os itens que retornar na requisição
           Select(conn,'Nome_da_Tabela').all()
           #Aqui ele retorna o(s) itens filtrando pelos campos desejados
           Select(conn,'Nome_da_Tabela').filter_by( NOME_DA_COLUNA = VALOR).all()
           #Aqui ele retorna a query criada pela funcionalidade
           Select(conn,'Nome_da_Tabela').filter_by( NOME_DA_COLUNA = VALOR).return_query()
        

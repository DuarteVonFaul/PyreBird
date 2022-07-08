# PyBird 0.2.0

[![Active Development](https://img.shields.io/badge/Maintenance%20Level-Actively%20Developed-brightgreen.svg)](https://gist.github.com/cheerfulstoic/d107229326a01ff0f333a1d3476e068d)
![status](https://img.shields.io/badge/status-stable-brightgreen.svg)![pyversions](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)

Uma extensão para FDB que facilita a integração de um banco FireBird

- **Versões FireBird**
  - 2.5.9(Unica testada)
  

## 1. Caracteristicas:

  * **Automap**
      * Faz mapeamento de todo o banco, de uma lista de tabelas, ou de uma tabela especifica
      * retorna esse mapeamento como um schema
      
  * **Session**
      * Cria uma sessão de conexão com o banco

  * **PyBird**
      * Faz as requisições basicas no banco (Select, Insert, Update e Delete)
      * retorna o Select em formato de Objeto
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
  - **AutoMap**
    
    O AutoMap tem como funcionalidade Mapear as tabelas e criar schemas para serem usados nas consultas e nas criações de Objetos.
    
    Logo abaixo temos as funcionalidades Basicas do AutoMap
          from pybird.orm.ext.automap     import auto_map
          
          #Retorna o mapeamento de todas as tabelas
          Base = auto_map(conn).all()
          
          #Retorna o mapeamento de tabelas especificas
          Base = auto_map(conn).filter_by(['TB_PRODUTO','TB_VENDA','TB_PAGAMENTO'])
          
          #Recebe todo o schema da tabela produto
          ProdutoTabela = Base.get_class('TB_PRODUTO')
          
  - **Select**
         
           from pybird.select    import Select
           
           
        

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
  
    O create_session cria uma conexão para o banco de dados FireBird
          
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
   
    O Select tem varias funcionalidades intrínsecas a ela e o modelo basico para utilizar o Select é o seguinte
    
    *Select(Sessão,SchemaTabela,"Filtro de Campos").all()*
    
    Caso não preencher o campo *"Filtro de campos"* ele retorna todos as colunas como padrão
    
    **Funcionalidades:**
    
    - *all()* retorna todos os elementos
    - *only()* retorna o primeiro elemento encontrado
    - *filter_by(coluna = valor)* filtra a pesquisa por coluna e valor
    - *orden_by('coluna1',... )* retorna em ordem decrescente
    - *orden_by('coluna1',..., Keyword = "Asc" )* retorna em ordem crescente
    - *return_query()* retorna a SQLQuery em formato String
    
    abaixo temos alguns exemplos de como utilizar o Select
         
           from pybird.select    import Select
           
           #Retorna todos os elementos da tabela em formato de Objeto sendo seus campos os atributos com seus respectivos tipos
           query = Select(conn, ProdutoTabela).all()
           
           #Retorna todos os elementos da tabela em formato de Objeto sendo que apenas os campos informados retornados como 
           #atributos com seus respectivos tipos
           query = Select(conn, ProdutoTabela, "PRD_CODI, PRD_NOME, PRD_PREC, PRD_PESO").all()
           
           #Retorna todos os elementos da tabela com o nome Arroz em uma Lista de Objeto
           query = Select(conn, ProdutoTabela).filter_by(PRD_NOME = 'Arroz').all()
           
           #Retorna o primeiro elemento encontrado na tabela em formato de Objeto que contem o nome arroz
           query = Select(conn, ProdutoTabela).filter_by(PRD_NOME = 'Arroz').only()
           
           #Retorna todos os elementos da tabela com nome arroz em ordem decrescente em uma lista de Objeto
           query = Select(conn, ProdutoTabela).filter_by(PRD_NOME = 'Arroz').orden_by('PRD_CODI').all()
           
           #Retorna todos os elementos da tabela com nome arroz em ordem crescente em uma lista de Objeto
           query = Select(conn, ProdutoTabela).filter_by(PRD_NOME = 'Arroz').orden_by('PRD_CODI', Keyword = "Asc").all()
           
           #Não é aconselhável a utilização do metodo manual, mas ele te possibilita colocar manualmente uma linha SQL no comando
           query = Select(db,ProdutoTabela).manual('Order By PRD_CODI Desc').all()
           
           #Retorna a Query SQL em formato String
           query = Select(db,ProdutoTabela).manual('Order By PRD_CODI Desc').return_query()
    
    - **Insert**
      O Insert tem um modelo basico bem direto a ser seguido
      
      *Insert(Sessão, TabelaSchema).value(Coluna1 = valor1,...).execute()*
      
      como no Select o Insert também tem a funcionalidade *return_quert()*, logo abaixo vemos um exemplo de inserção na Tabela Vendas
      
      
           from pybird.insert    import Insert
           
           #Inserção de uma venda 
           Insert(db,TabelaVenda).values(   VDA_DATA    = str(date.today()),
                                            VDA_CDPRD   = product.PRD_CODI,
                                            VDA_PRECO   = product.PRD_PREC,
                                            VDA_QUANT   = int(Item.amount),
                                            VDA_TOTAL   = float(product.PRD_PREC) * float(Item.amount)).execute()
                                            
           #Retorna a query em formato String
           Insert(db,TabelaVenda).values(   VDA_DATA    = str(date.today()),
                                            VDA_CDPRD   = product.PRD_CODI,
                                            VDA_PRECO   = product.PRD_PREC,
                                            VDA_QUANT   = int(Item.amount),
                                            VDA_TOTAL   = float(product.PRD_PREC) * float(Item.amount)).return_quert()
           
           
           
           
           
        

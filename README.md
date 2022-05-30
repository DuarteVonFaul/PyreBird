# PyBird

Uma experiencia de desenvolvimento de uma ORM para FireBird em Python

## 1. Estrutura do Projeto:

O projeto está organizado nos seguintes arquivos:

  - **main.py:** onde faço os testes das implementações
  - **database.py:** padrão de arquivo extension
  - **util.py:** Metodos para conversão de tipos e dict
  - **pybird.py:** Funcionalidades geral da Biblioteca PyBird

## 2. Como Usar:
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
  

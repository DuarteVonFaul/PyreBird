


class Migration():




    __metadata__ = {"Tables":[]}
    __query__ = []

    @classmethod
    def __create_arq(cls):
        sttr = "{'Tables':["
        for table in cls.__metadata__['Tables']:
            for key, value in table.items():
                sttr += '\n{'
                sttr += f"'{key}': [\n"
                for field in table[key]:
                    sttr += str(field)
                    sttr += ',\n'
                    ...
                sttr += ']},'
        sttr += ']}'
        with open('./migrations/migrate.txt', 'w') as arq:
            arq.write(sttr)

    @classmethod
    def makeMigrations(cls, con):
        import ast

        cur = con.cursor()

        with open('./migrations/migrate.txt', 'r') as arq:
            text = arq.read().replace('\n', '')

        dic = ast.literal_eval(text)
        
        for table in dic['Tables']:
            sql = ''
            for key, value in table.items():
                sql += f'create table "{key}"  ('
                for field in table[key]:
                    for k, v in field.items():
                        if k != 'PrimaryKey' and k != 'NotNUll':
                            if field['PrimaryKey'] == True:
                                sql += f'{k.upper()} {v}  not null,'
                                sql += f' constraint "PK_{key}" primary key ("{k.upper()}") '
                                break
                            else:
                                sql += f', {k.upper()} {v}'
                                break
            sql += ");"
            print(sql)
            cur.execute(sql) 
        
        con.commit()

        
                        
                

            



 
        

    @classmethod
    def migrations(cls, *args):
        
        for table in args:
            #cls.__query__.append(f'{table.create_query()}')
            cls.__create_migrations(table)
        ...
        cls.__create_arq()
        return cls

    @classmethod
    def __create_migrations(cls, field):
        import os
        
        name = field.return_name()
        list = field.__dict__
        try:
            os.mkdir('./migrations')
        except:
            ...

        table = {str(name):[]}
        for key in list:
            if key[:2] != '__':
                table[name].append({key:list[key]['Type'],
                                   'PrimaryKey':list[key]['PrimaryKey'],
                                   'NotNUll':list[key]['NotNUll']})
                
            ...
        
        cls.__metadata__['Tables'].append(table)



            

        
        
    
    
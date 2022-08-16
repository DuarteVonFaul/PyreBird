

class Migration():

    @classmethod
    def __create_arq(cls, dic):
        sttr = "{'Tables':{\n"
        for key, value in dic.items():
            sttr += "\t"
            sttr += f"'{str(key)}':"
            sttr += "{\n"
            for k in value:
                if k != 'Operation':
                    sttr += f"\t\t'{k}':"
                    sttr += '{'
                    sttr += f"'Type' : '{value[k]['Type']}', "
                    sttr += f"'PrimaryKey': {value[k]['PrimaryKey']}, "
                    sttr += f"'NotNULL': {value[k]['NotNULL']}, "
                    sttr += f"'Operation': {value[k]['Operation']} "
                    sttr += '},\n'
                else:
                    sttr += f"\t\t'Operation': '{value[k]}'"
                    sttr += '},\n'
                ...
            ...
        ...
        sttr += '}}'
        with open('./migrations/migrate.txt', 'w') as arq:
            arq.write(sttr)


    @classmethod
    def makeMigrations(cls, con):
        import ast

        cur = con.cursor()

        with open('./migrations/migrate.txt', 'r') as arq:
            text = arq.read().replace('\n', '').replace('\t', '')

        dcct = ast.literal_eval(text)['Tables']
        
        for key, value in dcct.items():
            if value['Operation'] == 'Create':
                value['Operation'] = 'None'
                sql = f'create table "{key}"  ('
                for k in value:
                    if k != 'Operation':
                        value[k]['Operation'] = 'None'
                        sql += str(f'{k.upper()} {value[k]["Type"]}')
                        if value[k]['NotNULL'] == True:
                            sql += ' not null,'
                        else:
                            sql += ','
                        if value[k]['PrimaryKey'] == True:
                            sql += f' constraint "PK_{key}" primary key ("{k.upper()}"),'    
                        ...
                per = True
                sql = sql[:len(sql) - 1] + f');'
            elif value['Operation'] == 'Update':
                sql = f'ALTER TABLE "{key}" ADD '
                for k in value:
                    if k != 'Operation':
                        if value[k]['Operation'] == 'Create':
                            value[k]['Operation'] = 'None'
                            sql += f'{k} {value[k]["Type"]}'
                            if value[k]['NotNULL'] == True:
                                sql += ' not null,'
                            print(sql)
                        
                        ...
                            
                per = True
            else:
                per = False
            
            
            if per:
                cur.execute(sql)
        if per:
            con.commit()
            cls.__create_arq(dcct)
    ...  
                        

    @classmethod
    def migrations(cls, *args):
        import ast
        sttr = ""
        try:
            with open('./migrations/migrate.txt', 'r') as arq:
                text = arq.read().replace('\n', '').replace('\t', '')
                dic = ast.literal_eval(text)['Tables']
                
        except:
            open('./migrations/migrate.txt', 'w')
            dic = {}
        i = 0
        for table in args:
            #cls.__query__.append(f'{table.create_query()}')
            if i == 0:
                sttr = cls.__create_migrations(table, dic)
            else:
                sttr.update(cls.__create_migrations(table, dic))
            i+= 1
        ...
        cls.__create_arq(sttr)
        return 

    @classmethod
    def __create_migrations(cls, field, dic):
        import os

        name = field.return_name()
        list = field.__dict__
        try:
            os.mkdir('./migrations')
        except:
            ...
        if name in dic :
            for key in list:
                if key[:2] != '__':
                    if key in dic[name]: 
                        per = False
                    else:
                        dic[name][key] = {
                            'Type':list[key]['Type'],
                            'PrimaryKey':list[key]['PrimaryKey'],
                            'NotNULL':list[key]['NotNUll'], 
                            'Operation': "'Create'" 
                        } 
                        per = True
            if per:
                dic[name]['Operation']= 'Update'
            else:
                dic[name]['Operation']= 'None'
        else:
            dic[name] = {}
            for key in list:
                if key[:2] != '__':
                    dic[name][key] = {
                            'Type':list[key]['Type'],
                            'PrimaryKey':list[key]['PrimaryKey'],
                            'NotNULL':list[key]['NotNUll'], 
                            'Operation': "'Create'" 
                    } 
            dic[name]['Operation']= 'Create'
 
        return dic



            

        
        
    
    
# -*- coding: utf-8 -*-

def create_engine(user,password,database,host='127.0.0.1',port=3306,**kw):

    params = dict(user=user, password=password, database=database, host=host, port=port)
    print params
    defaults = dict(use_unicode=True,charset='utf8',collation='utf8_general_ci',autocommit=False)
    for k,v in defaults.iteritems():
        #params[k] = kw.pop(k,v)
        params[k] = defaults[k]
        #print kw.pop(k,v)

        params.update(kw)
        params['buffered'] = True


    print params
if __name__ == "__main__":
    create_engine('root', 'root', 'test', '127.0.0.1')
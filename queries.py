import psycopg2

conn = psycopg2.connect(dbname='coins', user='postgres', password='QklbYm')
conn.autocommit = True
cur = conn.cursor()


def query_func(q_num):
	queries = ['select name from euro_countries', 'select value from euro_coins_table order by id', 
	'select name from euro_countries where national_side = True']
	cur.execute(queries[q_num])
	answer = cur.fetchall()
	return answer

def complex_query_func(q_num, c_name, c_value):
	queries = ["select * from select_coin_func('{}') where coin_value = '{}'"]
	cur.execute(queries[q_num].format(c_name, c_value))
	answer = cur.fetchall()
	return answer

def complex_query_func_insert(c_name, c_value, n_side):
	queries = ["insert_coin_func('{}', '{}', '{}')"]
	cur.execute(queries.format(c_name, c_value, n_side))	
	return ('OK')
	
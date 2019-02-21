import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import psycopg2

conn = psycopg2.connect(dbname='coins', user='postgres', password='QklbYm')
conn.autocommit = True
cur = conn.cursor()


def query_func(q_num):
	queries = ['select name from euro_countries', 'select value from euro_coins_table']
	cur.execute(queries[q_num])
	answer = cur.fetchall()
	return answer

def complex_query_func(q_num, c_name, c_value):
	queries = ["select * from select_coin_func('{}') where coin_value = '{}'"]
	cur.execute(queries[q_num].format(c_name, c_value))
	answer = cur.fetchall()
	return answer

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
	html.H3('Search'),

	dcc.Dropdown(
		id ='country_dropdown',
		options=[{'label': i[0], 'value': i[0]} for i in query_func(0)],
		value='Finland'),

	html.Br(), 

	dcc.Dropdown(
	id ='coin_dropdown',
	options=[{'label': i[0], 'value': i[0]} for i in query_func(1)],
	value='2 euro'),

	html.Div(id='first_output'),

	html.Br(), 

	html.H3('Add new'),

	html.Br(), 

	html.H3('Change status')

	])



@app.callback(
	Output('first_output', 'children'),
	[Input('country_dropdown', 'value'), Input('coin_dropdown', 'value'),])
def update_output(country_dropdown, coin_dropdown):
	answer = complex_query_func(0, country_dropdown, coin_dropdown)
	if answer != []:
		return ('Answer: ', str(answer))
	else:
		return ('No results')	

if __name__ == '__main__':
	app.run_server(debug=True)





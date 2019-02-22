import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from queries import query_func, complex_query_func, complex_query_func_insert


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config['suppress_callback_exceptions']=True
app.layout = html.Div([

    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Search', value='tab-1'),
        dcc.Tab(label='Add new', value='tab-2'),
        dcc.Tab(label='Change status', value='tab-3'),
    ]),
    html.Div(id='tabs-content')

	])


search_layout = html.Div([
	html.H3('Search coin in the database'),

	dcc.Dropdown(
		id ='country_dropdown',
		options=[{'label': i[0], 'value': i[0]} for i in query_func(0)],
		value='Finland'),

	html.Br(), 

	dcc.Dropdown(
	id ='coin_dropdown',
	options=[{'label': i[0], 'value': i[0]} for i in query_func(1)],
	value='2 euro'),

	html.Div(id='first_output')
	])


add_layout = html.Div([
	html.H3('Add new coin to the database'),
	html.Br(),
	html.H2('Country:'),
	dcc.Dropdown(
		id='coin_dropdown_add',
		options=[{'label': i[0], 'value': i[0]} for i in query_func(2)]),

	html.H2('Value:'),
		dcc.Dropdown(
		id='country_dropdown_add',
		options=[{'label': i[0], 'value': i[0]} for i in query_func(1)]),

	html.H2('National Side:'),
	dcc.Textarea(id='input_box_add', style={'width' : '100%'}),
	html.Button('Submit', id='add_button'),	
	html.Div(id='add_output')
	])


change_layout = html.Div([
	html.H3('Change coin\'s status')])



@app.callback(
	Output('tabs-content', 'children'),
    [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return search_layout
    elif tab == 'tab-2':
        return add_layout
    elif tab == 'tab-3':
    	return change_layout    


@app.callback(
	Output('first_output', 'children'),
	[Input('country_dropdown', 'value'), Input('coin_dropdown', 'value')])
def update_output(country_dropdown, coin_dropdown):
	answer = complex_query_func(0, country_dropdown, coin_dropdown)
	if answer != []:
		return ('Answer: ', str(answer))
	else:
		return ('No results')	


@app.callback(
	Output('add_output', 'children'),
	[Input('coin_dropdown_add', 'value'), Input('country_dropdown_add', 'value'), Input('input_box_add', 'value'), 
	Input('add_button', 'n_clicks')])
def update_insert(coin_dropdown_add, country_dropdown_add, input_box_add, n_clicks):
#	answer = complex_query_func_insert(coin_dropdown_add, country_dropdown_add, input_box_add)
#	print (answer)
	return str(coin_dropdown_add, country_dropdown_add, input_box_add, n_clicks)

		

if __name__ == '__main__':
	app.run_server(debug=True)





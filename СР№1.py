import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
from dash.dependencies import Input, Output

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Здравствуте! Вы находитесь на странице Габудиновой Данили Исмаиловны.',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Здесь Вы сможете узнать чуть больше обо мне. Мне 18 лет. Я родилась в городе Волгоград', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Markdown('''
                 **Больше информации обо мне Вы можете найти на моей странице [ВК](https://vk.com/id367929216).**''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Markdown('''
                 **Информация о лучшем в России [биофаке](https://biology.hse.ru/).**''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Div([
        html.Img(src='https://sun9-5.userapi.com/c639721/v639721090/584c/EJpCvgGmJRU.jpg', style={
            'width': '50%', 'margin-left': 130, 'margin-top': 45, 'textAlign': 'center'})
    ]),

    html.Label('Мой университетский путь'),
    dcc.Slider(
        id='my-slider',
        min=1,
        max=4,
        marks={i: 'курс {}'.format(i) for i in range(5)},
        value=1,
    ),
    html.Div(id='slider-output-container'),
    html.Label('А на какой ступени жизни ты?'),
    dcc.Slider(
        id='your-slider',
        min=1,
        max=4,
        marks={i: 'курс {}'.format(i) for i in range(5)},
        value=4,
    ),
    html.Div(id='slider-output-container2'),
    dcc.Tabs(
        id="tabs-with-classes",
        value='tab-2',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Моя любимая еда',
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Моя любимая музыка',
                value='tab-2',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Мои цели на ближайшее будущее',
                value='tab-3', className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Мои любимые животные',
                value='tab-4',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
        ]),
    html.Div(id='tabs-content-classes')
])


@app.callback(Output('tabs-content-classes', 'children'),
              [Input('tabs-with-classes', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Больше всего я люблю итальянскую кухню. Пицца, ризотто, паста и лазанья - самые вкусные кулинарные изобретения')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Вообще я меломан. Но на данный момент больше всего я слушаю именно русскую музыку. Больше всего мне нравится жанр местное инди. ')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Выучить английский, немецкий языки и лучше разбираться в программировании')
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('Мои любимые животные это коты. Обычно они очень ласковые и неагрессивные. А еще они просто няшки')
        ])



if __name__ == '__main__':
    app.run_server(debug=True)
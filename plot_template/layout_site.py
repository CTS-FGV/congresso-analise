import datetime
from copy import deepcopy
import plotly.graph_objs as go

def layout(df):

    #### RETANGULOS PRESIDENTES
    rectangle_color = '#ECEFF0'
    opacity = 0.8
    presidentes = [
        # LULA I
        {
            'type'     : 'rect', 'xref': 'x', 'yref': 'y', 'x0': '2003-01-01', 'y0': -1.1, 'x1': '2006-12-31', 'y1': 2,
            'fillcolor': rectangle_color, 'opacity': opacity, 'line': {
            'width': 0
        }, 'layer'     : 'below',
        },
        # DILMA I
        {
            'type'     : 'rect', 'xref': 'x', 'yref': 'y', 'x0': '2011-01-01', 'y0': -1.1, 'x1': '2014-12-31', 'y1': 2,
            'fillcolor': rectangle_color, 'opacity': opacity, 'line': {
            'width': 0
        }, 'layer'     : 'below'
        },
        # TEMER
        {
            'type'     : 'rect', 'xref': 'x', 'yref': 'y', 'x0': '2016-05-01', 'y0': -1.1,
            'x1'       : datetime.datetime.strftime(df.index[-1], '%Y-%m-%d'),
            'y1'       : 2,
            'fillcolor': rectangle_color, 'opacity': opacity, 'line': {
            'width': 0,
        }, 'layer'     : 'below'
        }]

    ### ANOTACOES PRESITENTES
    y_pred = 1.05
    presidentes_hist = [dict(x='2000-12-31',
                             y=y_pred,
                             xref='x', yref='paper',
                             text='FHC II',
                             ax=0, ay=-30,
                             showarrow=False,
                             font=dict(size=9)),
                        dict(x='2004-12-31',
                             y=y_pred,
                             xref='x', yref='paper',
                             text='LULA I',
                             ax=0, ay=-30,
                             showarrow=False,
                             font=dict(size=9)),
                        dict(x='2008-12-31',
                             y=y_pred,
                             xref='x', yref='paper',
                             text='LULA II',
                             ax=0, ay=-30,
                             showarrow=False,
                             font=dict(size=9)),
                        dict(x='2012-12-31',
                             y=y_pred,
                             xref='x', yref='paper',
                             text='DILMA I',
                             ax=0, ay=-30,
                             showarrow=False,
                             font=dict(size=9)),
                        dict(x='2015-08-15',
                             y=y_pred,
                             xref='x', yref='paper',
                             text='DILMA II',
                             ax=0, ay=-30,
                             showarrow=False,
                             font=dict(size=9)),
                        dict(x='2016-12-01',
                             y=y_pred,
                             xref='x', yref='paper',
                             text='TEMER',
                             ax=0, ay=-30,
                             showarrow=False,
                             font=dict(size=9))]

    #### RETANGULOS PRESIDENTE CAMARA
    rectangle_color = '#ECEFF0'
    opacity = 0.8
    shape_skeleton = {'type'     : 'rect', 'xref': 'x', 'yref': 'y', 'x0': '2003-01-01', 'y0': -1.1, 'x1': '2006-12-31',
                      'y1'       : 2,
                      'fillcolor': rectangle_color, 'opacity': opacity, 'line': {'width': 0}, 'layer': 'below'}

    presidentes_camara = [{'mandato': ('1999-02-02', '2001-02-13'), 'nome': 'TEMER', 'partido': 'PMDB'},
                          {'mandato': ('2001-02-13', '2002-12-17'), 'nome': 'AÉCIO', 'partido': 'PSDB'},
                          {'mandato': ('2003-02-02', '2005-02-14'), 'nome': 'LIMA', 'partido': 'PT'},
                          {'mandato': ('2005-02-14', '2005-07-21'), 'nome': '*', 'partido': ''},
                          {'mandato': ('2005-07-28', '2007-02-01'), 'nome': 'REBELO', 'partido': 'PCdoB'},
                          {'mandato': ('2007-02-01', '2009-02-02'), 'nome': 'CHINAGLIA', 'partido': 'PT'},
                          {'mandato': ('2009-02-02', '2010-12-17'), 'nome': 'TEMER', 'partido': 'PMDB'},
                          {'mandato': ('2010-12-17', '2013-02-04'), 'nome': 'AURELI', 'partido': 'PT'},
                          {'mandato': ('2013-02-04', '2015-02-01'), 'nome': 'ALVES', 'partido': 'PMDB'},
                          {'mandato': ('2015-02-01', '2016-07-07'), 'nome': 'CUNHA', 'partido': 'PMDB'},
                          {'mandato': ('2016-07-07',
                                       datetime.datetime.strftime(df.index[-1], '%Y-%m-%d')),
                           'nome'   : 'MAIA', 'partido': 'DEM'}]

    presidentes_camara_shapes = []
    for i in range(len(presidentes_camara)):
        if i % 2 != 0:
            shape_skeleton.update(dict(zip(['x0', 'x1'], presidentes_camara[i]['mandato'])))
            presidentes_camara_shapes.append(deepcopy(shape_skeleton))

    #### ANOTACOES PRESIDETES CAMARA

    y_pred = 1.05
    annot_skeleton = dict(x='2000-12-31', y=y_pred, xref='x', yref='paper', text='FHC II', ax=0, ay=-30,
                          showarrow=False,
                          font=dict(size=9))

    presidentes_camara_annot = []
    for presidente in presidentes_camara:
        a, b = presidente['mandato']
        a = datetime.datetime.strptime(a, '%Y-%m-%d')
        b = datetime.datetime.strptime(b, '%Y-%m-%d')
        mean = a + (b - a) / 2
        annot_skeleton.update(
            dict(zip(['x', 'text'], (mean, '{0}<br>{1}'.format(presidente['nome'], presidente['partido'])))))
        presidentes_camara_annot.append(deepcopy(annot_skeleton))

    severino = [dict(text='* SEVERINO PP', font=dict(size=9), x=0.5, y=-0.47, yref='paper', xref='paper', showarrow=False)]

    ### ACONTECIMENTOS
    acontecimentos = [dict(x='2013-06-23',
                           y=1,
                           xref='x', yref='paper',
                           text='Jornadas de <br> Junho',
                           ax=0, ay=-18,
                           font=dict(size=10)),
                      dict(x='2005-06-30',
                           y=1,
                           xref='x', yref='paper',
                           text='Mensalão',
                           ax=0, ay=-12,
                           font=dict(size=10)),
                      dict(x='2008-09-15',
                           y=1,
                           xref='x', yref='paper',
                           text='Crise <br> Financeira',
                           ax=0, ay=-18,
                           font=dict(size=10)),
                      dict(x='2016-05-12',
                           y=1,
                           xref='x', yref='paper',
                           text='Impeachment',
                           ax=0, ay=-12,
                           font=dict(size=10)), ]

    acontecimentos_lines = [{
        'type': 'line',
        'x0'  : ac['x'],
        'y0'  : -1.1,
        'x1'  : ac['x'],
        'y1'  : 1.1,
        'line': {
            'color': 'black',
            'width': 1,
        },
    } for ac in acontecimentos]

    y_arrows = [dict(x=-0.012, y=1.02, ax=0, ay=17, arrowsize=1, arrowhead=4, xref='paper')]

    ### TEXTO DO GRAFICO
    subtitulos = [dict(text='PRESIDENTES', font=dict(size=11), x=0, y=-0.12, yref='paper', xref='paper', showarrow=False),
                  dict(text='INFORMAÇÕES', font=dict(size=11), x=0, y=-0.32, yref='paper', xref='paper', showarrow=False),
                  dict(text='PARTIDOS', font=dict(size=11), x=0, y=-0.52, yref='paper', xref='paper', showarrow=False),
                  dict(
                      text='Dados: <a href=\"http://www2.camara.leg.br/transparencia/dados-abertos/dados-abertos-legislativo\">Câmara dos Deputados</a>',
                      font=dict(size=9), x=0, y=-0.95, yref='paper', xref='paper', showarrow=False),
                  dict(text='Atualizado: {}'.format(datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y')),
                       font=dict(size=9), x=0.35, y=-0.95, yref='paper', xref='paper', showarrow=False),
                  dict(text='Elaborado por Congresso Em Números',
                       font=dict(size=9), x=0.60, y=-0.95, yref='paper', xref='paper', showarrow=False), ]

    #### BOTOES PRESIDENTES
    y_button_president = -0.22
    updatemenus = list([
        dict(buttons=list([
            dict(label='FHC II',
                 method='relayout',
                 args=[{'xaxis': dict(range=[datetime.datetime.strftime(df.index[0],
                                                                        '%Y-%m-%d'),
                                             '2002-12-31'])}]),

            dict(label='LULA I',
                 method='relayout',
                 args=[{'xaxis': dict(range=['2003-01-01', '2006-12-31'])}]),

            dict(label='LULA II',
                 method='relayout',
                 args=[{'xaxis': dict(range=['2007-01-01', '2010-12-31'])}]),

            dict(label='DILMA I',
                 method='relayout',
                 args=[{'xaxis': dict(range=['2011-01-01', '2014-12-31'])}]),

            dict(label='DILMA II',
                 method='relayout',
                 args=[{'xaxis': dict(range=['2015-01-01', '2016-05-01'])}]),

            dict(label='TEMER',
                 method='relayout',
                 args=[{'xaxis': dict(range=['2016-05-01',
                                             datetime.datetime.strftime(df.index[-1],
                                                                        '%Y-%m-%d')])}]),
            dict(label='TODOS',
                 method='relayout',
                 args=[{'xaxis': dict(range=[datetime.datetime.strftime(df.index[0],
                                                                        '%Y-%m-%d'),
                                             datetime.datetime.strftime(df.index[-1],
                                                                        '%Y-%m-%d')])}]),
        ]),
            direction='left',
            pad={'r': 10, 't': 10},
            showactive=True,
            active=6,
            type='buttons',
            x=0,
            xanchor='left',
            y=y_button_president,
            yanchor='bottom'),

        ## BOTOES INFORMACOES
        dict(buttons=list([
            dict(label='Acontecimentos',
                 method='relayout',
                 args=[{'annotations': acontecimentos + subtitulos,
                        'shapes'     : acontecimentos_lines,
                        'xaxis'      : dict(tickvals=[x['x'] for x in acontecimentos])}]),
            dict(label='Presidentes',
                 method='relayout',
                 args=[{'annotations': presidentes_hist + subtitulos,
                        'shapes'     : presidentes,
                        'xaxis'      : dict(tickvals=['2003', '2007', '2011', '2015'], tickformat='%Y')}]),
            dict(label='Presidentes Câmara',
                 method='relayout',
                 args=[{'annotations': presidentes_camara_annot + subtitulos + severino,
                        'shapes'     : presidentes_camara_shapes,
                        'xaxis'      : dict(
                            tickvals=['2001', '2003', '2005', '2007', '2009', '2011', '2013', '2015', '2007', '2017'],
                            tickformat='%Y')}]),
            dict(label='Limpar',
                 method='relayout',
                 args=[{'annotations': subtitulos,
                        'shapes'     : [],
                        'xaxis'      : dict(tickvals=['2003', '2007', '2011', '2015'], tickformat='%Y')}]),
        ]),
            direction='left',
            pad={'r': 10, 't': 10},
            showactive=True,
            active=3,
            type='buttons',
            x=0,
            xanchor='left',
            y=-0.42,
            yanchor='bottom')
    ])

    legend = dict(orientation='h', x=0, y=-0.72, xanchor='center', yanchor='middle')

    yaxis = go.YAxis(
        # title="Apoio ao Governo",
        showgrid=False,
        showline=True,
        ticks="",
        showticklabels=True,
        # mirror=True,
        linewidth=1,
    )
    layout = dict(title='Apoio ao Governo das Bancadas Partidárias por Voto <br> Parlamentar na Câmara ',
                  xaxis=dict(  # rangeslider=dict(),
                      type='date'),
                  yaxis=yaxis,
                  autosize=False,
                  width=600,
                  height=880,
                  margin=go.Margin(
                      l=50,
                      r=30,
                      b=360,
                      t=110,
                      pad=0
                  ),
                  paper_bgcolor='#F2F2F2',
                  plot_bgcolor='#F2F2F2',
                  updatemenus=updatemenus,
                  annotations=subtitulos,
                  legend=legend,
                  font=dict(family='Lato, sans-serif')
                  # shapes = presidentes,
                  )

    return layout
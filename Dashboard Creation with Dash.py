import dash
from dash import dcc, html
import plotly.graph_objs as go
import psutil
import subprocess

app = dash.Dash(__name__)

# Fonction pour obtenir les données de performance en temps réel
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_gpu_usage():
    gpu_usage = subprocess.check_output(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits'])
    return gpu_usage.decode('utf-8').strip()

# Layout du dashboard
app.layout = html.Div([
    html.H1('Server Performance Dashboard'),
    dcc.Graph(id='cpu-usage-graph'),
    dcc.Graph(id='gpu-usage-graph'),
])

# Fonction pour mettre à jour les graphiques en temps réel
@app.callback(
    [dash.dependencies.Output('cpu-usage-graph', 'figure'),
     dash.dependencies.Output('gpu-usage-graph', 'figure')],
    [dash.dependencies.Input('cpu-usage-graph', 'id')]
)
def update_graph(input_value):
    cpu_usage = get_cpu_usage()
    gpu_usage = get_gpu_usage()

    cpu_fig = go.Figure(data=[go.Bar(x=['CPU Usage'], y=[cpu_usage])])
    cpu_fig.update_layout(title='CPU Usage')

    gpu_fig = go.Figure(data=[go.Bar(x=['GPU Usage'], y=[gpu_usage])])
    gpu_fig.update_layout(title='GPU Usage')

    return cpu_fig, gpu_fig

if __name__ == '__main__':
    app.run_server(debug=True)

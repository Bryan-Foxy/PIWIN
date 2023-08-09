import plotly.express as px
import plotly.graph_objs as go
import pandas as pd




def filter_features(data):
    features_list = ['/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/transport/foreign-port', 
                     '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/bgp-neighbor-counters/received/keepalives',
                     '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/prefix-activity/sent/explicit-withdraw',
                     '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/transport/local-port', 'type'
                     ]
    
    new_column_names = {
    '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/prefix-activity/sent/explicit-withdraw': 'sent_explicit_withdraw',
    '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/transport/foreign-port': 'foreign_port',
    '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/transport/local-port': 'local_port',
    '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/bgp-neighbor-counters/received/keepalives': 'received_keepalives'
    }


    #Affecter les nouvelles colonnes et renommer
    data_new = data[features_list]
    data_new = data_new.rename(columns=new_column_names)

    return data_new


def load_cpu15(data, col):
    fig=px.histogram(data, x=col, color='type_code')
    return fig

def type_pie(data, col):
    fig=px.pie(data, names=col, values='type_code', hole=0.5)
    return fig



#Activity network
def global_activity(data):

    data['hour'] = pd.to_datetime(data['/time']).dt.hour

    keys=[]
    hours=[]
    for key,hour in data.groupby('hour'):
        keys.append(key)
        hours.append(len(hour))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=keys, y=hours, mode='lines', name='Global activity of the virtual network'))
    fig.update_layout(title='Global activity of the virtual network in hour', xaxis_title='Hour of the day', yaxis_title='Activities of the all the network')
    
    return fig


def chart_messages_received(data, col):
    fig = px.histogram(data, x=col, color='type_code')
    return fig




#####Network Part

def bgp_total(data):
    ecom_type6=data.groupby('type')['/devices/modules/openconfig-interfaces/interfaces/interface/state/counters/in-unicast-pkts'].agg('sum').reset_index(name='Total parquet bgp openconfig unicast ($)')

    bar_fig6=px.bar(
    data_frame=ecom_type6, x='Total parquet bgp openconfig unicast ($)',y='type',color='type',
    orientation='h',title=' Total parquet bgp openconfig unicast')
    #bar_fig.update_layout({'bargap': 0.5})

    #affichage du graphique 
    return bar_fig6

def bgp2(data):
    ecom_type9=data.groupby('type')['/devices/modules/Cisco-IOS-XE-interfaces-oper/interfaces/interface/statistics/out-unicast-pkts'].agg('sum').reset_index(name='Total parquet bgp sortir cisco ($)')

    bar_fig9=px.bar(
    data_frame=ecom_type9, x='Total parquet bgp sortir cisco ($)',y='type',color='type',
    orientation='h',title=' Total parquet bgp sortir cisco ')
    #bar_fig.update_layout({'bargap': 0.5})

    #affichage du graphique 
    return bar_fig9

def bgp3(data):
    # Création de la figure
    fig = px.histogram(data, x="/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/transport/foreign-port", color="type", barmode="relative")

    # Affichage de la figure
    return fig

def bgp4(data):
    # Création de la figure
    fig = px.histogram(data, x="/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/transport/local-port", color="type", barmode="relative")

    # Affichage de la figure
    return fig






#####Virtual Part
def latency_v(data, col):
    fig = px.histogram(data, x=col, color='type_code')
    return fig

def cpu_v(data, col):
    fig = px.histogram(data, x=col, color='type')
    return fig

def cpu_v2(data, col):
    fig = px.histogram(data, x=col, color='type_code')
    return fig


#####Physical Part

def temp_2(data, col):
    fig = px.histogram(data, x=col, color='type_code')
    return fig


def cpu_load(df):
    ecom_type4=df.groupby('type')['/computes0/metrics/hardware/hardware-cpu-load-15min'].agg('sum').reset_index(name='Total cpu_load($)')
    bar_fig4=px.bar(
    data_frame=ecom_type4, x='Total cpu_load($)',y='type',color='type',
    orientation='h',title=' Total cpu_load by type')
    #bar_fig.update_layout({'bargap': 0.5})

    #affichage du graphique 
    return bar_fig4

def cpu_load2(df):
    ecom_type3=df.groupby('type')['/devices#IntGW-01/metrics/cpu_util'].agg('sum').reset_index(name='Total cpu_util($)')
    bar_fig3=px.bar(data_frame=ecom_type3, x='Total cpu_util($)',y='type',color='type',
    orientation='h',title=' total cpu_util by type')
    #bar_fig.update_layout({'bargap': 0.5})

    #affichage du graphique 
    return bar_fig3
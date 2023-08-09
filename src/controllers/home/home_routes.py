from flask import Blueprint, render_template, current_app
import pandas as pd
from .. import utilities 
import json
import plotly

#Initialisation of Blueprint
home_bp = Blueprint(
    'home_bp', __name__,
    static_folder = 'static',
    template_folder = 'templates'

)

@home_bp.route('/home', methods=['GET'])
def homepage():
    data = pd.read_csv(current_app.config['DASHBOARD_FILE'])
    data_select = utilities.filter_features(data)
    #cpu_chart15
    fig = utilities.load_cpu15(data, '/computes0/metrics/hardware/hardware-cpu-load-15min')
    fig = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    #type_pie
    pie_type = utilities.type_pie(data, 'type')
    pie_type = json.dumps(pie_type, cls=plotly.utils.PlotlyJSONEncoder)

    #activity_global
    activity = utilities.global_activity(data)
    activity = json.dumps(activity, cls=plotly.utils.PlotlyJSONEncoder)

    #message_bgp
    msg_bgp = utilities.chart_messages_received(data, '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/prefix-activity/sent/explicit-withdraw')
    msg_bgp = json.dumps(msg_bgp, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('index.html', data=data_select, fig_cpu15=fig, fig_type=pie_type,
                           fig_activity=activity,
                           msg_bgp=msg_bgp)



from flask import Blueprint, render_template, current_app
import pandas as pd
from .. import utilities 
import json
import plotly

virtual_bp = Blueprint(
    'virtual_bp', __name__,
    static_folder = 'static',
    template_folder = 'templates'
)

@virtual_bp.route('/virtual', methods=['GET'])
def virtualpage():
    data = pd.read_csv(current_app.config['DASHBOARD_FILE'])
    data_v = pd.read_csv(current_app.config['DASHBOARD_V'])
    #latency
    fig = utilities.latency_v(data_v, '/devices#IntGW-01/metrics/disk-device-write-latency')
    fig = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    #cpu
    fig_cpuv = utilities.cpu_v(data_v, '/devices#IntGW-01/metrics/cpu')
    fig_cpuv = json.dumps(fig_cpuv, cls=plotly.utils.PlotlyJSONEncoder)

    #cpu2
    fig_cpuv2 = utilities.cpu_v2(data_v, '/devices#IntGW-02/metrics/cpu')
    fig_cpuv2 = json.dumps(fig_cpuv2, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('virtual.html', data=data_v, fig_latency = fig,
                           fig_cpuv = fig_cpuv,
                           fig_cpuv2=fig_cpuv2)
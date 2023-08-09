from flask import Blueprint, render_template, current_app
import pandas as pd
from .. import utilities 
import json
import plotly

physic_bp = Blueprint(
    'physic_bp', __name__,
    static_folder = 'static',
    template_folder = 'templates'
)


@physic_bp.route('/physic', methods=['GET'])
def physicpage():
    data = pd.read_csv(current_app.config['DASHBOARD_FILE'])
    data_select = utilities.filter_features(data)
    #cpu_chart15
    fig = utilities.temp_2(data, '/computes0/metrics/hardware-ipmi-temperature#03-cpu_2_(0x5)/hardware-ipmi-temperature')
    fig = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    #cpu_load
    fig2 = utilities.cpu_load(data)
    fig2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    #cpu_load2
    fig3 = utilities.cpu_load2(data)
    fig3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('physics.html', data=data,
                           fig_temp = fig,
                           fig_cpu=fig2,
                           fig_cpu2=fig3)
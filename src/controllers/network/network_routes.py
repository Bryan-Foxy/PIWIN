from flask import Blueprint, render_template, current_app
import pandas as pd
from .. import utilities 
import json
import plotly

network_bp = Blueprint(
    'network_bp', __name__,
    static_folder = 'static',
    template_folder =  'templates'
)



@network_bp.route('/network', methods=['GET'])
def networkpage():
    data = pd.read_csv(current_app.config['DASHBOARD_FILE'])
    data_select = utilities.filter_features(data)
    #bgp1
    fig = utilities.bgp_total(data)
    fig = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    #bgp2
    fig2 = utilities.bgp2(data)
    fig2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    #bgp3
    fig3 = utilities.bgp3(data)
    fig3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    #bgp4
    fig4 = utilities.bgp4(data)
    fig4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('network.html', data=data, 
                           fig_bgp1=fig,
                           fig_bgp2=fig2,
                           fig_bgp3=fig3,
                           fig_bgp4=fig4)
from flask import Blueprint, render_template, request
import os
import pickle
import pandas as pd
from sklearn.cluster import KMeans
from keras.utils import to_categorical
import numpy as np 
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.preprocessing import RobustScaler
from collections import Counter

#from tensorflow.keras.models import load_model

ai_bp = Blueprint(
    'ai_bp', __name__,
    static_folder = 'static',
    template_folder = 'templates'
)



model_xgb = pickle.load(open('../models/xgb.sav', 'rb'))
print('model save')
#model_lstm = load_model('../models/lstm.h5')

@ai_bp.route('/model', methods=['GET', 'POST'])
def modelpage():

    if request.method=='POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join('src/uploads', filename))
        file_extension = os.path.splitext(filename)[1]
        if file_extension not in ['.xls', '.csv', '.json']:
            return render_template('model.html', message='Invalid file format. Please upload a .xls, .csv, or .json file.')
        

        # read in the data from the uploaded file
        if file_extension == '.xls':
            data = pd.read_excel(os.path.join('src/uploads', filename))
        elif file_extension == '.csv':
            data = pd.read_csv(os.path.join('src/uploads', filename))
        elif file_extension == '.json':
            data = pd.read_json(os.path.join('src/uploads', filename))
        else:
            return 0
        

        data_xgb = data.copy()

        # preprocessing
        #Initialize some parameters for the models 
        features = ['/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/transport/foreign-port',
                    '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/bgp-neighbor-counters/received/keepalives',
                    'type_code',
                    '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/prefix-activity/sent/explicit-withdraw',
                    '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/transport/local-port']
        
        new_cols = {'/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/transport/foreign-port': 'foreign_port',
            '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/prefix-activity/sent/explicit-withdraw': 'sent_explicit_withdraw',
            '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/bgp-neighbor-counters/received/keepalives': 'received_keepalives',
            '/devices/modules/Cisco-IOS-XE-bgp-oper/bgp-state-data/neighbors/neighbor/transport/local-port': 'local_port',
            'type_code': 'type_code'}
        
        data_xgb = data_xgb[features]

        data_xgb = data_xgb.rename(columns=new_cols)
       
        y_test = data_xgb['type_code']
        x_test = data_xgb.drop('type_code', axis=1)

        # Creation of the scaler
        scaler = RobustScaler() 
        #Normalize
        x_test = scaler.fit_transform(x_test)

        #predict
        pred=model_xgb.predict(x_test)

        #best class
        counter = Counter(pred)
        most_common = counter.most_common(2)
        top1 = most_common[0][0]
        top2 = most_common[1][0]



        #msgs
        info0='Classify state'
        info1 = 'The class '
        info2='have the highly probability '
        info3='The second state predicted who have the highly probability is: '
        title='The futur state in 10 min is : '
        info4='The futur class predict is :'



        
        
        

        return render_template('model.html', message='Successful upload.', data=top1, data2=top2, info1=info1, info2=info2,
                               info3=info3,
                               title=title,
                               info0=info0,
                               info4=info4)
    
    return render_template('model.html', message='Upload')




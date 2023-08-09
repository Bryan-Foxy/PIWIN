#Instance KMeans
        kmeans = KMeans(n_clusters=2, random_state=42)

        #Train the model
        kmeans.fit(data.drop('type_code', axis=1))

        #Obtain predict
        predictions = kmeans.predict(data.drop('type_code', axis=1))  
        data['predictions'] = predictions

        #convert to date and add index time series
        data['time'] = pd.to_datetime(data['time'], unit='s')
        data['time'].dt.tz_localize('UTC')
        data['time'].dt.strftime('%Y-%m-%d %H:%M:%S')
        data['time'].astype('datetime64[ns]')
        #Extract Hour
        data['hour'] = pd.to_datetime(data['time']).dt.hour
        data = data.set_index('time')
        #Extract Day
        data['day_of_week'] = data.index.dayofweek

        #Normalisation with RobustScaler
        scaler = RobustScaler()
        y = data['type']
        test = data.drop('type', axis=1)
        test_lstm = scaler.fit_transform(test)
        y_lstm = to_categorical(y)

        #hyperparams lstm
        n_input = 10 # Windows_size
        n_features = test_lstm.shape[1] # Numbers of Features
        batch_size = 32 # Batch 
        n_classes = len(np.unique(y)) # Numbers of classes 


        #model
        valid_generator = TimeseriesGenerator(test_lstm, y_lstm, length=n_input, batch_size=batch_size)

        #predict
        model_lstm.predict(valid_generator)
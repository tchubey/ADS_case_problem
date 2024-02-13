import pandas as pd

class DataFeautures:
    """A class for creating features."""  
    def __init__(self, date_column, target, lags):
        self.date_column = date_column
        self.target = target
        self.lags = lags
    
    def create_date_features(self, df):
        df[self.date_column] = pd.to_datetime(df[self.date_column])
        df['quarter'] = df[self.date_column].dt.quarter.astype('object')
        df['month'] = df[self.date_column].dt.month.astype('object')
        df['season'] = ((df[self.date_column].dt.month%12 + 3)//3).astype('object')
        df.drop(self.date_column, axis=1, inplace=True)
        return df
    
    def create_lag_features(self, df, lags):
        for i in range(1, lags+1):
            df[f'lag_{i}'] = df[self.target].shift(i)
        return df
    
    def transform(self, X):
        X = self.create_date_features(X)
        X = self.create_lag_features(X, self.lags)
        return X
    
    def fit(self, X, y=None):
        return self.transform(X)
    
    def fit_transform(self, X):
        return self.transform(X)
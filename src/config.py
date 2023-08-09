import os


class Config:
    DASHBOARD_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src/data/features_dashboard.csv'))
    DASHBOARD_V = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src/data/features_virtual.csv'))
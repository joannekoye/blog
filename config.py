import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY='ygquehdu9838bdbj;IU3E8981'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joan:Nekoye02@localhost/blog'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
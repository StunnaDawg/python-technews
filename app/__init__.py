from flask import Flask

def create_app(test_config=None):
    #sets up config (this is like index in react)
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        secret = 'SHHH_SEcret_key'
    )

    @app.route('/hello')
    def hello():
        return 'Hello World'
    
    return app
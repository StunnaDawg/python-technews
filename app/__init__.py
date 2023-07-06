from flask import Flask
## imports home form routes folders index
from app.routes import home
from app.routes import dashboard
#sets up config (this is like index in react)
def create_app(test_config=None):    
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    secret = 'SHHH_SEcret_key'
    )

#sets up routes
  @app.route('/hello')
  def hello():
    return 'Hello World'
    
  app.register_blueprint(home)
  app.register_blueprint(dashboard)

  return app
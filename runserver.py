# config=utf-8

from login import userRoute
from model import create_app

DEFAULT_MODULES = [userRoute]
app = create_app('../config.py')

for moudle  in DEFAULT_MODULES:
    app.register_blueprint(moudle)

@app.before_request
def before_request():
    pass

if __name__=='__main__':
    app.run(debug=True)

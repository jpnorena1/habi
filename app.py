from flask import Flask
from controllers import bp as consulta_bp

app = Flask(__name__)

app.register_blueprint(consulta_bp)

if __name__ == '__main__':
    app.run(debug=True)

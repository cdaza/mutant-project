import os

from app import blueprint
from app.main import create_app
from flask_migrate import Migrate
from flask_script import Manager

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app)


@manager.option('-h', '--host', dest='host', default='0.0.0.0')
@manager.option('-p', '--port', dest='port', type=int, default=8080)
@manager.option('-w', '--workers', dest='workers', type=int, default=3)
def gunicorn(host, port, workers):
    """Start the Server with Gunicorn"""
    from gunicorn.app.base import Application

    class FlaskApplication(Application):
        def init(self, parser, opts, args):
            return {
                'bind': f'{host}:{port}',
                'workers': workers
            }

        def load(self):
            return app

    application = FlaskApplication()
    return application.run()


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
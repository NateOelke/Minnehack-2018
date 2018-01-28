from flask_script import Manager, Server

from main import make_app

app = make_app()
manager = Manager(app)

manager.add_command("runserver", Server("0.0.0.0", 8000, use_debugger=True, use_reloader=True))


if __name__ == "__main__":
    manager.run()
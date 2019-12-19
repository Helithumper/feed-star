import click
from flask.cli import FlaskGroup

from feedstar.app import create_app


def create_feedstar(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_feedstar)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """
    from feedstar.extensions import db
    from feedstar.models import User
    from feedstar import config
    click.echo("create database")
    db.create_all()
    click.echo("done")

    click.echo("create user")
    user = User(
        username=config.ADMIN_USERNAME,
        email="admin@mail.com",
        password=config.ADMIN_PASSWORD,
        active=True
    )
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()

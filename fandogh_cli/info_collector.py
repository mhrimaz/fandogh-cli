import platform

import click

from fandogh_cli import VERSION
from fandogh_cli.utils import format_text, TextStyle
from fandogh_cli.fandogh_client.report_client import report

_static_info = {
    'python_version': platform.sys.version,
    'platform': platform.platform(),
    'cli_version': VERSION
}


def collect(cmd, ctx, exception=None):
    try:
        info = dict(_static_info)
        info['cmd'] = cmd.name
        info['params'] = ctx.params
        info['error'] = exception.message if exception else ''

        report(info)
    except Exception as e:
        click.echo(format_text('Error in reporting problem. Please share this error with to help us to improve the service.', TextStyle.FAIL), err=True)
        click.echo(format_text('Caused by {}'.format(exception.message), TextStyle.FAIL), err=True)
        click.echo(format_text('Report error: {}'.format(e), TextStyle.FAIL), err=True)

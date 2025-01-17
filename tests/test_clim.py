"""
mdapi
Copyright (C) 2015-2022 Red Hat, Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Any Red Hat trademarks that are incorporated in the source
code or documentation are not subject to the GNU General Public
License and may only be used or replicated with the express permission
of Red Hat, Inc.
"""

from click.testing import CliRunner

from mdapi.main import main


def test_cli_application_help_option():
    rnnrobjc = CliRunner()
    rsltobjc = rnnrobjc.invoke(main, ["--help"])
    assert rsltobjc.exit_code == 0


def test_cli_application_version_option():
    rnnrobjc = CliRunner()
    rsltobjc = rnnrobjc.invoke(main, ["--version"])
    assert rsltobjc.exit_code == 0

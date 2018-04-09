#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from os.path import exists as path_exists

from pyscaffold.api import create_project
from pyscaffold.cli import run
from pyscaffold.extensions import no_scm


def test_create_project_with_no_scm(tmpfolder):
    # Given options with the tox extension,
    opts = dict(project="proj",
                extensions=[no_scm.NoSCM('no-scm')])

    # when the project is created,
    create_project(opts)

    # then SCM file should not exist
    assert not path_exists("proj/.git")


def test_create_project_without_no_scm(tmpfolder):
    # Given options without the tox extension,
    opts = dict(project="proj")

    # when the project is created,
    create_project(opts)

    # then SCM file should exist
    assert path_exists("proj/.git")


def test_cli_with_no_scm(tmpfolder):
    # Given the command line with the tox option,
    sys.argv = ["pyscaffold", "--no-scm", "proj"]

    # when pyscaffold runs,
    run()

    # then SCM file should not exist
    assert not path_exists("proj/.git")


def test_cli_without_no_scm(tmpfolder):
    # Given the command line without the tox option,
    sys.argv = ["pyscaffold", "proj"]

    # when pyscaffold runs,
    run()

    # then SCM file should exist
    assert path_exists("proj/.git")

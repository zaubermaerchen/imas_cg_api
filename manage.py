#!/usr/bin/env python
import os
import sys
import api.module

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

    # If MySQL-python is not installed then use PyMySQL
    if "MySQLdb" not in api.module.names:
        import pymysql
        pymysql.install_as_MySQLdb()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

import os
from django.conf import settings


LIQUIBASE_JAR = getattr(settings, 'LIQUIBASE_JAR',
    os.path.join(os.path.dirname(__file__), 'vendor', 'liquibase.jar'))

LIQUIBASE_DB_DEFAULTS = getattr(settings, 'LIQUIBASE_DB_DEFAULTS', {
    'postgresql': {
        'tag': 'postgresql',
        'host': 'localhost',
        'port': 5432,
    },
    'mysql': {
        'tag': 'mysql',
        'host': 'localhost',
        'port': 3306,
    },
})

LIQUIBASE_DRIVERS = {
    'postgresql_psycopg2': ('postgresql', 'org.postgresql.Driver',
        os.path.join(os.path.dirname(__file__), 'vendor', 'connectors',
            'postgresql-jdbc3-8.2.jar')),
    'postgis': ('postgresql', 'org.postgresql.Driver',
        os.path.join(os.path.dirname(__file__), 'vendor', 'connectors',
            'postgresql-jdbc3-8.2.jar')),
    'mysql': ('mysql', 'com.mysql.jdbc.Driver',
        os.path.join(os.path.dirname(__file__), 'vendor', 'connectors',
            'mysql-connector-java-5.0.8-bin.jar')),
}

LIQUIBASE_DRIVERS.update(getattr(settings, 'LIQUIBASE_DRIVERS', {}))


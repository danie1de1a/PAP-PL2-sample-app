import os

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}'.format(
    dbuser=os.environ['AZURE_POSTGRESQL_USER'],
    dbpass=os.environ['AZURE_POSTGRESQL_PASSWORD'],
    dbhost=os.environ['AZURE_POSTGRESQL_HOST'],
    dbport=os.environ.get('AZURE_POSTGRESQL_PORT', 5432),  # Usa 5432 como valor predeterminado
    dbname=os.environ['AZURE_POSTGRESQL_DATABASE']
)

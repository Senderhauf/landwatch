CREATE DATABASE landwatch;
CREATE USER psql_docker WITH PASSWORD 'secret';
GRANT ALL PRIVILEGES ON DATABASE "landwatch" to psql_docker;
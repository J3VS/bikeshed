CREATE DATABASE bikeshed;

CREATE USER bikesheduser WITH PASSWORD 'bikeshed';

ALTER ROLE bikesheduser SET client_encoding TO 'utf8';
ALTER ROLE bikesheduser SET default_transaction_isolation TO 'read committed';
ALTER ROLE bikesheduser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE bikeshed TO bikesheduser;

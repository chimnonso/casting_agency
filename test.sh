sudo -u postgres dropdb casting_agency_test
sudo -u postgres createdb casting_agency_test
sudo -u postgres psql casting_agency_test < data.psql
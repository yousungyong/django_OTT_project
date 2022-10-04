#!/bin/bash
cd /var/www/OTT
find . ! -name "my_settings.py" -delete
# rm -rf `ls *|grep -v my_settings.py`
# rm -rf /var/www/OTT
# mkdir /var/www/OTT
# chown -R apache. /var/www/OTT
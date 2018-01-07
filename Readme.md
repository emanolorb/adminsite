Ubuntu 16.04
sudo apt-get install build-essential python3-dev python3-venv libev-dev binutils libproj-dev gdal-bin
Python Virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt

Puente Base de Datos
ssh -L 3307:127.0.0.1:3306 -N root@104.131.145.46
.env file
DEBUG=True
DATABASE_URL='mysql://bosc_super:BoscTR%252016@127.0.0.1:3307/tevi_sea'
API_KEY='H43WiAMBbLZy8ARO4cpydJEpScVXGJKj'
PUBLIC_KEY='PFdivDF6W2TLmDXD7gGDVJBO3pXLV7Ei'
SCRET_KEY='b3thzzE8kPdHUaTNi84q6f7SzEaRBEJM'
LOG_LEVEL='INFO'
JWT_SECRET_KEY=ABCsecret123456
JWT_ALGORITHM=HS256

Utilizar logging como print
Agregar en cada archivo que se ocupe el siguiete codigo:
- import logging
- log = logging.getLogger('django')

Agregar en el .env:
LOG_LEVEL='INFO'

Para imprimir 
log.info('hecho con todo mi cocoro! :%s' % (cocoro_temp,))

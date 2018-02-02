### Ubuntu 16.04
--

```
sudo apt-get install build-essential python3-dev python3-venv libev-dev binutils libproj-dev gdal-bin
```

### Python Virtualenv
--

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt

```


### .env file example
--

```
DEBUG=True
DATABASE_URL='mysql://bosc_super:BoscTR%252016@127.0.0.1
```

### Para utilizar logging como print
--

```
Agregar en cada archivo que se ocupe el siguiete codigo:
- import logging
- log = logging.getLogger('django')

Agregar en el .env:
LOG_LEVEL='INFO'

Para imprimir 
log.info('hecho con todo mi cocoro! :%s' % (cocoro_temp,))

```
### Install gdal
`brew install gdal`
`brew install libgeoip`

### Point to the path of the gdal and geo
`settings.py`
```GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH', '/opt/homebrew/Cellar/gdal/3.9.1_1/lib/libgdal.dylib') 
GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH', '/opt/homebrew/Cellar/geos/3.12.2/lib/libgeos_c.dylib')```
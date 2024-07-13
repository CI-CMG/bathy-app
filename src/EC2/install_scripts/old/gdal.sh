#
# gdal.sh
#
GDAL_VERSION=3.4.1
TARFILE=gdal-${GDAL_VERSION}.tar.gz
MD5FILE=gdal-${GDAL_VERSION}.tar.gz.md5
if [[ -f  ${TARFILE} ]]; then
echo "${TARFILE} already downloaded"
else
wget https://github.com/OSGeo/gdal/releases/download/v${GDAL_VERSION}/${TARFILE}
fi

if [[ -f ${MD5FILE} ]]; then
echo "${MD5FILE} already downloaded"
else
wget https://github.com/OSGeo/gdal/releases/download/v${GDAL_VERSION}/${MD5FILE}
fi

md5sum -c gdal-${GDAL_VERSION}.tar.gz.md5
tar -xzf gdal-${GDAL_VERSION}.tar.gz
cd gdal-${GDAL_VERSION}/

CONTRIB=$HOME/contrib 
./configure --prefix=${CONTRIB}/gdal\
  --with-proj=${CONTRIB}/proj\
  --with-hdf5=${CONTRIB}/hdf5\
  --with-curl=/usr/bin/curl-config\
  --with-sqlite3=${CONTRIB}/sqlite\
  --with-netcdf=${CONTRIB}/netcdf

make
make install

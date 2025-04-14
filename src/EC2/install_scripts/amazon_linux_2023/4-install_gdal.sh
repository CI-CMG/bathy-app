#
# install_gdal.sh
#
export LD_LIBRARY_PATH=/usr/local/lib64:/usr/local/lib
VERSION=3.10.3
TARFILE=gdal-${VERSION}.tar.gz
MD5FILE=gdal-${VERSION}.tar.gz.md5
if [[ -f  ${TARFILE} ]]; then
echo "${TARFILE} already downloaded"
else
wget https://github.com/OSGeo/gdal/releases/download/v${VERSION}/${TARFILE}
fi

if [[ -f ${MD5FILE} ]]; then
echo "${MD5FILE} already downloaded"
else
wget https://github.com/OSGeo/gdal/releases/download/v${VERSION}/${MD5FILE}
fi

md5sum --strict --status -c ${MD5FILE}
if [ $? -ne 0 ]; then
  echo "invalid checksum - exiting..."
  exit
fi

if [ -d "${VERSION}" ]; then
  echo "using existing source directory..."
else
  tar -xzf gdal-${VERSION}.tar.gz
fi

cd gdal-${VERSION}/

mkdir build
cd build
cmake -DCMAKE_PREFIX_PATH="/usr/local" -DCMAKE_BUILD_TYPE=Release -DGDAL_BUILD_OPTIONAL_DRIVERS=ON \
        -DOGR_BUILD_OPTIONAL_DRIVERS=ON -DGDAL_ENABLE_DRIVER_AIGRID=ON -DCMAKE_INSTALL_PREFIX="/usr/local" ..
cmake --build .
sudo cmake --build . --target install

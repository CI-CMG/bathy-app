#
# install_gdal.sh
#
GDAL_VERSION=3.8.4
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

# pattern recommended by shellcheck (https://github.com/koalaman/shellcheck/wiki/SC2181)
if ! md5sum --strict --status -c ${MD5FILE}
then
  echo "invalid checksum - exiting..."
  exit
fi
#md5sum --strict --status -c ${MD5FILE}
#if [ $? -ne 0 ]; then
#  echo "invalid checksum - exiting..."
#  exit
#fi

if [ -d "${GDAL_VERSION}" ]; then
  echo "using existing source directory..."
else
  tar -xzf gdal-${GDAL_VERSION}.tar.gz
fi

cd gdal-${GDAL_VERSION} || exit

mkdir build
cd build || exit
cmake -DCMAKE_PREFIX_PATH="/usr/local" -DCMAKE_BUILD_TYPE=Release -DGDAL_BUILD_OPTIONAL_DRIVERS=ON \
	-DOGR_BUILD_OPTIONAL_DRIVERS=ON -DGDAL_ENABLE_DRIVER_AIGRID=ON -DCMAKE_INSTALL_PREFIX="/usr/local" ..
cmake --build .
sudo cmake --build . --target install

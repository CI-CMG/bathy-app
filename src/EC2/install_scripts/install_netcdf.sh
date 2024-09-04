#
# install_netcdf.sh
#
VERSION=4.9.2
TARFILE=netcdf-c-${VERSION}.tar.gz
MD5FILE=netcdf-c-${VERSION}.tar.gz.sha256
if [[ -f  ${TARFILE} ]]; then
  echo "${TARFILE} already downloaded"
else
  echo "downloading https://downloads.unidata.ucar.edu/netcdf-c/${VERSION}/${TARFILE}..."
  wget https://downloads.unidata.ucar.edu/netcdf-c/${VERSION}/${TARFILE}
fi

if [[ -f ${MD5FILE} ]]; then
  echo "${MD5FILE} already downloaded"
else
  wget https://artifacts.unidata.ucar.edu/repository/downloads-netcdf-c/${VERSION}/${MD5FILE}
fi

sha256sum --strict --status -c ${MD5FILE}
if [ $? -ne 0 ]; then
  echo "invalid checksum - exiting..."
  exit
fi

tar -xzf ${TARFILE}
cd netcdf-c-${VERSION} || exit

# per NetCDF docs https://docs.unidata.ucar.edu/nug/current/getting_and_building_netcdf.html#build_default
export CPPFLAGS='-I/usr/local/include'
export LDFLAGS='-L/usr/local/lib'
./configure --prefix=/usr/local
make check
sudo make install

cd .. || exit

# cleanup
rm -rf ./${TARFILE} ./${MD5FILE} ./netcdf-c-${VERSION}
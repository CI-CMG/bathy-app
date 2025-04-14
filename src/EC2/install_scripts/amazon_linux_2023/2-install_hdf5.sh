#
# install_hdf5.sh
#
MAJOR_VERSION=1.14
VERSION=1.14.6
PATHFRAGMENT=`echo "v${MAJOR_VERSION}" | tr '.' '_'`/`echo "v$VERSION" | tr '.' '_'`
TARFILE=hdf5-${VERSION}.tar.gz
MD5FILE=hdf5-${VERSION}.tar.gz.sha256
URL=https://support.hdfgroup.org/releases/hdf5/${PATHFRAGMENT}/downloads

if [[ -f  ${TARFILE} ]]; then
  echo "${TARFILE} already downloaded"
else
  echo "downloading ${URL}/${TARFILE}..."
  wget ${URL}/${TARFILE}
fi

if [[ -f ${MD5FILE} ]]; then
  echo "${MD5FILE} already downloaded"
else
  echo "downloading ${URL}/hdf5-${VERSION}.sha256sums.txt..."
  curl -s ${URL}/hdf5-${VERSION}.sha256sums.txt | grep ${TARFILE} > $MD5FILE
fi

sha256sum --strict --status -c ${MD5FILE}
if [ $? -ne 0 ]; then
  echo "invalid checksum - exiting..."
  exit
fi

tar -xzf ${TARFILE}
cd hdf5-${VERSION}/

# per NetCDF docs https://docs.unidata.ucar.edu/nug/current/getting_and_building_netcdf.html#build_default
./configure --with-zlib --prefix=/usr/local --enable-hl
make check
sudo make install

cd ~

# cleanup
rm -rf ./${TARFILE} ./${MD5FILE} ./hdf5-${VERSION}
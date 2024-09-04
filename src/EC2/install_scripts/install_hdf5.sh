#
# install_hdf5.sh
#
MAJOR_VERSION=1.14
VERSION=1.14.3
TARFILE=hdf5-${VERSION}.tar.gz
MD5FILE=hdf5-${VERSION}.tar.gz.sha256
DOWNLOAD_URL=https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-${MAJOR_VERSION}/${VERSION}

if [[ -f  ${TARFILE} ]]; then
  echo "${TARFILE} already downloaded"
else
  echo "downloading ${URL}/${TARFILE}..."
  wget ${URL}/${TARFILE}
fi

if [[ -f ${MD5FILE} ]]; then
  echo "${MD5FILE} already downloaded"
else
  wget ${URL}/${MD5FILE}
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
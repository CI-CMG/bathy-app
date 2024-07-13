#
# netcdf.sh
#
VERSION=4.8.1
TARFILE=netcdf-c-${VERSION}.tar.gz
MD5FILE=netcdf-c-${VERSION}.tar.gz.md5
if [[ -f  ${TARFILE} ]]; then
echo "${TARFILE} already downloaded"
else
wget https://downloads.unidata.ucar.edu/netcdf-c/${VERSION}/src/${TARFILE}
fi

# no checksum file to verify?

tar -xzf ${TARFILE}
cd netcdf-c-${VERSION}

export CONTRIB=$HOME/contrib 
export LDFLAGS="-L$CONTRIB/hdf5/lib -L/usr/lib64"
export CPPFLAGS=-I$CONTRIB/hdf5/include
./configure --prefix=${CONTRIB}/netcdf --disable-dap-remote-tests

make && make check && make install

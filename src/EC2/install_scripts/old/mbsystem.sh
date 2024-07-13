#
# mbsystem.sh
#
VERSION=5.7.8
TARFILE=${VERSION}.tar.gz
if [[ -f  ${TARFILE} ]]; then
echo "${TARFILE} already downloaded"
else
wget https://github.com/dwcaress/MB-System/archive/${TARFILE}
fi
echo "tar -xzf ${TARFILE}"
tar -xzf ${TARFILE}

cd MB-System-${VERSION}

export PATH=$HOME/contrib/gdal/bin:$HOME/contrib/hdf5/bin:$HOME/contrib/netcdf/bin:$HOME/proj/bin:$HOME/contrib/gmt/bin:$PATH

./configure --prefix=$HOME/contrib/mbsystem --disable-mbtools --with-proj-lib=$HOME/contrib/proj/lib --with-proj-include=$HOME/contrib/proj/include

make
make install

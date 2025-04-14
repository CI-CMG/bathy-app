#
# mbsystem.sh
#
export LD_LIBRARY_PATH=/usr/local/lib64:/usr/local/lib
VERSION=5.8.1
TARFILE=${VERSION}.tar.gz
if [[ -f  ${TARFILE} ]]; then
echo "${TARFILE} already downloaded"
else
wget https://github.com/dwcaress/MB-System/archive/${TARFILE}
fi
echo "tar -xzf ${TARFILE}"
tar -xzf ${TARFILE}

cd MB-System-${VERSION}

./configure --prefix=/usr/local --disable-mbtools

make
sudo make install
#
# sqlite.sh
#
VERSION=3370200
TARFILE=sqlite-autoconf-${VERSION}.tar.gz

if [[ -f  ${TARFILE} ]]; then
echo "${TARFILE} already downloaded"
else
wget https://www.sqlite.org/2022/${TARFILE}
fi

# no checksum file to download

tar -xzf ${TARFILE}
cd sqlite-autoconf-${VERSION}/
./configure --prefix=$HOME/contrib/sqlite

make && make install

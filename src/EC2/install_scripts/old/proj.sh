#
# proj.sh
#
VERSION=7.2.1
TARFILE=proj-${VERSION}.tar.gz
MD5FILE=proj-${VERSION}.tar.gz.md5
if [[ -f  ${TARFILE} ]]; then
echo "${TARFILE} already downloaded"
else
wget https://download.osgeo.org/proj/${TARFILE}
fi

if [[ -f ${MD5FILE} ]]; then
echo "${MD5FILE} already downloaded"
else
wget https://download.osgeo.org/proj/${MD5FILE}
fi

md5sum -c ${MD5FILE}
tar -xzf ${TARFILE}
cd proj-${VERSION}/

export SQLITE3_LIBS="-L$HOME/contrib/sqlite/lib -lsqlite3"  
./configure --prefix=$HOME/contrib/proj
make && make check && make install
$HOME/contrib/proj/bin/projsync --system-directory --area-of-use World

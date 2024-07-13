#
# geos.sh
#
VERSION=3.10.2
TARFILE=geos-${VERSION}.tar.bz2
if [[ -f  ${TARFILE} ]]; then
echo "${TARFILE} already downloaded"
else
wget https://download.osgeo.org/geos/${TARFILE}
fi

tar -xjf ${TARFILE}
cd geos-${VERSION}
CONTRIB=$HOME/contrib

mkdir _build
cd _build/
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$CONTRIB/geos ..
make 
ctest3                
make install

#
# proj.sh
#
VERSION=9.6.0
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


mkdir build
cd build
cmake ..
cmake --build .
sudo cmake --build . --target install .

ctest

# TODO test if projections already installed with 'projsync --list-files'
projsync --system-directory --all

cd ~

# cleanup
rm -rf ./proj-${VERSION}
rm ${TARFILE}
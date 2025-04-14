#
# gmt.sh
#
export LD_LIBRARY_PATH=/usr/local/lib64:/usr/local/lib
VERSION=6.5.0
TARFILE=gmt-${VERSION}-src.tar.gz
MD5FILE=gmt-${VERSION}-checksums.txt
if [[ -f  ${TARFILE} ]]; then
echo "${TARFILE} already downloaded"
else
  wget https://github.com/GenericMappingTools/gmt/releases/download/${VERSION}/${TARFILE}
fi

if [[ -f ${MD5FILE} ]]; then
echo "${MD5FILE} already downloaded"
else
  wget -q https://github.com/GenericMappingTools/gmt/releases/download/${VERSION}/${MD5FILE} -O - | grep "gmt-${VERSION}-src.tar.gz" > ${MD5FILE}
fi

sha256sum -c ${MD5FILE}
tar -xzf ${TARFILE}
export PATH=$PATH:$HOME/contrib/gdal/bin:$HOME/contrib/netcdf/bin
cd gmt-${VERSION}/
echo 'set (CMAKE_INSTALL_PREFIX "/usr/local")' > cmake/ConfigUser.cmake
echo 'set (GSHHG_ROOT "/usr/local/share/gshhg")' >> cmake/ConfigUser.cmake
echo 'set (DCW_ROOT "/usr/local/share/dcw")' >> cmake/ConfigUser.cmake
mkdir build
cd build
cmake3 ..
cmake3 --build .
sudo cmake3 --build . --target install
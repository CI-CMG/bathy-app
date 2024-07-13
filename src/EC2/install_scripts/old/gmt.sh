#
# gmt.sh
#
VERSION=6.3.0
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
wget https://github.com/GenericMappingTools/gmt/releases/download/${VERSION}/${MD5FILE} -O - | grep "gmt-6.3.0-src.tar.
gz" > ${MD5FILE}
fi 

sha256sum -c ${MD5FILE}
tar -xzf ${TARFILE}
export PATH=$PATH:$HOME/contrib/gdal/bin:$HOME/contrib/netcdf/bin
cd gmt-${VERSION}/
echo 'set (CMAKE_INSTALL_PREFIX "/home/ec2-user/contrib/gmt")' > cmake/ConfigUser.cmake
echo 'set (GSHHG_ROOT "/home/ec2-user/contrib/gmt/share/gshhg")' >> cmake/ConfigUser.cmake
echo 'set (DCW_ROOT "/home/ec2-user/contrib/gmt/share/dcw")' >> cmake/ConfigUser.cmake
mkdir build
cd build
cmake3 ..
cmake3 --build .
cmake3 --build . --target install

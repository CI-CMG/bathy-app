#
# hdf5.sh
#
wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.12/hdf5-1.12.0/src/hdf5-1.12.0.tar.gz
wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.12/hdf5-1.12.0/src/hdf5-1.12.0.md5
md5sum -c hdf5-1.12.0.md5
tar -xvzf hdf5-1.12.0.tar.gz
cd hdf5-1.12.0/
./configure --prefix=/home/ec2-user/contrib/hdf5 --enable-threadsafe --enable-unsupported
make
make check
make install && make check-install

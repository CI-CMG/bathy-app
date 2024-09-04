# some dependencies taken from this article:
#  https://repost.aws/articles/ARJV3lAJE0TcWZMrxqpQ5D3Q/installing-python-package-geopandas-on-amazon-linux-2023-for-graviton

sudo dnf -y \
	install gcc-c++ cpp sqlite-devel libtiff cmake python3-pip python-devel \
	openssl-devel tcl libtiff-devel libcurl-devel swig libpng-devel libjpeg-turbo-devel \
	expat-devel zlib-devel libxml libxml2-devel m4 python3-numpy
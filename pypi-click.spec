#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : pypi-click
Version  : 8.1.3
Release  : 47
URL      : https://files.pythonhosted.org/packages/59/87/84326af34517fca8c58418d148f2403df25303e02736832403587318e9e8/click-8.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/59/87/84326af34517fca8c58418d148f2403df25303e02736832403587318e9e8/click-8.1.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/59/87/84326af34517fca8c58418d148f2403df25303e02736832403587318e9e8/click-8.1.3.tar.gz.asc
Summary  : Composable command line interface toolkit
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-click-license = %{version}-%{release}
Requires: pypi-click-python = %{version}-%{release}
Requires: pypi-click-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(click)
BuildRequires : pypi(colorama)
BuildRequires : pypi(pillow)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
Click Examples
This folder contains various Click examples.  Note that
all of these are not runnable by themselves but should be
installed into a virtualenv.

%package license
Summary: license components for the pypi-click package.
Group: Default

%description license
license components for the pypi-click package.


%package python
Summary: python components for the pypi-click package.
Group: Default
Requires: pypi-click-python3 = %{version}-%{release}

%description python
python components for the pypi-click package.


%package python3
Summary: python3 components for the pypi-click package.
Group: Default
Requires: python3-core
Provides: pypi(click)
Requires: pypi(click)
Requires: pypi(colorama)
Requires: pypi(pillow)

%description python3
python3 components for the pypi-click package.


%prep
%setup -q -n click-8.1.3
cd %{_builddir}/click-8.1.3
pushd ..
cp -a click-8.1.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653009347
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-click
cp %{_builddir}/click-8.1.3/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-click/6fb11e02ffe0f79b74f1c6034b4ae6e7717a69f8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-click/6fb11e02ffe0f79b74f1c6034b4ae6e7717a69f8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

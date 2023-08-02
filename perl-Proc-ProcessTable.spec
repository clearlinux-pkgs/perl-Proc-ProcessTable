#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Proc-ProcessTable
Version  : 0.636
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/J/JW/JWB/Proc-ProcessTable-0.636.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JW/JWB/Proc-ProcessTable-0.636.tar.gz
Source1  : http://cdn-fastly.deb.debian.org/debian/pool/main/libp/libproc-processtable-perl/libproc-processtable-perl_0.59-2.debian.tar.xz
Summary  : 'Perl extension to access the unix process table'
Group    : Development/Tools
License  : Artistic-2.0 BSD-3-Clause
Requires: perl-Proc-ProcessTable-license = %{version}-%{release}
Requires: perl-Proc-ProcessTable-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Proc::ProcessTable
Please use rt.cpan.org to submit bugs and patches.
MAINTENANCE STATUS
==================
This module is now being lightly "maintained" by Jonathan Swartz <swartz@pobox.com>.  I
have nearly zero knowledge of the implementation within but wanted to rescue the
distribution from abandonment and try to get critical bug fixes out. This will need to be
a community effort.

%package dev
Summary: dev components for the perl-Proc-ProcessTable package.
Group: Development
Provides: perl-Proc-ProcessTable-devel = %{version}-%{release}
Requires: perl-Proc-ProcessTable = %{version}-%{release}

%description dev
dev components for the perl-Proc-ProcessTable package.


%package license
Summary: license components for the perl-Proc-ProcessTable package.
Group: Default

%description license
license components for the perl-Proc-ProcessTable package.


%package perl
Summary: perl components for the perl-Proc-ProcessTable package.
Group: Default
Requires: perl-Proc-ProcessTable = %{version}-%{release}

%description perl
perl components for the perl-Proc-ProcessTable package.


%prep
%setup -q -n Proc-ProcessTable-0.636
cd %{_builddir}
tar xf %{_sourcedir}/libproc-processtable-perl_0.59-2.debian.tar.xz
cd %{_builddir}/Proc-ProcessTable-0.636
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Proc-ProcessTable-0.636/deblicense/
pushd ..
cp -a Proc-ProcessTable-0.636 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Proc-ProcessTable
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Proc-ProcessTable/d28dc18ecdea4b0cd75ec4d2af8d325a82cc1fd2 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Proc::Killall.3
/usr/share/man/man3/Proc::Killfam.3
/usr/share/man/man3/Proc::ProcessTable.3
/usr/share/man/man3/Proc::ProcessTable::Process.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Proc-ProcessTable/d28dc18ecdea4b0cd75ec4d2af8d325a82cc1fd2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

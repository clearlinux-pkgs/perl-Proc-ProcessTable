#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Proc-ProcessTable
Version  : 0.59
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/J/JW/JWB/Proc-ProcessTable-0.59.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JW/JWB/Proc-ProcessTable-0.59.tar.gz
Source1  : http://cdn-fastly.deb.debian.org/debian/pool/main/libp/libproc-processtable-perl/libproc-processtable-perl_0.59-2.debian.tar.xz
Summary  : 'Perl extension to access the unix process table'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Proc-ProcessTable-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

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


%package perl
Summary: perl components for the perl-Proc-ProcessTable package.
Group: Default
Requires: perl-Proc-ProcessTable = %{version}-%{release}

%description perl
perl components for the perl-Proc-ProcessTable package.


%prep
%setup -q -n Proc-ProcessTable-0.59
cd %{_builddir}
tar xf %{_sourcedir}/libproc-processtable-perl_0.59-2.debian.tar.xz
cd %{_builddir}/Proc-ProcessTable-0.59
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Proc-ProcessTable-0.59/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Proc::Killall.3
/usr/share/man/man3/Proc::Killfam.3
/usr/share/man/man3/Proc::ProcessTable.3
/usr/share/man/man3/Proc::ProcessTable::Process.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/Proc/Killall.pm
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/Proc/Killfam.pm
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/Proc/ProcessTable.pm
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/Proc/ProcessTable/Process.pm
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/auto/Proc/ProcessTable/Process/autosplit.ix
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/auto/Proc/ProcessTable/ProcessTable.so

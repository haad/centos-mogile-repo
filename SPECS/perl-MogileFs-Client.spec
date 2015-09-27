name:      perl-MogileFS-Client
summary:   perl-MogileFS-Client - Perl client library for accessing MogileFS
version:   1.17
release:   1%{?dist}
vendor:    Alan Kasindorf <dormando@rydia.net>
packager:  Jonathan Steinert <hachi@cpan.org>
license:   Artistic
group:     Applications/CPAN
buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
buildarch: noarch
source:    perl-MogileFS-Client-%{version}.tar.gz
requires:  perl(IO::WrapTie) >= 2.102
buildrequires:  perl(IO::WrapTie) >= 2.102

%description
Perl client library for accessing MogileFS

%prep
rm -rf "%{buildroot}"
%setup -n perl-MogileFS-Client-%{version}

%build
%{__perl} Makefile.PL PREFIX=%{buildroot}%{_prefix} INSTALL_BASE=
make all
make test

%install
make pure_install

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress


# remove special files
find %{buildroot} \(                    \
       -name "perllocal.pod"            \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    \) -exec rm -f {} \;

# no empty directories
find %{buildroot}%{_prefix}             \
    -type d -depth -empty               \
    -exec rmdir {} \;

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_prefix}/share/perl5/
%{_prefix}/share/man

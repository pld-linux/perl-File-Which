#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	File
%define		pnam	Which
Summary:	File::Which Perl module - portable implementation of the `which' utility
Summary(pl.UTF-8):	Moduł Perla File::Which - przenośna implementacja programu `which'
Name:		perl-File-Which
Version:	1.27
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d5c9154262b93398f0750ec364207639
URL:		https://metacpan.org/release/File-Which
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.60
BuildRequires:	perl-Test-Simple >= 0.94
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Which Perl module was created to be able to get the paths to
executable programs on systems under which the `which' program wasn't
implemented in the shell.

%description -l pl.UTF-8
Moduł Perla File::Which powstał, aby umożliwić znajdowanie ścieżki
zadanego programu w systemach, w których program `which' nie jest
dostępny z powłoki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/Which.pm
%{_mandir}/man3/File::Which.3pm*

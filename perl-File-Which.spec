#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Which
Summary:	File::Which Perl module - portable implementation of the `which' utility
Summary(pl):	Modu³ Perla File::Which - przeno¶na implementacja programu `which'
Name:		perl-File-Which
Version:	0.05
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bd671a65f770fc0a124095e74c7c8013
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Which Perl module was created to be able to get the paths to
executable programs on systems under which the `which' program wasn't
implemented in the shell.

%description -l pl
Modu³ Perla File::Which powsta³, aby umo¿liwiæ znajdowanie scie¿ki
zadanego programu w systemach, w których program `which' nie jest
dostêpny z pow³oki.

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
%{_bindir}/*
%{perl_vendorlib}/File/*.pm
%{_mandir}/man[13]/*

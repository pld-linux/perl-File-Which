#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Which
Summary:	File::Which Perl module - portable implementation of the `which' utility
Summary(pl):	Modu� Perla File::Which - przeno�na implementacja programu `which'
Name:		perl-File-Which
Version:	0.05
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Which Perl module was created to be able to get the paths to
executable programs on systems under which the `which' program wasn't
implemented in the shell.

%description -l pl
Modu� Perla File::Which powsta�, aby umo�liwi� znajdywanie scie�ki
zadanego programu w systemach, w kt�rych program `which' nie jest
dost�pny z pow�oki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

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
%{perl_sitelib}/File/*.pm
%{_mandir}/man[13]/*

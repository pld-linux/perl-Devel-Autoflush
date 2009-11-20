#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Autoflush
Summary:	Devel::Autoflush - Set autoflush from the command line
#Summary(pl.UTF-8):
Name:		perl-Devel-Autoflush
Version:	0.05
Release:	1
License:	apache
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	071061e12ce7ca4f3d62a2e329db0503
URL:		http://search.cpan.org/dist/Devel-Autoflush/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(IO::CaptureOutput) >= 1.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a hack to set autoflush for STDOUT and STDERR from the
command line or from PERL5OPT for code that needs it but doesn't have
it.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Devel/*.pm
%{_mandir}/man3/*

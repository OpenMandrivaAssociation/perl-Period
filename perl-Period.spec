%define modname	Period
%define modver	1.20

Summary:	Time::Period module for perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	15
License:	GPLv2
Group:		Development/Perl
Url:		http://search.perl.com/dist/%{modname}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Time/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Period.pm is a Perl module that contains code to deal with time periods.
Currently, there is only a function in this module.  That function is
called inPeriod().

inPeriod() determines if a given time is within a given time period.
It will return 1 if it is, 0 if not, and -1 if either the time or the
period passed to it were malformed.  The time is specified in non-leap
year seconds past January 1, 1970, as per the time() function.  The period
is a string which is of the form described in Period's man page.

%prep
%setup -qn %{modname}-%{modver}
chmod 644 README Period.html

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Period.html README
%{perl_vendorlib}/Time/*
%{_mandir}/man3/*


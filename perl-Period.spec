%define version	1.20
%define release %mkrel 10
%define name 	perl-Period
%define realname Period

Summary:	Time::Period module for perl
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Development/Perl
Source: 	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Time/%{realname}-%{version}.tar.bz2
URL: 		http://www.perl.com/CPAN/modules/by-module/Time/
BuildArch:	noarch

BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root/

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
%setup -q -n %{realname}-%{version}
chmod 644 README Period.html

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Period.html README
%{perl_vendorlib}/Time/*
%{_mandir}/*/*



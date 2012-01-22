%define upstream_name    Period
%define upstream_version 1.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Time::Period module for perl
License: 	GPL
Group: 		Development/Perl
Url: 		http://search.perl.com/dist/%{upstream_name}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Time/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 README Period.html

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Period.html README
%{perl_vendorlib}/Time/*
%{_mandir}/*/*

%define upstream_name    Period
%define upstream_version 1.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Time::Period module for perl
License:	GPL
Group:		Development/Perl
Url:		http://search.perl.com/dist/%{upstream_name}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Time/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Period.html README
%{perl_vendorlib}/Time/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-4mdv2012.0
+ Revision: 765590
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-3
+ Revision: 764100
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-2
+ Revision: 667290
- mass rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 407958
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.20-12mdv2009.1
+ Revision: 351770
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.20-11mdv2009.0
+ Revision: 223953
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.20-10mdv2008.1
+ Revision: 136335
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.20-10mdv2007.0
+ Revision: 108467
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Period


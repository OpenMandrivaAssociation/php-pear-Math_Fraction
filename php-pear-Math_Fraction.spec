%define		_class		Math
%define		_subclass	Fraction
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.4.0
Release:	10
Summary:	Classes that represent and manipulate fractions
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Math_Fraction/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Classes that represent and manipulate fractions (x = a/b).

The Math_FractionOp static class contains definitions for:
- basic arithmetic operations,
- comparing fractions,
- greatest common divisor (gcd) and least common multiple (lcm) of two
  integers,
- simplifying (reducing) and getting the reciprocal of a fraction,
- converting a float to fraction.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-8mdv2012.0
+ Revision: 742082
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-7
+ Revision: 679396
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-6mdv2011.0
+ Revision: 613710
- the mass rebuild of 2010.1 packages

* Wed Nov 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.0-5mdv2010.1
+ Revision: 470154
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.4.0-4mdv2010.0
+ Revision: 441299
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-3mdv2009.1
+ Revision: 322361
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2mdv2009.0
+ Revision: 236923
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.4.0-1mdv2008.1
+ Revision: 136408
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdv2007.0
+ Revision: 82105
- Import php-pear-Math_Fraction

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdk
- 0.4.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-1mdk
- initial Mandriva package (PLD import)


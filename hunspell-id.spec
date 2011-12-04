Name: hunspell-id
Summary: Indonesian hunspell dictionaries
%define upstreamid 20040812
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/id_ID.zip
Group: Applications/Text
URL: http://wiki.services.openoffice.org/wiki/Dictionaries#Indonesian_.28Indonesia.29
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2
BuildArch: noarch

Requires: hunspell

%description
Indonesian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-id

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_id_ID.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20040812-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040812-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20040812-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 06 2006 Caolan McNamara <caolanm@redhat.com> - 0.20040812-1
- latest version

* Mon Sep 01 2006 Caolan McNamara <caolanm@redhat.com> - 0.20040410-1
- initial version

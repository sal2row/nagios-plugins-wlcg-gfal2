%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0
%define site org.atlas
%define dir %{_libexecdir}/grid-monitoring/probes/%{site}
%define dirlcg %{_libexecdir}/grid-monitoring/probes/%{sitelcg}
%define dirpilot %{_libexecdir}/grid-monitoring/probes/%{sitepilot}
%define cronDaily /etc/cron.daily
%define debug_package %{nil}
%define ncgx /usr/lib/ncgx/x_plugins

Summary: WLCG Compliant Probes from %{site}
Name: nagios-plugins-wlcg-gfal2
Version: 0.1.0
Release: 1%{?dist}

License: ASL 2.0
Group: Network/Monitoring
Source0: %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Requires:
AutoReqProv: no
BuildArch: noarch
Requires: python-argparse >= 1.2.1
Requires: python-lxml >= 2.2.3
Requires: gfal2 >= 2.9.3
Requires: gfal2-all >= 2.9.3
Requires: gfal2-plugin-xrootd >= 0.4.0
Requires: gfal2-python >= 1.8.3

%description
TODO

%prep
%setup -q

%build

%install
export DONT_STRIP=1
%{__rm} -rf %{buildroot}
install --directory %{buildroot}/%{dir}
install --directory %{buildroot}/%{cronDaily}
install --directory %{buildroot}/%{www}
install --directory %{buildroot}/%{ncgx}
%{__cp} -rpf %{site}/src/wnjob  %{buildroot}/%{dir}
%{__cp} -rpf %{site}/src/DDM  %{buildroot}/%{dir}
%{__cp} -rpf %{site}/extras/vofeed_atlas.py %{buildroot}/%{ncgx}
%{__cp} -rpf %{site}/extras/webdav_atlas.py %{buildroot}/%{ncgx}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{dir}
%{ncgx}/vofeed_atlas.py
%{ncgx}/webdav_atlas.py

%changelog
* Fri Apr 15 2016 S. A. Tupputi <salvatore.a.tupputi@cnaf.infn.it> - 0.1.0-1
- First github commit of VO-independent probe

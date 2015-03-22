Name: solr
Version: 5.0.0
Release: 1%{?dist}
Summary: Solr is the popular, blazing-fast, open source enterprise search platform built on Apache Lucene
Group: Applications/System
License: Apache-2.0
BuildArch: noarch
URL: http://lucene.apache.org/solr/
Source0: http://archive.apache.org/dist/lucene/solr/%{version}/solr-%{version}.tgz
BuildRequires: ant

# do not repack JARs
%define __jar_repack %{nil}

%define installdir /opt/solr

%description
Solr is the popular, blazing-fast, open source enterprise search platform built
on Apache Lucene.

%prep
%autosetup

%build
true

%install
install -d -m 755 %{buildroot}%{installdir}
cp -Rp . %{buildroot}%{installdir}/

%files
%{installdir}

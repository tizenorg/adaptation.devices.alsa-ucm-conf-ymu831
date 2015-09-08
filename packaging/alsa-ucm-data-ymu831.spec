Name:       alsa-ucm-data-ymu831
Summary:    ALSA UCM data pkg for YMU831 codec
Version:    0.0.1
Release:    1
License:    LGPL-2.1+
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz

%description
ALSA UCM data for ymu831

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/alsa/ucm
cp -a ymu831 %{buildroot}/usr/share/alsa/ucm
mkdir -p %{buildroot}/usr/share/license
cp -a LICENSE.LGPL-2.1+ %{buildroot}/usr/share/license/%{name}

%post

%files
%manifest alsa-ucm-conf-ymu831.manifest
/usr/share/alsa/ucm/ymu831/*
/usr/share/license/alsa-ucm-data-ymu831

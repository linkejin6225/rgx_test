Name:         %{?name}
Version:      %{?version}
Release:      1%{?dist}
Summary:      RPM package for DEB deployment
License:      GPLv3+
Requires:     /bin/sh

%description
Deploys and manages DEB package during RPM lifecycle

%install
##__AUTO_INSTALL__##

%post
for deb in /opt/rgx-os/debs/*.deb; do
    [ -e "$deb" ] || continue
    dpkg -i "$deb" || true
done

%preun
for deb in /opt/rgx-os/debs/*.deb; do
    [ -e "$deb" ] || continue
    pkgname=$(dpkg-deb -f "$deb" Package)
    dpkg -r "$pkgname" || true
done

%files
##__AUTO_FILES__##

%changelog
* Tue Jun 25 2024 YourName <you@example.com>
- Initial package

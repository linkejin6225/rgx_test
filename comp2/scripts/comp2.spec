Name:         comp2
Version:      1.0
Release:      1%{?dist}
Summary:      RPM package for DEB deployment
License:      GPLv3+
Requires:     /bin/sh

%description
Deploys and manages DEB package during RPM lifecycle

%install
mkdir -p %{buildroot}/usr/lib/
cp %{_sourcedir}/libcomp2.so %{buildroot}/usr/lib/

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
/usr/lib/libcomp2.so

%changelog
* Tue Jun 25 2024 YourName <you@example.com>
- Initial package

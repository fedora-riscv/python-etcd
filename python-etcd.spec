%global modname etcd
%global srcname python-%{modname}

Name:           %{srcname}
Version:        0.4.5
Release:        10%{?dist}
Summary:        A python client library for etcd

License:        MIT
URL:            http://pypi.python.org/pypi/%{srcname}

# Using the github URL because the tarball file at pypi excludes
# the license file. But github tarball files are named awkwardly.
Source0:        https://github.com/jplana/%{srcname}/archive/%{version}.tar.gz

#VCS: git:https://github.com/jplana/python-etcd

BuildArch:      noarch

# See https://bugzilla.redhat.com/1393497
# Also https://fedoraproject.org/wiki/Packaging:Guidelines#Noarch_with_Unported_Dependencies
ExclusiveArch:  noarch %{ix86} x86_64 %{arm} aarch64 ppc64le s390x

BuildRequires:  python2-devel
BuildRequires:  python2-dns
BuildRequires:  python2-mock
BuildRequires:  python2-nose
BuildRequires:  python2-urllib3
BuildRequires:  python2-pyOpenSSL

BuildRequires:  python3-devel
BuildRequires:  python3-dns
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-urllib3
BuildRequires:  python3-pyOpenSSL

%description
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

%package -n python2-%{modname}
Summary:        %summary
Requires:       python2-dns
Requires:       python2-urllib3
Obsoletes:      python2-python-etcd
Provides:       python2-python-etcd
%{?python_provide:%python_provide python2-etcd}

%description -n python2-%{modname}
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

%package -n python3-%{modname}
Summary:        %summary
Requires:       python3-dns
Requires:       python3-urllib3
Obsoletes:      python3-python-etcd
Provides:       python3-python-etcd
%{?python_provide:%python_provide python3-etcd}

%description -n python3-%{modname}
Client library for interacting with an etcd service, providing Python
access to the full etcd REST API.  Includes authentication, accessing
and manipulating shared content, managing cluster members, and leader
election.

%prep
%autosetup -p1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
nosetests src/etcd/tests/unit/

# This seems to require a newer python3-mock than what's currently available
# in F23, and even Rawhide.  If I let it download mock-1.3.0 from the Python
# Package Index (pypi) then tests pass.
#%%{__python3} setup.py test

%files -n python2-%{modname}
%doc README.rst
%license LICENSE.txt
%{python2_sitelib}/*

%files -n python3-%{modname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/*

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.5-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Dec 18 2017 Steve Milner <smilner@redhat.com> - 0.4.5-8
- Fix naming per rhbz#1526788.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-6
- I'm told etcd works on s390x too; add it to ExclusiveArch.

* Mon Jun 19 2017 Steve Milner <smilner@redhat.com> - 0.4.5-5
- Remove requirements on etcd for build and install

* Mon Jun 19 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-4
- Last change didn't help and we were in compliance with Packaging
  Guidelines before the change, so revert.  The fact that it still
  randomly gets built on ppc64 seems to be a Fedora infrastructure
  issue.

* Wed Jun 14 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-3
- Try excluding ppc64 directly, since ExclusiveArch doesn't.

* Wed Apr 12 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-2
- Add missing requires python[3]-urllib3 (rhbz#1440546).
- Patch from Oleg Gashev <oleg@gashev.net>

* Thu Mar  2 2017 Steve Milner <smilner@redhat.com> - 0.4.5-1
- Update to 0.4.5

* Fri Feb 17 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.4-1
- Update to 0.4.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-6
- Rebuild for Python 3.6

* Fri Nov 18 2016 Steve Milner <smilner@redhat.com> - 0.4.3-5
- Running unittests only.

* Wed Nov 16 2016 Steve Milner <smilner@redhat.com> - 0.4.3-4
- Added noarch to the list to build.
- Fixed provides (see rhbz#1374240)
- Disabled the new auth module (see https://github.com/jplana/python-etcd/issues/210)

* Wed Nov 09 2016 Matthew Barnes <mbarnes@redhat.com> - 0.4.3-3
- etcd now excludes ppc64; follow suit.
  related: #1393497

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 22 2016 Matthew Barnes <mbarnes@redhat.com> - 0.4.3-1
- Initial packaging.

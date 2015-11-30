#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (not needed for Python 3.4+)

Summary:	Backport of Python 3.4 Enum
Name:		python-enum34
Version:	1.0.4
Release:	3
License:	BSD
Group:		Development/Libraries
Source0:	https://pypi.python.org/packages/source/e/enum34/enum34-%{version}.tar.gz
# Source0-md5:	ac80f432ac9373e7d162834b264034b6
URL:		https://pypi.python.org/pypi/enum34
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 3.4 introduced official support for enumerations. This is a
backport of that feature to Python 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and
2.4.

An enumeration is a set of symbolic names (members) bound to unique,
constant values. Within an enumeration, the members can be compared by
identity, and the enumeration itself can be iterated over.

This module defines two enumeration classes that can be used to define
unique sets of names and values: Enum and IntEnum. It also defines one
decorator, unique, that ensures only unique member names are present
in an enumeration.

%package -n python3-enum34
Summary:	Backport of Python 3.4 Enum
Group:		Development/Libraries

%description -n python3-enum34
Python 3.4 introduced official support for enumerations. This is a
backport of that feature to Python 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and
2.4.

An enumeration is a set of symbolic names (members) bound to unique,
constant values. Within an enumeration, the members can be compared by
identity, and the enumeration itself can be iterated over.

This module defines two enumeration classes that can be used to define
unique sets of names and values: Enum and IntEnum. It also defines one
decorator, unique, that ensures only unique member names are present
in an enumeration.

%prep
%setup -q -n enum34-%{version}

%build
%if %{with python2}
%py_build
%{?with_tests:%{__python} enum/test_enum.py}
%endif

%if %{with python3}
%py3_build
%{?with_tests:%{__python3} enum/test_enum.py}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install

rm -r $RPM_BUILD_ROOT%{py_sitescriptdir}/enum/{LICENSE,README,doc}
rm -r $RPM_BUILD_ROOT%{py_sitescriptdir}/enum/test_*.py*

%py_postclean
%endif

%if %{with python3}
%py3_install

rm -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/enum/{LICENSE,README,doc}
rm $RPM_BUILD_ROOT%{py3_sitescriptdir}/enum/test_enum.py
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc PKG-INFO enum/LICENSE enum/README enum/doc/enum.rst
%dir %{py_sitescriptdir}/enum
%{py_sitescriptdir}/enum/*.py[co]
%{py_sitescriptdir}/enum34-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-enum34
%defattr(644,root,root,755)
%doc PKG-INFO enum/LICENSE enum/README enum/doc/enum.rst
%{py3_sitescriptdir}/enum/*.py
%{py3_sitescriptdir}/enum/__pycache__
%{py3_sitescriptdir}/enum34-%{version}-py*.egg-info
%endif

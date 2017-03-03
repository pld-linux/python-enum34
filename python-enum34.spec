#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (not needed for Python 3.4+)

Summary:	Backport of Python 3.4 Enum
Summary(pl.UTF-8):	Backport klasy Enum z Pythona 3.4
Name:		python-enum34
Version:	1.1.6
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/enum34/
Source0:	https://pypi.python.org/packages/bf/3e/31d502c25302814a7c2f1d3959d2a3b3f78e509002ba91aea64993936876/enum34-%{version}.tar.gz
# Source0-md5:	5f13a0841a61f7fc295c514490d120d0
URL:		https://pypi.python.org/pypi/enum34
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python >= 1:2.4
BuildRequires:	python-modules >= 1:2.4
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
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

%description -l pl.UTF-8
Python wraz z wersją 3.4 wprowadził obsługę typów wyliczeniowych. Ten
pakiet to backport tego elementu języka do Pythona 3.3, 3.2, 3.2, 2.7,
2.6, 2.5 oraz 2.4.

Typ wyliczeniowy to zbiór nazw symbolicznych (elementów) ograniczonych
do unikatowych, stałych wartości. Wewnątrz typu wyliczeniowego jego
elementy można porównywać pod kątem identyczności oraz iterować po
nich.

Moduł definiuje dwie klasy wyliczeniowe, których można używać do
definiowania unikatowych zbiorów nazw i wartości: Enum oraz IntEnum.
Definiuje także jeden dekorator (unique), zapewniający obecność
wyłącznie unikatowych nazw elementów w typie wyliczeniowym.

%package -n python3-enum34
Summary:	Backport of Python 3.4 Enum
Summary(pl.UTF-8):	Backport klasy Enum z Pythona 3.4
Group:		Libraries/Python

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

%description -n python3-enum34 -l pl.UTF-8
Python wraz z wersją 3.4 wprowadził obsługę typów wyliczeniowych. Ten
pakiet to backport tego elementu języka do Pythona 3.3, 3.2, 3.2, 2.7,
2.6, 2.5 oraz 2.4.

Typ wyliczeniowy to zbiór nazw symbolicznych (elementów) ograniczonych
do unikatowych, stałych wartości. Wewnątrz typu wyliczeniowego jego
elementy można porównywać pod kątem identyczności oraz iterować po
nich.

Moduł definiuje dwie klasy wyliczeniowe, których można używać do
definiowania unikatowych zbiorów nazw i wartości: Enum oraz IntEnum.
Definiuje także jeden dekorator (unique), zapewniający obecność
wyłącznie unikatowych nazw elementów w typie wyliczeniowym.

%prep
%setup -q -n enum34-%{version}

%build
%if %{with python2}
%py_build
cd build-2
%{?with_tests:PYTHONPATH=lib %{__python} lib/enum/test.py}
cd ..
%endif

%if %{with python3}
%py3_build
cd build-3
%{?with_tests:PYTHONPATH=lib %{__python3} lib/enum/test.py}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/enum/{LICENSE,README,doc}
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/enum/test.py*

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/enum/{LICENSE,README,doc}
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/enum/test.py
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc enum/LICENSE enum/README enum/doc/enum.rst
%dir %{py_sitescriptdir}/enum
%{py_sitescriptdir}/enum/*.py[co]
%{py_sitescriptdir}/enum34-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-enum34
%defattr(644,root,root,755)
%doc enum/LICENSE enum/README enum/doc/enum.rst
%{py3_sitescriptdir}/enum/*.py
%{py3_sitescriptdir}/enum/__pycache__
%{py3_sitescriptdir}/enum34-%{version}-py*.egg-info
%endif

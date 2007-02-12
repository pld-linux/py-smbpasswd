%define 	module smbpasswd

Summary:	Python package providing SMB Password Hash Generator
Summary(pl.UTF-8):   Pakiet Pythona generujący skróty LM/NT takie jak smbpasswd
Name:		py-%{module}
Version:	1.0.1
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://barryp.org/software/py-smbpasswd/files/%{name}-%{version}.tar.gz
# Source0-md5:	0eab2c29588e32e77ce6e5d2faea7874
URL:		http://barryp.org/software/py-smbpasswd/
BuildRequires:	python-devel
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can generate both LANMAN and NT password hashes, suitable
for use with Samba.

%description -l pl.UTF-8
Ten moduł udostępnia funkcje do generowania skrótów LM/NT, używanych w
plikach z hasłami dla Samby - tak, jak robi to program smbpasswd.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{py_sitedir}/*.so

%define snap    20031125
Summary:	Collection of George W. Bush fortunes
Summary(pl):	Kolekcja fortunek z wypowiedzi Georga W. Busha
Name:		fortune-mod-dubya
Version:	0.%{snap}
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dubya.seiler.us/files/dubya-20031125.tar.gz
# Source0-md5:	c752ab197c7278761f3c267a01305440
URL:		http://dubya.seiler.us/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

%description -l pl
Fortune-mod zawiera wci±¿ popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotê na odrobinê m±dro¶ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog± dodaæ fortune do plików .login u¿ytkowników tak,
by ka¿dy otrzyma³ swoj± dawkê m±dro¶ci przy logowaniu.

%prep
%setup -q -n dubya

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes
install dubya* $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*

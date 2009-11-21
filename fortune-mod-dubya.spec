%define snap    20031125
Summary:	Collection of George W. Bush fortunes
Summary(pl.UTF-8):	Kolekcja fortunek z wypowiedzi Georga W. Busha
Name:		fortune-mod-dubya
Version:	0.%{snap}
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dubya.seiler.us/files/dubya-20031125.tar.gz
# Source0-md5:	c752ab197c7278761f3c267a01305440
URL:		http://dubya.seiler.us/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

%description -l pl.UTF-8
Fortune-mod zawiera wciąż popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotę na odrobinę mądrości przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mogą dodać fortune do plików .login użytkowników tak,
by każdy otrzymał swoją dawkę mądrości przy logowaniu.

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

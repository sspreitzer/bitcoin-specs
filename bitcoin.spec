Name:		bitcoin
Version:	0.12.1
Release:	1%{?dist}
Summary:	peer-to-peer network based digital currency - Qt gui

Group:		Applications/Productivity
License:	MIT
URL:		https://bitcoincore.org
Source0:	https://bitcoin.org/bin/bitcoin-core-%{version}/bitcoin-%{version}.tar.gz
Source1:	https://github.com/bitcoin/bitcoin/archive/v%{version}.tar.gz#/bitcoin-contribs-%{version}.tar.gz

BuildRequires:	openssl-devel
BuildRequires:	boost-devel
BuildRequires:	libevent-devel
BuildRequires:	libdb4-cxx-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	protobuf-devel
BuildRequires:	qrencode-devel
BuildRequires:	zeromq-devel
BuildRequires:	qt5-linguist


%description
Bitcoin is an experimental new digital currency that enables instant
payments to anyone, anywhere in the world. Bitcoin uses peer-to-peer
technology to operate with no central authority: managing transactions
and issuing money are carried out collectively by the network. Bitcoin Core
is the name of the open source software which enables the use of this currency.


%package cli
Summary:	peer-to-peer network based digital currency - cli
%description cli
Bitcoin is an experimental new digital currency that enables instant
payments to anyone, anywhere in the world. Bitcoin uses peer-to-peer
technology to operate with no central authority: managing transactions
and issuing money are carried out collectively by the network. Bitcoin Core
is the name of the open source software which enables the use of this currency.


%package daemon
Summary:	peer-to-peer network based digital currency - daemon
Requires:	systemd
%description daemon
Bitcoin is an experimental new digital currency that enables instant
payments to anyone, anywhere in the world. Bitcoin uses peer-to-peer
technology to operate with no central authority: managing transactions
and issuing money are carried out collectively by the network. Bitcoin Core
is the name of the open source software which enables the use of this currency.


%package libs
Summary:	peer-to-peer network based digital currency - libs
%description libs
Bitcoin is an experimental new digital currency that enables instant
payments to anyone, anywhere in the world. Bitcoin uses peer-to-peer
technology to operate with no central authority: managing transactions
and issuing money are carried out collectively by the network. Bitcoin Core
is the name of the open source software which enables the use of this currency.


%package devel
Summary:	peer-to-peer network based digital currency - devel
Requires:	bitcoin-libs
%description devel
Bitcoin is an experimental new digital currency that enables instant
payments to anyone, anywhere in the world. Bitcoin uses peer-to-peer
technology to operate with no central authority: managing transactions
and issuing money are carried out collectively by the network. Bitcoin Core
is the name of the open source software which enables the use of this currency.


%prep
%setup -q
%setup -q -a 1


%build
%configure --disable-tests
make %{?_smp_mflags}


%install
%make_install

mkdir -p %{buildroot}/%{_unitdir}
cp -v bitcoin-%{version}/contrib/init/bitcoind.service %{buildroot}/%{_unitdir}/bitcoind.service

mkdir -p %{buildroot}/%{_sharedstatedir}/bitcoind

mkdir -p %{buildroot}/%{_datadir}/pixmaps
cp -v bitcoin-%{version}/share/pixmaps/bitcoin*.png %{buildroot}/%{_datadir}/pixmaps/

mkdir -p %{buildroot}/%{_datadir}/applications
cp -v bitcoin-%{version}/contrib/debian/bitcoin-qt.desktop %{buildroot}/%{_datadir}/applications/bitcoin-qt.desktop


%files
%license COPYING
%doc doc/README.md
%{_bindir}/bitcoin-qt
%{_datadir}/pixmaps/bitcoin*
%{_datadir}/applications/bitcoin-qt.desktop


%files cli
%license COPYING
%doc doc/README.md
%doc doc/files.md
%doc doc/reduce-traffic.md
%doc doc/tor.md
%{_bindir}/bench_bitcoin
%{_bindir}/bitcoin-cli
%{_bindir}/bitcoin-tx


%files daemon
%license COPYING
%doc doc/README.md
%doc doc/zmq.md
%{_bindir}/bitcoind
%{_unitdir}/bitcoind.service
%{_sharedstatedir}/bitcoind


%files libs
%license COPYING
%doc doc/README.md
%doc doc/shared-libraries.md
%{_libdir}/libbitcoinconsensus.so*


%files devel
%license COPYING
%doc doc/README.md
%doc doc/shared-libraries.md
%{_libdir}/pkgconfig/libbitcoinconsensus.pc
%{_includedir}/bitcoinconsensus.h
%{_libdir}/libbitcoinconsensus.a
%{_libdir}/libbitcoinconsensus.la


%post daemon
useradd -r -s /sbin/nologin -d %{_sharedstatedir}/bitcoind bitcoin
%systemd_post


%postun daemon
userdel bitcoin
%systemd_postun


%changelog
* Wed Apr 27 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.12.1-2
- add contribs for systemd unit and pixmaps and desktop file

* Sun Apr 24 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.12.1-1
- initial spec file


Summary:	C++ class library of cryptographic schemes
Name:		libcrypto++
Version:	5.6.2
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://www.cryptopp.com/cryptopp562.zip
# Source0-md5:	7ed022585698df48e65ce9218f6c6a67
Patch0:		strict-gcc43-include.diff
Patch1:		doxygen-setup.diff
Patch2:		doxygen-main-link.diff
Patch3:		cryptest-data-files-location.diff
Patch4:		debian-config.diff
Patch8:		ac.patch
Patch9:		%{name}-pld.patch
BuildRequires:	dos2unix
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_ld    -Wl,--as-needed

%description
Crypto++ Library is a free C++ class library of cryptographic schemes.
Currently the library contains the following algorithms:
- high speed stream ciphers: Panama, Salsa20, Sosemanuk
- AES and AES candidates: AES (Rijndael), RC6, MARS, Twofish, Serpent,
  CAST-256
- other block ciphers: IDEA, Triple-DES (DES-EDE2 and DES-EDE3),
  Camellia, RC5, Blowfish, TEA, XTEA, Skipjack, SHACAL-2
- block cipher modes of operation: ECB, CBC, CBC ciphertext stealing
  (CTS), CFB, OFB, counter mode (CTR)
- message authentication codes: VMAC, HMAC, CBC-MAC, DMAC,
  Two-Track-MAC
- hash functions: SHA-1, SHA-2 (SHA-224, SHA-256, SHA-384, and
  SHA-512), Tiger, WHIRLPOOL, RIPEMD-128, RIPEMD-256, RIPEMD-160,
  RIPEMD-320
- public-key cryptography: RSA, DSA, ElGamal, Nyberg-Rueppel (NR),
  Rabin, Rabin-Williams (RW), LUC, LUCELG, DLIES (variants of DHAES),
  ESIGN
- padding schemes for public-key systems: PKCS#1 v2.0, OAEP, PSS,
  PSSR, IEEE P1363 EMSA2 and EMSA5
- key agreement schemes: Diffie-Hellman (DH), Unified Diffie-Hellman
  (DH2), Menezes-Qu-Vanstone (MQV), LUCDIF, XTR-DH
- elliptic curve cryptography: ECDSA, ECNR, ECIES, ECDH, ECMQV
- insecure or obsolescent algorithms retained for backwards
  compatibility and historical value: MD2, MD4, MD5, Panama Hash, DES,
  ARC4, SEAL 3.0, WAKE, WAKE-OFB, DESX (DES-XEX3), RC2, SAFER, 3-WAY,
  GOST, SHARK, CAST-128, Square

%package devel
Summary:	Header files for developing with libcrypto++
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia programów używających libcrypto++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package provides the necessary header files files to allow you to
develop with libcrypto++.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki nagłówkowe potrzebne do tworzenia
oprogramowania korzystającego z libcrypto++.

%package static
Summary:	Static version of libcrypto++ library
Summary(pl.UTF-8):	Statyczna wersja biblioteki libcrypto++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libcrypto++ library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libcrypto++.

%prep
%setup -q -c
rm GNUmakefile
dos2unix -q *.h *.cpp Doxyfile
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P8 -p0
%patch -P9 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/crypto++

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a TestData TestVectors $RPM_BUILD_ROOT%{_datadir}/crypto++

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/crypt*
%attr(755,root,root) %{_libdir}/libcrypto++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcrypto++.so.9
%{_datadir}/crypto*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcrypto++.so
%{_libdir}/libcrypto++.la
%{_includedir}/crypto*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcrypto++.a

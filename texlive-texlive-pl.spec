Name:		texlive-texlive-pl
Version:	66576
Release:	1
Summary:	TeX Live manual (Polish)
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-pl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-pl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-pl package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/texlive/texlive-pl/Makefile
%doc %{_texmfdistdir}/doc/texlive/texlive-pl/live4ht.cfg
%doc %{_texmfdistdir}/doc/texlive/texlive-pl/tex-live.css
%doc %{_texmfdistdir}/doc/texlive/texlive-pl/texlive-pl.css
%doc %{_texmfdistdir}/doc/texlive/texlive-pl/texlive-pl.html
%doc %{_texmfdistdir}/doc/texlive/texlive-pl/texlive-pl.pdf
%doc %{_texmfdistdir}/doc/texlive/texlive-pl/texlive-pl.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

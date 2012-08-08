# revision 26827
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-pl
Version:	20120808
Release:	1
Summary:	TeX Live manual (Polish)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-pl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-pl.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-pl package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdir}/doc/texlive/texlive-pl/Makefile
%doc %{_texmfdir}/doc/texlive/texlive-pl/live4ht.cfg
%doc %{_texmfdir}/doc/texlive/texlive-pl/tex-live.css
%doc %{_texmfdir}/doc/texlive/texlive-pl/tex-livep.sty
%doc %{_texmfdir}/doc/texlive/texlive-pl/texlive-pl.css
%doc %{_texmfdir}/doc/texlive/texlive-pl/texlive-pl.html
%doc %{_texmfdir}/doc/texlive/texlive-pl/texlive-pl.pdf
%doc %{_texmfdir}/doc/texlive/texlive-pl/texlive-pl.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}

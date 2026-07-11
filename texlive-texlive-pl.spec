%global tl_name texlive-pl
%global tl_revision 78337

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	TeX Live manual (Polish)
Group:		Publishing
URL:		https://www.ctan.org/pkg/texlive-pl
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-pl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-pl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeX Live manual (Polish)


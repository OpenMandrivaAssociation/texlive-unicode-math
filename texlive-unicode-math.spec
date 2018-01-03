Name:		texlive-unicode-math
Version:	0.8i
Release:	1
Summary:	Unicode mathematics support for XeTeX and LuaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unicode-math
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-math.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-math.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-math.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-fontspec

%description
The current release of this package typesets mathematics with
unicode input and using OpenType maths fonts. (There is little
compatibility with older maths packages.) XeTeX support is well
tested, though LuaTeX support less so. The package can typeset
using STIX fonts, the XITS development of those fonts, the
Asana-Math fonts, the Latin Modern Math, and the TeX Gyre Math
font familiess, as well as the commercial Cambria Math fonts.
There is no support for extra alphabets in the Unicode 'private
use area'. The package relies on recent versions of the
fontspec package and the l3kernel and l3packages bundles.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/unicode-math
%doc %{_texmfdistdir}/doc/latex/unicode-math
#- source
%doc %{_texmfdistdir}/source/latex/unicode-math

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

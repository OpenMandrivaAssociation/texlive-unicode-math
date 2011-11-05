# revision 24022
# category Package
# catalog-ctan /macros/latex/contrib/unicode-math
# catalog-date 2011-09-18 12:56:12 +0200
# catalog-license lppl1.3
# catalog-version 0.6
Name:		texlive-unicode-math
Version:	0.6
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The current release of this package typesets mathematics with
unicode input and using OpenType maths fonts. (There is little
compatibility with older maths packages.) XeTeX support is well
tested, though LuaTeX support less so. The package can typeset
using STIX fonts, the XITS development of those fonts, the
Asana-Math fonts and the commercial Cambria Math fonts. There
is no support yet for any extra alphabets in the Unicode
'private use area'. The package relies on recent versions of
the fontspec package and the l3kernel and l3packages bundles.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/unicode-math/unicode-math-luatex.sty
%{_texmfdistdir}/tex/latex/unicode-math/unicode-math-table.tex
%{_texmfdistdir}/tex/latex/unicode-math/unicode-math-xetex.sty
%{_texmfdistdir}/tex/latex/unicode-math/unicode-math.lua
%{_texmfdistdir}/tex/latex/unicode-math/unicode-math.sty
%doc %{_texmfdistdir}/doc/latex/unicode-math/README
%doc %{_texmfdistdir}/doc/latex/unicode-math/unicode-math-testsuite.pdf
%doc %{_texmfdistdir}/doc/latex/unicode-math/unicode-math.pdf
%doc %{_texmfdistdir}/doc/latex/unicode-math/unimath-example.ltx
%doc %{_texmfdistdir}/doc/latex/unicode-math/unimath-symbols.pdf
#- source
%doc %{_texmfdistdir}/source/latex/unicode-math/Makefile
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-active-sscripts.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-alph-spaces.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-arrow-accents.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-mathstyle-french.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-mathstyle-iso.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-mathstyle-literal.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-mathstyle-tex.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-mathstyle-upright.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-mathversion.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-nolimits-spec.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-over-under-2.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-over-under.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-pkg-url.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-primes-1.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-primes-2.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-primes-back.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-query-mathstyle.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-range-prime-check.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-slash-delim-2.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-sqrt-n.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-sqrt.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/F-sscript-features.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L-sscale-dimen.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L600a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L600b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L600c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L600f.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L601a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L601b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L601f.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L602b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L603b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L604a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L604b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L650a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/L650b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X002a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X002b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X002c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X002d.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X002e.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003d.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003e.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003f.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003g.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003h.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003i.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003j.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003k.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003l.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003m.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003n.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003o.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X003p.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X004a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X004b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X004c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X004d.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X004e.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X004f.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005d.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005e.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005f.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005g.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005h.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005i.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005j.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005k.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X005l.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X010a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X010b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X010c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X010d.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X011a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X011b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X012a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X012b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X013a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X013b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X013c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X013d.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X013e.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X014a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X014b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X014c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X015a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X015b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X016a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X016b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X016c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X017a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X017b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X017c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X017d.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X018a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X018b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X019a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X019b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X020a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X020b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X021a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X021b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X030a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X031a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X031b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X031c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X032a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X032b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X032c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X033a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X100a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X100b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X100c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X100d.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X100e.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X101a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X102a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X150a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X151a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X202a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X202b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X203a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X206a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X206b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X206c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X207a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X401a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X500a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X501a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X501b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X501d.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X501e.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X502a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X502b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X503a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X600a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X600b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X600c.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X600d.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X600f.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X601a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X601b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X601f.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X604a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X604b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X610f.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X620b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X650a.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/X650b.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/umtest-preamble.tex
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/umtest-suite-F.tex
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/umtest-suite-L.tex
%doc %{_texmfdistdir}/source/latex/unicode-math/testfiles/umtest-suite-X.tex
%doc %{_texmfdistdir}/source/latex/unicode-math/unicode-math-testsuite.ltx
%doc %{_texmfdistdir}/source/latex/unicode-math/unicode-math.dtx
%doc %{_texmfdistdir}/source/latex/unicode-math/unimath-symbols.ltx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

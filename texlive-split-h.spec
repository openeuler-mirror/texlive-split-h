%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-h
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Patch0101:      etex-addlanguage-fix-bz1215257.patch
Source0003:     texlive-licenses.tar.xz
Source1343:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/enctex.tar.xz
Source1344:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/enctex.doc.tar.xz
Source1345:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etex.tar.xz
Source1346:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etex.doc.tar.xz
Source1347:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etex-pkg.tar.xz
Source1348:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etex-pkg.doc.tar.xz
Source1447:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/economic.tar.xz
Source1448:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/economic.doc.tar.xz
Source1791:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ean.tar.xz
Source1792:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ean.doc.tar.xz
Source1793:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebgaramond.tar.xz
Source1794:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebgaramond.doc.tar.xz
Source1795:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebgaramond-maths.tar.xz
Source1796:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebgaramond-maths.doc.tar.xz
Source1797:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecc.tar.xz
Source1798:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecc.doc.tar.xz
Source1799:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eco.tar.xz
Source1800:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eco.doc.tar.xz
Source1802:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eiad.tar.xz
Source1803:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eiad.doc.tar.xz
Source1804:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eiad-ltx.tar.xz
Source1805:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eiad-ltx.doc.tar.xz
Source1807:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/electrum.tar.xz
Source1808:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/electrum.doc.tar.xz
Source1810:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elvish.tar.xz
Source1811:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elvish.doc.tar.xz
Source1812:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epigrafica.tar.xz
Source1813:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epigrafica.doc.tar.xz
Source1814:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epsdice.tar.xz
Source1815:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epsdice.doc.tar.xz
Source1817:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/erewhon.tar.xz
Source1818:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/erewhon.doc.tar.xz
Source1819:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esrelation.tar.xz
Source1820:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esrelation.doc.tar.xz
Source1822:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esstix.tar.xz
Source1823:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esstix.doc.tar.xz
Source1824:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esvect.tar.xz
Source1825:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esvect.doc.tar.xz
Source1827:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eulervm.tar.xz
Source1828:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eulervm.doc.tar.xz
Source1830:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/euxm.tar.xz
Source2121:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ec.tar.xz
Source2122:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ec.doc.tar.xz
Source2123:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/euro.tar.xz
Source2124:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/euro.doc.tar.xz
Source2126:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eurosym.tar.xz
Source2127:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eurosym.doc.tar.xz
Source2188:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/edmac.tar.xz
Source2189:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/edmac.doc.tar.xz
Source2212:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/egameps.tar.xz
Source2213:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/egameps.doc.tar.xz
Source2276:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eijkhout.tar.xz
Source2277:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/encxvlna.tar.xz
Source2278:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/encxvlna.doc.tar.xz
Source2279:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epigram.tar.xz
Source2344:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epsf.tar.xz
Source2345:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epsf.doc.tar.xz
Source2380:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecltree.tar.xz
Source2381:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecltree.doc.tar.xz
Source2382:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/edfnotes.tar.xz
Source2383:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/edfnotes.doc.tar.xz
Source2385:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ednotes.tar.xz
Source2386:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ednotes.doc.tar.xz
Source2390:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eledform.tar.xz
Source2391:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eledform.doc.tar.xz
Source2393:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eledmac.tar.xz
Source2394:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eledmac.doc.tar.xz
Source2396:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/expex.tar.xz
Source2397:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/expex.doc.tar.xz
Source2485:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ethiop.tar.xz
Source2486:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ethiop.doc.tar.xz
Source2488:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ethiop-t1.tar.xz
Source2489:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ethiop-t1.doc.tar.xz
Source2545:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eskd.tar.xz
Source2546:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eskd.doc.tar.xz
Source2548:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eskdx.tar.xz
Source2549:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eskdx.doc.tar.xz
Source2710:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/e-french.tar.xz
Source2711:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/e-french.doc.tar.xz
Source2712:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epslatex-fr.doc.tar.xz
Source2747:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/einfuehrung.doc.tar.xz
Source2748:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etdipa.doc.tar.xz
Source2749:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etoolbox-de.doc.tar.xz
Source2985:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/es-tex-faq.doc.tar.xz
Source3002:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eso-pic.tar.xz
Source3003:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eso-pic.doc.tar.xz
Source3005:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/euenc.tar.xz
Source3006:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/euenc.doc.tar.xz
Source3008:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/euler.tar.xz
Source3009:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/euler.doc.tar.xz
Source3011:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/extsizes.tar.xz
Source3012:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/extsizes.doc.tar.xz
Source3136:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eepic.tar.xz
Source3137:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eepic.doc.tar.xz
Source3140:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epspdfconversion.tar.xz
Source3141:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epspdfconversion.doc.tar.xz
Source3142:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esk.tar.xz
Source3143:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esk.doc.tar.xz
Source3764:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ean13isbn.tar.xz
Source3765:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ean13isbn.doc.tar.xz
Source3766:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easy.tar.xz
Source3767:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easy.doc.tar.xz
Source3768:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easy-todo.tar.xz
Source3769:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easy-todo.doc.tar.xz
Source3770:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easyfig.tar.xz
Source3771:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easyfig.doc.tar.xz
Source3773:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easylist.tar.xz
Source3774:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easylist.doc.tar.xz
Source3775:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easyreview.tar.xz
Source3776:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easyreview.doc.tar.xz
Source3778:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebezier.tar.xz
Source3779:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebezier.doc.tar.xz
Source3781:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecclesiastic.tar.xz
Source3782:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecclesiastic.doc.tar.xz
Source3784:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecv.tar.xz
Source3785:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecv.doc.tar.xz
Source3787:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ed.tar.xz
Source3788:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ed.doc.tar.xz
Source3790:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/edmargin.tar.xz
Source3791:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/edmargin.doc.tar.xz
Source3793:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eemeir.tar.xz
Source3794:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eemeir.doc.tar.xz
Source3796:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/efbox.tar.xz
Source3797:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/efbox.doc.tar.xz
Source3799:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/egplot.tar.xz
Source3800:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/egplot.doc.tar.xz
Source3802:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elements.tar.xz
Source3803:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elements.doc.tar.xz
Source3804:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ellipsis.tar.xz
Source3805:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ellipsis.doc.tar.xz
Source3807:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elmath.tar.xz
Source3808:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elmath.doc.tar.xz
Source3810:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elocalloc.tar.xz
Source3811:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elocalloc.doc.tar.xz
Source3813:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elpres.tar.xz
Source3814:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elpres.doc.tar.xz
Source3815:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elzcards.tar.xz
Source3816:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elzcards.doc.tar.xz
Source3818:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emarks.tar.xz
Source3819:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emarks.doc.tar.xz
Source3821:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/embedall.tar.xz
Source3822:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/embedall.doc.tar.xz
Source3824:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/embrac.tar.xz
Source3825:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/embrac.doc.tar.xz
Source3826:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emptypage.tar.xz
Source3827:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emptypage.doc.tar.xz
Source3829:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emulateapj.tar.xz
Source3830:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emulateapj.doc.tar.xz
Source3831:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endfloat.tar.xz
Source3832:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endfloat.doc.tar.xz
Source3834:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endheads.tar.xz
Source3835:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endheads.doc.tar.xz
Source3837:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endnotes.tar.xz
Source3838:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endnotes.doc.tar.xz
Source3839:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/engpron.tar.xz
Source3840:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/engpron.doc.tar.xz
Source3842:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/engrec.tar.xz
Source3843:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/engrec.doc.tar.xz
Source3845:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/enotez.tar.xz
Source3846:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/enotez.doc.tar.xz
Source3847:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/enumitem.tar.xz
Source3848:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/enumitem.doc.tar.xz
Source3849:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/enumitem-zref.tar.xz
Source3850:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/enumitem-zref.doc.tar.xz
Source3852:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/envbig.tar.xz
Source3853:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/envbig.doc.tar.xz
Source3854:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/environ.tar.xz
Source3855:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/environ.doc.tar.xz
Source3857:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/envlab.tar.xz
Source3858:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/envlab.doc.tar.xz
Source3860:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epigraph.tar.xz
Source3861:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epigraph.doc.tar.xz
Source3863:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epiolmec.tar.xz
Source3864:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epiolmec.doc.tar.xz
Source3868:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqell.tar.xz
Source3869:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqell.doc.tar.xz
Source3870:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqlist.tar.xz
Source3871:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqlist.doc.tar.xz
Source3873:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqname.tar.xz
Source3874:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqparbox.tar.xz
Source3875:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqparbox.doc.tar.xz
Source3877:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/errata.tar.xz
Source3878:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/errata.doc.tar.xz
Source3880:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esami.tar.xz
Source3881:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esami.doc.tar.xz
Source3882:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esdiff.tar.xz
Source3883:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esdiff.doc.tar.xz
Source3885:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esint.tar.xz
Source3886:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esint.doc.tar.xz
Source3888:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esint-type1.tar.xz
Source3889:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/esint-type1.doc.tar.xz
Source3890:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etaremune.tar.xz
Source3891:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etaremune.doc.tar.xz
Source3893:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etextools.tar.xz
Source3894:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etextools.doc.tar.xz
Source3896:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etoc.tar.xz
Source3897:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etoc.doc.tar.xz
Source3899:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etoolbox.tar.xz
Source3900:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etoolbox.doc.tar.xz
Source3901:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eukdate.tar.xz
Source3902:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eukdate.doc.tar.xz
Source3904:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/europasscv.tar.xz
Source3905:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/europasscv.doc.tar.xz
Source3906:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/europecv.tar.xz
Source3907:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/europecv.doc.tar.xz
Source3908:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/everyhook.tar.xz
Source3909:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/everyhook.doc.tar.xz
Source3911:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/everypage.tar.xz
Source3912:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/everypage.doc.tar.xz
Source3914:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exam.tar.xz
Source3915:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exam.doc.tar.xz
Source3916:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exam-n.tar.xz
Source3917:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exam-n.doc.tar.xz
Source3919:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/examdesign.tar.xz
Source3920:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/examdesign.doc.tar.xz
Source3922:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/example.tar.xz
Source3923:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/examplep.tar.xz
Source3924:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/examplep.doc.tar.xz
Source3927:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/excludeonly.tar.xz
Source3928:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/excludeonly.doc.tar.xz
Source3929:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exercise.tar.xz
Source3930:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exercise.doc.tar.xz
Source3932:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exp-testopt.tar.xz
Source3933:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exp-testopt.doc.tar.xz
Source3935:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/expdlist.tar.xz
Source3936:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/expdlist.doc.tar.xz
Source3938:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/export.tar.xz
Source3939:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/export.doc.tar.xz
Source3941:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exsheets.tar.xz
Source3942:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exsheets.doc.tar.xz
Source3943:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exsol.tar.xz
Source3944:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exsol.doc.tar.xz
Source3946:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/extract.tar.xz
Source3947:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/extract.doc.tar.xz
Source5755:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/enigma.tar.xz
Source5756:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/enigma.doc.tar.xz
Source5834:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebproof.tar.xz
Source5835:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebproof.doc.tar.xz
Source5836:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqnarray.tar.xz
Source5837:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqnarray.doc.tar.xz
Source5839:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/extarrows.tar.xz
Source5840:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/extarrows.doc.tar.xz
Source5841:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/extpfeil.tar.xz
Source5842:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/extpfeil.doc.tar.xz
Source5950:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emp.tar.xz
Source5951:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emp.doc.tar.xz
Source5953:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epsincl.tar.xz
Source5954:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epsincl.doc.tar.xz
Source5955:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/expressg.tar.xz
Source5956:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/expressg.doc.tar.xz
Source5958:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exteps.tar.xz
Source5959:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exteps.doc.tar.xz
Source6075:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epsf-dvipdfmx.tar.xz
Source6076:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epsf-dvipdfmx.doc.tar.xz
Source6350:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebook.tar.xz
Source6351:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebook.doc.tar.xz
Source6352:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebsthesis.tar.xz
Source6353:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebsthesis.doc.tar.xz
Source6355:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ejpecp.tar.xz
Source6356:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ejpecp.doc.tar.xz
Source6358:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ekaia.tar.xz
Source6359:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ekaia.doc.tar.xz
Source6361:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elbioimp.tar.xz
Source6362:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elbioimp.doc.tar.xz
Source6364:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elsarticle.tar.xz
Source6365:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elsarticle.doc.tar.xz
Source6367:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elteikthesis.tar.xz
Source6368:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/elteikthesis.doc.tar.xz
Source6370:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/erdc.tar.xz
Source6371:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/erdc.doc.tar.xz
Source6373:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/estcpmm.tar.xz
Source6374:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/estcpmm.doc.tar.xz
Source6654:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eltex.tar.xz
Source6655:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eltex.doc.tar.xz
Source6656:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endiagram.tar.xz
Source6657:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endiagram.doc.tar.xz
Source6658:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/engtlc.tar.xz
Source6659:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/engtlc.doc.tar.xz
Source7318:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecobiblatex.tar.xz
Source7319:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecobiblatex.doc.tar.xz
Source7320:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/econometrics.tar.xz
Source7321:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/econometrics.doc.tar.xz
Source7322:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/einfuehrung2.doc.tar.xz
Source7323:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ellipse.tar.xz
Source7324:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ellipse.doc.tar.xz
Source7326:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emisa.tar.xz
Source7327:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emisa.doc.tar.xz
Source7329:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exercises.tar.xz
Source7330:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exercises.doc.tar.xz
Source7731:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easyformat.tar.xz
Source7732:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/easyformat.doc.tar.xz
Source7735:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecgdraw.tar.xz
Source7736:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ecgdraw.doc.tar.xz
Source7737:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endofproofwd.tar.xz
Source7738:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endofproofwd.doc.tar.xz
Source7739:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqnalign.tar.xz
Source7740:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqnalign.doc.tar.xz
Source7741:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eulerpx.tar.xz
Source7742:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eulerpx.doc.tar.xz
Source8130:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emf.tar.xz
Source8131:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/emf.doc.tar.xz
Source8132:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endnotesj.tar.xz
Source8133:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/endnotesj.doc.tar.xz
Source8134:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqnnumwarn.tar.xz
Source8135:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eqnnumwarn.doc.tar.xz
Source8136:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/erw-l3.tar.xz
Source8137:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/erw-l3.doc.tar.xz
Source8138:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etsvthor.tar.xz
Source8139:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/etsvthor.doc.tar.xz
Source8140:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/euro-ce.tar.xz
Source8141:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/euro-ce.doc.tar.xz
Source8142:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exercisebank.tar.xz
Source8143:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exercisebank.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.


%package -n texlive-enctex
Provides:       tex-enctex = %{tl_version}
License:        GPL+
Summary:        A TeX extension that translates input on its way into TeX
Version:        svn34957.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(1250-csf.tex) = %{tl_version}, tex(1250-il2.tex) = %{tl_version}
Provides:       tex(1250-latex.tex) = %{tl_version}, tex(1250-t1.tex) = %{tl_version}
Provides:       tex(852-csf.tex) = %{tl_version}, tex(852-il2.tex) = %{tl_version}
Provides:       tex(852-latex.tex) = %{tl_version}, tex(852-t1.tex) = %{tl_version}
Provides:       tex(csfmacro.tex) = %{tl_version}, tex(enc-u.tex) = %{tl_version}
Provides:       tex(encmacro.tex) = %{tl_version}, tex(il2-1250.tex) = %{tl_version}
Provides:       tex(il2-852.tex) = %{tl_version}, tex(il2-csf.tex) = %{tl_version}
Provides:       tex(il2-kam.tex) = %{tl_version}, tex(il2-t1.tex) = %{tl_version}
Provides:       tex(kam-csf.tex) = %{tl_version}, tex(kam-il2.tex) = %{tl_version}
Provides:       tex(kam-latex.tex) = %{tl_version}, tex(kam-t1.tex) = %{tl_version}
Provides:       tex(mixcodes.tex) = %{tl_version}, tex(noprefnt.tex) = %{tl_version}
Provides:       tex(plain-1250-cs.tex) = %{tl_version}, tex(plain-852-cs.tex) = %{tl_version}
Provides:       tex(plain-il2-cs.tex) = %{tl_version}, tex(plain-kam-cs.tex) = %{tl_version}
Provides:       tex(plain-utf8-cs.tex) = %{tl_version}, tex(plain-utf8-ec.tex) = %{tl_version}
Provides:       tex(polyset.tex) = %{tl_version}, tex(t1macro.tex) = %{tl_version}
Provides:       tex(utf8-csf.tex) = %{tl_version}, tex(utf8-t1.tex) = %{tl_version}
Provides:       tex(utf8cseq.tex) = %{tl_version}, tex(utf8lat1.tex) = %{tl_version}
Provides:       tex(utf8lata.tex) = %{tl_version}, tex(utf8math.tex) = %{tl_version}
Provides:       tex(utf8off.tex) = %{tl_version}, tex(utf8raw.tex) = %{tl_version}
Provides:       tex(utf8unkn.tex) = %{tl_version}, tex(utf8warn.tex) = %{tl_version}

%description -n texlive-enctex
EncTeX is (another) TeX extension, written at the change-file
level. It provides means of translating input on the way into
TeX. It allows, for example, translation of multibyte
sequences, such as utf-8 encoding.

%package -n texlive-enctex-doc
Summary:        Documentation for enctex
Version:        svn34957.0

Provides:       tex-enctex-doc
AutoReqProv:    No

%description -n texlive-enctex-doc
Documentation for enctex

%package -n texlive-etex
Provides:       tex-etex = %{tl_version}
License:        Knuth
Summary:        An extended version of TeX, from the NTS project
Version:        svn37057.0
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(xbmc10.tfm) = %{tl_version}

%description -n texlive-etex
An extended version of TeX (which is capable of running as if
it were TeX unmodified). E-TeX has been specified by the LaTeX
team as the engine for the development of LaTeX 2e, in the
immediate future; as a result, LaTeX programmers may (in all
current TeX distributions) assume e-TeX functionality.
Development versions of e-TeX are to be found in the TeX live
source repository.

%package -n texlive-etex-doc
Summary:        Documentation for etex
Version:        svn37057.0
Provides:       tex-etex-doc
AutoReqProv:    No

%description -n texlive-etex-doc
Documentation for etex

%package -n texlive-etex-pkg
Provides:       tex-etex-pkg = %{tl_version}
License:        LPPL
Summary:        E-TeX support package
Version:        svn41784
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(etex.sty) = %{tl_version}

%description -n texlive-etex-pkg
The package provides support for LaTeX documents to use many of
the extensions offered by e-TeX; in particular, it modifies
LaTeX's register allocation macros to make use of the extended
register range. The etextools package provides macros that make
more sophisticated use of e-TeX's facilities.

%package -n texlive-etex-pkg-doc
Summary:        Documentation for etex-pkg
Version:        svn41784
Provides:       tex-etex-pkg-doc
AutoReqProv:    No

%description -n texlive-etex-pkg-doc
Documentation for etex-pkg

%package -n texlive-economic
Provides:       tex-economic = %{tl_version}
License:        LPPL
Summary:        BibTeX support for submitting to Economics journals
Version:        svn32639.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ulem.sty), tex(ifthen.sty), tex(babel.sty), tex(geometry.sty)
Requires:       tex(setspace.sty), tex(titlesec.sty), tex(lmodern.sty), tex(amsmath.sty)
Requires:       tex(url.sty), tex(natbib.sty), tex(endfloat.sty), tex(mathptmx.sty)
Requires:       tex(helvet.sty), tex(courier.sty), tex(bm.sty), tex(endnotes.sty)
Requires:       tex(textcomp.sty), tex(stringstrings.sty)
Requires:       tex(fancyhdr.sty), tex(soul.sty), tex(verbatim.sty)
Provides:       tex(aer.sty) = %{tl_version}, tex(aertt.sty) = %{tl_version}
Provides:       tex(agecon.cls) = %{tl_version}, tex(ajae.cls) = %{tl_version}
Provides:       tex(apecon.cls) = %{tl_version}, tex(cje.sty) = %{tl_version}
Provides:       tex(ecca.cls) = %{tl_version}, tex(erae.cls) = %{tl_version}
Provides:       tex(itaxpf.cls) = %{tl_version}, tex(jrurstud.cls) = %{tl_version}
Provides:       tex(njf.cls) = %{tl_version}, tex(oegatb.cls) = %{tl_version}
Provides:       tex(pocoec.cls) = %{tl_version}, tex(regstud.cls) = %{tl_version}
Provides:       tex(worlddev.cls) = %{tl_version}

%description -n texlive-economic
The bundle offers macros and BibTeX styles for the American
Economic Review (AER), the American Journal of Agricultural
Economics (AJAE), the Canadian Journal of Economics (CJE), the
European Review of Agricultural Economics (ERAE), the
International Economic Review (IER) and Economica. The macro
sets are based on (and require) the harvard package, and all
provide variations of author-date styles of presentation.

%package -n texlive-economic-doc
Summary:        Documentation for economic
Version:        svn32639.0

Provides:       tex-economic-doc
AutoReqProv:    No

%description -n texlive-economic-doc
Documentation for economic

%package -n texlive-ean
Provides:       tex-ean = %{tl_version}
License:        GPL+
Summary:        Macros for making EAN barcodes
Version:        svn20851.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ean13.tex) = %{tl_version}, tex(ean8.tex) = %{tl_version}

%description -n texlive-ean
Provides EAN-8 and EAN-13 forms. The package needs the ocr-b
fonts; note that the fonts are not available under a free
licence, as the macros are.

%package -n texlive-ean-doc
Summary:        Documentation for ean
Version:        svn20851.0

Provides:       tex-ean-doc
AutoReqProv:    No

%description -n texlive-ean-doc
Documentation for ean

%package -n texlive-ebgaramond
Provides:       tex-ebgaramond = %{tl_version}
License:        OFL
Summary:        LaTeX support for EBGaramond fonts
Version:        svn35662.0.16

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty)
Provides:       tex(ebgm_2ahwji.enc) = %{tl_version}, tex(ebgm_2cg6vv.enc) = %{tl_version}
Provides:       tex(ebgm_2jdbaj.enc) = %{tl_version}, tex(ebgm_2qji24.enc) = %{tl_version}
Provides:       tex(ebgm_2s43qf.enc) = %{tl_version}, tex(ebgm_2z5l6v.enc) = %{tl_version}
Provides:       tex(ebgm_3rwz74.enc) = %{tl_version}, tex(ebgm_4bz7gr.enc) = %{tl_version}
Provides:       tex(ebgm_4o5twj.enc) = %{tl_version}, tex(ebgm_6qsdbg.enc) = %{tl_version}
Provides:       tex(ebgm_73unsq.enc) = %{tl_version}, tex(ebgm_73usqg.enc) = %{tl_version}
Provides:       tex(ebgm_7qoeji.enc) = %{tl_version}, tex(ebgm_7vyzed.enc) = %{tl_version}
Provides:       tex(ebgm_afjqor.enc) = %{tl_version}, tex(ebgm_anxopp.enc) = %{tl_version}
Provides:       tex(ebgm_apg365.enc) = %{tl_version}, tex(ebgm_bm4jeu.enc) = %{tl_version}
Provides:       tex(ebgm_cx2on6.enc) = %{tl_version}, tex(ebgm_dx53yq.enc) = %{tl_version}
Provides:       tex(ebgm_e7e6uz.enc) = %{tl_version}, tex(ebgm_evsh4b.enc) = %{tl_version}
Provides:       tex(ebgm_fn43k6.enc) = %{tl_version}, tex(ebgm_g7yatv.enc) = %{tl_version}
Provides:       tex(ebgm_gk35hz.enc) = %{tl_version}, tex(ebgm_gmvmrc.enc) = %{tl_version}
Provides:       tex(ebgm_gsqhuu.enc) = %{tl_version}, tex(ebgm_gzwq56.enc) = %{tl_version}
Provides:       tex(ebgm_hbc3re.enc) = %{tl_version}, tex(ebgm_hjfzcx.enc) = %{tl_version}
Provides:       tex(ebgm_i7zvqf.enc) = %{tl_version}, tex(ebgm_iymieh.enc) = %{tl_version}
Provides:       tex(ebgm_j3s3oh.enc) = %{tl_version}, tex(ebgm_jf2v6g.enc) = %{tl_version}
Provides:       tex(ebgm_jwyujo.enc) = %{tl_version}, tex(ebgm_kmvlni.enc) = %{tl_version}
Provides:       tex(ebgm_ku4qmh.enc) = %{tl_version}, tex(ebgm_kzajuf.enc) = %{tl_version}
Provides:       tex(ebgm_l5duak.enc) = %{tl_version}, tex(ebgm_l6jy5u.enc) = %{tl_version}
Provides:       tex(ebgm_liamow.enc) = %{tl_version}, tex(ebgm_lz6s54.enc) = %{tl_version}
Provides:       tex(ebgm_m4xdvf.enc) = %{tl_version}, tex(ebgm_mqmdo5.enc) = %{tl_version}
Provides:       tex(ebgm_mvmxzb.enc) = %{tl_version}, tex(ebgm_n5uvbv.enc) = %{tl_version}
Provides:       tex(ebgm_n6g2jk.enc) = %{tl_version}, tex(ebgm_ny6sxo.enc) = %{tl_version}
Provides:       tex(ebgm_o6elnt.enc) = %{tl_version}, tex(ebgm_q57nnl.enc) = %{tl_version}
Provides:       tex(ebgm_qgwbgp.enc) = %{tl_version}, tex(ebgm_qjlp7p.enc) = %{tl_version}
Provides:       tex(ebgm_qrhapd.enc) = %{tl_version}, tex(ebgm_r7l7q7.enc) = %{tl_version}
Provides:       tex(ebgm_rcjgcc.enc) = %{tl_version}, tex(ebgm_suwt22.enc) = %{tl_version}
Provides:       tex(ebgm_twdjbv.enc) = %{tl_version}, tex(ebgm_uroaj5.enc) = %{tl_version}
Provides:       tex(ebgm_vhiyif.enc) = %{tl_version}, tex(ebgm_voynk7.enc) = %{tl_version}
Provides:       tex(ebgm_w43j3l.enc) = %{tl_version}, tex(ebgm_wqntdr.enc) = %{tl_version}
Provides:       tex(ebgm_xbjzpk.enc) = %{tl_version}, tex(ebgm_xfziqt.enc) = %{tl_version}
Provides:       tex(ebgm_xkuggc.enc) = %{tl_version}, tex(ebgm_y3lrq6.enc) = %{tl_version}
Provides:       tex(ebgm_yhoxvo.enc) = %{tl_version}, tex(ebgm_zf3ijx.enc) = %{tl_version}
Provides:       tex(ebgm_zu3eah.enc) = %{tl_version}, tex(EBGaramond.map) = %{tl_version}
Provides:       tex(EBGaramond12-Italic.otf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular.otf) = %{tl_version}
Provides:       tex(EBGaramondInitials.otf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-swash-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-swash-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-swash-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-swash-ot1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(EBGaramondInitials-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramondInitials-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(EBGaramondInitials-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(EBGaramondInitials-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(EBGaramondInitials-tlf-t1.tfm) = %{tl_version}
Provides:       tex(EBGaramondInitials-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(EBGaramond12-Italic.pfb) = %{tl_version}
Provides:       tex(EBGaramond12-Regular.pfb) = %{tl_version}
Provides:       tex(EBGaramondInitials.pfb) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-swash-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-swash-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-swash-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-swash-ot1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(EBGaramond12-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(EBGaramondInitials-tlf-ly1.vf) = %{tl_version}
Provides:       tex(EBGaramondInitials-tlf-t1.vf) = %{tl_version}
Provides:       tex(EBGaramondInitials-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1EBGaramond-Inf.fd) = %{tl_version}
Provides:       tex(LY1EBGaramond-LF.fd) = %{tl_version}
Provides:       tex(LY1EBGaramond-OsF.fd) = %{tl_version}
Provides:       tex(LY1EBGaramond-Sup.fd) = %{tl_version}
Provides:       tex(LY1EBGaramond-TLF.fd) = %{tl_version}
Provides:       tex(LY1EBGaramond-TOsF.fd) = %{tl_version}
Provides:       tex(LY1EBGaramondInitials-TLF.fd) = %{tl_version}
Provides:       tex(OT1EBGaramond-Inf.fd) = %{tl_version}
Provides:       tex(OT1EBGaramond-LF.fd) = %{tl_version}
Provides:       tex(OT1EBGaramond-OsF.fd) = %{tl_version}
Provides:       tex(OT1EBGaramond-Sup.fd) = %{tl_version}
Provides:       tex(OT1EBGaramond-TLF.fd) = %{tl_version}
Provides:       tex(OT1EBGaramond-TOsF.fd) = %{tl_version}
Provides:       tex(OT1EBGaramondInitials-TLF.fd) = %{tl_version}
Provides:       tex(T1EBGaramond-Inf.fd) = %{tl_version}
Provides:       tex(T1EBGaramond-LF.fd) = %{tl_version}, tex(T1EBGaramond-OsF.fd) = %{tl_version}
Provides:       tex(T1EBGaramond-Sup.fd) = %{tl_version}
Provides:       tex(T1EBGaramond-TLF.fd) = %{tl_version}
Provides:       tex(T1EBGaramond-TOsF.fd) = %{tl_version}
Provides:       tex(T1EBGaramondInitials-TLF.fd) = %{tl_version}
Provides:       tex(TS1EBGaramond-LF.fd) = %{tl_version}
Provides:       tex(TS1EBGaramond-OsF.fd) = %{tl_version}
Provides:       tex(TS1EBGaramond-TLF.fd) = %{tl_version}
Provides:       tex(TS1EBGaramond-TOsF.fd) = %{tl_version}
Provides:       tex(TS1EBGaramondInitials-TLF.fd) = %{tl_version}
Provides:       tex(ebgaramond.sty) = %{tl_version}, tex(mt-EBGaramond.cfg) = %{tl_version}

%description -n texlive-ebgaramond
EB Garamond is a revival by Georg Duffner of the 16th century
fonts designed by Claude Garamond. The LaTeX support package
works for (pdf)LaTeX, xeLaTeX and luaLaTeX users; configuration
files for use with microtype are provided.

%package -n texlive-ebgaramond-doc
Summary:        Documentation for ebgaramond
Version:        svn35662.0.16

Provides:       tex-ebgaramond-doc
AutoReqProv:    No

%description -n texlive-ebgaramond-doc
Documentation for ebgaramond

%package -n texlive-ebgaramond-maths
Provides:       tex-ebgaramond-maths = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX support for EBGaramond fonts in mathematics
Version:        svn35701.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ebgaramond.sty)
Provides:       tex(a_42pejf.enc) = %{tl_version}, tex(EBGaramond-Maths.map) = %{tl_version}
Provides:       tex(EBGaramond12-Italic--oml-ebgaramond.tfm) = %{tl_version}
Provides:       tex(OMLEBGaramond-Maths.fd) = %{tl_version}
Provides:       tex(ebgaramond-maths.sty) = %{tl_version}

%description -n texlive-ebgaramond-maths
This package provides some LaTeX support for the use of
EBGaramond12 in mathematics. It is based on, and requires,
ebgaramond. The package was created in response to a question
at TeX-stackexchange. and tested in the form of an answer in
the same forum.

%package -n texlive-ebgaramond-maths-doc
Summary:        Documentation for ebgaramond-maths
Version:        svn35701.1.1

Provides:       tex-ebgaramond-maths-doc
AutoReqProv:    No

%description -n texlive-ebgaramond-maths-doc
Documentation for ebgaramond-maths

%package -n texlive-ecc
Provides:       tex-ecc = %{tl_version}
License:        LPPL
Summary:        Sources for the European Concrete fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(eocc10.tfm) = %{tl_version}, tex(eorm10.tfm) = %{tl_version}
Provides:       tex(eorm5.tfm) = %{tl_version}, tex(eorm6.tfm) = %{tl_version}
Provides:       tex(eorm7.tfm) = %{tl_version}, tex(eorm8.tfm) = %{tl_version}
Provides:       tex(eorm9.tfm) = %{tl_version}, tex(eosl10.tfm) = %{tl_version}
Provides:       tex(eosl5.tfm) = %{tl_version}, tex(eosl6.tfm) = %{tl_version}
Provides:       tex(eosl7.tfm) = %{tl_version}, tex(eosl8.tfm) = %{tl_version}
Provides:       tex(eosl9.tfm) = %{tl_version}, tex(eoti10.tfm) = %{tl_version}
Provides:       tex(tcssdc10.tfm) = %{tl_version}, tex(torm10.tfm) = %{tl_version}
Provides:       tex(torm5.tfm) = %{tl_version}, tex(torm6.tfm) = %{tl_version}
Provides:       tex(torm7.tfm) = %{tl_version}, tex(torm8.tfm) = %{tl_version}
Provides:       tex(torm9.tfm) = %{tl_version}, tex(tosl10.tfm) = %{tl_version}
Provides:       tex(tosl5.tfm) = %{tl_version}, tex(tosl6.tfm) = %{tl_version}
Provides:       tex(tosl7.tfm) = %{tl_version}, tex(tosl8.tfm) = %{tl_version}
Provides:       tex(tosl9.tfm) = %{tl_version}, tex(toti10.tfm) = %{tl_version}

%description -n texlive-ecc
The Metafont sources and TFM files of the European Concrete
Fonts. This is the T1-encoded extension of Knuth's Concrete
fonts, including also the corresponding text companion fonts.
Adobe Type 1 versions of the fonts are available as part of the
cm-super font bundle.

%package -n texlive-ecc-doc
Summary:        Documentation for ecc
Version:        svn15878.0

Provides:       tex-ecc-doc
AutoReqProv:    No

%description -n texlive-ecc-doc
Documentation for ecc

%package -n texlive-eco
Provides:       tex-eco = %{tl_version}
License:        GPL+
Summary:        Oldstyle numerals using EC fonts
Version:        svn29349.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontenc.sty), tex(ifthen.sty)
Provides:       tex(ecobi0500.tfm) = %{tl_version}, tex(ecobi0600.tfm) = %{tl_version}
Provides:       tex(ecobi0700.tfm) = %{tl_version}, tex(ecobi0800.tfm) = %{tl_version}
Provides:       tex(ecobi0900.tfm) = %{tl_version}, tex(ecobi1000.tfm) = %{tl_version}
Provides:       tex(ecobi1095.tfm) = %{tl_version}, tex(ecobi1200.tfm) = %{tl_version}
Provides:       tex(ecobi1440.tfm) = %{tl_version}, tex(ecobi1728.tfm) = %{tl_version}
Provides:       tex(ecobi2074.tfm) = %{tl_version}, tex(ecobi2488.tfm) = %{tl_version}
Provides:       tex(ecobi2986.tfm) = %{tl_version}, tex(ecobi3583.tfm) = %{tl_version}
Provides:       tex(ecobl0500.tfm) = %{tl_version}, tex(ecobl0600.tfm) = %{tl_version}
Provides:       tex(ecobl0700.tfm) = %{tl_version}, tex(ecobl0800.tfm) = %{tl_version}
Provides:       tex(ecobl0900.tfm) = %{tl_version}, tex(ecobl1000.tfm) = %{tl_version}
Provides:       tex(ecobl1095.tfm) = %{tl_version}, tex(ecobl1200.tfm) = %{tl_version}
Provides:       tex(ecobl1440.tfm) = %{tl_version}, tex(ecobl1728.tfm) = %{tl_version}
Provides:       tex(ecobl2074.tfm) = %{tl_version}, tex(ecobl2488.tfm) = %{tl_version}
Provides:       tex(ecobl2986.tfm) = %{tl_version}, tex(ecobl3583.tfm) = %{tl_version}
Provides:       tex(ecobx0500.tfm) = %{tl_version}, tex(ecobx0600.tfm) = %{tl_version}
Provides:       tex(ecobx0700.tfm) = %{tl_version}, tex(ecobx0800.tfm) = %{tl_version}
Provides:       tex(ecobx0900.tfm) = %{tl_version}, tex(ecobx1000.tfm) = %{tl_version}
Provides:       tex(ecobx1095.tfm) = %{tl_version}, tex(ecobx1200.tfm) = %{tl_version}
Provides:       tex(ecobx1440.tfm) = %{tl_version}, tex(ecobx1728.tfm) = %{tl_version}
Provides:       tex(ecobx2074.tfm) = %{tl_version}, tex(ecobx2488.tfm) = %{tl_version}
Provides:       tex(ecobx2986.tfm) = %{tl_version}, tex(ecobx3583.tfm) = %{tl_version}
Provides:       tex(ecodh0500.tfm) = %{tl_version}, tex(ecodh0600.tfm) = %{tl_version}
Provides:       tex(ecodh0700.tfm) = %{tl_version}, tex(ecodh0800.tfm) = %{tl_version}
Provides:       tex(ecodh0900.tfm) = %{tl_version}, tex(ecodh1000.tfm) = %{tl_version}
Provides:       tex(ecodh1095.tfm) = %{tl_version}, tex(ecodh1200.tfm) = %{tl_version}
Provides:       tex(ecodh1440.tfm) = %{tl_version}, tex(ecodh1728.tfm) = %{tl_version}
Provides:       tex(ecodh2074.tfm) = %{tl_version}, tex(ecodh2488.tfm) = %{tl_version}
Provides:       tex(ecodh2986.tfm) = %{tl_version}, tex(ecodh3583.tfm) = %{tl_version}
Provides:       tex(ecoit0600.tfm) = %{tl_version}, tex(ecoit0700.tfm) = %{tl_version}
Provides:       tex(ecoit0800.tfm) = %{tl_version}, tex(ecoit0900.tfm) = %{tl_version}
Provides:       tex(ecoit1000.tfm) = %{tl_version}, tex(ecoit1095.tfm) = %{tl_version}
Provides:       tex(ecoit1200.tfm) = %{tl_version}, tex(ecoit1440.tfm) = %{tl_version}
Provides:       tex(ecoit1728.tfm) = %{tl_version}, tex(ecoit2074.tfm) = %{tl_version}
Provides:       tex(ecoit2488.tfm) = %{tl_version}, tex(ecoit2986.tfm) = %{tl_version}
Provides:       tex(ecoit3583.tfm) = %{tl_version}, tex(ecorb0500.tfm) = %{tl_version}
Provides:       tex(ecorb0600.tfm) = %{tl_version}, tex(ecorb0700.tfm) = %{tl_version}
Provides:       tex(ecorb0800.tfm) = %{tl_version}, tex(ecorb0900.tfm) = %{tl_version}
Provides:       tex(ecorb1000.tfm) = %{tl_version}, tex(ecorb1095.tfm) = %{tl_version}
Provides:       tex(ecorb1200.tfm) = %{tl_version}, tex(ecorb1440.tfm) = %{tl_version}
Provides:       tex(ecorb1728.tfm) = %{tl_version}, tex(ecorb2074.tfm) = %{tl_version}
Provides:       tex(ecorb2488.tfm) = %{tl_version}, tex(ecorb2986.tfm) = %{tl_version}
Provides:       tex(ecorb3583.tfm) = %{tl_version}, tex(ecorm0500.tfm) = %{tl_version}
Provides:       tex(ecorm0600.tfm) = %{tl_version}, tex(ecorm0700.tfm) = %{tl_version}
Provides:       tex(ecorm0800.tfm) = %{tl_version}, tex(ecorm0900.tfm) = %{tl_version}
Provides:       tex(ecorm1000.tfm) = %{tl_version}, tex(ecorm1095.tfm) = %{tl_version}
Provides:       tex(ecorm1200.tfm) = %{tl_version}, tex(ecorm1440.tfm) = %{tl_version}
Provides:       tex(ecorm1728.tfm) = %{tl_version}, tex(ecorm2074.tfm) = %{tl_version}
Provides:       tex(ecorm2488.tfm) = %{tl_version}, tex(ecorm2986.tfm) = %{tl_version}
Provides:       tex(ecorm3583.tfm) = %{tl_version}, tex(ecosi0500.tfm) = %{tl_version}
Provides:       tex(ecosi0600.tfm) = %{tl_version}, tex(ecosi0700.tfm) = %{tl_version}
Provides:       tex(ecosi0800.tfm) = %{tl_version}, tex(ecosi0900.tfm) = %{tl_version}
Provides:       tex(ecosi1000.tfm) = %{tl_version}, tex(ecosi1095.tfm) = %{tl_version}
Provides:       tex(ecosi1200.tfm) = %{tl_version}, tex(ecosi1440.tfm) = %{tl_version}
Provides:       tex(ecosi1728.tfm) = %{tl_version}, tex(ecosi2074.tfm) = %{tl_version}
Provides:       tex(ecosi2488.tfm) = %{tl_version}, tex(ecosi2986.tfm) = %{tl_version}
Provides:       tex(ecosi3583.tfm) = %{tl_version}, tex(ecosl0500.tfm) = %{tl_version}
Provides:       tex(ecosl0600.tfm) = %{tl_version}, tex(ecosl0700.tfm) = %{tl_version}
Provides:       tex(ecosl0800.tfm) = %{tl_version}, tex(ecosl0900.tfm) = %{tl_version}
Provides:       tex(ecosl1000.tfm) = %{tl_version}, tex(ecosl1095.tfm) = %{tl_version}
Provides:       tex(ecosl1200.tfm) = %{tl_version}, tex(ecosl1440.tfm) = %{tl_version}
Provides:       tex(ecosl1728.tfm) = %{tl_version}, tex(ecosl2074.tfm) = %{tl_version}
Provides:       tex(ecosl2488.tfm) = %{tl_version}, tex(ecosl2986.tfm) = %{tl_version}
Provides:       tex(ecosl3583.tfm) = %{tl_version}, tex(ecoso0500.tfm) = %{tl_version}
Provides:       tex(ecoso0600.tfm) = %{tl_version}, tex(ecoso0700.tfm) = %{tl_version}
Provides:       tex(ecoso0800.tfm) = %{tl_version}, tex(ecoso0900.tfm) = %{tl_version}
Provides:       tex(ecoso1000.tfm) = %{tl_version}, tex(ecoso1095.tfm) = %{tl_version}
Provides:       tex(ecoso1200.tfm) = %{tl_version}, tex(ecoso1440.tfm) = %{tl_version}
Provides:       tex(ecoso1728.tfm) = %{tl_version}, tex(ecoso2074.tfm) = %{tl_version}
Provides:       tex(ecoso2488.tfm) = %{tl_version}, tex(ecoso2986.tfm) = %{tl_version}
Provides:       tex(ecoso3583.tfm) = %{tl_version}, tex(ecoss0500.tfm) = %{tl_version}
Provides:       tex(ecoss0600.tfm) = %{tl_version}, tex(ecoss0700.tfm) = %{tl_version}
Provides:       tex(ecoss0800.tfm) = %{tl_version}, tex(ecoss0900.tfm) = %{tl_version}
Provides:       tex(ecoss1000.tfm) = %{tl_version}, tex(ecoss1095.tfm) = %{tl_version}
Provides:       tex(ecoss1200.tfm) = %{tl_version}, tex(ecoss1440.tfm) = %{tl_version}
Provides:       tex(ecoss1728.tfm) = %{tl_version}, tex(ecoss2074.tfm) = %{tl_version}
Provides:       tex(ecoss2488.tfm) = %{tl_version}, tex(ecoss2986.tfm) = %{tl_version}
Provides:       tex(ecoss3583.tfm) = %{tl_version}, tex(ecost0600.tfm) = %{tl_version}
Provides:       tex(ecost0700.tfm) = %{tl_version}, tex(ecost0800.tfm) = %{tl_version}
Provides:       tex(ecost0900.tfm) = %{tl_version}, tex(ecost1000.tfm) = %{tl_version}
Provides:       tex(ecost1095.tfm) = %{tl_version}, tex(ecost1200.tfm) = %{tl_version}
Provides:       tex(ecost1440.tfm) = %{tl_version}, tex(ecost1728.tfm) = %{tl_version}
Provides:       tex(ecost2074.tfm) = %{tl_version}, tex(ecost2488.tfm) = %{tl_version}
Provides:       tex(ecost2986.tfm) = %{tl_version}, tex(ecost3583.tfm) = %{tl_version}
Provides:       tex(ecosx0500.tfm) = %{tl_version}, tex(ecosx0600.tfm) = %{tl_version}
Provides:       tex(ecosx0700.tfm) = %{tl_version}, tex(ecosx0800.tfm) = %{tl_version}
Provides:       tex(ecosx0900.tfm) = %{tl_version}, tex(ecosx1000.tfm) = %{tl_version}
Provides:       tex(ecosx1095.tfm) = %{tl_version}, tex(ecosx1200.tfm) = %{tl_version}
Provides:       tex(ecosx1440.tfm) = %{tl_version}, tex(ecosx1728.tfm) = %{tl_version}
Provides:       tex(ecosx2074.tfm) = %{tl_version}, tex(ecosx2488.tfm) = %{tl_version}
Provides:       tex(ecosx2986.tfm) = %{tl_version}, tex(ecosx3583.tfm) = %{tl_version}
Provides:       tex(ecoti0500.tfm) = %{tl_version}, tex(ecoti0600.tfm) = %{tl_version}
Provides:       tex(ecoti0700.tfm) = %{tl_version}, tex(ecoti0800.tfm) = %{tl_version}
Provides:       tex(ecoti0900.tfm) = %{tl_version}, tex(ecoti1000.tfm) = %{tl_version}
Provides:       tex(ecoti1095.tfm) = %{tl_version}, tex(ecoti1200.tfm) = %{tl_version}
Provides:       tex(ecoti1440.tfm) = %{tl_version}, tex(ecoti1728.tfm) = %{tl_version}
Provides:       tex(ecoti2074.tfm) = %{tl_version}, tex(ecoti2488.tfm) = %{tl_version}
Provides:       tex(ecoti2986.tfm) = %{tl_version}, tex(ecoti3583.tfm) = %{tl_version}
Provides:       tex(ecott0600.tfm) = %{tl_version}, tex(ecott0700.tfm) = %{tl_version}
Provides:       tex(ecott0800.tfm) = %{tl_version}, tex(ecott0900.tfm) = %{tl_version}
Provides:       tex(ecott1000.tfm) = %{tl_version}, tex(ecott1095.tfm) = %{tl_version}
Provides:       tex(ecott1200.tfm) = %{tl_version}, tex(ecott1440.tfm) = %{tl_version}
Provides:       tex(ecott1728.tfm) = %{tl_version}, tex(ecott2074.tfm) = %{tl_version}
Provides:       tex(ecott2488.tfm) = %{tl_version}, tex(ecott2986.tfm) = %{tl_version}
Provides:       tex(ecott3583.tfm) = %{tl_version}, tex(ecoui0500.tfm) = %{tl_version}
Provides:       tex(ecoui0600.tfm) = %{tl_version}, tex(ecoui0700.tfm) = %{tl_version}
Provides:       tex(ecoui0800.tfm) = %{tl_version}, tex(ecoui0900.tfm) = %{tl_version}
Provides:       tex(ecoui1000.tfm) = %{tl_version}, tex(ecoui1095.tfm) = %{tl_version}
Provides:       tex(ecoui1200.tfm) = %{tl_version}, tex(ecoui1440.tfm) = %{tl_version}
Provides:       tex(ecoui1728.tfm) = %{tl_version}, tex(ecoui2074.tfm) = %{tl_version}
Provides:       tex(ecoui2488.tfm) = %{tl_version}, tex(ecoui2986.tfm) = %{tl_version}
Provides:       tex(ecoui3583.tfm) = %{tl_version}, tex(ecovi0600.tfm) = %{tl_version}
Provides:       tex(ecovi0700.tfm) = %{tl_version}, tex(ecovi0800.tfm) = %{tl_version}
Provides:       tex(ecovi0900.tfm) = %{tl_version}, tex(ecovi1000.tfm) = %{tl_version}
Provides:       tex(ecovi1095.tfm) = %{tl_version}, tex(ecovi1200.tfm) = %{tl_version}
Provides:       tex(ecovi1440.tfm) = %{tl_version}, tex(ecovi1728.tfm) = %{tl_version}
Provides:       tex(ecovi2074.tfm) = %{tl_version}, tex(ecovi2488.tfm) = %{tl_version}
Provides:       tex(ecovi2986.tfm) = %{tl_version}, tex(ecovi3583.tfm) = %{tl_version}
Provides:       tex(ecovt0600.tfm) = %{tl_version}, tex(ecovt0700.tfm) = %{tl_version}
Provides:       tex(ecovt0800.tfm) = %{tl_version}, tex(ecovt0900.tfm) = %{tl_version}
Provides:       tex(ecovt1000.tfm) = %{tl_version}, tex(ecovt1095.tfm) = %{tl_version}
Provides:       tex(ecovt1200.tfm) = %{tl_version}, tex(ecovt1440.tfm) = %{tl_version}
Provides:       tex(ecovt1728.tfm) = %{tl_version}, tex(ecovt2074.tfm) = %{tl_version}
Provides:       tex(ecovt2488.tfm) = %{tl_version}, tex(ecovt2986.tfm) = %{tl_version}
Provides:       tex(ecovt3583.tfm) = %{tl_version}, tex(ecobi0500.vf) = %{tl_version}
Provides:       tex(ecobi0600.vf) = %{tl_version}, tex(ecobi0700.vf) = %{tl_version}
Provides:       tex(ecobi0800.vf) = %{tl_version}, tex(ecobi0900.vf) = %{tl_version}
Provides:       tex(ecobi1000.vf) = %{tl_version}, tex(ecobi1095.vf) = %{tl_version}
Provides:       tex(ecobi1200.vf) = %{tl_version}, tex(ecobi1440.vf) = %{tl_version}
Provides:       tex(ecobi1728.vf) = %{tl_version}, tex(ecobi2074.vf) = %{tl_version}
Provides:       tex(ecobi2488.vf) = %{tl_version}, tex(ecobi2986.vf) = %{tl_version}
Provides:       tex(ecobi3583.vf) = %{tl_version}, tex(ecobl0500.vf) = %{tl_version}
Provides:       tex(ecobl0600.vf) = %{tl_version}, tex(ecobl0700.vf) = %{tl_version}
Provides:       tex(ecobl0800.vf) = %{tl_version}, tex(ecobl0900.vf) = %{tl_version}
Provides:       tex(ecobl1000.vf) = %{tl_version}, tex(ecobl1095.vf) = %{tl_version}
Provides:       tex(ecobl1200.vf) = %{tl_version}, tex(ecobl1440.vf) = %{tl_version}
Provides:       tex(ecobl1728.vf) = %{tl_version}, tex(ecobl2074.vf) = %{tl_version}
Provides:       tex(ecobl2488.vf) = %{tl_version}, tex(ecobl2986.vf) = %{tl_version}
Provides:       tex(ecobl3583.vf) = %{tl_version}, tex(ecobx0500.vf) = %{tl_version}
Provides:       tex(ecobx0600.vf) = %{tl_version}, tex(ecobx0700.vf) = %{tl_version}
Provides:       tex(ecobx0800.vf) = %{tl_version}, tex(ecobx0900.vf) = %{tl_version}
Provides:       tex(ecobx1000.vf) = %{tl_version}, tex(ecobx1095.vf) = %{tl_version}
Provides:       tex(ecobx1200.vf) = %{tl_version}, tex(ecobx1440.vf) = %{tl_version}
Provides:       tex(ecobx1728.vf) = %{tl_version}, tex(ecobx2074.vf) = %{tl_version}
Provides:       tex(ecobx2488.vf) = %{tl_version}, tex(ecobx2986.vf) = %{tl_version}
Provides:       tex(ecobx3583.vf) = %{tl_version}, tex(ecodh0500.vf) = %{tl_version}
Provides:       tex(ecodh0600.vf) = %{tl_version}, tex(ecodh0700.vf) = %{tl_version}
Provides:       tex(ecodh0800.vf) = %{tl_version}, tex(ecodh0900.vf) = %{tl_version}
Provides:       tex(ecodh1000.vf) = %{tl_version}, tex(ecodh1095.vf) = %{tl_version}
Provides:       tex(ecodh1200.vf) = %{tl_version}, tex(ecodh1440.vf) = %{tl_version}
Provides:       tex(ecodh1728.vf) = %{tl_version}, tex(ecodh2074.vf) = %{tl_version}
Provides:       tex(ecodh2488.vf) = %{tl_version}, tex(ecodh2986.vf) = %{tl_version}
Provides:       tex(ecodh3583.vf) = %{tl_version}, tex(ecoit0600.vf) = %{tl_version}
Provides:       tex(ecoit0700.vf) = %{tl_version}, tex(ecoit0800.vf) = %{tl_version}
Provides:       tex(ecoit0900.vf) = %{tl_version}, tex(ecoit1000.vf) = %{tl_version}
Provides:       tex(ecoit1095.vf) = %{tl_version}, tex(ecoit1200.vf) = %{tl_version}
Provides:       tex(ecoit1440.vf) = %{tl_version}, tex(ecoit1728.vf) = %{tl_version}
Provides:       tex(ecoit2074.vf) = %{tl_version}, tex(ecoit2488.vf) = %{tl_version}
Provides:       tex(ecoit2986.vf) = %{tl_version}, tex(ecoit3583.vf) = %{tl_version}
Provides:       tex(ecorb0500.vf) = %{tl_version}, tex(ecorb0600.vf) = %{tl_version}
Provides:       tex(ecorb0700.vf) = %{tl_version}, tex(ecorb0800.vf) = %{tl_version}
Provides:       tex(ecorb0900.vf) = %{tl_version}, tex(ecorb1000.vf) = %{tl_version}
Provides:       tex(ecorb1095.vf) = %{tl_version}, tex(ecorb1200.vf) = %{tl_version}
Provides:       tex(ecorb1440.vf) = %{tl_version}, tex(ecorb1728.vf) = %{tl_version}
Provides:       tex(ecorb2074.vf) = %{tl_version}, tex(ecorb2488.vf) = %{tl_version}
Provides:       tex(ecorb2986.vf) = %{tl_version}, tex(ecorb3583.vf) = %{tl_version}
Provides:       tex(ecorm0500.vf) = %{tl_version}, tex(ecorm0600.vf) = %{tl_version}
Provides:       tex(ecorm0700.vf) = %{tl_version}, tex(ecorm0800.vf) = %{tl_version}
Provides:       tex(ecorm0900.vf) = %{tl_version}, tex(ecorm1000.vf) = %{tl_version}
Provides:       tex(ecorm1095.vf) = %{tl_version}, tex(ecorm1200.vf) = %{tl_version}
Provides:       tex(ecorm1440.vf) = %{tl_version}, tex(ecorm1728.vf) = %{tl_version}
Provides:       tex(ecorm2074.vf) = %{tl_version}, tex(ecorm2488.vf) = %{tl_version}
Provides:       tex(ecorm2986.vf) = %{tl_version}, tex(ecorm3583.vf) = %{tl_version}
Provides:       tex(ecosi0500.vf) = %{tl_version}, tex(ecosi0600.vf) = %{tl_version}
Provides:       tex(ecosi0700.vf) = %{tl_version}, tex(ecosi0800.vf) = %{tl_version}
Provides:       tex(ecosi0900.vf) = %{tl_version}, tex(ecosi1000.vf) = %{tl_version}
Provides:       tex(ecosi1095.vf) = %{tl_version}, tex(ecosi1200.vf) = %{tl_version}
Provides:       tex(ecosi1440.vf) = %{tl_version}, tex(ecosi1728.vf) = %{tl_version}
Provides:       tex(ecosi2074.vf) = %{tl_version}, tex(ecosi2488.vf) = %{tl_version}
Provides:       tex(ecosi2986.vf) = %{tl_version}, tex(ecosi3583.vf) = %{tl_version}
Provides:       tex(ecosl0500.vf) = %{tl_version}, tex(ecosl0600.vf) = %{tl_version}
Provides:       tex(ecosl0700.vf) = %{tl_version}, tex(ecosl0800.vf) = %{tl_version}
Provides:       tex(ecosl0900.vf) = %{tl_version}, tex(ecosl1000.vf) = %{tl_version}
Provides:       tex(ecosl1095.vf) = %{tl_version}, tex(ecosl1200.vf) = %{tl_version}
Provides:       tex(ecosl1440.vf) = %{tl_version}, tex(ecosl1728.vf) = %{tl_version}
Provides:       tex(ecosl2074.vf) = %{tl_version}, tex(ecosl2488.vf) = %{tl_version}
Provides:       tex(ecosl2986.vf) = %{tl_version}, tex(ecosl3583.vf) = %{tl_version}
Provides:       tex(ecoso0500.vf) = %{tl_version}, tex(ecoso0600.vf) = %{tl_version}
Provides:       tex(ecoso0700.vf) = %{tl_version}, tex(ecoso0800.vf) = %{tl_version}
Provides:       tex(ecoso0900.vf) = %{tl_version}, tex(ecoso1000.vf) = %{tl_version}
Provides:       tex(ecoso1095.vf) = %{tl_version}, tex(ecoso1200.vf) = %{tl_version}
Provides:       tex(ecoso1440.vf) = %{tl_version}, tex(ecoso1728.vf) = %{tl_version}
Provides:       tex(ecoso2074.vf) = %{tl_version}, tex(ecoso2488.vf) = %{tl_version}
Provides:       tex(ecoso2986.vf) = %{tl_version}, tex(ecoso3583.vf) = %{tl_version}
Provides:       tex(ecoss0500.vf) = %{tl_version}, tex(ecoss0600.vf) = %{tl_version}
Provides:       tex(ecoss0700.vf) = %{tl_version}, tex(ecoss0800.vf) = %{tl_version}
Provides:       tex(ecoss0900.vf) = %{tl_version}, tex(ecoss1000.vf) = %{tl_version}
Provides:       tex(ecoss1095.vf) = %{tl_version}, tex(ecoss1200.vf) = %{tl_version}
Provides:       tex(ecoss1440.vf) = %{tl_version}, tex(ecoss1728.vf) = %{tl_version}
Provides:       tex(ecoss2074.vf) = %{tl_version}, tex(ecoss2488.vf) = %{tl_version}
Provides:       tex(ecoss2986.vf) = %{tl_version}, tex(ecoss3583.vf) = %{tl_version}
Provides:       tex(ecost0600.vf) = %{tl_version}, tex(ecost0700.vf) = %{tl_version}
Provides:       tex(ecost0800.vf) = %{tl_version}, tex(ecost0900.vf) = %{tl_version}
Provides:       tex(ecost1000.vf) = %{tl_version}, tex(ecost1095.vf) = %{tl_version}
Provides:       tex(ecost1200.vf) = %{tl_version}, tex(ecost1440.vf) = %{tl_version}
Provides:       tex(ecost1728.vf) = %{tl_version}, tex(ecost2074.vf) = %{tl_version}
Provides:       tex(ecost2488.vf) = %{tl_version}, tex(ecost2986.vf) = %{tl_version}
Provides:       tex(ecost3583.vf) = %{tl_version}, tex(ecosx0500.vf) = %{tl_version}
Provides:       tex(ecosx0600.vf) = %{tl_version}, tex(ecosx0700.vf) = %{tl_version}
Provides:       tex(ecosx0800.vf) = %{tl_version}, tex(ecosx0900.vf) = %{tl_version}
Provides:       tex(ecosx1000.vf) = %{tl_version}, tex(ecosx1095.vf) = %{tl_version}
Provides:       tex(ecosx1200.vf) = %{tl_version}, tex(ecosx1440.vf) = %{tl_version}
Provides:       tex(ecosx1728.vf) = %{tl_version}, tex(ecosx2074.vf) = %{tl_version}
Provides:       tex(ecosx2488.vf) = %{tl_version}, tex(ecosx2986.vf) = %{tl_version}
Provides:       tex(ecosx3583.vf) = %{tl_version}, tex(ecoti0500.vf) = %{tl_version}
Provides:       tex(ecoti0600.vf) = %{tl_version}, tex(ecoti0700.vf) = %{tl_version}
Provides:       tex(ecoti0800.vf) = %{tl_version}, tex(ecoti0900.vf) = %{tl_version}
Provides:       tex(ecoti1000.vf) = %{tl_version}, tex(ecoti1095.vf) = %{tl_version}
Provides:       tex(ecoti1200.vf) = %{tl_version}, tex(ecoti1440.vf) = %{tl_version}
Provides:       tex(ecoti1728.vf) = %{tl_version}, tex(ecoti2074.vf) = %{tl_version}
Provides:       tex(ecoti2488.vf) = %{tl_version}, tex(ecoti2986.vf) = %{tl_version}
Provides:       tex(ecoti3583.vf) = %{tl_version}, tex(ecott0600.vf) = %{tl_version}
Provides:       tex(ecott0700.vf) = %{tl_version}, tex(ecott0800.vf) = %{tl_version}
Provides:       tex(ecott0900.vf) = %{tl_version}, tex(ecott1000.vf) = %{tl_version}
Provides:       tex(ecott1095.vf) = %{tl_version}, tex(ecott1200.vf) = %{tl_version}
Provides:       tex(ecott1440.vf) = %{tl_version}, tex(ecott1728.vf) = %{tl_version}
Provides:       tex(ecott2074.vf) = %{tl_version}, tex(ecott2488.vf) = %{tl_version}
Provides:       tex(ecott2986.vf) = %{tl_version}, tex(ecott3583.vf) = %{tl_version}
Provides:       tex(ecoui0500.vf) = %{tl_version}, tex(ecoui0600.vf) = %{tl_version}
Provides:       tex(ecoui0700.vf) = %{tl_version}, tex(ecoui0800.vf) = %{tl_version}
Provides:       tex(ecoui0900.vf) = %{tl_version}, tex(ecoui1000.vf) = %{tl_version}
Provides:       tex(ecoui1095.vf) = %{tl_version}, tex(ecoui1200.vf) = %{tl_version}
Provides:       tex(ecoui1440.vf) = %{tl_version}, tex(ecoui1728.vf) = %{tl_version}
Provides:       tex(ecoui2074.vf) = %{tl_version}, tex(ecoui2488.vf) = %{tl_version}
Provides:       tex(ecoui2986.vf) = %{tl_version}, tex(ecoui3583.vf) = %{tl_version}
Provides:       tex(ecovi0600.vf) = %{tl_version}, tex(ecovi0700.vf) = %{tl_version}
Provides:       tex(ecovi0800.vf) = %{tl_version}, tex(ecovi0900.vf) = %{tl_version}
Provides:       tex(ecovi1000.vf) = %{tl_version}, tex(ecovi1095.vf) = %{tl_version}
Provides:       tex(ecovi1200.vf) = %{tl_version}, tex(ecovi1440.vf) = %{tl_version}
Provides:       tex(ecovi1728.vf) = %{tl_version}, tex(ecovi2074.vf) = %{tl_version}
Provides:       tex(ecovi2488.vf) = %{tl_version}, tex(ecovi2986.vf) = %{tl_version}
Provides:       tex(ecovi3583.vf) = %{tl_version}, tex(ecovt0600.vf) = %{tl_version}
Provides:       tex(ecovt0700.vf) = %{tl_version}, tex(ecovt0800.vf) = %{tl_version}
Provides:       tex(ecovt0900.vf) = %{tl_version}, tex(ecovt1000.vf) = %{tl_version}
Provides:       tex(ecovt1095.vf) = %{tl_version}, tex(ecovt1200.vf) = %{tl_version}
Provides:       tex(ecovt1440.vf) = %{tl_version}, tex(ecovt1728.vf) = %{tl_version}
Provides:       tex(ecovt2074.vf) = %{tl_version}, tex(ecovt2488.vf) = %{tl_version}
Provides:       tex(ecovt2986.vf) = %{tl_version}, tex(ecovt3583.vf) = %{tl_version}
Provides:       tex(T1cmodh.fd) = %{tl_version}, tex(T1cmor.fd) = %{tl_version}
Provides:       tex(T1cmoss.fd) = %{tl_version}, tex(T1cmott.fd) = %{tl_version}
Provides:       tex(T1cmovt.fd) = %{tl_version}, tex(eco.sty) = %{tl_version}

%description -n texlive-eco
A set of font metric files and virtual fonts for using the EC
fonts with oldstyle numerals. These files can only be used
together with the standard ec fonts. The style file eco.sty is
sufficient to use the eco fonts but if you intend to use other
font families as well, e.g., PostScript fonts, try altfont.

%package -n texlive-eco-doc
Summary:        Documentation for eco
Version:        svn29349.1.3

Provides:       tex-eco-doc
AutoReqProv:    No

%description -n texlive-eco-doc
Documentation for eco

%package -n texlive-eiad
Provides:       tex-eiad = %{tl_version}
License:        Public Domain
Summary:        Traditional style Irish fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(eiadb10.tfm) = %{tl_version}, tex(eiadbx10.tfm) = %{tl_version}
Provides:       tex(eiadbxi10.tfm) = %{tl_version}, tex(eiadbxsl10.tfm) = %{tl_version}
Provides:       tex(eiadccsc10.tfm) = %{tl_version}, tex(eiadci10.tfm) = %{tl_version}
Provides:       tex(eiadcr10.tfm) = %{tl_version}, tex(eiadcsc10.tfm) = %{tl_version}
Provides:       tex(eiadcsl10.tfm) = %{tl_version}, tex(eiadcslc9.tfm) = %{tl_version}
Provides:       tex(eiaddunh10.tfm) = %{tl_version}, tex(eiadff10.tfm) = %{tl_version}
Provides:       tex(eiadfi10.tfm) = %{tl_version}, tex(eiadfib8.tfm) = %{tl_version}
Provides:       tex(eiadi10.tfm) = %{tl_version}, tex(eiaditt10.tfm) = %{tl_version}
Provides:       tex(eiadr10.tfm) = %{tl_version}, tex(eiadr12.tfm) = %{tl_version}
Provides:       tex(eiadr17.tfm) = %{tl_version}, tex(eiadsl10.tfm) = %{tl_version}
Provides:       tex(eiadsltt10.tfm) = %{tl_version}, tex(eiadss10.tfm) = %{tl_version}
Provides:       tex(eiadssbx10.tfm) = %{tl_version}, tex(eiadssdc10.tfm) = %{tl_version}
Provides:       tex(eiadssi10.tfm) = %{tl_version}, tex(eiadssq8.tfm) = %{tl_version}
Provides:       tex(eiadssqi8.tfm) = %{tl_version}, tex(eiadtcsc10.tfm) = %{tl_version}
Provides:       tex(eiadtt10.tfm) = %{tl_version}, tex(eiadvtt10.tfm) = %{tl_version}
Provides:       tex(OT1eiad.fd) = %{tl_version}, tex(OT1eiadcc.fd) = %{tl_version}
Provides:       tex(OT1eiadss.fd) = %{tl_version}, tex(OT1eiadtt.fd) = %{tl_version}

%description -n texlive-eiad
In both lower and upper case 32 letters are defined (18 'plain'
ones, 5 long vowels and 9 aspirated consonants). The ligature
'agus' is also made available. The remaining characters
(digits, punctuation and accents) are inherited from the
Computer Modern family of fonts. The font definitions use code
from the sauter fonts, so those fonts have to be installed
before using eiad. OT1*.fd files are provided for use with
LaTeX.

%package -n texlive-eiad-doc
Summary:        Documentation for eiad
Version:        svn15878.0

Provides:       tex-eiad-doc
AutoReqProv:    No

%description -n texlive-eiad-doc
Documentation for eiad

%package -n texlive-eiad-ltx
Provides:       tex-eiad-ltx = %{tl_version}
License:        LPPL
Summary:        LaTeX support for the eiad font
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(eiad.sty) = %{tl_version}

%description -n texlive-eiad-ltx
The package provides macros to support use of the eiad fonts in
OT1 encoding. Also offered are a couple of Metafont files
described in the font package, but not provided there.

%package -n texlive-eiad-ltx-doc
Summary:        Documentation for eiad-ltx
Version:        svn15878.1.0

Provides:       tex-eiad-ltx-doc
AutoReqProv:    No

%description -n texlive-eiad-ltx-doc
Documentation for eiad-ltx

%package -n texlive-electrum
Provides:       tex-electrum = %{tl_version}
License:        GPLv2+ with exceptions and LPPL
Summary:        Electrum ADF fonts collection
Version:        svn19705.1.005_b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty), tex(fontenc.sty), tex(textcomp.sty), tex(nfssext-cfr.sty)
Provides:       tex(supp-yes.enc) = %{tl_version}, tex(yes.map) = %{tl_version}
Provides:       tex(yesb08c.tfm) = %{tl_version}, tex(yesb08t.tfm) = %{tl_version}
Provides:       tex(yesb0o8c.tfm) = %{tl_version}, tex(yesb0o8t.tfm) = %{tl_version}
Provides:       tex(yesb18c.tfm) = %{tl_version}, tex(yesb18t.tfm) = %{tl_version}
Provides:       tex(yesb1o8c.tfm) = %{tl_version}, tex(yesb1o8t.tfm) = %{tl_version}
Provides:       tex(yesb8c.tfm) = %{tl_version}, tex(yesb8r.tfm) = %{tl_version}
Provides:       tex(yesb8s.tfm) = %{tl_version}, tex(yesb8t.tfm) = %{tl_version}
Provides:       tex(yesbc8t.tfm) = %{tl_version}, tex(yesbcj8t.tfm) = %{tl_version}
Provides:       tex(yesbcjo8t.tfm) = %{tl_version}, tex(yesbcjow8t.tfm) = %{tl_version}
Provides:       tex(yesbcjw8t.tfm) = %{tl_version}, tex(yesbco8t.tfm) = %{tl_version}
Provides:       tex(yesbcow8t.tfm) = %{tl_version}, tex(yesbcw8t.tfm) = %{tl_version}
Provides:       tex(yesbj8c.tfm) = %{tl_version}, tex(yesbj8t.tfm) = %{tl_version}
Provides:       tex(yesbjo8c.tfm) = %{tl_version}, tex(yesbjo8t.tfm) = %{tl_version}
Provides:       tex(yesbjow8t.tfm) = %{tl_version}, tex(yesbjw8t.tfm) = %{tl_version}
Provides:       tex(yesbo8c.tfm) = %{tl_version}, tex(yesbo8r.tfm) = %{tl_version}
Provides:       tex(yesbo8s.tfm) = %{tl_version}, tex(yesbo8t.tfm) = %{tl_version}
Provides:       tex(yesbow8t.tfm) = %{tl_version}, tex(yesbw8t.tfm) = %{tl_version}
Provides:       tex(yesl08c.tfm) = %{tl_version}, tex(yesl08t.tfm) = %{tl_version}
Provides:       tex(yesl0o8c.tfm) = %{tl_version}, tex(yesl0o8t.tfm) = %{tl_version}
Provides:       tex(yesl18c.tfm) = %{tl_version}, tex(yesl18t.tfm) = %{tl_version}
Provides:       tex(yesl1o8c.tfm) = %{tl_version}, tex(yesl1o8t.tfm) = %{tl_version}
Provides:       tex(yesl8c.tfm) = %{tl_version}, tex(yesl8r.tfm) = %{tl_version}
Provides:       tex(yesl8s.tfm) = %{tl_version}, tex(yesl8t.tfm) = %{tl_version}
Provides:       tex(yeslc8t.tfm) = %{tl_version}, tex(yeslcj8t.tfm) = %{tl_version}
Provides:       tex(yeslcjo8t.tfm) = %{tl_version}, tex(yeslcjow8t.tfm) = %{tl_version}
Provides:       tex(yeslcjw8t.tfm) = %{tl_version}, tex(yeslco8t.tfm) = %{tl_version}
Provides:       tex(yeslcow8t.tfm) = %{tl_version}, tex(yeslcw8t.tfm) = %{tl_version}
Provides:       tex(yeslj8c.tfm) = %{tl_version}, tex(yeslj8t.tfm) = %{tl_version}
Provides:       tex(yesljo8c.tfm) = %{tl_version}, tex(yesljo8t.tfm) = %{tl_version}
Provides:       tex(yesljow8t.tfm) = %{tl_version}, tex(yesljw8t.tfm) = %{tl_version}
Provides:       tex(yeslo8c.tfm) = %{tl_version}, tex(yeslo8r.tfm) = %{tl_version}
Provides:       tex(yeslo8s.tfm) = %{tl_version}, tex(yeslo8t.tfm) = %{tl_version}
Provides:       tex(yeslow8t.tfm) = %{tl_version}, tex(yeslw8t.tfm) = %{tl_version}
Provides:       tex(yesr08c.tfm) = %{tl_version}, tex(yesr08t.tfm) = %{tl_version}
Provides:       tex(yesr0o8c.tfm) = %{tl_version}, tex(yesr0o8t.tfm) = %{tl_version}
Provides:       tex(yesr18c.tfm) = %{tl_version}, tex(yesr18t.tfm) = %{tl_version}
Provides:       tex(yesr1o8c.tfm) = %{tl_version}, tex(yesr1o8t.tfm) = %{tl_version}
Provides:       tex(yesr8c.tfm) = %{tl_version}, tex(yesr8r.tfm) = %{tl_version}
Provides:       tex(yesr8s.tfm) = %{tl_version}, tex(yesr8t.tfm) = %{tl_version}
Provides:       tex(yesrc8t.tfm) = %{tl_version}, tex(yesrcj8t.tfm) = %{tl_version}
Provides:       tex(yesrcjo8t.tfm) = %{tl_version}, tex(yesrcjow8t.tfm) = %{tl_version}
Provides:       tex(yesrcjw8t.tfm) = %{tl_version}, tex(yesrco8t.tfm) = %{tl_version}
Provides:       tex(yesrcow8t.tfm) = %{tl_version}, tex(yesrcw8t.tfm) = %{tl_version}
Provides:       tex(yesrj8c.tfm) = %{tl_version}, tex(yesrj8t.tfm) = %{tl_version}
Provides:       tex(yesrjo8c.tfm) = %{tl_version}, tex(yesrjo8t.tfm) = %{tl_version}
Provides:       tex(yesrjow8t.tfm) = %{tl_version}, tex(yesrjw8t.tfm) = %{tl_version}
Provides:       tex(yesro8c.tfm) = %{tl_version}, tex(yesro8r.tfm) = %{tl_version}
Provides:       tex(yesro8s.tfm) = %{tl_version}, tex(yesro8t.tfm) = %{tl_version}
Provides:       tex(yesrow8t.tfm) = %{tl_version}, tex(yesrw8t.tfm) = %{tl_version}
Provides:       tex(yess08c.tfm) = %{tl_version}, tex(yess08t.tfm) = %{tl_version}
Provides:       tex(yess0o8c.tfm) = %{tl_version}, tex(yess0o8t.tfm) = %{tl_version}
Provides:       tex(yess18c.tfm) = %{tl_version}, tex(yess18t.tfm) = %{tl_version}
Provides:       tex(yess1o8c.tfm) = %{tl_version}, tex(yess1o8t.tfm) = %{tl_version}
Provides:       tex(yess8c.tfm) = %{tl_version}, tex(yess8r.tfm) = %{tl_version}
Provides:       tex(yess8s.tfm) = %{tl_version}, tex(yess8t.tfm) = %{tl_version}
Provides:       tex(yessc8t.tfm) = %{tl_version}, tex(yesscj8t.tfm) = %{tl_version}
Provides:       tex(yesscjo8t.tfm) = %{tl_version}, tex(yesscjow8t.tfm) = %{tl_version}
Provides:       tex(yesscjw8t.tfm) = %{tl_version}, tex(yessco8t.tfm) = %{tl_version}
Provides:       tex(yesscow8t.tfm) = %{tl_version}, tex(yesscw8t.tfm) = %{tl_version}
Provides:       tex(yessj8c.tfm) = %{tl_version}, tex(yessj8t.tfm) = %{tl_version}
Provides:       tex(yessjo8c.tfm) = %{tl_version}, tex(yessjo8t.tfm) = %{tl_version}
Provides:       tex(yessjow8t.tfm) = %{tl_version}, tex(yessjw8t.tfm) = %{tl_version}
Provides:       tex(yesso8c.tfm) = %{tl_version}, tex(yesso8r.tfm) = %{tl_version}
Provides:       tex(yesso8s.tfm) = %{tl_version}, tex(yesso8t.tfm) = %{tl_version}
Provides:       tex(yessow8t.tfm) = %{tl_version}, tex(yessw8t.tfm) = %{tl_version}
Provides:       tex(yesb8a.pfb) = %{tl_version}, tex(yesbo8a.pfb) = %{tl_version}
Provides:       tex(yesl8a.pfb) = %{tl_version}, tex(yeslo8a.pfb) = %{tl_version}
Provides:       tex(yesr8a.pfb) = %{tl_version}, tex(yesro8a.pfb) = %{tl_version}
Provides:       tex(yess8a.pfb) = %{tl_version}, tex(yesso8a.pfb) = %{tl_version}
Provides:       tex(yesb08c.vf) = %{tl_version}, tex(yesb08t.vf) = %{tl_version}
Provides:       tex(yesb0o8c.vf) = %{tl_version}, tex(yesb0o8t.vf) = %{tl_version}
Provides:       tex(yesb18c.vf) = %{tl_version}, tex(yesb18t.vf) = %{tl_version}
Provides:       tex(yesb1o8c.vf) = %{tl_version}, tex(yesb1o8t.vf) = %{tl_version}
Provides:       tex(yesb8c.vf) = %{tl_version}, tex(yesb8t.vf) = %{tl_version}
Provides:       tex(yesbc8t.vf) = %{tl_version}, tex(yesbcj8t.vf) = %{tl_version}
Provides:       tex(yesbcjo8t.vf) = %{tl_version}, tex(yesbcjow8t.vf) = %{tl_version}
Provides:       tex(yesbcjw8t.vf) = %{tl_version}, tex(yesbco8t.vf) = %{tl_version}
Provides:       tex(yesbcow8t.vf) = %{tl_version}, tex(yesbcw8t.vf) = %{tl_version}
Provides:       tex(yesbj8c.vf) = %{tl_version}, tex(yesbj8t.vf) = %{tl_version}
Provides:       tex(yesbjo8c.vf) = %{tl_version}, tex(yesbjo8t.vf) = %{tl_version}
Provides:       tex(yesbjow8t.vf) = %{tl_version}, tex(yesbjw8t.vf) = %{tl_version}
Provides:       tex(yesbo8c.vf) = %{tl_version}, tex(yesbo8t.vf) = %{tl_version}
Provides:       tex(yesbow8t.vf) = %{tl_version}, tex(yesbw8t.vf) = %{tl_version}
Provides:       tex(yesl08c.vf) = %{tl_version}, tex(yesl08t.vf) = %{tl_version}
Provides:       tex(yesl0o8c.vf) = %{tl_version}, tex(yesl0o8t.vf) = %{tl_version}
Provides:       tex(yesl18c.vf) = %{tl_version}, tex(yesl18t.vf) = %{tl_version}
Provides:       tex(yesl1o8c.vf) = %{tl_version}, tex(yesl1o8t.vf) = %{tl_version}
Provides:       tex(yesl8c.vf) = %{tl_version}, tex(yesl8t.vf) = %{tl_version}
Provides:       tex(yeslc8t.vf) = %{tl_version}, tex(yeslcj8t.vf) = %{tl_version}
Provides:       tex(yeslcjo8t.vf) = %{tl_version}, tex(yeslcjow8t.vf) = %{tl_version}
Provides:       tex(yeslcjw8t.vf) = %{tl_version}, tex(yeslco8t.vf) = %{tl_version}
Provides:       tex(yeslcow8t.vf) = %{tl_version}, tex(yeslcw8t.vf) = %{tl_version}
Provides:       tex(yeslj8c.vf) = %{tl_version}, tex(yeslj8t.vf) = %{tl_version}
Provides:       tex(yesljo8c.vf) = %{tl_version}, tex(yesljo8t.vf) = %{tl_version}
Provides:       tex(yesljow8t.vf) = %{tl_version}, tex(yesljw8t.vf) = %{tl_version}
Provides:       tex(yeslo8c.vf) = %{tl_version}, tex(yeslo8t.vf) = %{tl_version}
Provides:       tex(yeslow8t.vf) = %{tl_version}, tex(yeslw8t.vf) = %{tl_version}
Provides:       tex(yesr08c.vf) = %{tl_version}, tex(yesr08t.vf) = %{tl_version}
Provides:       tex(yesr0o8c.vf) = %{tl_version}, tex(yesr0o8t.vf) = %{tl_version}
Provides:       tex(yesr18c.vf) = %{tl_version}, tex(yesr18t.vf) = %{tl_version}
Provides:       tex(yesr1o8c.vf) = %{tl_version}, tex(yesr1o8t.vf) = %{tl_version}
Provides:       tex(yesr8c.vf) = %{tl_version}, tex(yesr8t.vf) = %{tl_version}
Provides:       tex(yesrc8t.vf) = %{tl_version}, tex(yesrcj8t.vf) = %{tl_version}
Provides:       tex(yesrcjo8t.vf) = %{tl_version}, tex(yesrcjow8t.vf) = %{tl_version}
Provides:       tex(yesrcjw8t.vf) = %{tl_version}, tex(yesrco8t.vf) = %{tl_version}
Provides:       tex(yesrcow8t.vf) = %{tl_version}, tex(yesrcw8t.vf) = %{tl_version}
Provides:       tex(yesrj8c.vf) = %{tl_version}, tex(yesrj8t.vf) = %{tl_version}
Provides:       tex(yesrjo8c.vf) = %{tl_version}, tex(yesrjo8t.vf) = %{tl_version}
Provides:       tex(yesrjow8t.vf) = %{tl_version}, tex(yesrjw8t.vf) = %{tl_version}
Provides:       tex(yesro8c.vf) = %{tl_version}, tex(yesro8t.vf) = %{tl_version}
Provides:       tex(yesrow8t.vf) = %{tl_version}, tex(yesrw8t.vf) = %{tl_version}
Provides:       tex(yess08c.vf) = %{tl_version}, tex(yess08t.vf) = %{tl_version}
Provides:       tex(yess0o8c.vf) = %{tl_version}, tex(yess0o8t.vf) = %{tl_version}
Provides:       tex(yess18c.vf) = %{tl_version}, tex(yess18t.vf) = %{tl_version}
Provides:       tex(yess1o8c.vf) = %{tl_version}, tex(yess1o8t.vf) = %{tl_version}
Provides:       tex(yess8c.vf) = %{tl_version}, tex(yess8t.vf) = %{tl_version}
Provides:       tex(yessc8t.vf) = %{tl_version}, tex(yesscj8t.vf) = %{tl_version}
Provides:       tex(yesscjo8t.vf) = %{tl_version}, tex(yesscjow8t.vf) = %{tl_version}
Provides:       tex(yesscjw8t.vf) = %{tl_version}, tex(yessco8t.vf) = %{tl_version}
Provides:       tex(yesscow8t.vf) = %{tl_version}, tex(yesscw8t.vf) = %{tl_version}
Provides:       tex(yessj8c.vf) = %{tl_version}, tex(yessj8t.vf) = %{tl_version}
Provides:       tex(yessjo8c.vf) = %{tl_version}, tex(yessjo8t.vf) = %{tl_version}
Provides:       tex(yessjow8t.vf) = %{tl_version}, tex(yessjw8t.vf) = %{tl_version}
Provides:       tex(yesso8c.vf) = %{tl_version}, tex(yesso8t.vf) = %{tl_version}
Provides:       tex(yessow8t.vf) = %{tl_version}, tex(yessw8t.vf) = %{tl_version}
Provides:       tex(electrum.sty) = %{tl_version}, tex(t1yes.fd) = %{tl_version}
Provides:       tex(t1yes0.fd) = %{tl_version}, tex(t1yes1.fd) = %{tl_version}
Provides:       tex(t1yesj.fd) = %{tl_version}, tex(t1yesjw.fd) = %{tl_version}
Provides:       tex(t1yesw.fd) = %{tl_version}, tex(ts1yes.fd) = %{tl_version}
Provides:       tex(ts1yes0.fd) = %{tl_version}, tex(ts1yes1.fd) = %{tl_version}
Provides:       tex(ts1yesj.fd) = %{tl_version}, tex(ts1yesjw.fd) = %{tl_version}
Provides:       tex(ts1yesw.fd) = %{tl_version}

%description -n texlive-electrum
Electrum ADF is a slab-serif font featuring optical and italic
small-caps; additional ligatures and an alternate Q; lining,
hanging, inferior and superior digits; and four weights. The
fonts are provided in Adobe Type 1 format and the support
material enables use with LaTeX. Licence is mixed: LPPL for
LaTeX support; GPL with font exception for the fonts.

%package -n texlive-electrum-doc
Summary:        Documentation for electrum
Version:        svn19705.1.005_b

Provides:       tex-electrum-doc
AutoReqProv:    No

%description -n texlive-electrum-doc
Documentation for electrum

%package -n texlive-elvish
Provides:       tex-elvish = %{tl_version}
License:        Elvish
Summary:        Fonts for typesetting Tolkien Elvish scripts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cirth.tfm) = %{tl_version}, tex(teng10.tfm) = %{tl_version}

%description -n texlive-elvish
The bundle provides fonts for Cirth (cirth.mf, etc.) and for
Tengwar (teng10.mf). The Tengwar fonts are supported by macros
in teng.tex, or by the (better documented) tengtex package.

%package -n texlive-elvish-doc
Summary:        Documentation for elvish
Version:        svn15878.0

Provides:       tex-elvish-doc
AutoReqProv:    No

%description -n texlive-elvish-doc
Documentation for elvish

%package -n texlive-epigrafica
Provides:       tex-epigrafica = %{tl_version}
License:        GPL+
Summary:        A Greek and Latin font
Version:        svn17210.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(pxfonts.sty)
Provides:       tex(epigraficahellenic.enc) = %{tl_version}
Provides:       tex(epigrafica.map) = %{tl_version}, tex(epigraficab8a.tfm) = %{tl_version}
Provides:       tex(epigraficab8r.tfm) = %{tl_version}, tex(epigraficabi8a.tfm) = %{tl_version}
Provides:       tex(epigraficabi8r.tfm) = %{tl_version}, tex(epigraficabo8a.tfm) = %{tl_version}
Provides:       tex(epigraficabo8r.tfm) = %{tl_version}, tex(epigraficac8a.tfm) = %{tl_version}
Provides:       tex(epigraficac8r.tfm) = %{tl_version}, tex(epigraficahb7a.tfm) = %{tl_version}
Provides:       tex(epigraficahb7r.tfm) = %{tl_version}, tex(epigraficahbi7a.tfm) = %{tl_version}
Provides:       tex(epigraficahbi7r.tfm) = %{tl_version}
Provides:       tex(epigraficahbo7a.tfm) = %{tl_version}
Provides:       tex(epigraficahbo7r.tfm) = %{tl_version}
Provides:       tex(epigraficahc7a.tfm) = %{tl_version}, tex(epigraficahc7r.tfm) = %{tl_version}
Provides:       tex(epigraficahi7a.tfm) = %{tl_version}, tex(epigraficahi7r.tfm) = %{tl_version}
Provides:       tex(epigraficahn7r.tfm) = %{tl_version}, tex(epigraficaho7a.tfm) = %{tl_version}
Provides:       tex(epigraficaho7r.tfm) = %{tl_version}, tex(epigraficai8a.tfm) = %{tl_version}
Provides:       tex(epigraficai8r.tfm) = %{tl_version}, tex(epigrafican8a.tfm) = %{tl_version}
Provides:       tex(epigrafican8r.tfm) = %{tl_version}, tex(epigraficao8a.tfm) = %{tl_version}
Provides:       tex(epigraficao8r.tfm) = %{tl_version}, tex(gepigraficahn7a.tfm) = %{tl_version}
Provides:       tex(Epigrafica-Entona.pfb) = %{tl_version}
Provides:       tex(Epigrafica-EntonaReonta.pfb) = %{tl_version}
Provides:       tex(Epigrafica-Ortha.pfb) = %{tl_version}
Provides:       tex(Epigrafica-Pezokefalaia.pfb) = %{tl_version}
Provides:       tex(Epigrafica-Reonta.pfb) = %{tl_version}
Provides:       tex(epigraficab8r.vf) = %{tl_version}, tex(epigraficabi8r.vf) = %{tl_version}
Provides:       tex(epigraficabo8r.vf) = %{tl_version}, tex(epigraficac8r.vf) = %{tl_version}
Provides:       tex(epigraficahb7r.vf) = %{tl_version}, tex(epigraficahbi7r.vf) = %{tl_version}
Provides:       tex(epigraficahbo7r.vf) = %{tl_version}, tex(epigraficahc7r.vf) = %{tl_version}
Provides:       tex(epigraficahi7r.vf) = %{tl_version}, tex(epigraficahn7r.vf) = %{tl_version}
Provides:       tex(epigraficaho7r.vf) = %{tl_version}, tex(epigraficai8r.vf) = %{tl_version}
Provides:       tex(epigrafican8r.vf) = %{tl_version}, tex(epigraficao8r.vf) = %{tl_version}
Provides:       tex(epigrafica.sty) = %{tl_version}, tex(lgrepigrafica.fd) = %{tl_version}
Provides:       tex(ot1epigrafica.fd) = %{tl_version}

%description -n texlive-epigrafica
Epigrafica is forked from the development of the MgOpen font
Cosmetica, which is a similar design to Optima and includes
Greek. Development has been supported by the Laboratory of
Digital Typography and Mathematical Software, of the Department
of Mathematics of the University of the Aegean, Greece.

%package -n texlive-epigrafica-doc
Summary:        Documentation for epigrafica
Version:        svn17210.1.01

Provides:       tex-epigrafica-doc
AutoReqProv:    No

%description -n texlive-epigrafica-doc
Documentation for epigrafica

%package -n texlive-epsdice
Provides:       tex-epsdice = %{tl_version}
License:        LPPL
Summary:        A scalable dice "font"
Version:        svn15878.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(ifthen.sty)
Provides:       tex(epsdice.cfg) = %{tl_version}, tex(epsdice.sty) = %{tl_version}

%description -n texlive-epsdice
The epsdice package defines a single command \epsdice that
takes a numeric argument (in the range 1-6), and selects a face
image from a file that contains each of the 6 possible die
faces. The graphic file is provided in both Encapsulated
PostScript and PDF formats.

%package -n texlive-epsdice-doc
Summary:        Documentation for epsdice
Version:        svn15878.2.1

Provides:       tex-epsdice-doc
AutoReqProv:    No

%description -n texlive-epsdice-doc
Documentation for epsdice

%package -n texlive-erewhon
Provides:       tex-erewhon = %{tl_version}
License:        OFL
Summary:        Font package derived from Heuristica and Utopia
Version:        svn43506
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(fontenc.sty)
Requires:       tex(textcomp.sty), tex(mweights.sty), tex(etoolbox.sty), tex(fontaxes.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(zut1_23adt6.enc) = %{tl_version}, tex(zut1_26fc24.enc) = %{tl_version}
Provides:       tex(zut1_2pdzb4.enc) = %{tl_version}, tex(zut1_2rsg4x.enc) = %{tl_version}
Provides:       tex(zut1_33qyrq.enc) = %{tl_version}, tex(zut1_36wkbs.enc) = %{tl_version}
Provides:       tex(zut1_3qes6a.enc) = %{tl_version}, tex(zut1_3sdh4x.enc) = %{tl_version}
Provides:       tex(zut1_3zzbgn.enc) = %{tl_version}, tex(zut1_46udvc.enc) = %{tl_version}
Provides:       tex(zut1_4gejho.enc) = %{tl_version}, tex(zut1_55od57.enc) = %{tl_version}
Provides:       tex(zut1_55vlpj.enc) = %{tl_version}, tex(zut1_5gd3w7.enc) = %{tl_version}
Provides:       tex(zut1_5osyhn.enc) = %{tl_version}, tex(zut1_5qg2z3.enc) = %{tl_version}
Provides:       tex(zut1_5uug7k.enc) = %{tl_version}, tex(zut1_5vzi2j.enc) = %{tl_version}
Provides:       tex(zut1_6fbto3.enc) = %{tl_version}, tex(zut1_6ff2fp.enc) = %{tl_version}
Provides:       tex(zut1_6hpp45.enc) = %{tl_version}, tex(zut1_6odewi.enc) = %{tl_version}
Provides:       tex(zut1_6qui4c.enc) = %{tl_version}, tex(zut1_6zm6gs.enc) = %{tl_version}
Provides:       tex(zut1_72r2qm.enc) = %{tl_version}, tex(zut1_7cvson.enc) = %{tl_version}
Provides:       tex(zut1_7il5js.enc) = %{tl_version}, tex(zut1_7whbrd.enc) = %{tl_version}
Provides:       tex(zut1_a5mbkd.enc) = %{tl_version}, tex(zut1_aboxub.enc) = %{tl_version}
Provides:       tex(zut1_agkjyb.enc) = %{tl_version}, tex(zut1_akndxy.enc) = %{tl_version}
Provides:       tex(zut1_asyhxx.enc) = %{tl_version}, tex(zut1_b66crt.enc) = %{tl_version}
Provides:       tex(zut1_bhrl5o.enc) = %{tl_version}, tex(zut1_buav3i.enc) = %{tl_version}
Provides:       tex(zut1_c4updo.enc) = %{tl_version}, tex(zut1_cd75bx.enc) = %{tl_version}
Provides:       tex(zut1_diubwb.enc) = %{tl_version}, tex(zut1_dmu6i6.enc) = %{tl_version}
Provides:       tex(zut1_ebpzys.enc) = %{tl_version}, tex(zut1_efqq6z.enc) = %{tl_version}
Provides:       tex(zut1_egk5ui.enc) = %{tl_version}, tex(zut1_emma2w.enc) = %{tl_version}
Provides:       tex(zut1_enosfl.enc) = %{tl_version}, tex(zut1_enxj7r.enc) = %{tl_version}
Provides:       tex(zut1_erfmsm.enc) = %{tl_version}, tex(zut1_fs7nm6.enc) = %{tl_version}
Provides:       tex(zut1_g4aneu.enc) = %{tl_version}, tex(zut1_gdnnr3.enc) = %{tl_version}
Provides:       tex(zut1_gmwaxb.enc) = %{tl_version}, tex(zut1_hbrlcj.enc) = %{tl_version}
Provides:       tex(zut1_io433z.enc) = %{tl_version}, tex(zut1_izhoij.enc) = %{tl_version}
Provides:       tex(zut1_j2yrpr.enc) = %{tl_version}, tex(zut1_jlgnzs.enc) = %{tl_version}
Provides:       tex(zut1_kqgewl.enc) = %{tl_version}, tex(zut1_mb3zuf.enc) = %{tl_version}
Provides:       tex(zut1_mczjfg.enc) = %{tl_version}, tex(zut1_mnqfpi.enc) = %{tl_version}
Provides:       tex(zut1_namll4.enc) = %{tl_version}, tex(zut1_okgrmm.enc) = %{tl_version}
Provides:       tex(zut1_opwl73.enc) = %{tl_version}, tex(zut1_p3lteh.enc) = %{tl_version}
Provides:       tex(zut1_p3smp3.enc) = %{tl_version}, tex(zut1_p725ca.enc) = %{tl_version}
Provides:       tex(zut1_pdw4cs.enc) = %{tl_version}, tex(zut1_plclts.enc) = %{tl_version}
Provides:       tex(zut1_ppbl3l.enc) = %{tl_version}, tex(zut1_pt32q7.enc) = %{tl_version}
Provides:       tex(zut1_pua4mh.enc) = %{tl_version}, tex(zut1_q4fsp5.enc) = %{tl_version}
Provides:       tex(zut1_qpgbnz.enc) = %{tl_version}, tex(zut1_qytqkd.enc) = %{tl_version}
Provides:       tex(zut1_qzlrfe.enc) = %{tl_version}, tex(zut1_sodton.enc) = %{tl_version}
Provides:       tex(zut1_sxnwby.enc) = %{tl_version}, tex(zut1_szqr4x.enc) = %{tl_version}
Provides:       tex(zut1_tyrjhz.enc) = %{tl_version}, tex(zut1_u4kfm3.enc) = %{tl_version}
Provides:       tex(zut1_uaoxy2.enc) = %{tl_version}, tex(zut1_uxztme.enc) = %{tl_version}
Provides:       tex(zut1_vgtdgz.enc) = %{tl_version}, tex(zut1_vz5ynf.enc) = %{tl_version}
Provides:       tex(zut1_vzlxgj.enc) = %{tl_version}, tex(zut1_wft4nn.enc) = %{tl_version}
Provides:       tex(zut1_x5g3l6.enc) = %{tl_version}, tex(zut1_x6jwsz.enc) = %{tl_version}
Provides:       tex(zut1_yat6q4.enc) = %{tl_version}, tex(zut1_ympoog.enc) = %{tl_version}
Provides:       tex(zut1_ynhtih.enc) = %{tl_version}, tex(zut1_ytwp45.enc) = %{tl_version}
Provides:       tex(zut1_z2p4l2.enc) = %{tl_version}, tex(zut1_z3xbwl.enc) = %{tl_version}
Provides:       tex(zut1_zm7h5z.enc) = %{tl_version}, tex(erewhon.map) = %{tl_version}
Provides:       tex(Erewhon-Bold.otf) = %{tl_version}, tex(Erewhon-BoldItalic.otf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted.otf) = %{tl_version}
Provides:       tex(Erewhon-Italic.otf) = %{tl_version}, tex(Erewhon-Regular.otf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted.otf) = %{tl_version}
Provides:       tex(Erewhon-Bold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-dnom-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-dnom-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-dnom-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-inf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-inf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-inf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-numr-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-numr-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-numr-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-numr-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-sup-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-sup-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-dnom-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-dnom-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-dnom-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-inf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-inf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-inf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-lf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-lf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-lf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-numr-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-numr-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-numr-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-osf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-osf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-osf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-sup-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-sup-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tosf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tosf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-dnom-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-dnom-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-dnom-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-inf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-inf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-inf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-inf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-numr-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-numr-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-numr-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-numr-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-sup-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-sup-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-sup-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-dnom-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-dnom-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-dnom-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-inf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-inf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-inf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-lf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-lf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-lf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-numr-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-numr-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-numr-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-numr-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-osf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-osf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-osf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-sup-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-sup-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tosf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tosf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-dnom-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-dnom-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-dnom-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-inf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-inf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-inf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-numr-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-numr-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-numr-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-numr-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-sup-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-sup-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-dnom-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-dnom-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-dnom-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-inf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-inf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-inf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-inf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-numr-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-numr-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-numr-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-numr-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-numr-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-sup-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-sup-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-sup-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-sc-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-sc-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-sc-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-t2b.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-t2c.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Erewhon-Bold.pfb) = %{tl_version}, tex(Erewhon-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted.pfb) = %{tl_version}
Provides:       tex(Erewhon-Italic.pfb) = %{tl_version}, tex(Erewhon-Regular.pfb) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted.pfb) = %{tl_version}
Provides:       tex(Erewhon-Bold-dnom-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-numr-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-dnom-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-inf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-lf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-numr-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-osf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-sup-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-BoldSlanted-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-numr-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-dnom-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-numr-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-dnom-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-inf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-lf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-numr-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-osf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-sup-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-t1.vf) = %{tl_version}
Provides:       tex(Erewhon-RegularSlanted-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LY1erewhon-Dnom.fd) = %{tl_version}, tex(LY1erewhon-Inf.fd) = %{tl_version}
Provides:       tex(LY1erewhon-LF.fd) = %{tl_version}, tex(LY1erewhon-Numr.fd) = %{tl_version}
Provides:       tex(LY1erewhon-OsF.fd) = %{tl_version}, tex(LY1erewhon-Sup.fd) = %{tl_version}
Provides:       tex(LY1erewhon-TLF.fd) = %{tl_version}, tex(LY1erewhon-TOsF.fd) = %{tl_version}
Provides:       tex(T1erewhon-Dnom.fd) = %{tl_version}, tex(T1erewhon-Inf.fd) = %{tl_version}
Provides:       tex(T1erewhon-LF.fd) = %{tl_version}, tex(T1erewhon-Numr.fd) = %{tl_version}
Provides:       tex(T1erewhon-OsF.fd) = %{tl_version}, tex(T1erewhon-Sup.fd) = %{tl_version}
Provides:       tex(T1erewhon-TLF.fd) = %{tl_version}, tex(T1erewhon-TOsF.fd) = %{tl_version}
Provides:       tex(T2Aerewhon-Dnom.fd) = %{tl_version}, tex(T2Aerewhon-Inf.fd) = %{tl_version}
Provides:       tex(T2Aerewhon-LF.fd) = %{tl_version}, tex(T2Aerewhon-Numr.fd) = %{tl_version}
Provides:       tex(T2Aerewhon-OsF.fd) = %{tl_version}, tex(T2Aerewhon-Sup.fd) = %{tl_version}
Provides:       tex(T2Aerewhon-TLF.fd) = %{tl_version}, tex(T2Aerewhon-TOsF.fd) = %{tl_version}
Provides:       tex(T2Berewhon-Dnom.fd) = %{tl_version}, tex(T2Berewhon-Inf.fd) = %{tl_version}
Provides:       tex(T2Berewhon-LF.fd) = %{tl_version}, tex(T2Berewhon-Numr.fd) = %{tl_version}
Provides:       tex(T2Berewhon-OsF.fd) = %{tl_version}, tex(T2Berewhon-Sup.fd) = %{tl_version}
Provides:       tex(T2Berewhon-TLF.fd) = %{tl_version}, tex(T2Berewhon-TOsF.fd) = %{tl_version}
Provides:       tex(T2Cerewhon-Dnom.fd) = %{tl_version}, tex(T2Cerewhon-Inf.fd) = %{tl_version}
Provides:       tex(T2Cerewhon-LF.fd) = %{tl_version}, tex(T2Cerewhon-Numr.fd) = %{tl_version}
Provides:       tex(T2Cerewhon-OsF.fd) = %{tl_version}, tex(T2Cerewhon-Sup.fd) = %{tl_version}
Provides:       tex(T2Cerewhon-TLF.fd) = %{tl_version}, tex(T2Cerewhon-TOsF.fd) = %{tl_version}
Provides:       tex(TS1erewhon-LF.fd) = %{tl_version}, tex(TS1erewhon-OsF.fd) = %{tl_version}
Provides:       tex(TS1erewhon-TLF.fd) = %{tl_version}, tex(TS1erewhon-TOsF.fd) = %{tl_version}
Provides:       tex(erewhon.sty) = %{tl_version}

%description -n texlive-erewhon
Erewhon is based on the Heuristica package, which is based in
turn on Utopia. Erewhon adds a number of new features -- small
caps in all styles rather than just regular, added figure
styles (proportional, inferior, numerator, denominator) and
superior letters. The size is 6% smaller than Heuristica,
matching that of UtopiaStd.

%package -n texlive-erewhon-doc
Summary:        Documentation for erewhon
Version:        svn43506
Provides:       tex-erewhon-doc
AutoReqProv:    No

%description -n texlive-erewhon-doc
Documentation for erewhon

%package -n texlive-esrelation
Provides:       tex-esrelation = %{tl_version}
License:        LPPL 1.3
Summary:        Provides a symbol set for describing relations between ordered pairs
Version:        svn37236.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(esrelation.map) = %{tl_version}, tex(esrelation10.tfm) = %{tl_version}
Provides:       tex(esrelation10.pfb) = %{tl_version}, tex(esrelation.sty) = %{tl_version}
Provides:       tex(uesrelation.fd) = %{tl_version}

%description -n texlive-esrelation
Around 2008, researcher Byron Cook and several colleagues began
developing a new set of interrelated algorithms capable of
automatically reasoning about the behavior of computer programs
and other systems (such as biological systems, circuit designs,
etc). At the center of these algorithms were new ideas about
the relationships between structures expressable as
mathematical sets and relations. Using the language of
mathematics and logic, the researchers communicated these new
results to others in their community via published papers,
research talks, etc. Unfortunately, they found the symbols
already available for reasoning about relations lacking (in
contrast to sets, which have a long-ago developed and robust
symbol vocabulary). Early presentations were unnecessarily
cluttered. To more elegantly express these ideas around
relations, Cook recruited artist Tauba Auerbach to help develop
a set of symbols. This package provides an math symbol font for
describing relations between ordered pairs by using Metafont.

%package -n texlive-esrelation-doc
Summary:        Documentation for esrelation
Version:        svn37236.0

Provides:       tex-esrelation-doc
AutoReqProv:    No

%description -n texlive-esrelation-doc
Documentation for esrelation

%package -n texlive-esstix
Provides:       tex-esstix = %{tl_version}
License:        OFL
Summary:        PostScript versions of the ESSTIX, with macro support
Version:        svn22426.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty)
Provides:       tex(ESSTIX.map) = %{tl_version}, tex(esstixbb.tfm) = %{tl_version}
Provides:       tex(esstixcal.tfm) = %{tl_version}, tex(esstixfrak.tfm) = %{tl_version}
Provides:       tex(rESSTIX13.tfm) = %{tl_version}, tex(rESSTIX14.tfm) = %{tl_version}
Provides:       tex(rESSTIX15.tfm) = %{tl_version}, tex(ESSTIX10.pfb) = %{tl_version}
Provides:       tex(ESSTIX11.pfb) = %{tl_version}, tex(ESSTIX12.pfb) = %{tl_version}
Provides:       tex(ESSTIX13.pfb) = %{tl_version}, tex(ESSTIX14.pfb) = %{tl_version}
Provides:       tex(ESSTIX15.pfb) = %{tl_version}, tex(ESSTIX16.pfb) = %{tl_version}
Provides:       tex(ESSTIX17.pfb) = %{tl_version}, tex(ESSTIX1_.pfb) = %{tl_version}
Provides:       tex(ESSTIX2_.pfb) = %{tl_version}, tex(ESSTIX3_.pfb) = %{tl_version}
Provides:       tex(ESSTIX4_.pfb) = %{tl_version}, tex(ESSTIX5_.pfb) = %{tl_version}
Provides:       tex(ESSTIX6_.pfb) = %{tl_version}, tex(ESSTIX7_.pfb) = %{tl_version}
Provides:       tex(ESSTIX8_.pfb) = %{tl_version}, tex(ESSTIX9_.pfb) = %{tl_version}
Provides:       tex(esstixbb.vf) = %{tl_version}, tex(esstixcal.vf) = %{tl_version}
Provides:       tex(esstixfrak.vf) = %{tl_version}, tex(esstixbb.sty) = %{tl_version}
Provides:       tex(esstixcal.sty) = %{tl_version}, tex(esstixfrak.sty) = %{tl_version}
Provides:       tex(uesstixbb.fd) = %{tl_version}, tex(uesstixcal.fd) = %{tl_version}
Provides:       tex(uesstixfrak.fd) = %{tl_version}

%description -n texlive-esstix
These fonts represent translation to PostScript Type 1 of the
ESSTIX fonts. ESSTIX seem to have been a precursor to the STIX
project, and were donated by Elsevier to that project. The
accompanying virtual fonts with customized metrics and LaTeX
support files allow their use as calligraphic, fraktur and
double-struck (blackboard bold) in maths mode.

%package -n texlive-esstix-doc
Summary:        Documentation for esstix
Version:        svn22426.1.0

Provides:       tex-esstix-doc
AutoReqProv:    No

%description -n texlive-esstix-doc
Documentation for esstix

%package -n texlive-esvect
Provides:       tex-esvect = %{tl_version}
License:        GPL+
Summary:        Vector arrows
Version:        svn32098.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(esvect.map) = %{tl_version}, tex(vect10.tfm) = %{tl_version}
Provides:       tex(vect5.tfm) = %{tl_version}, tex(vect6.tfm) = %{tl_version}
Provides:       tex(vect7.tfm) = %{tl_version}, tex(vect8.tfm) = %{tl_version}
Provides:       tex(vect9.tfm) = %{tl_version}, tex(vect10.pfb) = %{tl_version}
Provides:       tex(vect5.pfb) = %{tl_version}, tex(vect6.pfb) = %{tl_version}
Provides:       tex(vect7.pfb) = %{tl_version}, tex(vect8.pfb) = %{tl_version}
Provides:       tex(vect9.pfb) = %{tl_version}, tex(esvect.sty) = %{tl_version}
Provides:       tex(uesvect.fd) = %{tl_version}

%description -n texlive-esvect
Write vectors using an arrow which differs from the Computer
Modern one. You have the choice between several kinds of
arrows. The package consists of the relevant Metafont code and
a package to use it.

%package -n texlive-esvect-doc
Summary:        Documentation for esvect
Version:        svn32098.1.3

Provides:       tex-esvect-doc
AutoReqProv:    No

%description -n texlive-esvect-doc
Documentation for esvect

%package -n texlive-eulervm
Provides:       tex-eulervm = %{tl_version}
License:        LPPL
Summary:        Euler virtual math fonts
Version:        svn15878.4.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(zeuex10.tfm) = %{tl_version}, tex(zeurb10.tfm) = %{tl_version}
Provides:       tex(zeurb5.tfm) = %{tl_version}, tex(zeurb7.tfm) = %{tl_version}
Provides:       tex(zeurm10.tfm) = %{tl_version}, tex(zeurm5.tfm) = %{tl_version}
Provides:       tex(zeurm7.tfm) = %{tl_version}, tex(zeusb10.tfm) = %{tl_version}
Provides:       tex(zeusb5.tfm) = %{tl_version}, tex(zeusb7.tfm) = %{tl_version}
Provides:       tex(zeusm10.tfm) = %{tl_version}, tex(zeusm5.tfm) = %{tl_version}
Provides:       tex(zeusm7.tfm) = %{tl_version}, tex(zeuex10.vf) = %{tl_version}
Provides:       tex(zeurb10.vf) = %{tl_version}, tex(zeurb5.vf) = %{tl_version}
Provides:       tex(zeurb7.vf) = %{tl_version}, tex(zeurm10.vf) = %{tl_version}
Provides:       tex(zeurm5.vf) = %{tl_version}, tex(zeurm7.vf) = %{tl_version}
Provides:       tex(zeusb10.vf) = %{tl_version}, tex(zeusb5.vf) = %{tl_version}
Provides:       tex(zeusb7.vf) = %{tl_version}, tex(zeusm10.vf) = %{tl_version}
Provides:       tex(zeusm5.vf) = %{tl_version}, tex(zeusm7.vf) = %{tl_version}
Provides:       tex(eulervm.sty) = %{tl_version}, tex(uzeuex.fd) = %{tl_version}
Provides:       tex(uzeur.fd) = %{tl_version}, tex(uzeus.fd) = %{tl_version}

%description -n texlive-eulervm
The well-known Euler fonts are suitable for typsetting
mathematics in conjunction with a variety of text fonts which
do not provide mathematical character sets of their own. Euler-
VM is a set of virtual mathematics fonts based on Euler and CM.
This approach has several advantages over immediately using the
real Euler fonts: Most noticeably, less TeX resources are
consumed, the quality of various math symbols is improved and a
usable \hslash symbol can be provided. The virtual fonts are
accompanied by a LaTeX package which makes them easy to use,
particularly in conjunction with Type1 PostScript text fonts.
They are compatible with amsmath. A package option allows the
fonts to be loaded at 95% of their nominal size, thus blending
better with certain text fonts, e.g., Minion.

%package -n texlive-eulervm-doc
Summary:        Documentation for eulervm
Version:        svn15878.4.0

Provides:       tex-eulervm-doc
AutoReqProv:    No

%description -n texlive-eulervm-doc
Documentation for eulervm

%package -n texlive-euxm
Provides:       tex-euxm = %{tl_version}
License:        LPPL
Summary:        euxm package
Version:        svn45696
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(euxm10.tfm) = %{tl_version}, tex(euxm5.tfm) = %{tl_version}
Provides:       tex(euxm7.tfm) = %{tl_version}

%description -n texlive-euxm
euxm package

%package -n texlive-ec
Provides:       tex-ec = %{tl_version}
License:        ec
Summary:        Computer modern fonts in T1 and TS1 encodings
Version:        svn25033.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ecbi0500.tfm) = %{tl_version}, tex(ecbi0600.tfm) = %{tl_version}
Provides:       tex(ecbi0700.tfm) = %{tl_version}, tex(ecbi0800.tfm) = %{tl_version}
Provides:       tex(ecbi0900.tfm) = %{tl_version}, tex(ecbi1000.tfm) = %{tl_version}
Provides:       tex(ecbi1095.tfm) = %{tl_version}, tex(ecbi1200.tfm) = %{tl_version}
Provides:       tex(ecbi1440.tfm) = %{tl_version}, tex(ecbi1728.tfm) = %{tl_version}
Provides:       tex(ecbi2074.tfm) = %{tl_version}, tex(ecbi2488.tfm) = %{tl_version}
Provides:       tex(ecbi2986.tfm) = %{tl_version}, tex(ecbi3583.tfm) = %{tl_version}
Provides:       tex(ecbl0500.tfm) = %{tl_version}, tex(ecbl0600.tfm) = %{tl_version}
Provides:       tex(ecbl0700.tfm) = %{tl_version}, tex(ecbl0800.tfm) = %{tl_version}
Provides:       tex(ecbl0900.tfm) = %{tl_version}, tex(ecbl1000.tfm) = %{tl_version}
Provides:       tex(ecbl1095.tfm) = %{tl_version}, tex(ecbl1200.tfm) = %{tl_version}
Provides:       tex(ecbl1440.tfm) = %{tl_version}, tex(ecbl1728.tfm) = %{tl_version}
Provides:       tex(ecbl2074.tfm) = %{tl_version}, tex(ecbl2488.tfm) = %{tl_version}
Provides:       tex(ecbl2986.tfm) = %{tl_version}, tex(ecbl3583.tfm) = %{tl_version}
Provides:       tex(ecbx0500.tfm) = %{tl_version}, tex(ecbx0600.tfm) = %{tl_version}
Provides:       tex(ecbx0700.tfm) = %{tl_version}, tex(ecbx0800.tfm) = %{tl_version}
Provides:       tex(ecbx0900.tfm) = %{tl_version}, tex(ecbx1000.tfm) = %{tl_version}
Provides:       tex(ecbx1095.tfm) = %{tl_version}, tex(ecbx1200.tfm) = %{tl_version}
Provides:       tex(ecbx1440.tfm) = %{tl_version}, tex(ecbx1728.tfm) = %{tl_version}
Provides:       tex(ecbx2074.tfm) = %{tl_version}, tex(ecbx2488.tfm) = %{tl_version}
Provides:       tex(ecbx2986.tfm) = %{tl_version}, tex(ecbx3583.tfm) = %{tl_version}
Provides:       tex(eccc0500.tfm) = %{tl_version}, tex(eccc0600.tfm) = %{tl_version}
Provides:       tex(eccc0700.tfm) = %{tl_version}, tex(eccc0800.tfm) = %{tl_version}
Provides:       tex(eccc0900.tfm) = %{tl_version}, tex(eccc1000.tfm) = %{tl_version}
Provides:       tex(eccc1095.tfm) = %{tl_version}, tex(eccc1200.tfm) = %{tl_version}
Provides:       tex(eccc1440.tfm) = %{tl_version}, tex(eccc1728.tfm) = %{tl_version}
Provides:       tex(eccc2074.tfm) = %{tl_version}, tex(eccc2488.tfm) = %{tl_version}
Provides:       tex(eccc2986.tfm) = %{tl_version}, tex(eccc3583.tfm) = %{tl_version}
Provides:       tex(ecci0500.tfm) = %{tl_version}, tex(ecci0600.tfm) = %{tl_version}
Provides:       tex(ecci0700.tfm) = %{tl_version}, tex(ecci0800.tfm) = %{tl_version}
Provides:       tex(ecci0900.tfm) = %{tl_version}, tex(ecci1000.tfm) = %{tl_version}
Provides:       tex(ecci1095.tfm) = %{tl_version}, tex(ecci1200.tfm) = %{tl_version}
Provides:       tex(ecci1440.tfm) = %{tl_version}, tex(ecci1728.tfm) = %{tl_version}
Provides:       tex(ecci2074.tfm) = %{tl_version}, tex(ecci2488.tfm) = %{tl_version}
Provides:       tex(ecci2986.tfm) = %{tl_version}, tex(ecci3583.tfm) = %{tl_version}
Provides:       tex(ecdh0500.tfm) = %{tl_version}, tex(ecdh0600.tfm) = %{tl_version}
Provides:       tex(ecdh0700.tfm) = %{tl_version}, tex(ecdh0800.tfm) = %{tl_version}
Provides:       tex(ecdh0900.tfm) = %{tl_version}, tex(ecdh1000.tfm) = %{tl_version}
Provides:       tex(ecdh1095.tfm) = %{tl_version}, tex(ecdh1200.tfm) = %{tl_version}
Provides:       tex(ecdh1440.tfm) = %{tl_version}, tex(ecdh1728.tfm) = %{tl_version}
Provides:       tex(ecdh2074.tfm) = %{tl_version}, tex(ecdh2488.tfm) = %{tl_version}
Provides:       tex(ecdh2986.tfm) = %{tl_version}, tex(ecdh3583.tfm) = %{tl_version}
Provides:       tex(ecit0800.tfm) = %{tl_version}, tex(ecit0900.tfm) = %{tl_version}
Provides:       tex(ecit1000.tfm) = %{tl_version}, tex(ecit1095.tfm) = %{tl_version}
Provides:       tex(ecit1200.tfm) = %{tl_version}, tex(ecit1440.tfm) = %{tl_version}
Provides:       tex(ecit1728.tfm) = %{tl_version}, tex(ecit2074.tfm) = %{tl_version}
Provides:       tex(ecit2488.tfm) = %{tl_version}, tex(ecit2986.tfm) = %{tl_version}
Provides:       tex(ecit3583.tfm) = %{tl_version}, tex(eclb8.tfm) = %{tl_version}
Provides:       tex(ecli8.tfm) = %{tl_version}, tex(eclo8.tfm) = %{tl_version}
Provides:       tex(eclq8.tfm) = %{tl_version}, tex(ecltt8.tfm) = %{tl_version}
Provides:       tex(ecoc0500.tfm) = %{tl_version}, tex(ecoc0600.tfm) = %{tl_version}
Provides:       tex(ecoc0700.tfm) = %{tl_version}, tex(ecoc0800.tfm) = %{tl_version}
Provides:       tex(ecoc0900.tfm) = %{tl_version}, tex(ecoc1000.tfm) = %{tl_version}
Provides:       tex(ecoc1095.tfm) = %{tl_version}, tex(ecoc1200.tfm) = %{tl_version}
Provides:       tex(ecoc1440.tfm) = %{tl_version}, tex(ecoc1728.tfm) = %{tl_version}
Provides:       tex(ecoc2074.tfm) = %{tl_version}, tex(ecoc2488.tfm) = %{tl_version}
Provides:       tex(ecoc2986.tfm) = %{tl_version}, tex(ecoc3583.tfm) = %{tl_version}
Provides:       tex(ecrb0500.tfm) = %{tl_version}, tex(ecrb0600.tfm) = %{tl_version}
Provides:       tex(ecrb0700.tfm) = %{tl_version}, tex(ecrb0800.tfm) = %{tl_version}
Provides:       tex(ecrb0900.tfm) = %{tl_version}, tex(ecrb1000.tfm) = %{tl_version}
Provides:       tex(ecrb1095.tfm) = %{tl_version}, tex(ecrb1200.tfm) = %{tl_version}
Provides:       tex(ecrb1440.tfm) = %{tl_version}, tex(ecrb1728.tfm) = %{tl_version}
Provides:       tex(ecrb2074.tfm) = %{tl_version}, tex(ecrb2488.tfm) = %{tl_version}
Provides:       tex(ecrb2986.tfm) = %{tl_version}, tex(ecrb3583.tfm) = %{tl_version}
Provides:       tex(ecrm0500.tfm) = %{tl_version}, tex(ecrm0600.tfm) = %{tl_version}
Provides:       tex(ecrm0700.tfm) = %{tl_version}, tex(ecrm0800.tfm) = %{tl_version}
Provides:       tex(ecrm0900.tfm) = %{tl_version}, tex(ecrm1000.tfm) = %{tl_version}
Provides:       tex(ecrm1095.tfm) = %{tl_version}, tex(ecrm1200.tfm) = %{tl_version}
Provides:       tex(ecrm1440.tfm) = %{tl_version}, tex(ecrm1728.tfm) = %{tl_version}
Provides:       tex(ecrm2074.tfm) = %{tl_version}, tex(ecrm2488.tfm) = %{tl_version}
Provides:       tex(ecrm2986.tfm) = %{tl_version}, tex(ecrm3583.tfm) = %{tl_version}
Provides:       tex(ecsc0500.tfm) = %{tl_version}, tex(ecsc0600.tfm) = %{tl_version}
Provides:       tex(ecsc0700.tfm) = %{tl_version}, tex(ecsc0800.tfm) = %{tl_version}
Provides:       tex(ecsc0900.tfm) = %{tl_version}, tex(ecsc1000.tfm) = %{tl_version}
Provides:       tex(ecsc1095.tfm) = %{tl_version}, tex(ecsc1200.tfm) = %{tl_version}
Provides:       tex(ecsc1440.tfm) = %{tl_version}, tex(ecsc1728.tfm) = %{tl_version}
Provides:       tex(ecsc2074.tfm) = %{tl_version}, tex(ecsc2488.tfm) = %{tl_version}
Provides:       tex(ecsc2986.tfm) = %{tl_version}, tex(ecsc3583.tfm) = %{tl_version}
Provides:       tex(ecsi0500.tfm) = %{tl_version}, tex(ecsi0600.tfm) = %{tl_version}
Provides:       tex(ecsi0700.tfm) = %{tl_version}, tex(ecsi0800.tfm) = %{tl_version}
Provides:       tex(ecsi0900.tfm) = %{tl_version}, tex(ecsi1000.tfm) = %{tl_version}
Provides:       tex(ecsi1095.tfm) = %{tl_version}, tex(ecsi1200.tfm) = %{tl_version}
Provides:       tex(ecsi1440.tfm) = %{tl_version}, tex(ecsi1728.tfm) = %{tl_version}
Provides:       tex(ecsi2074.tfm) = %{tl_version}, tex(ecsi2488.tfm) = %{tl_version}
Provides:       tex(ecsi2986.tfm) = %{tl_version}, tex(ecsi3583.tfm) = %{tl_version}
Provides:       tex(ecsl0500.tfm) = %{tl_version}, tex(ecsl0600.tfm) = %{tl_version}
Provides:       tex(ecsl0700.tfm) = %{tl_version}, tex(ecsl0800.tfm) = %{tl_version}
Provides:       tex(ecsl0900.tfm) = %{tl_version}, tex(ecsl1000.tfm) = %{tl_version}
Provides:       tex(ecsl1095.tfm) = %{tl_version}, tex(ecsl1200.tfm) = %{tl_version}
Provides:       tex(ecsl1440.tfm) = %{tl_version}, tex(ecsl1728.tfm) = %{tl_version}
Provides:       tex(ecsl2074.tfm) = %{tl_version}, tex(ecsl2488.tfm) = %{tl_version}
Provides:       tex(ecsl2986.tfm) = %{tl_version}, tex(ecsl3583.tfm) = %{tl_version}
Provides:       tex(ecso0500.tfm) = %{tl_version}, tex(ecso0600.tfm) = %{tl_version}
Provides:       tex(ecso0700.tfm) = %{tl_version}, tex(ecso0800.tfm) = %{tl_version}
Provides:       tex(ecso0900.tfm) = %{tl_version}, tex(ecso1000.tfm) = %{tl_version}
Provides:       tex(ecso1095.tfm) = %{tl_version}, tex(ecso1200.tfm) = %{tl_version}
Provides:       tex(ecso1440.tfm) = %{tl_version}, tex(ecso1728.tfm) = %{tl_version}
Provides:       tex(ecso2074.tfm) = %{tl_version}, tex(ecso2488.tfm) = %{tl_version}
Provides:       tex(ecso2986.tfm) = %{tl_version}, tex(ecso3583.tfm) = %{tl_version}
Provides:       tex(ecss0500.tfm) = %{tl_version}, tex(ecss0600.tfm) = %{tl_version}
Provides:       tex(ecss0700.tfm) = %{tl_version}, tex(ecss0800.tfm) = %{tl_version}
Provides:       tex(ecss0900.tfm) = %{tl_version}, tex(ecss1000.tfm) = %{tl_version}
Provides:       tex(ecss1095.tfm) = %{tl_version}, tex(ecss1200.tfm) = %{tl_version}
Provides:       tex(ecss1440.tfm) = %{tl_version}, tex(ecss1728.tfm) = %{tl_version}
Provides:       tex(ecss2074.tfm) = %{tl_version}, tex(ecss2488.tfm) = %{tl_version}
Provides:       tex(ecss2986.tfm) = %{tl_version}, tex(ecss3583.tfm) = %{tl_version}
Provides:       tex(ecst0800.tfm) = %{tl_version}, tex(ecst0900.tfm) = %{tl_version}
Provides:       tex(ecst1000.tfm) = %{tl_version}, tex(ecst1095.tfm) = %{tl_version}
Provides:       tex(ecst1200.tfm) = %{tl_version}, tex(ecst1440.tfm) = %{tl_version}
Provides:       tex(ecst1728.tfm) = %{tl_version}, tex(ecst2074.tfm) = %{tl_version}
Provides:       tex(ecst2488.tfm) = %{tl_version}, tex(ecst2986.tfm) = %{tl_version}
Provides:       tex(ecst3583.tfm) = %{tl_version}, tex(ecsx0500.tfm) = %{tl_version}
Provides:       tex(ecsx0600.tfm) = %{tl_version}, tex(ecsx0700.tfm) = %{tl_version}
Provides:       tex(ecsx0800.tfm) = %{tl_version}, tex(ecsx0900.tfm) = %{tl_version}
Provides:       tex(ecsx1000.tfm) = %{tl_version}, tex(ecsx1095.tfm) = %{tl_version}
Provides:       tex(ecsx1200.tfm) = %{tl_version}, tex(ecsx1440.tfm) = %{tl_version}
Provides:       tex(ecsx1728.tfm) = %{tl_version}, tex(ecsx2074.tfm) = %{tl_version}
Provides:       tex(ecsx2488.tfm) = %{tl_version}, tex(ecsx2986.tfm) = %{tl_version}
Provides:       tex(ecsx3583.tfm) = %{tl_version}, tex(ectc0800.tfm) = %{tl_version}
Provides:       tex(ectc0900.tfm) = %{tl_version}, tex(ectc1000.tfm) = %{tl_version}
Provides:       tex(ectc1095.tfm) = %{tl_version}, tex(ectc1200.tfm) = %{tl_version}
Provides:       tex(ectc1440.tfm) = %{tl_version}, tex(ectc1728.tfm) = %{tl_version}
Provides:       tex(ectc2074.tfm) = %{tl_version}, tex(ectc2488.tfm) = %{tl_version}
Provides:       tex(ectc2986.tfm) = %{tl_version}, tex(ectc3583.tfm) = %{tl_version}
Provides:       tex(ecti0500.tfm) = %{tl_version}, tex(ecti0600.tfm) = %{tl_version}
Provides:       tex(ecti0700.tfm) = %{tl_version}, tex(ecti0800.tfm) = %{tl_version}
Provides:       tex(ecti0900.tfm) = %{tl_version}, tex(ecti1000.tfm) = %{tl_version}
Provides:       tex(ecti1095.tfm) = %{tl_version}, tex(ecti1200.tfm) = %{tl_version}
Provides:       tex(ecti1440.tfm) = %{tl_version}, tex(ecti1728.tfm) = %{tl_version}
Provides:       tex(ecti2074.tfm) = %{tl_version}, tex(ecti2488.tfm) = %{tl_version}
Provides:       tex(ecti2986.tfm) = %{tl_version}, tex(ecti3583.tfm) = %{tl_version}
Provides:       tex(ectt0800.tfm) = %{tl_version}, tex(ectt0900.tfm) = %{tl_version}
Provides:       tex(ectt1000.tfm) = %{tl_version}, tex(ectt1095.tfm) = %{tl_version}
Provides:       tex(ectt1200.tfm) = %{tl_version}, tex(ectt1440.tfm) = %{tl_version}
Provides:       tex(ectt1728.tfm) = %{tl_version}, tex(ectt2074.tfm) = %{tl_version}
Provides:       tex(ectt2488.tfm) = %{tl_version}, tex(ectt2986.tfm) = %{tl_version}
Provides:       tex(ectt3583.tfm) = %{tl_version}, tex(ecui0500.tfm) = %{tl_version}
Provides:       tex(ecui0600.tfm) = %{tl_version}, tex(ecui0700.tfm) = %{tl_version}
Provides:       tex(ecui0800.tfm) = %{tl_version}, tex(ecui0900.tfm) = %{tl_version}
Provides:       tex(ecui1000.tfm) = %{tl_version}, tex(ecui1095.tfm) = %{tl_version}
Provides:       tex(ecui1200.tfm) = %{tl_version}, tex(ecui1440.tfm) = %{tl_version}
Provides:       tex(ecui1728.tfm) = %{tl_version}, tex(ecui2074.tfm) = %{tl_version}
Provides:       tex(ecui2488.tfm) = %{tl_version}, tex(ecui2986.tfm) = %{tl_version}
Provides:       tex(ecui3583.tfm) = %{tl_version}, tex(ecvi0800.tfm) = %{tl_version}
Provides:       tex(ecvi0900.tfm) = %{tl_version}, tex(ecvi1000.tfm) = %{tl_version}
Provides:       tex(ecvi1095.tfm) = %{tl_version}, tex(ecvi1200.tfm) = %{tl_version}
Provides:       tex(ecvi1440.tfm) = %{tl_version}, tex(ecvi1728.tfm) = %{tl_version}
Provides:       tex(ecvi2074.tfm) = %{tl_version}, tex(ecvi2488.tfm) = %{tl_version}
Provides:       tex(ecvi2986.tfm) = %{tl_version}, tex(ecvi3583.tfm) = %{tl_version}
Provides:       tex(ecvt0800.tfm) = %{tl_version}, tex(ecvt0900.tfm) = %{tl_version}
Provides:       tex(ecvt1000.tfm) = %{tl_version}, tex(ecvt1095.tfm) = %{tl_version}
Provides:       tex(ecvt1200.tfm) = %{tl_version}, tex(ecvt1440.tfm) = %{tl_version}
Provides:       tex(ecvt1728.tfm) = %{tl_version}, tex(ecvt2074.tfm) = %{tl_version}
Provides:       tex(ecvt2488.tfm) = %{tl_version}, tex(ecvt2986.tfm) = %{tl_version}
Provides:       tex(ecvt3583.tfm) = %{tl_version}, tex(ecxc0500.tfm) = %{tl_version}
Provides:       tex(ecxc0600.tfm) = %{tl_version}, tex(ecxc0700.tfm) = %{tl_version}
Provides:       tex(ecxc0800.tfm) = %{tl_version}, tex(ecxc0900.tfm) = %{tl_version}
Provides:       tex(ecxc1000.tfm) = %{tl_version}, tex(ecxc1095.tfm) = %{tl_version}
Provides:       tex(ecxc1200.tfm) = %{tl_version}, tex(ecxc1440.tfm) = %{tl_version}
Provides:       tex(ecxc1728.tfm) = %{tl_version}, tex(ecxc2074.tfm) = %{tl_version}
Provides:       tex(ecxc2488.tfm) = %{tl_version}, tex(ecxc2986.tfm) = %{tl_version}
Provides:       tex(ecxc3583.tfm) = %{tl_version}, tex(ieclb8.tfm) = %{tl_version}
Provides:       tex(iecli8.tfm) = %{tl_version}, tex(ieclo8.tfm) = %{tl_version}
Provides:       tex(ieclq8.tfm) = %{tl_version}, tex(iecltt8.tfm) = %{tl_version}
Provides:       tex(tcbi0500.tfm) = %{tl_version}, tex(tcbi0600.tfm) = %{tl_version}
Provides:       tex(tcbi0700.tfm) = %{tl_version}, tex(tcbi0800.tfm) = %{tl_version}
Provides:       tex(tcbi0900.tfm) = %{tl_version}, tex(tcbi1000.tfm) = %{tl_version}
Provides:       tex(tcbi1095.tfm) = %{tl_version}, tex(tcbi1200.tfm) = %{tl_version}
Provides:       tex(tcbi1440.tfm) = %{tl_version}, tex(tcbi1728.tfm) = %{tl_version}
Provides:       tex(tcbi2074.tfm) = %{tl_version}, tex(tcbi2488.tfm) = %{tl_version}
Provides:       tex(tcbi2986.tfm) = %{tl_version}, tex(tcbi3583.tfm) = %{tl_version}
Provides:       tex(tcbl0500.tfm) = %{tl_version}, tex(tcbl0600.tfm) = %{tl_version}
Provides:       tex(tcbl0700.tfm) = %{tl_version}, tex(tcbl0800.tfm) = %{tl_version}
Provides:       tex(tcbl0900.tfm) = %{tl_version}, tex(tcbl1000.tfm) = %{tl_version}
Provides:       tex(tcbl1095.tfm) = %{tl_version}, tex(tcbl1200.tfm) = %{tl_version}
Provides:       tex(tcbl1440.tfm) = %{tl_version}, tex(tcbl1728.tfm) = %{tl_version}
Provides:       tex(tcbl2074.tfm) = %{tl_version}, tex(tcbl2488.tfm) = %{tl_version}
Provides:       tex(tcbl2986.tfm) = %{tl_version}, tex(tcbl3583.tfm) = %{tl_version}
Provides:       tex(tcbx0500.tfm) = %{tl_version}, tex(tcbx0600.tfm) = %{tl_version}
Provides:       tex(tcbx0700.tfm) = %{tl_version}, tex(tcbx0800.tfm) = %{tl_version}
Provides:       tex(tcbx0900.tfm) = %{tl_version}, tex(tcbx1000.tfm) = %{tl_version}
Provides:       tex(tcbx1095.tfm) = %{tl_version}, tex(tcbx1200.tfm) = %{tl_version}
Provides:       tex(tcbx1440.tfm) = %{tl_version}, tex(tcbx1728.tfm) = %{tl_version}
Provides:       tex(tcbx2074.tfm) = %{tl_version}, tex(tcbx2488.tfm) = %{tl_version}
Provides:       tex(tcbx2986.tfm) = %{tl_version}, tex(tcbx3583.tfm) = %{tl_version}
Provides:       tex(tcci0500.tfm) = %{tl_version}, tex(tcci0600.tfm) = %{tl_version}
Provides:       tex(tcci0700.tfm) = %{tl_version}, tex(tcci0800.tfm) = %{tl_version}
Provides:       tex(tcci0900.tfm) = %{tl_version}, tex(tcci1000.tfm) = %{tl_version}
Provides:       tex(tcci1095.tfm) = %{tl_version}, tex(tcci1200.tfm) = %{tl_version}
Provides:       tex(tcci1440.tfm) = %{tl_version}, tex(tcci1728.tfm) = %{tl_version}
Provides:       tex(tcci2074.tfm) = %{tl_version}, tex(tcci2488.tfm) = %{tl_version}
Provides:       tex(tcci2986.tfm) = %{tl_version}, tex(tcci3583.tfm) = %{tl_version}
Provides:       tex(tcit0800.tfm) = %{tl_version}, tex(tcit0900.tfm) = %{tl_version}
Provides:       tex(tcit1000.tfm) = %{tl_version}, tex(tcit1095.tfm) = %{tl_version}
Provides:       tex(tcit1200.tfm) = %{tl_version}, tex(tcit1440.tfm) = %{tl_version}
Provides:       tex(tcit1728.tfm) = %{tl_version}, tex(tcit2074.tfm) = %{tl_version}
Provides:       tex(tcit2488.tfm) = %{tl_version}, tex(tcit2986.tfm) = %{tl_version}
Provides:       tex(tcit3583.tfm) = %{tl_version}, tex(tcrb0500.tfm) = %{tl_version}
Provides:       tex(tcrb0600.tfm) = %{tl_version}, tex(tcrb0700.tfm) = %{tl_version}
Provides:       tex(tcrb0800.tfm) = %{tl_version}, tex(tcrb0900.tfm) = %{tl_version}
Provides:       tex(tcrb1000.tfm) = %{tl_version}, tex(tcrb1095.tfm) = %{tl_version}
Provides:       tex(tcrb1200.tfm) = %{tl_version}, tex(tcrb1440.tfm) = %{tl_version}
Provides:       tex(tcrb1728.tfm) = %{tl_version}, tex(tcrb2074.tfm) = %{tl_version}
Provides:       tex(tcrb2488.tfm) = %{tl_version}, tex(tcrb2986.tfm) = %{tl_version}
Provides:       tex(tcrb3583.tfm) = %{tl_version}, tex(tcrm0500.tfm) = %{tl_version}
Provides:       tex(tcrm0600.tfm) = %{tl_version}, tex(tcrm0700.tfm) = %{tl_version}
Provides:       tex(tcrm0800.tfm) = %{tl_version}, tex(tcrm0900.tfm) = %{tl_version}
Provides:       tex(tcrm1000.tfm) = %{tl_version}, tex(tcrm1095.tfm) = %{tl_version}
Provides:       tex(tcrm1200.tfm) = %{tl_version}, tex(tcrm1440.tfm) = %{tl_version}
Provides:       tex(tcrm1728.tfm) = %{tl_version}, tex(tcrm2074.tfm) = %{tl_version}
Provides:       tex(tcrm2488.tfm) = %{tl_version}, tex(tcrm2986.tfm) = %{tl_version}
Provides:       tex(tcrm3583.tfm) = %{tl_version}, tex(tcsi0500.tfm) = %{tl_version}
Provides:       tex(tcsi0600.tfm) = %{tl_version}, tex(tcsi0700.tfm) = %{tl_version}
Provides:       tex(tcsi0800.tfm) = %{tl_version}, tex(tcsi0900.tfm) = %{tl_version}
Provides:       tex(tcsi1000.tfm) = %{tl_version}, tex(tcsi1095.tfm) = %{tl_version}
Provides:       tex(tcsi1200.tfm) = %{tl_version}, tex(tcsi1440.tfm) = %{tl_version}
Provides:       tex(tcsi1728.tfm) = %{tl_version}, tex(tcsi2074.tfm) = %{tl_version}
Provides:       tex(tcsi2488.tfm) = %{tl_version}, tex(tcsi2986.tfm) = %{tl_version}
Provides:       tex(tcsi3583.tfm) = %{tl_version}, tex(tcsl0500.tfm) = %{tl_version}
Provides:       tex(tcsl0600.tfm) = %{tl_version}, tex(tcsl0700.tfm) = %{tl_version}
Provides:       tex(tcsl0800.tfm) = %{tl_version}, tex(tcsl0900.tfm) = %{tl_version}
Provides:       tex(tcsl1000.tfm) = %{tl_version}, tex(tcsl1095.tfm) = %{tl_version}
Provides:       tex(tcsl1200.tfm) = %{tl_version}, tex(tcsl1440.tfm) = %{tl_version}
Provides:       tex(tcsl1728.tfm) = %{tl_version}, tex(tcsl2074.tfm) = %{tl_version}
Provides:       tex(tcsl2488.tfm) = %{tl_version}, tex(tcsl2986.tfm) = %{tl_version}
Provides:       tex(tcsl3583.tfm) = %{tl_version}, tex(tcso0500.tfm) = %{tl_version}
Provides:       tex(tcso0600.tfm) = %{tl_version}, tex(tcso0700.tfm) = %{tl_version}
Provides:       tex(tcso0800.tfm) = %{tl_version}, tex(tcso0900.tfm) = %{tl_version}
Provides:       tex(tcso1000.tfm) = %{tl_version}, tex(tcso1095.tfm) = %{tl_version}
Provides:       tex(tcso1200.tfm) = %{tl_version}, tex(tcso1440.tfm) = %{tl_version}
Provides:       tex(tcso1728.tfm) = %{tl_version}, tex(tcso2074.tfm) = %{tl_version}
Provides:       tex(tcso2488.tfm) = %{tl_version}, tex(tcso2986.tfm) = %{tl_version}
Provides:       tex(tcso3583.tfm) = %{tl_version}, tex(tcss0500.tfm) = %{tl_version}
Provides:       tex(tcss0600.tfm) = %{tl_version}, tex(tcss0700.tfm) = %{tl_version}
Provides:       tex(tcss0800.tfm) = %{tl_version}, tex(tcss0900.tfm) = %{tl_version}
Provides:       tex(tcss1000.tfm) = %{tl_version}, tex(tcss1095.tfm) = %{tl_version}
Provides:       tex(tcss1200.tfm) = %{tl_version}, tex(tcss1440.tfm) = %{tl_version}
Provides:       tex(tcss1728.tfm) = %{tl_version}, tex(tcss2074.tfm) = %{tl_version}
Provides:       tex(tcss2488.tfm) = %{tl_version}, tex(tcss2986.tfm) = %{tl_version}
Provides:       tex(tcss3583.tfm) = %{tl_version}, tex(tcst0800.tfm) = %{tl_version}
Provides:       tex(tcst0900.tfm) = %{tl_version}, tex(tcst1000.tfm) = %{tl_version}
Provides:       tex(tcst1095.tfm) = %{tl_version}, tex(tcst1200.tfm) = %{tl_version}
Provides:       tex(tcst1440.tfm) = %{tl_version}, tex(tcst1728.tfm) = %{tl_version}
Provides:       tex(tcst2074.tfm) = %{tl_version}, tex(tcst2488.tfm) = %{tl_version}
Provides:       tex(tcst2986.tfm) = %{tl_version}, tex(tcst3583.tfm) = %{tl_version}
Provides:       tex(tcsx0500.tfm) = %{tl_version}, tex(tcsx0600.tfm) = %{tl_version}
Provides:       tex(tcsx0700.tfm) = %{tl_version}, tex(tcsx0800.tfm) = %{tl_version}
Provides:       tex(tcsx0900.tfm) = %{tl_version}, tex(tcsx1000.tfm) = %{tl_version}
Provides:       tex(tcsx1095.tfm) = %{tl_version}, tex(tcsx1200.tfm) = %{tl_version}
Provides:       tex(tcsx1440.tfm) = %{tl_version}, tex(tcsx1728.tfm) = %{tl_version}
Provides:       tex(tcsx2074.tfm) = %{tl_version}, tex(tcsx2488.tfm) = %{tl_version}
Provides:       tex(tcsx2986.tfm) = %{tl_version}, tex(tcsx3583.tfm) = %{tl_version}
Provides:       tex(tcti0500.tfm) = %{tl_version}, tex(tcti0600.tfm) = %{tl_version}
Provides:       tex(tcti0700.tfm) = %{tl_version}, tex(tcti0800.tfm) = %{tl_version}
Provides:       tex(tcti0900.tfm) = %{tl_version}, tex(tcti1000.tfm) = %{tl_version}
Provides:       tex(tcti1095.tfm) = %{tl_version}, tex(tcti1200.tfm) = %{tl_version}
Provides:       tex(tcti1440.tfm) = %{tl_version}, tex(tcti1728.tfm) = %{tl_version}
Provides:       tex(tcti2074.tfm) = %{tl_version}, tex(tcti2488.tfm) = %{tl_version}
Provides:       tex(tcti2986.tfm) = %{tl_version}, tex(tcti3583.tfm) = %{tl_version}
Provides:       tex(tctt0800.tfm) = %{tl_version}, tex(tctt0900.tfm) = %{tl_version}
Provides:       tex(tctt1000.tfm) = %{tl_version}, tex(tctt1095.tfm) = %{tl_version}
Provides:       tex(tctt1200.tfm) = %{tl_version}, tex(tctt1440.tfm) = %{tl_version}
Provides:       tex(tctt1728.tfm) = %{tl_version}, tex(tctt2074.tfm) = %{tl_version}
Provides:       tex(tctt2488.tfm) = %{tl_version}, tex(tctt2986.tfm) = %{tl_version}
Provides:       tex(tctt3583.tfm) = %{tl_version}, tex(tcui0500.tfm) = %{tl_version}
Provides:       tex(tcui0600.tfm) = %{tl_version}, tex(tcui0700.tfm) = %{tl_version}
Provides:       tex(tcui0800.tfm) = %{tl_version}, tex(tcui0900.tfm) = %{tl_version}
Provides:       tex(tcui1000.tfm) = %{tl_version}, tex(tcui1095.tfm) = %{tl_version}
Provides:       tex(tcui1200.tfm) = %{tl_version}, tex(tcui1440.tfm) = %{tl_version}
Provides:       tex(tcui1728.tfm) = %{tl_version}, tex(tcui2074.tfm) = %{tl_version}
Provides:       tex(tcui2488.tfm) = %{tl_version}, tex(tcui2986.tfm) = %{tl_version}
Provides:       tex(tcui3583.tfm) = %{tl_version}, tex(tcvi0800.tfm) = %{tl_version}
Provides:       tex(tcvi0900.tfm) = %{tl_version}, tex(tcvi1000.tfm) = %{tl_version}
Provides:       tex(tcvi1095.tfm) = %{tl_version}, tex(tcvi1200.tfm) = %{tl_version}
Provides:       tex(tcvi1440.tfm) = %{tl_version}, tex(tcvi1728.tfm) = %{tl_version}
Provides:       tex(tcvi2074.tfm) = %{tl_version}, tex(tcvi2488.tfm) = %{tl_version}
Provides:       tex(tcvi2986.tfm) = %{tl_version}, tex(tcvi3583.tfm) = %{tl_version}
Provides:       tex(tcvt0800.tfm) = %{tl_version}, tex(tcvt0900.tfm) = %{tl_version}
Provides:       tex(tcvt1000.tfm) = %{tl_version}, tex(tcvt1095.tfm) = %{tl_version}
Provides:       tex(tcvt1200.tfm) = %{tl_version}, tex(tcvt1440.tfm) = %{tl_version}
Provides:       tex(tcvt1728.tfm) = %{tl_version}, tex(tcvt2074.tfm) = %{tl_version}
Provides:       tex(tcvt2488.tfm) = %{tl_version}, tex(tcvt2986.tfm) = %{tl_version}
Provides:       tex(tcvt3583.tfm) = %{tl_version}

%description -n texlive-ec
The EC fonts are European Computer Modern Fonts, supporting the
complete LaTeX T1 encoding defined at the 1990 TUG conference
hold at Cork/Ireland. These fonts are intended to be stable
with no changes being made to the tfm files. The set also
contains a Text Companion Symbol font, called tc, featuring
many useful characters needed in text typesetting, for example
oldstyle digits, currency symbols (including the newly created
Euro symbol), the permille sign, copyright, trade mark and
servicemark as well as a copyleft sign, and many others. Recent
releases of LaTeX2e support the EC fonts. The EC fonts
supersede the preliminary version released as the DC fonts. The
fonts are available in (traced) Adobe Type 1 format, as part of
the cm-super bundle. The other Computer Modern-style T1-encoded
Type 1 set, Latin Modern, is not actually a direct development
of the EC set, and differs from the EC in a number of
particulars.

%package -n texlive-ec-doc
Summary:        Documentation for ec
Version:        svn25033.1.0

Provides:       tex-ec-doc
AutoReqProv:    No

%description -n texlive-ec-doc
Documentation for ec

%package -n texlive-euro
Provides:       tex-euro = %{tl_version}
License:        LPPL
Summary:        Provide Euro values for national currency amounts
Version:        svn22191.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fp-basic.sty), tex(fp-snap.sty)
Provides:       tex(euro.sty) = %{tl_version}

%description -n texlive-euro
Converts arbitrary national currency amounts using the Euro as
base unit, and typesets monetary amounts in almost any desired
way. Write, e.g., \ATS{17.6} to get something like '17,60 oS
(1,28 Euro)' automatically. Conversion rates for the initial
Euro-zone countries are already built-in. Further rates can be
added easily. The package uses the fp package to do its sums.

%package -n texlive-euro-doc
Summary:        Documentation for euro
Version:        svn22191.1.1

Provides:       tex-euro-doc
AutoReqProv:    No

%description -n texlive-euro-doc
Documentation for euro

%package -n texlive-eurosym
Provides:       tex-eurosym = %{tl_version}
License:        Eurosym
Summary:        Metafont and macros for Euro sign
Version:        svn17265.1.4_subrfix

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(eurosym.map) = %{tl_version}, tex(feybl10.tfm) = %{tl_version}
Provides:       tex(feybo10.tfm) = %{tl_version}, tex(feybr10.tfm) = %{tl_version}
Provides:       tex(feyml10.tfm) = %{tl_version}, tex(feymo10.tfm) = %{tl_version}
Provides:       tex(feymr10.tfm) = %{tl_version}, tex(feybl10.pfb) = %{tl_version}
Provides:       tex(feybo10.pfb) = %{tl_version}, tex(feybr10.pfb) = %{tl_version}
Provides:       tex(feyml10.pfb) = %{tl_version}, tex(feymo10.pfb) = %{tl_version}
Provides:       tex(feymr10.pfb) = %{tl_version}, tex(geybl10.pfb) = %{tl_version}
Provides:       tex(geybo10.pfb) = %{tl_version}, tex(geybr10.pfb) = %{tl_version}
Provides:       tex(geyml10.pfb) = %{tl_version}, tex(geymo10.pfb) = %{tl_version}
Provides:       tex(geymr10.pfb) = %{tl_version}, tex(eurosym.sty) = %{tl_version}

%description -n texlive-eurosym
The European currency symbol for the Euro implemented in
Metafont, using the official European Commission dimensions,
and providing several shapes (normal, slanted, bold, outline).
The package also includes a LaTeX package which defines the
macro, pre-compiled tfm files, and documentation.

%package -n texlive-eurosym-doc
Summary:        Documentation for eurosym
Version:        svn17265.1.4_subrfix

Provides:       tex-eurosym-doc
AutoReqProv:    No

%description -n texlive-eurosym-doc
Documentation for eurosym

%package -n texlive-edmac
Provides:       tex-edmac = %{tl_version}
License:        GPLv2+
Summary:        Typeset critical editions
Version:        svn15878.3.17

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(edmac.tex) = %{tl_version}, tex(edmacfss.sty) = %{tl_version}
Provides:       tex(edstanza.tex) = %{tl_version}, tex(tabmac.tex) = %{tl_version}

%description -n texlive-edmac
This is the type example package for typesetting scholarly
critical editions.

%package -n texlive-edmac-doc
Summary:        Documentation for edmac
Version:        svn15878.3.17

Provides:       tex-edmac-doc
AutoReqProv:    No

%description -n texlive-edmac-doc
Documentation for edmac

%package -n texlive-egameps
Provides:       tex-egameps = %{tl_version}
License:        LPPL
Summary:        LaTeX package for typesetting extensive games
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(egameps.sty) = %{tl_version}

%description -n texlive-egameps
The style is intended to have enough features to draw any
extensive game with relative ease. The facilities of PSTricks
are used for graphics. (An older version of the package, which
uses the LaTeX picture environment rather than PSTricks and
consequently has many fewer features is available on the
package home page.)

%package -n texlive-egameps-doc
Summary:        Documentation for egameps
Version:        svn15878.1.1

Provides:       tex-egameps-doc
AutoReqProv:    No

%description -n texlive-egameps-doc
Documentation for egameps

%package -n texlive-eijkhout
Provides:       tex-eijkhout = %{tl_version}
License:        Public Domain
Summary:        Victor Eijkhout's packages
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(CD_labeler.tex) = %{tl_version}, tex(CD_labeler_test.tex) = %{tl_version}
Provides:       tex(DB_process.tex) = %{tl_version}, tex(repeat.tex) = %{tl_version}

%description -n texlive-eijkhout
Three unrelated packages: DB_process, to parse and process
database output; CD_labeler, to typeset user text to fit on a
CD label; and repeat, a nestable, generic loop macro.

%package -n texlive-encxvlna
Provides:       tex-encxvlna = %{tl_version}
License:        LPPL
Summary:        Insert nonbreakable spaces, using encTeX
Version:        svn34087.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(encxvlna.sty) = %{tl_version}, tex(encxvlna.tex) = %{tl_version}

%description -n texlive-encxvlna
The package provides tools for inserting nonbreakable spaces
after nonsyllabic prepositions and single letter conjunctions
as required by Czech and Slovak typographical rules. It is
implemented using encTeX and provides files both for plain TeX
and LaTeX. The LaTeX solution tries to avoid conflicts with
other packages.

%package -n texlive-encxvlna-doc
Summary:        Documentation for encxvlna
Version:        svn34087.1.1

Provides:       tex-encxvlna-doc
AutoReqProv:    No

%description -n texlive-encxvlna-doc
Documentation for encxvlna

%package -n texlive-epigram
Provides:       tex-epigram = %{tl_version}
License:        Public Domain
Summary:        Display short quotations
Version:        svn20513.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(epigram.tex) = %{tl_version}

%description -n texlive-epigram
The package determines (on the basis of the width of the text
of the epigram, laid out on a single line) whether to produce a
line or a displayed paragraph.

%package -n texlive-epsf
Provides:       tex-epsf = %{tl_version}
License:        Public Domain
Summary:        Simple macros for EPS inclusion
Version:        svn21461.2.7.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(epsf.sty) = %{tl_version}, tex(epsf.tex) = %{tl_version}

%description -n texlive-epsf
The original (and now obsolescent) graphics inclusion macros
for use with dvips, still widely used by Plain TeX users (in
particular). For LaTeX users, the package is nowadays (rather
strongly) deprecated in favour of the more sophisticated
standard LaTeX graphics bundle of packages. (The graphics
bundle is also available to Plain TeX users, via its Plain TeX
version.)

%package -n texlive-epsf-doc
Summary:        Documentation for epsf
Version:        svn21461.2.7.4

Provides:       tex-epsf-doc
AutoReqProv:    No

%description -n texlive-epsf-doc
Documentation for epsf

%package -n texlive-ecltree
Provides:       tex-ecltree = %{tl_version}
License:        LPPL
Summary:        Trees using epic and eepic macros
Version:        svn15878.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ecltree.sty) = %{tl_version}

%description -n texlive-ecltree
The package recursively draws trees: each subtree is defined in
a 'bundle' environment, with a set of leaves described by
\chunk macros. A chunk may have a bundle environment inside it.

%package -n texlive-ecltree-doc
Summary:        Documentation for ecltree
Version:        svn15878.1.1a

Provides:       tex-ecltree-doc
AutoReqProv:    No

%description -n texlive-ecltree-doc
Documentation for ecltree

%package -n texlive-edfnotes
Provides:       tex-edfnotes = %{tl_version}
License:        LPPL 1.3
Summary:        Critical annotations to footnotes with ednotes
Version:        svn21540.0.6b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fnlineno.sty)
Provides:       tex(edfnotes.sty) = %{tl_version}

%description -n texlive-edfnotes
The package modifies the annotation commands and label-test
mechanism of the ednotes package so that critical notes appear
on the pages and in the order that one would expect.

%package -n texlive-edfnotes-doc
Summary:        Documentation for edfnotes
Version:        svn21540.0.6b

Provides:       tex-edfnotes-doc
AutoReqProv:    No

%description -n texlive-edfnotes-doc
Documentation for edfnotes

%package -n texlive-ednotes
Provides:       tex-ednotes = %{tl_version}
License:        LPPL
Summary:        Typeset scholarly editions
Version:        svn35829.1.3a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex-ncctools, tex(mfparptc.sty), tex(manyfoot.sty), tex(lineno.sty)
Provides:       tex(edcntwd0.sty) = %{tl_version}, tex(ednotes.sty) = %{tl_version}
Provides:       tex(lblchng1.sty) = %{tl_version}, tex(mfparptc.sty) = %{tl_version}
Provides:       tex(mfparxsp.sty) = %{tl_version}

%description -n texlive-ednotes
A macro package for typesetting scholarly critical editions.
Provides macros for critical edition typesetting with LaTeX,
including support for line numbers and layers of footnotes.

%package -n texlive-ednotes-doc
Summary:        Documentation for ednotes
Version:        svn35829.1.3a

Provides:       tex-ednotes-doc
AutoReqProv:    No
Requires:       tex-ncctools-doc

%description -n texlive-ednotes-doc
Documentation for ednotes

%package -n texlive-eledform
Provides:       tex-eledform = %{tl_version}
License:        LPPL 1.3
Summary:        Define textual variants
Version:        svn38114.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(eledmac.sty)
Provides:       tex(eledform.sty) = %{tl_version}

%description -n texlive-eledform
The package provides commands to formalize textual variants in
critical editions typeset using eledmac.

%package -n texlive-eledform-doc
Summary:        Documentation for eledform
Version:        svn38114.1.1a

Provides:       tex-eledform-doc
AutoReqProv:    No

%description -n texlive-eledform-doc
Documentation for eledform

%package -n texlive-eledmac
Provides:       tex-eledmac = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset scholarly editions
Version:        svn45418
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(xargs.sty), tex(etoolbox.sty), tex(etex.sty)
Requires:       tex(suffix.sty), tex(xstring.sty), tex(ifluatex.sty), tex(ragged2e.sty)
Requires:       tex(ifxetex.sty), tex(xspace.sty)
Provides:       tex(eledmac.sty) = %{tl_version}, tex(eledpar.sty) = %{tl_version}

%description -n texlive-eledmac
A package for typesetting scholarly critical editions,
replacing the established ledmac package. Ledmac itself was a
LaTeX port of the plain TeX EDMAC macros. The package supports
indexing by page and by line numbers, and simple tabular- and
array-style environments. The package is distributed with the
related eledpar package. The package is now superseded by
reledmac.

%package -n texlive-eledmac-doc
Summary:        Documentation for eledmac
Version:        svn45418
Provides:       tex-eledmac-doc
AutoReqProv:    No

%description -n texlive-eledmac-doc
Documentation for eledmac

%package -n texlive-expex
Provides:       tex-expex = %{tl_version}
License:        LPPL
Summary:        Format linguistic examples and glosses, with reference capabilities
Version:        svn44499
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty)
Provides:       tex(epltxchapno.sty) = %{tl_version}, tex(epltxfn.sty) = %{tl_version}
Provides:       tex(eptexfn.tex) = %{tl_version}, tex(expex-demo.tex) = %{tl_version}
Provides:       tex(expex.sty) = %{tl_version}, tex(expex.tex) = %{tl_version}

%description -n texlive-expex
The package provides macros for typesetting linguistic examples
and glosses, with a refined mechanism for referencing examples
and parts of examples. The package can be used with LaTex using
the .sty wrapper or with PlainTex.

%package -n texlive-expex-doc
Summary:        Documentation for expex
Version:        svn44499
Provides:       tex-expex-doc
AutoReqProv:    No

%description -n texlive-expex-doc
Documentation for expex

%package -n texlive-ethiop
Provides:       tex-ethiop = %{tl_version}
License:        GPL+
Summary:        LaTeX macros and fonts for typesetting Amharic
Version:        svn15878.0.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(etha10.tfm) = %{tl_version}, tex(etha6.tfm) = %{tl_version}
Provides:       tex(etha7.tfm) = %{tl_version}, tex(etha8.tfm) = %{tl_version}
Provides:       tex(ethab10.tfm) = %{tl_version}, tex(ethab11.tfm) = %{tl_version}
Provides:       tex(ethab12.tfm) = %{tl_version}, tex(ethab14.tfm) = %{tl_version}
Provides:       tex(ethab18.tfm) = %{tl_version}, tex(ethab24.tfm) = %{tl_version}
Provides:       tex(ethab36.tfm) = %{tl_version}, tex(ethab9.tfm) = %{tl_version}
Provides:       tex(ethas10.tfm) = %{tl_version}, tex(ethasb10.tfm) = %{tl_version}
Provides:       tex(ethasb11.tfm) = %{tl_version}, tex(ethasb12.tfm) = %{tl_version}
Provides:       tex(ethasb14.tfm) = %{tl_version}, tex(ethasb18.tfm) = %{tl_version}
Provides:       tex(ethasb24.tfm) = %{tl_version}, tex(ethasb36.tfm) = %{tl_version}
Provides:       tex(ethasb9.tfm) = %{tl_version}, tex(ethatt10.tfm) = %{tl_version}
Provides:       tex(ethb10.tfm) = %{tl_version}, tex(ethb6.tfm) = %{tl_version}
Provides:       tex(ethb7.tfm) = %{tl_version}, tex(ethb8.tfm) = %{tl_version}
Provides:       tex(ethbb10.tfm) = %{tl_version}, tex(ethbb11.tfm) = %{tl_version}
Provides:       tex(ethbb12.tfm) = %{tl_version}, tex(ethbb14.tfm) = %{tl_version}
Provides:       tex(ethbb18.tfm) = %{tl_version}, tex(ethbb24.tfm) = %{tl_version}
Provides:       tex(ethbb36.tfm) = %{tl_version}, tex(ethbb9.tfm) = %{tl_version}
Provides:       tex(ethbs10.tfm) = %{tl_version}, tex(ethbsb10.tfm) = %{tl_version}
Provides:       tex(ethbsb11.tfm) = %{tl_version}, tex(ethbsb12.tfm) = %{tl_version}
Provides:       tex(ethbsb14.tfm) = %{tl_version}, tex(ethbsb18.tfm) = %{tl_version}
Provides:       tex(ethbsb24.tfm) = %{tl_version}, tex(ethbsb36.tfm) = %{tl_version}
Provides:       tex(ethbsb9.tfm) = %{tl_version}, tex(ethbtt10.tfm) = %{tl_version}
Provides:       tex(etharab.sty) = %{tl_version}, tex(ethiop.ldf) = %{tl_version}
Provides:       tex(ethiop.sty) = %{tl_version}, tex(uetha.fd) = %{tl_version}
Provides:       tex(uethb.fd) = %{tl_version}, tex(uetho.fd) = %{tl_version}

%description -n texlive-ethiop
Ethiopian language support for the babel package, including a
collection of fonts and TeX macros for typesetting the
characters of the languages of Ethiopia, with Metafont fonts
based on EthTeX's. The macros use the Babel framework.

%package -n texlive-ethiop-doc
Summary:        Documentation for ethiop
Version:        svn15878.0.7

Provides:       tex-ethiop-doc
AutoReqProv:    No

%description -n texlive-ethiop-doc
Documentation for ethiop

%package -n texlive-ethiop-t1
Provides:       tex-ethiop-t1 = %{tl_version}
License:        GPL+
Summary:        Type 1 versions of Amharic fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(ethiop.map) = %{tl_version}, tex(etha10.pfb) = %{tl_version}
Provides:       tex(etha6.pfb) = %{tl_version}, tex(etha7.pfb) = %{tl_version}
Provides:       tex(etha8.pfb) = %{tl_version}, tex(ethab10.pfb) = %{tl_version}
Provides:       tex(ethab11.pfb) = %{tl_version}, tex(ethab12.pfb) = %{tl_version}
Provides:       tex(ethab14.pfb) = %{tl_version}, tex(ethab18.pfb) = %{tl_version}
Provides:       tex(ethab24.pfb) = %{tl_version}, tex(ethab36.pfb) = %{tl_version}
Provides:       tex(ethab9.pfb) = %{tl_version}, tex(ethas10.pfb) = %{tl_version}
Provides:       tex(ethasb10.pfb) = %{tl_version}, tex(ethasb11.pfb) = %{tl_version}
Provides:       tex(ethasb12.pfb) = %{tl_version}, tex(ethasb14.pfb) = %{tl_version}
Provides:       tex(ethasb18.pfb) = %{tl_version}, tex(ethasb24.pfb) = %{tl_version}
Provides:       tex(ethasb36.pfb) = %{tl_version}, tex(ethasb9.pfb) = %{tl_version}
Provides:       tex(ethatt10.pfb) = %{tl_version}, tex(ethb10.pfb) = %{tl_version}
Provides:       tex(ethb6.pfb) = %{tl_version}, tex(ethb7.pfb) = %{tl_version}
Provides:       tex(ethb8.pfb) = %{tl_version}, tex(ethbb10.pfb) = %{tl_version}
Provides:       tex(ethbb11.pfb) = %{tl_version}, tex(ethbb12.pfb) = %{tl_version}
Provides:       tex(ethbb14.pfb) = %{tl_version}, tex(ethbb18.pfb) = %{tl_version}
Provides:       tex(ethbb24.pfb) = %{tl_version}, tex(ethbb36.pfb) = %{tl_version}
Provides:       tex(ethbb9.pfb) = %{tl_version}, tex(ethbs10.pfb) = %{tl_version}
Provides:       tex(ethbsb10.pfb) = %{tl_version}, tex(ethbsb11.pfb) = %{tl_version}
Provides:       tex(ethbsb12.pfb) = %{tl_version}, tex(ethbsb14.pfb) = %{tl_version}
Provides:       tex(ethbsb18.pfb) = %{tl_version}, tex(ethbsb24.pfb) = %{tl_version}
Provides:       tex(ethbsb36.pfb) = %{tl_version}, tex(ethbsb9.pfb) = %{tl_version}
Provides:       tex(ethbtt10.pfb) = %{tl_version}

%description -n texlive-ethiop-t1
These fonts are drop-in Adobe type 1 replacements for the fonts
of the ethiop package.

%package -n texlive-ethiop-t1-doc
Summary:        Documentation for ethiop-t1
Version:        svn15878.0

Provides:       tex-ethiop-t1-doc
AutoReqProv:    No

%description -n texlive-ethiop-t1-doc
Documentation for ethiop-t1

%package -n texlive-eskd
Provides:       tex-eskd = %{tl_version}
License:        LPPL
Summary:        Modern Russian typesetting
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(inputenc.sty), tex(babel.sty), tex(fontenc.sty)
Requires:       tex(rotating.sty), tex(lastpage.sty), tex(ifthen.sty), tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Provides:       tex(eskd.cls) = %{tl_version}

%description -n texlive-eskd
The class offers modern Russian text formatting, in accordance
with accepted design standards. Fonts not (apparently)
available on CTAN are required for use of the class.

%package -n texlive-eskd-doc
Summary:        Documentation for eskd
Version:        svn15878.0

Provides:       tex-eskd-doc
AutoReqProv:    No

%description -n texlive-eskd-doc
Documentation for eskd

%package -n texlive-eskdx
Provides:       tex-eskdx = %{tl_version}
License:        LPPL 1.3
Summary:        Modern Russian typesetting
Version:        svn29235.0.98

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(eskdtitle.sty), tex(caption.sty), tex(array.sty), tex(longtable.sty)
Requires:       tex(amsmath.sty), tex(zref-perpage.sty), tex(ifpdf.sty), tex(indentfirst.sty)
Requires:       tex(inputenc.sty), tex(babel.sty), tex(calc.sty), tex(rotating.sty)
Requires:       tex(chngpage.sty), tex(lscape.sty), tex(keyval.sty), tex(geometry.sty)
Requires:       tex(lastpage.sty), tex(everyshi.sty)
Provides:       tex(eskdafterpkg.sty) = %{tl_version}, tex(eskdappsheet.sty) = %{tl_version}
Provides:       tex(eskdbiblist.sty) = %{tl_version}, tex(eskdcap.sty) = %{tl_version}
Provides:       tex(eskdchngsheet.sty) = %{tl_version}, tex(eskddstu.sty) = %{tl_version}
Provides:       tex(eskdexplan.sty) = %{tl_version}, tex(eskdfont.sty) = %{tl_version}
Provides:       tex(eskdfootnote.sty) = %{tl_version}, tex(eskdfreesize.sty) = %{tl_version}
Provides:       tex(eskdgraph.cls) = %{tl_version}, tex(eskdhash.sty) = %{tl_version}
Provides:       tex(eskdindent.sty) = %{tl_version}, tex(eskdinfo.sty) = %{tl_version}
Provides:       tex(eskdlang.sty) = %{tl_version}, tex(eskdlist.sty) = %{tl_version}
Provides:       tex(eskdpara.sty) = %{tl_version}, tex(eskdplain.sty) = %{tl_version}
Provides:       tex(eskdrussian.def) = %{tl_version}, tex(eskdsect.sty) = %{tl_version}
Provides:       tex(eskdspec.sty) = %{tl_version}, tex(eskdspecii.sty) = %{tl_version}
Provides:       tex(eskdstamp.sty) = %{tl_version}, tex(eskdtab.cls) = %{tl_version}
Provides:       tex(eskdtext.cls) = %{tl_version}, tex(eskdtitle.sty) = %{tl_version}
Provides:       tex(eskdtitlebase.sty) = %{tl_version}, tex(eskdtotal.sty) = %{tl_version}
Provides:       tex(eskdukrainian.def) = %{tl_version}

%description -n texlive-eskdx
Eskdx is a collection of LaTeX classes and packages to typeset
textual and graphical documents in accordance with Russian (and
probably post USSR) standards for designers.

%package -n texlive-eskdx-doc
Summary:        Documentation for eskdx
Version:        svn29235.0.98

Provides:       tex-eskdx-doc
AutoReqProv:    No

%description -n texlive-eskdx-doc
Documentation for eskdx

%package -n texlive-e-french
Provides:       tex-e-french = %{tl_version}
License:        LPPL 1.3
Summary:        Comprehensive LaTeX support for French-language typesetting
Version:        svn45091
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(msg.sty), tex(latexsym.sty), tex(german.sty), tex(ngerman.sty)
Provides:       tex(efrench.ldf) = %{tl_version}, tex(efrench.sty) = %{tl_version}
Provides:       tex(enbib.ldf) = %{tl_version}, tex(epreuve.sty) = %{tl_version}
Provides:       tex(fenglish.sty) = %{tl_version}, tex(frabbrev.tex) = %{tl_version}
Provides:       tex(frbabel.sty) = %{tl_version}, tex(frbib.ldf) = %{tl_version}
Provides:       tex(french-msg.tex) = %{tl_version}, tex(french.cfg) = %{tl_version}
Provides:       tex(french.ldf) = %{tl_version}, tex(french.sty) = %{tl_version}
Provides:       tex(french_french-msg.tex) = %{tl_version}
Provides:       tex(frenchle.cfg) = %{tl_version}, tex(frenchle.ldf) = %{tl_version}
Provides:       tex(frenchle.sty) = %{tl_version}, tex(frenchpro.ldf) = %{tl_version}
Provides:       tex(frenchpro.sty) = %{tl_version}, tex(frhyphex.tex) = %{tl_version}
Provides:       tex(fxabbrev.tex) = %{tl_version}, tex(german_french-msg.tex) = %{tl_version}
Provides:       tex(mlp-01.sty) = %{tl_version}, tex(mlp-31.sty) = %{tl_version}
Provides:       tex(mlp-33.sty) = %{tl_version}, tex(mlp-49.sty) = %{tl_version}
Provides:       tex(mlp-49n.sty) = %{tl_version}, tex(mlp-opts.sty) = %{tl_version}
Provides:       tex(mlp.sty) = %{tl_version}, tex(pmfrench.sty) = %{tl_version}

%description -n texlive-e-french
E-french is a distribution that keeps alive the work of Bernard
Gaulle (now deceased), under a free licence. It replaces the
the old "full" frenchpro (the "professional" distribution) and
the light-weight frenchle packages.

%package -n texlive-e-french-doc
Summary:        Documentation for e-french
Version:        svn45091
Provides:       tex-e-french-doc
AutoReqProv:    No

%description -n texlive-e-french-doc
Documentation for e-french

%package -n texlive-epslatex-fr-doc
Summary:        Documentation for epslatex-fr
Version:        svn19440.0

Provides:       tex-epslatex-fr-doc
AutoReqProv:    No

%description -n texlive-epslatex-fr-doc
Documentation for epslatex-fr

%package -n texlive-einfuehrung-doc
Summary:        Documentation for einfuehrung
Version:        svn29349.0

Provides:       tex-einfuehrung-doc
AutoReqProv:    No

%description -n texlive-einfuehrung-doc
Documentation for einfuehrung

%package -n texlive-etdipa-doc
Summary:        Documentation for etdipa
Version:        svn36354.2.6

Provides:       tex-etdipa-doc
AutoReqProv:    No

%description -n texlive-etdipa-doc
Documentation for etdipa

%package -n texlive-etoolbox-de-doc
Summary:        Documentation for etoolbox-de
Version:        svn21906.1

Provides:       tex-etoolbox-de-doc
AutoReqProv:    No

%description -n texlive-etoolbox-de-doc
Documentation for etoolbox-de

%package -n texlive-es-tex-faq-doc
Summary:        Documentation for es-tex-faq
Version:        svn15878.1.97

Provides:       tex-es-tex-faq-doc
AutoReqProv:    No

%description -n texlive-es-tex-faq-doc
Documentation for es-tex-faq

%package -n texlive-eso-pic
Provides:       tex-eso-pic = %{tl_version}
License:        LPPL 1.2
Summary:        Add picture commands (or backgrounds) to every page
Version:        svn47694
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(atbegshi.sty), tex(keyval.sty), tex(xcolor.sty), tex(color.sty)
Provides:       tex(eso-pic.sty) = %{tl_version}, tex(showframe.sty) = %{tl_version}

%description -n texlive-eso-pic
The package adds one or more user commands to LaTeX's shipout
routine, which may be used to place the output at fixed
positions. The grid option may be used to find the correct
places.

%package -n texlive-eso-pic-doc
Summary:        Documentation for eso-pic
Version:        svn47694
Provides:       tex-eso-pic-doc
AutoReqProv:    No

%description -n texlive-eso-pic-doc
Documentation for eso-pic

%package -n texlive-euenc
Provides:       tex-euenc = %{tl_version}
License:        LPPL 1.3
Summary:        Unicode font encoding definitions for XeTeX
Version:        svn19795.0.1h

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(eu1enc.def) = %{tl_version}, tex(eu1lmdh.fd) = %{tl_version}
Provides:       tex(eu1lmr.fd) = %{tl_version}, tex(eu1lmss.fd) = %{tl_version}
Provides:       tex(eu1lmssq.fd) = %{tl_version}, tex(eu1lmtt.fd) = %{tl_version}
Provides:       tex(eu1lmvtt.fd) = %{tl_version}, tex(eu2enc.def) = %{tl_version}
Provides:       tex(eu2lmdh.fd) = %{tl_version}, tex(eu2lmr.fd) = %{tl_version}
Provides:       tex(eu2lmss.fd) = %{tl_version}, tex(eu2lmssq.fd) = %{tl_version}
Provides:       tex(eu2lmtt.fd) = %{tl_version}, tex(eu2lmvtt.fd) = %{tl_version}

%description -n texlive-euenc
Font encoding definitions for unicode fonts loaded by LaTeX in
XeTeX or LuaTeX. The package provides two encodings: EU1,
designed for use with XeTeX, which the fontspec uses for
unicode fonts which require no macro-level processing for
accents, and EU2, which provides the same facilities for use
with LuaTeX. Neither encoding places any restriction on the
glyphs provided by a font; use of EU2 causes the package
euxunicode to be loaded (the package is part of this
distribution). The package includes font definition files for
use with the Latin Modern OpenType fonts.

%package -n texlive-euenc-doc
Summary:        Documentation for euenc
Version:        svn19795.0.1h

Provides:       tex-euenc-doc
AutoReqProv:    No

%description -n texlive-euenc-doc
Documentation for euenc

%package -n texlive-euler
Provides:       tex-euler = %{tl_version}
License:        LPPL
Summary:        Use AMS Euler fonts for math
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(euler.sty) = %{tl_version}

%description -n texlive-euler
Provides a setup for using the AMS Euler family of fonts for
mathematics in LaTeX documents. "The underlying philosophy of
Zapf's Euler design was to capture the flavour of mathematics
as it might be written by a mathematician with excellent
handwriting." The euler package is based on Knuth's macros for
the book 'Concrete Mathematics'. The text fonts for the
Concrete book are supported by the beton package.

%package -n texlive-euler-doc
Summary:        Documentation for euler
Version:        svn42428
Provides:       tex-euler-doc
AutoReqProv:    No

%description -n texlive-euler-doc
Documentation for euler

%package -n texlive-extsizes
Provides:       tex-extsizes = %{tl_version}
License:        LPPL
Summary:        Extend the standard classes' size options
Version:        svn17263.1.4a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(exscale.sty)
Provides:       tex(autopagewidth.sty) = %{tl_version}, tex(extarticle.cls) = %{tl_version}
Provides:       tex(extbook.cls) = %{tl_version}, tex(extletter.cls) = %{tl_version}
Provides:       tex(extproc.cls) = %{tl_version}, tex(extreport.cls) = %{tl_version}
Provides:       tex(extsizes.sty) = %{tl_version}, tex(size14.clo) = %{tl_version}
Provides:       tex(size17.clo) = %{tl_version}, tex(size20.clo) = %{tl_version}
Provides:       tex(size8.clo) = %{tl_version}, tex(size9.clo) = %{tl_version}

%description -n texlive-extsizes
Provides classes extarticle, extreport, extletter, extbook and
extproc which provide for documents with a base font size from
8-20pt.

%package -n texlive-extsizes-doc
Summary:        Documentation for extsizes
Version:        svn17263.1.4a

Provides:       tex-extsizes-doc
AutoReqProv:    No

%description -n texlive-extsizes-doc
Documentation for extsizes

%package -n texlive-eepic
Provides:       tex-eepic = %{tl_version}
License:        Public Domain
Summary:        Extensions to epic and the LaTeX drawing tools
Version:        svn15878.1.1e

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(eepic.sty) = %{tl_version}, tex(eepicemu.sty) = %{tl_version}
Provides:       tex(epic.sty) = %{tl_version}

%description -n texlive-eepic
Extensions to epic and the LaTeX picture drawing environment,
include the drawing of lines at any slope, the drawing of
circles in any radii, and the drawing of dotted and dashed
lines much faster with much less TeX memory, and providing
several new commands for drawing ellipses, arcs, splines, and
filled circles and ellipses. The package uses tpic \special
commands.

%package -n texlive-eepic-doc
Summary:        Documentation for eepic
Version:        svn15878.1.1e

Provides:       tex-eepic-doc
AutoReqProv:    No

%description -n texlive-eepic-doc
Documentation for eepic

%package -n texlive-epspdfconversion
Provides:       tex-epspdfconversion = %{tl_version}
License:        LPPL
Summary:        On-the-fly conversion of EPS to PDF
Version:        svn18703.0.61

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty), tex(epstopdf-base.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(epspdfconversion.sty) = %{tl_version}

%description -n texlive-epspdfconversion
The package calls the epstopdf package to convert EPS graphics
to PDF, on the fly. It servs as a vehicle for passing
conversion options (such as grayscale, prepress or pdfversion)
to the epspdf converter.

%package -n texlive-epspdfconversion-doc
Summary:        Documentation for epspdfconversion
Version:        svn18703.0.61

Provides:       tex-epspdfconversion-doc
AutoReqProv:    No

%description -n texlive-epspdfconversion-doc
Documentation for epspdfconversion

%package -n texlive-esk
Provides:       tex-esk = %{tl_version}
License:        GPL+
Summary:        Package to encapsulate Sketch files in LaTeX sources
Version:        svn18115.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty), tex(kvsetkeys.sty)
Provides:       tex(esk.sty) = %{tl_version}

%description -n texlive-esk
The ESK package allows to encapsulate Sketch files in LaTeX
sources. This is very useful for keeping illustrations in sync
with the text. It also frees the user from inventing
descriptive names for new files that fit into the confines of
file system conventions. Sketch is a 3D scene description
language by Eugene K. Ressler and can generate TikZ and
PSTricks code. ESK behaves in a similar fashion to EMP (which
encapsulates Metapost files), and was in fact developed from
it.

%package -n texlive-esk-doc
Summary:        Documentation for esk
Version:        svn18115.1.0

Provides:       tex-esk-doc
AutoReqProv:    No

%description -n texlive-esk-doc
Documentation for esk

%package -n texlive-ean13isbn
Provides:       tex-ean13isbn = %{tl_version}
License:        LPPL
Summary:        Print EAN13 for ISBN
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(ean13.tex)
Provides:       tex(ean13isbn.sty) = %{tl_version}

%description -n texlive-ean13isbn
The package provides the means to typeset ISBN codes with EAN-
13; it uses the (generic) package ean13.tex to typeset the
actual barcode.

%package -n texlive-ean13isbn-doc
Summary:        Documentation for ean13isbn
Version:        svn15878.0

Provides:       tex-ean13isbn-doc
AutoReqProv:    No

%description -n texlive-ean13isbn-doc
Documentation for ean13isbn

%package -n texlive-easy
Provides:       tex-easy = %{tl_version}
License:        LPPL
Summary:        A collection of easy-to-use macros
Version:        svn19440.0.99

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(easy.sty) = %{tl_version}, tex(easybib.sty) = %{tl_version}
Provides:       tex(easybmat.sty) = %{tl_version}, tex(easyeqn.sty) = %{tl_version}
Provides:       tex(easymat.sty) = %{tl_version}, tex(easytable.sty) = %{tl_version}
Provides:       tex(easyvector.sty) = %{tl_version}

%description -n texlive-easy
The collection comprises: easybib, support for customising
bibliographies; easybmat, support for composing block matrices;
easyeqn, support for various aspects of equations; easymat,
support for composing matrices; easytable, support for writing
tables; easyvector, a C-like syntax for writing vectors.

%package -n texlive-easy-doc
Summary:        Documentation for easy
Version:        svn19440.0.99

Provides:       tex-easy-doc
AutoReqProv:    No

%description -n texlive-easy-doc
Documentation for easy

%package -n texlive-easy-todo
Provides:       tex-easy-todo = %{tl_version}
License:        ASL 2.0
Summary:        To-do notes in a document
Version:        svn32677.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(tocloft.sty), tex(ifthen.sty), tex(ifdraft.sty)
Provides:       tex(easy-todo.sty) = %{tl_version}

%description -n texlive-easy-todo
The package provides to-do notes throughout a document, and
will provide an index of things to do.

%package -n texlive-easy-todo-doc
Summary:        Documentation for easy-todo
Version:        svn32677.0

Provides:       tex-easy-todo-doc
AutoReqProv:    No

%description -n texlive-easy-todo-doc
Documentation for easy-todo

%package -n texlive-easyfig
Provides:       tex-easyfig = %{tl_version}
License:        LPPL 1.3
Summary:        Simplifying the use of common figures
Version:        svn47193
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(adjustbox.sty), tex(xkeyval.sty), tex(ifetex.sty)
Provides:       tex(easyfig.sty) = %{tl_version}

%description -n texlive-easyfig
The package provides the command \Figure[<key=value>...]{<image
filename>} to simplify the business of including an image as
figure in the most common form (centred and with caption and
label). Caption and label are set using the caption and label
keys; the label fig:<image filename> is used if none is given.
If the here key is given, the figure is not 'floated', and the
user is responsible for placement. The package uses the
author's package adjustbox to centre an image and to simplify
further modifications.

%package -n texlive-easyfig-doc
Summary:        Documentation for easyfig
Version:        svn47193
Provides:       tex-easyfig-doc
AutoReqProv:    No

%description -n texlive-easyfig-doc
Documentation for easyfig

%package -n texlive-easylist
Provides:       tex-easylist = %{tl_version}
License:        LPPL
Summary:        Lists using a single active character
Version:        svn32661.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(easylist.sty) = %{tl_version}

%description -n texlive-easylist
This package allows you to create lists of numbered items (as
in Wittgenstein's 'Tractatus') with a single active character
as the only command. A variety of parameters are available to
configure the appearance of the list; lists may be nested
(effectively to unlimited depth).

%package -n texlive-easylist-doc
Summary:        Documentation for easylist
Version:        svn32661.1.3

Provides:       tex-easylist-doc
AutoReqProv:    No

%description -n texlive-easylist-doc
Documentation for easylist

%package -n texlive-easyreview
Provides:       tex-easyreview = %{tl_version}
License:        LPPL
Summary:        Package to provide a way to review (or perform editorial process) in LaTeX
Version:        svn38352.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(soul.sty), tex(xcolor.sty), tex(todonotes.sty)
Provides:       tex(easyReview.sty) = %{tl_version}

%description -n texlive-easyreview
The easyReview package provides a way to review (or perform
editorial process) in LaTeX. You can use the provided commands
to claim attention in different ways to part of the text, or
even to indicate that a text was added, needs to be removed,
needs to be replaced and add comments to the text.

%package -n texlive-easyreview-doc
Summary:        Documentation for easyreview
Version:        svn38352.1.0

Provides:       tex-easyreview-doc
AutoReqProv:    No

%description -n texlive-easyreview-doc
Documentation for easyreview

%package -n texlive-ebezier
Provides:       tex-ebezier = %{tl_version}
License:        LPPL
Summary:        Device independent picture environment enhancement
Version:        svn15878.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty)
Provides:       tex(ebezier.sty) = %{tl_version}

%description -n texlive-ebezier
Ebezier is a device independent extension for the standard
picture environment. Linear, quadratic, and cubic bezier curves
are supplied in connection with higher level circle drawing
commands. Additionally some macros for the calculation of curve
lenghts are part of this package.

%package -n texlive-ebezier-doc
Summary:        Documentation for ebezier
Version:        svn15878.4

Provides:       tex-ebezier-doc
AutoReqProv:    No

%description -n texlive-ebezier-doc
Documentation for ebezier

%package -n texlive-ecclesiastic
Provides:       tex-ecclesiastic = %{tl_version}
License:        LPPL 1.3
Summary:        Typesetting Ecclesiastic Latin
Version:        svn38172.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(iftex.sty)
Provides:       tex(ecclesiastic.sty) = %{tl_version}

%description -n texlive-ecclesiastic
The package modifies the way the latin option to babel operates
when typesetting Latin. The style is somewhat 'frenchified' in
respect of punctuation spacings and footnote style; shortcuts
are available in order to set accents on all vowels, including
y and the diphthongs ae and oe.

%package -n texlive-ecclesiastic-doc
Summary:        Documentation for ecclesiastic
Version:        svn38172.0.3

Provides:       tex-ecclesiastic-doc
AutoReqProv:    No

%description -n texlive-ecclesiastic-doc
Documentation for ecclesiastic

%package -n texlive-ecv
Provides:       tex-ecv = %{tl_version}
License:        Copyright only
Summary:        A fancy Curriculum Vitae class
Version:        svn24928.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(ifthen.sty), tex(geometry.sty), tex(longtable.sty)
Requires:       tex(pgf.sty), tex(paralist.sty), tex(helvet.sty), tex(xcolor.sty)
Requires:       tex(fancyhdr.sty), tex(inputenc.sty), tex(selinput.sty), tex(fontenc.sty)
Requires:       tex(url.sty), tex(hyperref.sty), tex(babel.sty)
Provides:       tex(ecv.cls) = %{tl_version}, tex(ecvEnglish.ldf) = %{tl_version}
Provides:       tex(ecvGerman.ldf) = %{tl_version}, tex(ecvNLS.sty) = %{tl_version}

%description -n texlive-ecv
The class provides an environment for creating a fancily laid
out tabular curriculum vitae inspired by the european
curriculum vitae. The distribution comes with a German and an
English template.

%package -n texlive-ecv-doc
Summary:        Documentation for ecv
Version:        svn24928.0.3

Provides:       tex-ecv-doc
AutoReqProv:    No

%description -n texlive-ecv-doc
Documentation for ecv

%package -n texlive-ed
Provides:       tex-ed = %{tl_version}
License:        LPPL
Summary:        Editorial Notes for LaTeX documents
Version:        svn25231.1.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(paralist.sty), tex(xcolor.sty), tex(verbatim.sty)
Provides:       tex(ed.sty) = %{tl_version}

%description -n texlive-ed
This package defines a couple of editorial notes that simplify
collaboration on a LaTeX text. These allow authors to annotate
status information in the source. In draft mode, the
annotations are shown for communication, and in publication
mode these are suppressed.

%package -n texlive-ed-doc
Summary:        Documentation for ed
Version:        svn25231.1.8

Provides:       tex-ed-doc
AutoReqProv:    No

%description -n texlive-ed-doc
Documentation for ed

%package -n texlive-edmargin
Provides:       tex-edmargin = %{tl_version}
License:        LPPL
Summary:        Multiple series of endnotes for critical editions
Version:        svn27599.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(edmargin.sty) = %{tl_version}

%description -n texlive-edmargin
Edmargin provides a very simple scheme for endnote sections for
critical editions. Endnotes can either be marked in the text,
or with marginal references to the page in the note sections
where the note is to be found. Notes can be set in individual
paragraphs, or in block paragraph mode (where there are many
short notes). Note sections will have running headers of the
form "Textual notes to pp. xx--yy". New note sections can be
created on the fly. There are predefined endnote sections for
textual notes, emendations, and explanatory notes.

%package -n texlive-edmargin-doc
Summary:        Documentation for edmargin
Version:        svn27599.1.2

Provides:       tex-edmargin-doc
AutoReqProv:    No

%description -n texlive-edmargin-doc
Documentation for edmargin

%package -n texlive-eemeir
Provides:       tex-eemeir = %{tl_version}
License:        LPPL
Summary:        Adjust the gender of words in a document
Version:        svn15878.1.1b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty)
Provides:       tex(eemeir.sty) = %{tl_version}

%description -n texlive-eemeir
Defines macros for third-person singular pronouns (\E, \Em,
\Eir, \Eirs), which expand differently according to a
masculine/feminine switch. (If the switch is 'masculine', they
would expand to 'he', 'him', 'his' and 'his'; if 'feminine',
they would expand to 'she', 'her', 'her' and 'hers'. Apart from
the pronouns, one can define 'word pairs', such as
mother/father, daughter/son, and so on. Gender may be defined
once per document, as an environment, or may be flipped on the
fly.

%package -n texlive-eemeir-doc
Summary:        Documentation for eemeir
Version:        svn15878.1.1b

Provides:       tex-eemeir-doc
AutoReqProv:    No

%description -n texlive-eemeir-doc
Documentation for eemeir

%package -n texlive-efbox
Provides:       tex-efbox = %{tl_version}
License:        LPPL 1.3
Summary:        Extension of \fbox, with controllable frames and colours
Version:        svn33236.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(pgfkeys.sty)
Provides:       tex(efbox.sty) = %{tl_version}

%description -n texlive-efbox
The package defines the \efbox command, which creates a box
just wide enough to hold the text created by its argument. The
command optionally puts a (possibly partial) frame around the
box, and allows setting the box background colour.

%package -n texlive-efbox-doc
Summary:        Documentation for efbox
Version:        svn33236.1.0

Provides:       tex-efbox-doc
AutoReqProv:    No

%description -n texlive-efbox-doc
Documentation for efbox

%package -n texlive-egplot
Provides:       tex-egplot = %{tl_version}
License:        GPL+
Summary:        Encapsulate Gnuplot sources in LaTeX documents
Version:        svn20617.1.02a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty), tex(ifthen.sty), tex(graphicx.sty)
Provides:       tex(egplot.sty) = %{tl_version}

%description -n texlive-egplot
A package to encapsulate gnuplot commands in a LaTeX source
file, so that a document's figures are maintained in parallel
with the document source itself.

%package -n texlive-egplot-doc
Summary:        Documentation for egplot
Version:        svn20617.1.02a

Provides:       tex-egplot-doc
AutoReqProv:    No

%description -n texlive-egplot-doc
Documentation for egplot

%package -n texlive-elements
Provides:       tex-elements = %{tl_version}
License:        LPPL 1.3
Summary:        Provides properties of chemical elements
Version:        svn46505
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(translations.sty)
Provides:       tex(elements.sty) = %{tl_version}, tex(elements_names_english.def) = %{tl_version}
Provides:       tex(elements_names_french.def) = %{tl_version}
Provides:       tex(elements_names_german.def) = %{tl_version}

%description -n texlive-elements
The package provides means for retrieving properties of
chemical elements like atomic number, element symbol, element
name, electron distribution or isotope number. Properties are
defined for the elements up to the atomic number 112. This
package is a spin-off of the package bohr by the same author.

%package -n texlive-elements-doc
Summary:        Documentation for elements
Version:        svn46505
Provides:       tex-elements-doc
AutoReqProv:    No

%description -n texlive-elements-doc
Documentation for elements

%package -n texlive-ellipsis
Provides:       tex-ellipsis = %{tl_version}
License:        LPPL
Summary:        Fix uneven spacing around ellipses in LaTeX text mode
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty)
Provides:       tex(ellipsis.sty) = %{tl_version}

%description -n texlive-ellipsis
This is a simple package that fixes a problem in the way LaTeX
handles ellipses: it always puts a tiny bit more space after
\dots in text mode than before it, which results in the
ellipsis being off-center when used between two words.

%package -n texlive-ellipsis-doc
Summary:        Documentation for ellipsis
Version:        svn15878.0

Provides:       tex-ellipsis-doc
AutoReqProv:    No

%description -n texlive-ellipsis-doc
Documentation for ellipsis

%package -n texlive-elmath
Provides:       tex-elmath = %{tl_version}
License:        LPPL
Summary:        Mathematics in Greek texts
Version:        svn15878.v1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(elmath.sty) = %{tl_version}

%description -n texlive-elmath
This package has been designed to facilitate the use of Greek
letters in mathematical mode. The package allows one to
directly type in Greek letters (in ISO 8859-7 encoding) in math
mode.

%package -n texlive-elmath-doc
Summary:        Documentation for elmath
Version:        svn15878.v1.2

Provides:       tex-elmath-doc
AutoReqProv:    No

%description -n texlive-elmath-doc
Documentation for elmath

%package -n texlive-elocalloc
Provides:       tex-elocalloc = %{tl_version}
License:        LPPL
Summary:        Local allocation macros for LaTeX 2015
Version:        svn42712
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etex.sty)
Provides:       tex(elocalloc.sty) = %{tl_version}

%description -n texlive-elocalloc
Local allocation macros, with names taken from etex.sty but
with implementation based on the LaTeX 2015 allocation macros.

%package -n texlive-elocalloc-doc
Summary:        Documentation for elocalloc
Version:        svn42712
Provides:       tex-elocalloc-doc
AutoReqProv:    No

%description -n texlive-elocalloc-doc
Documentation for elocalloc

%package -n texlive-elpres
Provides:       tex-elpres = %{tl_version}
License:        LPPL
Summary:        A simple class for electronic presentations
Version:        svn46429
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(geometry.sty), tex(ifthen.sty), tex(fancyhdr.sty), tex(mathptmx.sty)
Requires:       tex(courier.sty), tex(helvet.sty)
Provides:       tex(elpres.cls) = %{tl_version}

%description -n texlive-elpres
Elpres is a simple class for electronic presentations to be
shown on screen or a beamer. Elpres is derived from article.cls
and may be used with LaTeX or pdfLaTeX.

%package -n texlive-elpres-doc
Summary:        Documentation for elpres
Version:        svn46429
Provides:       tex-elpres-doc
AutoReqProv:    No

%description -n texlive-elpres-doc
Documentation for elpres

%package -n texlive-elzcards
Provides:       tex-elzcards = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset business cards, index cards and flash cards easyly
Version:        svn44785
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(calc.sty), tex(xparse.sty), tex(keyval.sty)
Provides:       tex(elzcards.sty) = %{tl_version}

%description -n texlive-elzcards
A class, based on article.cls, for typesetting business cards,
index cards, and flash cards in an easy and flexible way,
optionally also the reverse side. You will have to furnish the
paper size, the desired size of your card, the printable area
of your printer, and the design of the card. Everything else is
taken care of by elzcards.

%package -n texlive-elzcards-doc
Summary:        Documentation for elzcards
Version:        svn44785
Provides:       tex-elzcards-doc
AutoReqProv:    No

%description -n texlive-elzcards-doc
Documentation for elzcards

%package -n texlive-emarks
Provides:       tex-emarks = %{tl_version}
License:        LPPL 1.3
Summary:        Named mark registers with e-TeX
Version:        svn24504.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty)
Provides:       tex(emarks.sty) = %{tl_version}

%description -n texlive-emarks
E-TeX provides 32 768 mark registers; using this facility is
far more comfortable than LaTeX tricks with \markright,
\markboth, \leftmark and \rightmark. The package provides two
commands for marking: \marksthe and \marksthecs, which have *
forms which disable expansion; new mark registers are allocated
as needed. Syntax is closely modelled on the \marks primitive.
Four commands are provided for retrieving the marks registers'
content: \thefirstmarks, \thebotmarks, thetopmarks and
\getthemarks; and the command \ifmarksequal is available for
comparing the content of marks registers. The package requires
an e-TeX-enabled engine, and the etex package.

%package -n texlive-emarks-doc
Summary:        Documentation for emarks
Version:        svn24504.1.0

Provides:       tex-emarks-doc
AutoReqProv:    No

%description -n texlive-emarks-doc
Documentation for emarks

%package -n texlive-embedall
Provides:       tex-embedall = %{tl_version}
License:        LPPL 1.2
Summary:        Embed source files into the generated PDF
Version:        svn31903.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(embedfile.sty), tex(graphicx.sty), tex(listings.sty), tex(letltxmacro.sty)
Provides:       tex(embedall.sty) = %{tl_version}

%description -n texlive-embedall
The package provides a means of storing a project, without
losing anything. It uses the embedfile package to attach to the
generated PDF all files used in creating your project. In
particular, it can embed images, external TeX files, external
codes and

%package -n texlive-embedall-doc
Summary:        Documentation for embedall
Version:        svn31903.1.0

Provides:       tex-embedall-doc
AutoReqProv:    No

%description -n texlive-embedall-doc
Documentation for embedall

%package -n texlive-embrac
Provides:       tex-embrac = %{tl_version}
License:        LPPL 1.3
Summary:        Upright brackets in emphasised text
Version:        svn44757
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty)
Provides:       tex(embrac.sty) = %{tl_version}

%description -n texlive-embrac
The package redefines the commands \emph and \textit so that
parentheses and square brackets are typeset in an upright font
in their arguments. The package requires expl3 from the
l3kernel bundle, and xparse and l3keys2e from the l3packages
bundle.

%package -n texlive-embrac-doc
Summary:        Documentation for embrac
Version:        svn44757
Provides:       tex-embrac-doc
AutoReqProv:    No

%description -n texlive-embrac-doc
Documentation for embrac

%package -n texlive-emptypage
Provides:       tex-emptypage = %{tl_version}
License:        LPPL 1.2
Summary:        Make empty pages really empty
Version:        svn18064.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(emptypage.sty) = %{tl_version}

%description -n texlive-emptypage
This package prevents page numbers and headings from appearing
on empty pages.

%package -n texlive-emptypage-doc
Summary:        Documentation for emptypage
Version:        svn18064.1.2

Provides:       tex-emptypage-doc
AutoReqProv:    No

%description -n texlive-emptypage-doc
Documentation for emptypage

%package -n texlive-emulateapj
Provides:       tex-emulateapj = %{tl_version}
License:        LPPL
Summary:        Produce output similar to that of APJ
Version:        svn28469.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(latexsym.sty), tex(graphicx.sty), tex(amssymb.sty), tex(longtable.sty)
Requires:       tex(epsf.sty)
Provides:       tex(emulateapj.cls) = %{tl_version}

%description -n texlive-emulateapj
A LaTeX class (based on current RevTeX) to produce preprints
with the page layout similar to that of the Astrophysical
Journal.

%package -n texlive-emulateapj-doc
Summary:        Documentation for emulateapj
Version:        svn28469.0

Provides:       tex-emulateapj-doc
AutoReqProv:    No

%description -n texlive-emulateapj-doc
Documentation for emulateapj

%package -n texlive-endfloat
Provides:       tex-endfloat = %{tl_version}
License:        GPL+
Summary:        Move floats to the end, leaving markers where they belong
Version:        svn47108
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(efxmpl.cfg) = %{tl_version}, tex(endfloat.sty) = %{tl_version}

%description -n texlive-endfloat
Place all floats on pages by themselves at the end of the
document, optionally leaving markers like "[Figure 3 about
here]" in the text near to where the figure (or table) would
normally have occurred. Float types figure and table are
recognised by the package, unmodified. Since several packages
define other types of float, it is possible to register these
float types with endfloat.

%package -n texlive-endfloat-doc
Summary:        Documentation for endfloat
Version:        svn47108
Provides:       tex-endfloat-doc
AutoReqProv:    No

%description -n texlive-endfloat-doc
Documentation for endfloat

%package -n texlive-endheads
Provides:       tex-endheads = %{tl_version}
License:        LPPL
Summary:        Running headers of the form "Notes to pp.xx-yy"
Version:        svn43750
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(endheads.sty) = %{tl_version}

%description -n texlive-endheads
Endheads provides running headers of the form "Notes to pp. xx-
yy" for endnotes sections. It also enables one to reset the
endnotes counter, and put a line marking the chapter change in
the endnotes, at the beginning of every chapter. Endheads
requires the fancyhdr, needspace, ifthen, and endnotes
packages.

%package -n texlive-endheads-doc
Summary:        Documentation for endheads
Version:        svn43750
Provides:       tex-endheads-doc
AutoReqProv:    No

%description -n texlive-endheads-doc
Documentation for endheads

%package -n texlive-endnotes
Provides:       tex-endnotes = %{tl_version}
License:        LPPL 1.2
Summary:        Place footnotes at the end
Version:        svn17197.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(endnotes.sty) = %{tl_version}

%description -n texlive-endnotes
Accumulates notes (using the \endnote command, which can be
used as a replacement for \footnote), and places them at the
end of the section, chapter or document.

%package -n texlive-endnotes-doc
Summary:        Documentation for endnotes
Version:        svn17197.0

Provides:       tex-endnotes-doc
AutoReqProv:    No

%description -n texlive-endnotes-doc
Documentation for endnotes

%package -n texlive-engpron
Provides:       tex-engpron = %{tl_version}
License:        LPPL
Summary:        Helps to type the pronunciation of English words
Version:        svn16558.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(fancyvrb.sty), tex(tipa.sty), tex(ifthen.sty)
Requires:       tex(drac.sty)
Provides:       tex(engpron-tools.sty) = %{tl_version}, tex(engpron.sty) = %{tl_version}

%description -n texlive-engpron
This package provides macros beginning with the 'PS' character,
made active, which enable us to write the British or American
English pronunciation as one can find it in the 'English
Pronouncing Dictionary' by Daniel Jones. There is an option to
typeset the pronunciation in the style of Harrap's dictionary.

%package -n texlive-engpron-doc
Summary:        Documentation for engpron
Version:        svn16558.2

Provides:       tex-engpron-doc
AutoReqProv:    No

%description -n texlive-engpron-doc
Documentation for engpron

%package -n texlive-engrec
Provides:       tex-engrec = %{tl_version}
License:        LPPL
Summary:        Enumerate with lower- or uppercase Greek letters
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amstext.sty), tex(upgreek.sty)
Provides:       tex(engrec.sty) = %{tl_version}

%description -n texlive-engrec
This package provides two macros \engrec and \EnGrec to convert
number arguments to lower case or upper case greek letters.
They have the syntax of \alph, i.e. \engrec{a_counter},
\EnGrec{a_counter}. Options are provided to work with the
upgreek and fourier packages. Requires amstext.

%package -n texlive-engrec-doc
Summary:        Documentation for engrec
Version:        svn15878.1.1

Provides:       tex-engrec-doc
AutoReqProv:    No

%description -n texlive-engrec-doc
Documentation for engrec

%package -n texlive-enotez
Provides:       tex-enotez = %{tl_version}
License:        LPPL 1.3
Summary:        Support for end-notes
Version:        svn44024
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty), tex(xtemplate.sty)
Requires:       tex(etoolbox.sty), tex(xpatch.sty), tex(scrlfile.sty), tex(translations.sty)
Provides:       tex(enotez.sty) = %{tl_version}

%description -n texlive-enotez
The package allows nested endnotes, supports hyperref and
provides means for easy customization of the list of notes. The
package requires the expl3 bundle and packages from the LaTeX 3
'package set'.

%package -n texlive-enotez-doc
Summary:        Documentation for enotez
Version:        svn44024
Provides:       tex-enotez-doc
AutoReqProv:    No

%description -n texlive-enotez-doc
Documentation for enotez

%package -n texlive-enumitem
Provides:       tex-enumitem = %{tl_version}
License:        LPPL
Summary:        Control layout of itemize, enumerate, description
Version:        svn24146.3.5.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(enumitem.sty) = %{tl_version}

%description -n texlive-enumitem
This package provides user control over the layout of the three
basic list environments: enumerate, itemize and description. It
supersedes both enumerate and mdwlist (providing well-
structured replacements for all their funtionality), and in
addition provides functions to compute the layout of labels,
and to 'clone' the standard environments, to create new
environments with counters of their own.

%package -n texlive-enumitem-doc
Summary:        Documentation for enumitem
Version:        svn24146.3.5.2

Provides:       tex-enumitem-doc
AutoReqProv:    No

%description -n texlive-enumitem-doc
Documentation for enumitem

%package -n texlive-enumitem-zref
Provides:       tex-enumitem-zref = %{tl_version}
License:        LPPL 1.3
Summary:        Extended references to items for enumitem package
Version:        svn21472.1.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ltxcmds.sty), tex(etoolbox.sty), tex(kvoptions.sty), tex(gettitlestring.sty)
Requires:       tex(enumitem.sty), tex(zref.sty), tex(zref-user.sty), tex(zref-counter.sty)
Requires:       tex(engrec.sty), tex(alphalph.sty), tex(greekctr.sty)
Provides:       tex(enumitem-zref.sty) = %{tl_version}

%description -n texlive-enumitem-zref
The package is a companion for the enumitem package; it makes
it possible to reference any item in lists formatted by
enumitem lists, viz., enumerated, itemize and description
lists, and any list defined (or customised) with \newlist or
\setlist. References may be typeset differently with
options/properties and even arbitrary text. With hyperref,
anchors are added for each item to enable hyperlinks within the
document or even to external documents. Three schemes are
provided to make reference names (including the standard \label
command).

%package -n texlive-enumitem-zref-doc
Summary:        Documentation for enumitem-zref
Version:        svn21472.1.8

Provides:       tex-enumitem-zref-doc
AutoReqProv:    No

%description -n texlive-enumitem-zref-doc
Documentation for enumitem-zref

%package -n texlive-envbig
Provides:       tex-envbig = %{tl_version}
License:        LPPL
Summary:        Printing addresses on envelopes
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(envbig.sty) = %{tl_version}

%description -n texlive-envbig
A simple package, that prints both 'from' and 'to' addresses.

%package -n texlive-envbig-doc
Summary:        Documentation for envbig
Version:        svn15878.0

Provides:       tex-envbig-doc
AutoReqProv:    No

%description -n texlive-envbig-doc
Documentation for envbig

%package -n texlive-environ
Provides:       tex-environ = %{tl_version}
License:        LPPL
Summary:        A new interface for environments in LaTeX
Version:        svn33821.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(trimspaces.sty)
Provides:       tex(environ.sty) = %{tl_version}

%description -n texlive-environ
The package provides the \collect@body command (as in amsmath),
as well as a \long version \Collect@Body, for collecting the
body text of an environment. These commands are used to define
a new author interface to creating new environments. For
example: \NewEnviron{test} wraps the entire environment body in
square brackets, doing the right thing in ignoring leading and
trailing spaces.

%package -n texlive-environ-doc
Summary:        Documentation for environ
Version:        svn33821.0.3

Provides:       tex-environ-doc
AutoReqProv:    No

%description -n texlive-environ-doc
Documentation for environ

%package -n texlive-envlab
Provides:       tex-envlab = %{tl_version}
License:        LPPL
Summary:        Addresses on envelopes or mailing labels
Version:        svn15878.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty)
Provides:       tex(envlab.cfg) = %{tl_version}, tex(envlab.sty) = %{tl_version}

%description -n texlive-envlab
A LaTeX package for producing mailing envelopes and labels,
including barcodes and address formatting according to the US
Postal Service rules. Redefines the standard \makelabels
command of the LaTeX letter documentclass.

%package -n texlive-envlab-doc
Summary:        Documentation for envlab
Version:        svn15878.1.2

Provides:       tex-envlab-doc
AutoReqProv:    No

%description -n texlive-envlab-doc
Documentation for envlab

%package -n texlive-epigraph
Provides:       tex-epigraph = %{tl_version}
License:        LPPL 1.3
Summary:        A package for typesetting epigraphs
Version:        svn15878.1.5c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(epigraph.sty) = %{tl_version}

%description -n texlive-epigraph
Epigraphs are the pithy quotations often found at the start (or
end) of a chapter. Both single epigraphs and lists of epigraphs
are catered for. Various aspects are easily configurable.

%package -n texlive-epigraph-doc
Summary:        Documentation for epigraph
Version:        svn15878.1.5c

Provides:       tex-epigraph-doc
AutoReqProv:    No

%description -n texlive-epigraph-doc
Documentation for epigraph

%package -n texlive-epiolmec
Provides:       tex-epiolmec = %{tl_version}
License:        LPPL
Summary:        Typesetting the Epi-Olmec Language
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(epiolmec.map) = %{tl_version}, tex(EpiOlmec.tfm) = %{tl_version}
Provides:       tex(Epi-Olmec.pfb) = %{tl_version}, tex(epiolmec.sty) = %{tl_version}

%description -n texlive-epiolmec
The package contains all the necessary files to typeset Epi-
Olmec "documents", in a script used in Southern Middle America
until about 500 AD.

%package -n texlive-epiolmec-doc
Summary:        Documentation for epiolmec
Version:        svn15878.0

Provides:       tex-epiolmec-doc
AutoReqProv:    No

%description -n texlive-epiolmec-doc
Documentation for epiolmec

%package -n texlive-eqell
Provides:       tex-eqell = %{tl_version}
License:        GPL+
Summary:        Sympathetically spaced ellipsis after punctuation
Version:        svn22931.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty)
Provides:       tex(eqell.sty) = %{tl_version}

%description -n texlive-eqell
The package provides commands that give a well-spaced ellipsis
after !, ?, !? or ?!.

%package -n texlive-eqell-doc
Summary:        Documentation for eqell
Version:        svn22931.0

Provides:       tex-eqell-doc
AutoReqProv:    No

%description -n texlive-eqell-doc
Documentation for eqell

%package -n texlive-eqlist
Provides:       tex-eqlist = %{tl_version}
License:        LPPL
Summary:        Description lists with equal indentation
Version:        svn32257.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(eqparbox.sty)
Provides:       tex(eqlist.sty) = %{tl_version}

%description -n texlive-eqlist
This package provides a list environment which sets a
description-like list in which the indentation corresponds to
the longest item of the list.

%package -n texlive-eqlist-doc
Summary:        Documentation for eqlist
Version:        svn32257.2.1

Provides:       tex-eqlist-doc
AutoReqProv:    No

%description -n texlive-eqlist-doc
Documentation for eqlist

%package -n texlive-eqname
Provides:       tex-eqname = %{tl_version}
License:        Copyright only
Summary:        Name tags for equations
Version:        svn20678.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(eqname.sty) = %{tl_version}

%description -n texlive-eqname
The \eqname command provides a name tag for the current
equation, in place of an equation number. The name tag will be
picked up by a subsequent \label command.

%package -n texlive-eqparbox
Provides:       tex-eqparbox = %{tl_version}
License:        LPPL 1.3
Summary:        Create equal-widthed parboxes
Version:        svn45215
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(array.sty), tex(environ.sty)
Provides:       tex(eqparbox.sty) = %{tl_version}

%description -n texlive-eqparbox
LaTeX users sometimes need to ensure that two or more blocks of
text occupy the same amount of horizontal space on the page. To
that end, the eqparbox package defines a new command,
\eqparbox, which works just like \parbox, except that instead
of specifying a width, one specifies a tag. All eqparboxes with
the same tag--regardless of where they are in the document--
will stretch to fit the widest eqparbox with that tag. This
simple, equal-width mechanism can be used for a variety of
alignment purposes, as is evidenced by the examples in
eqparbox's documentation. Various derivatives of \eqparbox are
also provided.

%package -n texlive-eqparbox-doc
Summary:        Documentation for eqparbox
Version:        svn45215
Provides:       tex-eqparbox-doc
AutoReqProv:    No

%description -n texlive-eqparbox-doc
Documentation for eqparbox

%package -n texlive-errata
Provides:       tex-errata = %{tl_version}
License:        LPPL
Summary:        Error markup for LaTeX documents
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty)
Provides:       tex(errata.sty) = %{tl_version}

%description -n texlive-errata
This package provides a simple infrastructure for recording
errata in LaTeX documents. This allows the user to maintain an
updated version of the document (with all errors corrected) and
to automatically generate an errata document highlighting the
difference to the published version.

%package -n texlive-errata-doc
Summary:        Documentation for errata
Version:        svn42428
Provides:       tex-errata-doc
AutoReqProv:    No

%description -n texlive-errata-doc
Documentation for errata

%package -n texlive-esami
Provides:       tex-esami = %{tl_version}
License:        LPPL
Summary:        Typeset exams with scrambled questions and answers
Version:        svn47639
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(random.tex)
Provides:       tex(esami.sty) = %{tl_version}

%description -n texlive-esami
The package enables the user to typeset exams with multiple
choice, open questions and many other types of exercise. Both
questions and answers may be randomly distributed within the
exam, and the solutions are typeset automatically. Exercises
may contain a wide number of random parameters and it is
possible to do arithmetical operations on them. The package is
localised in Italian, English, French, German, Greek and
Spanish.

%package -n texlive-esami-doc
Summary:        Documentation for esami
Version:        svn47639
Provides:       tex-esami-doc
AutoReqProv:    No

%description -n texlive-esami-doc
Documentation for esami

%package -n texlive-esdiff
Provides:       tex-esdiff = %{tl_version}
License:        LPPL
Summary:        Simplify typesetting of derivatives
Version:        svn21385.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(esdiff.sty) = %{tl_version}

%description -n texlive-esdiff
The package makes writing derivatives very easy. It offers
macros for derivatives, partial derivatives and multiple
derivatives, and allows specification of the point at which the
value is calculated. Some typographic alternatives may be
selected by package options

%package -n texlive-esdiff-doc
Summary:        Documentation for esdiff
Version:        svn21385.1.2

Provides:       tex-esdiff-doc
AutoReqProv:    No

%description -n texlive-esdiff-doc
Documentation for esdiff

%package -n texlive-esint
Provides:       tex-esint = %{tl_version}
License:        Public Domain
Summary:        Extended set of integrals for Computer Modern
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(esint10.tfm) = %{tl_version}, tex(esint.sty) = %{tl_version}
Provides:       tex(uesint.fd) = %{tl_version}

%description -n texlive-esint
The esint package permits access to alternate integral symbols
when you're using the Computer Modern fonts. In the original
set, several integral symbols are missing, such as \oiint. Many
of these symbols are available in other font sets (pxfonts,
txfonts, etc.), but there is no good solution if you want to
use Computer Modern. The package provides Metafont source and
LaTeX macro support.

%package -n texlive-esint-doc
Summary:        Documentation for esint
Version:        svn15878.1.1

Provides:       tex-esint-doc
AutoReqProv:    No

%description -n texlive-esint-doc
Documentation for esint

%package -n texlive-esint-type1
Provides:       tex-esint-type1 = %{tl_version}
License:        Public Domain
Summary:        Font esint10 in Type 1 format
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex-esint
Provides:       tex(esint.map) = %{tl_version}, tex(esint10.pfb) = %{tl_version}
Provides:       tex(esint.tex) = %{tl_version}

%description -n texlive-esint-type1
This is Eddie Saudrais's font esint10 in Adobe Type 1 format.
The Adobe Type 1 implementation was generated from the original
Metafont using mftrace. This distribution does not contain the
TFM files that are necessary to use the fonts with TeX; the TFM
files can be generated from the Metafont sources obtained by
following the instructions in the normal way.

%package -n texlive-esint-type1-doc
Summary:        Documentation for esint-type1
Version:        svn15878.0

Provides:       tex-esint-type1-doc
AutoReqProv:    No
Requires:       tex-esint-doc

%description -n texlive-esint-type1-doc
Documentation for esint-type1

%package -n texlive-etaremune
Provides:       tex-etaremune = %{tl_version}
License:        LPPL
Summary:        Reverse-counting enumerate environment
Version:        svn15878.v1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty)
Provides:       tex(etaremune.sty) = %{tl_version}

%description -n texlive-etaremune
The package implements the etaremune environment which is an
enumerate environment in which the labels decrease instead of
increasing. The package is noticeably more efficient than the
revnum package, which uses painfully many counters.

%package -n texlive-etaremune-doc
Summary:        Documentation for etaremune
Version:        svn15878.v1.2

Provides:       tex-etaremune-doc
AutoReqProv:    No

%description -n texlive-etaremune-doc
Documentation for etaremune

%package -n texlive-etextools
Provides:       tex-etextools = %{tl_version}
License:        LPPL
Summary:        e-TeX tools for LaTeX users and package writers
Version:        svn20694.3.1415926

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(etoolbox.sty), tex(letltxmacro.sty)
Provides:       tex(etextools.sty) = %{tl_version}

%description -n texlive-etextools
The package provides many (purely expandable) tools for LaTeX:
Extensive list management (csv lists, lists of single
tokens/characters, etoolbox lists); purely expandable loops
(csvloop, forcsvloop, etc.); conversion (csvtolist, etc.));
addition/deletion (csvadd, listdel, etc.); Expansion and group
control: \expandnext, \ExpandAfterCmds, \AfterGroup...; Tests
on tokens, characters and control sequences (\iffirstchar,
\ifiscs, \ifdefcount, \@ifchar...); Tests on strings
(\ifstrnum, \ifuppercase, \DeclareStringFilter...); Purely
expandable macros with options (\FE@testopt, \FE@ifstar) or
modifiers (\FE@modifiers); Some purely expandable numerics
(\interval, \locinterplin). The package is dependent on the
etex and the etoolbox packages.

%package -n texlive-etextools-doc
Summary:        Documentation for etextools
Version:        svn20694.3.1415926

Provides:       tex-etextools-doc
AutoReqProv:    No

%description -n texlive-etextools-doc
Documentation for etextools

%package -n texlive-etoc
Provides:       tex-etoc = %{tl_version}
License:        LPPL 1.3
Summary:        Completely customisable TOCs
Version:        svn48136
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(multicol.sty)
Provides:       tex(etoc.sty) = %{tl_version}

%description -n texlive-etoc
The package gives the user complete control of how the entries
of the table of contents should be constituted from the name,
number, and page number of each sectioning unit. The layout is
controlled by the definition of 'line styles' for each
sectioning level used in the document. The package provides its
own custom line styles (which may be used as examples), and
continues to support the standard formatting inherited from the
LaTeX document classes, but the package can also allow the user
to delegate the details to packages dealing with list making
environments (such as enumitem). The package's default global
style typesets tables of contents in a multi-column format,
with either a standard heading, or a ruled title (optionally
with a frame around the table). The \tableofcontents command
may be used arbitrarily many times in the same document, while
\localtableofcontents provides a 'local' table of contents.

%package -n texlive-etoc-doc
Summary:        Documentation for etoc
Version:        svn48136
Provides:       tex-etoc-doc
AutoReqProv:    No

%description -n texlive-etoc-doc
Documentation for etoc

%package -n texlive-etoolbox
Provides:       tex-etoolbox = %{tl_version}
License:        LPPL 1.3
Summary:        e-TeX tools for LaTeX
Version:        svn46602
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etex.sty)
Provides:       tex(etoolbox.def) = %{tl_version}, tex(etoolbox.sty) = %{tl_version}

%description -n texlive-etoolbox
The package is a toolbox of programming facilities geared
primarily towards LaTeX class and package authors. It provides
LaTeX frontends to some of the new primitives provided by e-TeX
as well as some generic tools which are not strictly related to
e-TeX but match the profile of this package. Note that the
initial versions of this package were released under the name
elatex. The package provides functions that seem to offer
alternative ways of implementing some LaTeX kernel commands;
nevertheless, the package will not modify any part of the LaTeX
kernel.

%package -n texlive-etoolbox-doc
Summary:        Documentation for etoolbox
Version:        svn46602
Provides:       tex-etoolbox-doc
AutoReqProv:    No

%description -n texlive-etoolbox-doc
Documentation for etoolbox

%package -n texlive-eukdate
Provides:       tex-eukdate = %{tl_version}
License:        LPPL
Summary:        UK format dates, with weekday
Version:        svn15878.1.04

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(eukdate.sty) = %{tl_version}

%description -n texlive-eukdate
The package is used to change the format of \today's date,
including the weekday, e.g., "Saturday, 26 June 2008", the 'UK
format', which is preferred in many parts of the world, as
distinct from that which is used in \maketitle of the article
class, "June 26, 2008", the 'US format'.

%package -n texlive-eukdate-doc
Summary:        Documentation for eukdate
Version:        svn15878.1.04

Provides:       tex-eukdate-doc
AutoReqProv:    No

%description -n texlive-eukdate-doc
Documentation for eukdate

%package -n texlive-europasscv
Provides:       tex-europasscv = %{tl_version}
License:        LPPL 1.3
Summary:        Unofficial class for the new version of the Europass curriculum vitae
Version:        svn45878
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(totpages.sty), tex(inputenc.sty), tex(array.sty), tex(fancyhdr.sty)
Requires:       tex(xcolor.sty), tex(url.sty), tex(soul.sty), tex(tabu.sty)
Requires:       tex(setspace.sty), tex(geometry.sty), tex(textcomp.sty), tex(enumitem.sty)
Requires:       tex(hyperref.sty), tex(colortbl.sty), tex(graphicx.sty), tex(showframe.sty)
Requires:       tex(fontenc.sty)
Provides:       tex(europasscv.cls) = %{tl_version}, tex(europasscv_de.def) = %{tl_version}
Provides:       tex(europasscv_en.def) = %{tl_version}, tex(europasscv_it.def) = %{tl_version}

%description -n texlive-europasscv
This class is an unofficial LaTeX implementation of the the
Europass CV, the standard model for curriculum vitae as
recommended by the European Commission. It includes the major
style updates that came out in 2013, featuring a neater, more
compact and somewhat fancier layout.

%package -n texlive-europasscv-doc
Summary:        Documentation for europasscv
Version:        svn45878
Provides:       tex-europasscv-doc
AutoReqProv:    No

%description -n texlive-europasscv-doc
Documentation for europasscv

%package -n texlive-europecv
Provides:       tex-europecv = %{tl_version}
License:        LPPL
Summary:        Unofficial class for European curricula vitae
Version:        svn48257
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(totpages.sty), tex(booktabs.sty), tex(ucs.sty), tex(inputenc.sty)
Requires:       tex(array.sty), tex(longtable.sty), tex(fancyhdr.sty)
Provides:       tex(ecvbg.def) = %{tl_version}, tex(ecvca.def) = %{tl_version}
Provides:       tex(ecvcs.def) = %{tl_version}, tex(ecvda.def) = %{tl_version}
Provides:       tex(ecvde.def) = %{tl_version}, tex(ecven.def) = %{tl_version}
Provides:       tex(ecves.def) = %{tl_version}, tex(ecvet.def) = %{tl_version}
Provides:       tex(ecvfi.def) = %{tl_version}, tex(ecvfr.def) = %{tl_version}
Provides:       tex(ecvgl.def) = %{tl_version}, tex(ecvgr.def) = %{tl_version}
Provides:       tex(ecvhu.def) = %{tl_version}, tex(ecvis.def) = %{tl_version}
Provides:       tex(ecvit.def) = %{tl_version}, tex(ecvlt.def) = %{tl_version}
Provides:       tex(ecvlv.def) = %{tl_version}, tex(ecvmt.def) = %{tl_version}
Provides:       tex(ecvnl.def) = %{tl_version}, tex(ecvno.def) = %{tl_version}
Provides:       tex(ecvpl.def) = %{tl_version}, tex(ecvpt.def) = %{tl_version}
Provides:       tex(ecvro.def) = %{tl_version}, tex(ecvsk.def) = %{tl_version}
Provides:       tex(ecvsl.def) = %{tl_version}, tex(ecvsr.def) = %{tl_version}
Provides:       tex(ecvsv.def) = %{tl_version}, tex(europecv.cls) = %{tl_version}

%description -n texlive-europecv
The europecv class is an unofficial LaTeX implementation of the
standard model for curricula vitae (the "Europass CV") as
recommended by the European Commission. Although primarily
intended for users in the European Union, the class is flexible
enough to be used for any kind of curriculum vitae. The class
has localisations for all the official languages of the EU
(plus Catalan), as well as options permitting input in UTF-8
and koi8-r.

%package -n texlive-europecv-doc
Summary:        Documentation for europecv
Version:        svn48257
Provides:       tex-europecv-doc
AutoReqProv:    No

%description -n texlive-europecv-doc
Documentation for europecv

%package -n texlive-everyhook
Provides:       tex-everyhook = %{tl_version}
License:        LPPL 1.3
Summary:        Hooks for standard TeX token lists
Version:        svn35675.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(svn-prov.sty), tex(etoolbox.sty)
Provides:       tex(everyhook.sty) = %{tl_version}

%description -n texlive-everyhook
The package takes control of the six TeX token registers
\everypar, \everymath, \everydisplay, \everyhbox, \everyvbox
and \everycr. Real hooks for each of the registers may be
installed using a stack like interface. For backwards
compatibility, each of the \everyX token lists can be set
without interfering with the hooks.

%package -n texlive-everyhook-doc
Summary:        Documentation for everyhook
Version:        svn35675.1.2

Provides:       tex-everyhook-doc
AutoReqProv:    No

%description -n texlive-everyhook-doc
Documentation for everyhook

%package -n texlive-everypage
Provides:       tex-everypage = %{tl_version}
License:        LPPL
Summary:        Provide hooks to be run on every page of a document
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(everypage.sty) = %{tl_version}

%description -n texlive-everypage
The package provides hooks to perform actions on every page, or
on the current page. Specifically, actions are performed after
the page is composed, but before it is shipped, so they can be
used to prepare the output page in tasks like putting
watermarks in the background, or in setting the next page
layout, etc.

%package -n texlive-everypage-doc
Summary:        Documentation for everypage
Version:        svn15878.1.1

Provides:       tex-everypage-doc
AutoReqProv:    No

%description -n texlive-everypage-doc
Documentation for everypage

%package -n texlive-exam
Provides:       tex-exam = %{tl_version}
License:        LPPL 1.3
Summary:        Package for typesetting exam scripts
Version:        svn46084
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(exam.cls) = %{tl_version}

%description -n texlive-exam
Provides a class exam, which eases production of exams, even by
a LaTeX novice. Simple commands are provided to: create
questions, parts of questions, subparts of parts, and
subsubparts of subparts, all with optional point values; create
a grading table, indexed either by question number (listing
each question and the total possible points for that question)
or by page number (listing each page with points and the total
possible points for that page); create headers and footers that
are each specified in three parts: one part to be left
justified, one part to be centered, and one part to be right
justified, in the manner of fancyhdr Headers and/or footers can
be different on the first page of the exam, can be different on
the last page of the exam, and can vary depending on whether
the page number is odd or even, or on whether the current page
continues a question from a previous page, or on whether the
last question on the current page continues onto the following
page. Multiple line headers and/or footers are allowed, and
it's easy to increase the part of the page devoted to headers
and/or footers to allow for this. Note that the bundle exams
also provides a file exam.cls; the two bundles therefore clash,
and should not be installed on the same system.

%package -n texlive-exam-doc
Summary:        Documentation for exam
Version:        svn46084
Provides:       tex-exam-doc
AutoReqProv:    No

%description -n texlive-exam-doc
Documentation for exam

%package -n texlive-exam-n
Provides:       tex-exam-n = %{tl_version}
License:        LPPL
Summary:        Exam class, focused on collaborative authoring
Version:        svn42755
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(babel.sty), tex(amsmath.sty), tex(color.sty), tex(ifpdf.sty)
Requires:       tex(times.sty), tex(helvet.sty), tex(mathptm.sty), tex(fontenc.sty)
Requires:       tex(textcomp.sty), tex(fancyhdr.sty)
Provides:       tex(exam-n.cls) = %{tl_version}

%description -n texlive-exam-n
The class design offers: Direct support for collaborative
development of an exam, using a model in which a departmental
'exams convener' or 'exam chair' coordinates multiple authors
writing individual questions (the class file and associated
process is in regular use within a physics and astronomy
department). All of the 'traditional' exam paper features such
as sectioning, per-part running marks, 'Question n continued'
catchwords, and so on. Readily configured local adaptation.

%package -n texlive-exam-n-doc
Summary:        Documentation for exam-n
Version:        svn42755
Provides:       tex-exam-n-doc
AutoReqProv:    No

%description -n texlive-exam-n-doc
Documentation for exam-n

%package -n texlive-examdesign
Provides:       tex-examdesign = %{tl_version}
License:        GPL+
Summary:        LaTeX class for typesetting exams
Version:        svn15878.1.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(enumerate.sty), tex(multicol.sty), tex(keyval.sty)
Provides:       tex(examdesign.cls) = %{tl_version}

%description -n texlive-examdesign
This bundle provides a class examdesign. The class provides
several features useful for designing tests or question sets:
it allows for explicit markup of questions and answers; the
class will, at the user's request, automatically generate
answer keys; multiple versions of the same test can be
generated automatically, with the ordering of questions within
each section randomly permuted so as to minimize cheating; the
generated answer keys can be constructed either with or without
the questions included; environments are provided to assist in
constructing the most common types of test question: matching,
true/false, multiple-choice, fill-in-the-blank, and short
answer/essay questions.

%package -n texlive-examdesign-doc
Summary:        Documentation for examdesign
Version:        svn15878.1.02

Provides:       tex-examdesign-doc
AutoReqProv:    No

%description -n texlive-examdesign-doc
Documentation for examdesign

%package -n texlive-example
Provides:       tex-example = %{tl_version}
License:        GPL+
Summary:        Typeset examples for TeX courses
Version:        svn33398.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(example.sty) = %{tl_version}

%description -n texlive-example
The package makes it easier to produce examples for TeX course.
It provides an example environment, which typesets its contents
on the left of the page, and prints it verbatim on the right.

%package -n texlive-examplep
Provides:       tex-examplep = %{tl_version}
License:        GPL+
Summary:        Verbatim phrases and listings in LaTeX
Version:        svn16916.0.04

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbfwr.sty)
Provides:       tex(codep.sty) = %{tl_version}, tex(examplep.sty) = %{tl_version}
Provides:       tex(verbfwr.sty) = %{tl_version}

%description -n texlive-examplep
Examplep provides sophisticated features for typesetting
verbatim source code listings, including the display of the
source code and its compiled LaTeX or Metapost output side-by-
side, with automatic width detection and enabled page breaks
(in the source), without the need for specifying the source
twice. Special care is taken that section, page and footnote
numbers do not interfere with the main document. For
typesetting short verbatim phrases, a replacement for the \verb
command is also provided in the package, which can be used
inside tables and moving arguments such as footnotes and
section titles. The listings package is used for syntax
highlighting. The accompanying codep package and the wrfiles.pl
Perl script provide a convenient interface to the examplep
package for authors of manuals. With codep it is possible to
generate the source code, the LaTeX or METAPOST output and the
compilable example file from a single source embedded into the
appropriate place of the .tex document file.

%package -n texlive-examplep-doc
Summary:        Documentation for examplep
Version:        svn16916.0.04

Provides:       tex-examplep-doc
AutoReqProv:    No

%description -n texlive-examplep-doc
Documentation for examplep

%package -n texlive-excludeonly
Provides:       tex-excludeonly = %{tl_version}
License:        Public Domain
Summary:        Prevent files being \include-ed
Version:        svn17262.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(excludeonly.sty) = %{tl_version}

%description -n texlive-excludeonly
The package defines an \excludeonly command, which is (in
effect) the opposite of \includeonly. If both \includeonly and
\excludeonly exist in a document, only files "allowed" by both
will be included. The package redefines the internal \@include
command, so it conflicts with packages that do the same.
Examples are the classes paper.cls and thesis.cls.

%package -n texlive-excludeonly-doc
Summary:        Documentation for excludeonly
Version:        svn17262.1.0

Provides:       tex-excludeonly-doc
AutoReqProv:    No

%description -n texlive-excludeonly-doc
Documentation for excludeonly

%package -n texlive-exercise
Provides:       tex-exercise = %{tl_version}
License:        GPLv2+
Summary:        Typeset exercises, problems, etc. and their answers
Version:        svn35417.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(ifthen.sty)
Provides:       tex(exercise.sty) = %{tl_version}

%description -n texlive-exercise
The package helps to typeset exercises or list of exercises
within any document. Exercises, questions and sub-questions are
automatically numbered. It is possible to put answers in the
same document, and display them immediatly, later in the
document or not to print answers at all. The layout of
exercises is fully customisable. It is possible to typeset long
problems, short exercises, questionnaires, etc. Usage of the
babel package is detected, but not fully supported yet (only
English and French are implemented).

%package -n texlive-exercise-doc
Summary:        Documentation for exercise
Version:        svn35417.1.6

Provides:       tex-exercise-doc
AutoReqProv:    No

%description -n texlive-exercise-doc
Documentation for exercise

%package -n texlive-exp-testopt
Provides:       tex-exp-testopt = %{tl_version}
License:        LPPL
Summary:        Expandable \@testopt (and related) macros
Version:        svn15878.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(exp-testopt.sty) = %{tl_version}

%description -n texlive-exp-testopt
The package provides an expandable variant of the LaTeX kernel
command \@testopt, named \@expandable@testopt, and a more
general \@expandable@ifopt, both intended for package writers.
Also we have a variant of \newcommand which uses these macros
to check for optional arguments.

%package -n texlive-exp-testopt-doc
Summary:        Documentation for exp-testopt
Version:        svn15878.0.3

Provides:       tex-exp-testopt-doc
AutoReqProv:    No

%description -n texlive-exp-testopt-doc
Documentation for exp-testopt

%package -n texlive-expdlist
Provides:       tex-expdlist = %{tl_version}
License:        LPPL
Summary:        Expanded description environments
Version:        svn15878.2.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(expdlist.sty) = %{tl_version}

%description -n texlive-expdlist
The package provides additional features for the LaTeX
description environment, including adjustable left margin. The
package also allows the user to 'break' a list (for example, to
interpose a comment) without affecting the structure of the
list (this works for itemize and eumerate lists and numbered
lists remain in sequence).

%package -n texlive-expdlist-doc
Summary:        Documentation for expdlist
Version:        svn15878.2.4

Provides:       tex-expdlist-doc
AutoReqProv:    No

%description -n texlive-expdlist-doc
Documentation for expdlist

%package -n texlive-export
Provides:       tex-export = %{tl_version}
License:        LPPL
Summary:        Import and export values of LaTeX registers
Version:        svn27206.1.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dvipaste.sty) = %{tl_version}, tex(export.sty) = %{tl_version}

%description -n texlive-export
The package allows the user to export/import the values of
LaTeX registers (counters, rigid and rubber lengths only). It
is not for faint-hearted users. The package may be used, for
example, to communicate between documents for the purposes of
dvipaste.

%package -n texlive-export-doc
Summary:        Documentation for export
Version:        svn27206.1.8

Provides:       tex-export-doc
AutoReqProv:    No

%description -n texlive-export-doc
Documentation for export

%package -n texlive-exsheets
Provides:       tex-exsheets = %{tl_version}
License:        LPPL 1.3
Summary:        Create exercise sheets and exams
Version:        svn43188
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(listings.sty), tex(expl3.sty), tex(xparse.sty), tex(xtemplate.sty)
Requires:       tex(l3sort.sty), tex(l3keys2e.sty), tex(xcolor.sty), tex(etoolbox.sty)
Requires:       tex(environ.sty), tex(pgfcore.sty), tex(cntformats.sty), tex(tasks.sty)
Requires:       tex(ulem.sty), tex(translations.sty)
Provides:       tex(exsheets-listings.sty) = %{tl_version}
Provides:       tex(exsheets.sty) = %{tl_version}, tex(exsheets_configurations.cfg) = %{tl_version}
Provides:       tex(exsheets_headings.cfg) = %{tl_version}
Provides:       tex(exsheets_headings.def) = %{tl_version}

%description -n texlive-exsheets
The package provides the means to create exercises or questions
and their corresponding solutions. The questions may be divided
into classes and/or topics and may be printed selectively. Meta-
data to questions can be added and recovered. The solutions may
be printed where they are, or collected and printed at a later
point in the document all together, section-wise or selectively
by ID. The package provides the means to selectively include
questions from an external file, and to control the style of
headings of both questions and solutions.

%package -n texlive-exsheets-doc
Summary:        Documentation for exsheets
Version:        svn43188
Provides:       tex-exsheets-doc
AutoReqProv:    No

%description -n texlive-exsheets-doc
Documentation for exsheets

%package -n texlive-exsol
Provides:       tex-exsol = %{tl_version}
License:        LPPL 1.3
Summary:        Exercises and solutions from the same source, into a book
Version:        svn41377

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fancyvrb.sty), tex(ifthen.sty), tex(kvoptions.sty)
Provides:       tex(exsol.sty) = %{tl_version}

%description -n texlive-exsol
The packageThe exsol package provides macros to allow for
embedding exercises and solutions in the LaTeX source of an
instructional text (e.g., a book or a course text) while
generating the following separate documents: your original text
that only contains the exercises, and a solution book that
contains only the solutions to the exercises (optionally, the
exercises themselves are also copied to the solution book). The
exercise data are generated when running LaTeX on your
document; the first run also writes the solutions to a
secondary file that may be included in a simple document
harness, may be processed by LaTeX, to generate a nice solution
book. The code of the package was derived (in large part) from
fancyvrb.

%package -n texlive-exsol-doc
Summary:        Documentation for exsol
Version:        svn41377

Provides:       tex-exsol-doc
AutoReqProv:    No

%description -n texlive-exsol-doc
Documentation for exsol

%package -n texlive-extract
Provides:       tex-extract = %{tl_version}
License:        LPPL
Summary:        Extract parts of a document and write to another document
Version:        svn15878.1.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbatim.sty), tex(xkeyval.sty)
Provides:       tex(extract.sty) = %{tl_version}

%description -n texlive-extract
The package provides the means to extract specific content from
a source document and write that to a target document. One
could, for instance, use this to extract all exercises from
lecture notes and generate an exercises book on the fly. The
package also provides an environment which writes its body
entirely to the target file. Another environment will write to
the target file, but will also execute the body. This allows to
share code (for instance, a preamble) between the source
document and the target file. Finally, the package provides an
interface to conditionally extract content. With a single
package option, one can specify exactly which commands (counted
from the start of the document) should be extracted and which
not. This might be useful for extracting specific slides from a
presentation and use them in a new file.

%package -n texlive-extract-doc
Summary:        Documentation for extract
Version:        svn15878.1.8

Provides:       tex-extract-doc
AutoReqProv:    No

%description -n texlive-extract-doc
Documentation for extract

%package -n texlive-enigma
Provides:       tex-enigma = %{tl_version}
License:        BSD
Summary:        Encrypt documents with a three rotor Enigma
Version:        svn29802.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(luatexbase.sty)
Provides:       tex(enigma.sty) = %{tl_version}, tex(enigma.tex) = %{tl_version}

%description -n texlive-enigma
The package provides historical encryption (Enigma cipher) for
LuaTeX-based formats.

%package -n texlive-enigma-doc
Summary:        Documentation for enigma
Version:        svn29802.0.1

Provides:       tex-enigma-doc
AutoReqProv:    No

%description -n texlive-enigma-doc
Documentation for enigma

%package -n texlive-ebproof
Provides:       tex-ebproof = %{tl_version}
License:        LPPL 1.3
Summary:        Formal proofs in the style of sequent calculus
Version:        svn44392
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pgfkeys.sty)
Provides:       tex(ebproof.sty) = %{tl_version}

%description -n texlive-ebproof
This package provides commands to typeset proof trees in the
style of sequent calculus and related systems. The commands
allow for writing inferences with any number of premises and
alignment of successive formulas on an arbitrary point. Various
options allow complete control over spacing, styles of
inference rules, placement of labels, etc. The package requires
pgfkeys (from the PGF/TikZ bundle) for the option system.

%package -n texlive-ebproof-doc
Summary:        Documentation for ebproof
Version:        svn44392
Provides:       tex-ebproof-doc
AutoReqProv:    No

%description -n texlive-ebproof-doc
Documentation for ebproof

%package -n texlive-eqnarray
Provides:       tex-eqnarray = %{tl_version}
License:        GPLv3+
Summary:        More generalised equation arrays with numbering
Version:        svn20641.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty)
Provides:       tex(eqnarray.sty) = %{tl_version}

%description -n texlive-eqnarray
Defines an equationarray environment, that allows more than
three columns, but otherwise behaves like LaTeX's eqnarray
environment. This environment is similar, in some ways, to the
align environment of amsmath. The package requires the array
package.

%package -n texlive-eqnarray-doc
Summary:        Documentation for eqnarray
Version:        svn20641.1.3

Provides:       tex-eqnarray-doc
AutoReqProv:    No

%description -n texlive-eqnarray-doc
Documentation for eqnarray

%package -n texlive-extarrows
Provides:       tex-extarrows = %{tl_version}
License:        LGPLv2+
Summary:        Extra Arrows beyond those provided in AMSmath
Version:        svn15878.1.0b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty)
Provides:       tex(extarrows.sty) = %{tl_version}

%description -n texlive-extarrows
Arrows are provided to supplement \xleftarrow and \xrightarrow
of the AMSMath package: \xlongequal, \xLongleftarrow,
\xLongrightarrow, \xLongleftrightarrow, \xLeftrightarrow.
\xlongleftrightarrow, \xleftrightarrow, \xlongleftarrow and
\xlongrightarrow.

%package -n texlive-extarrows-doc
Summary:        Documentation for extarrows
Version:        svn15878.1.0b

Provides:       tex-extarrows-doc
AutoReqProv:    No

%description -n texlive-extarrows-doc
Documentation for extarrows

%package -n texlive-extpfeil
Provides:       tex-extpfeil = %{tl_version}
License:        LPPL 1.3
Summary:        Extensible arrows in mathematics
Version:        svn16243.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(amssymb.sty), tex(mathtools.sty), tex(stmaryrd.sty)
Provides:       tex(extpfeil.sty) = %{tl_version}

%description -n texlive-extpfeil
The package provides some more extensible arrows (usable in the
same way as \xleftarrow from amsmath), and a simple command to
create new ones.

%package -n texlive-extpfeil-doc
Summary:        Documentation for extpfeil
Version:        svn16243.0.4

Provides:       tex-extpfeil-doc
AutoReqProv:    No

%description -n texlive-extpfeil-doc
Documentation for extpfeil

%package -n texlive-emp
Provides:       tex-emp = %{tl_version}
License:        GPL+
Summary:        "Encapsulate" MetaPost figures in a document
Version:        svn23483.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty), tex(verbatim.sty)
Provides:       tex(emp.sty) = %{tl_version}

%description -n texlive-emp
Emp is a package for encapsulating MetaPost figures in LaTeX:
the package provides environments where you can place MetaPost
commands, and means of using that code as fragments for
building up figures to include in your document. So, with emp,
the procedure is to run your document with LaTeX, run MetaPost,
and then complete running your document in the normal way. Emp
is therefore useful for keeping illustrations in synchrony with
the text. It also frees you from inventing descriptive names
for PostScript files that fit into the confines of file system
conventions.

%package -n texlive-emp-doc
Summary:        Documentation for emp
Version:        svn23483.0

Provides:       tex-emp-doc
AutoReqProv:    No

%description -n texlive-emp-doc
Documentation for emp

%package -n texlive-epsincl
Provides:       tex-epsincl = %{tl_version}
License:        Public Domain
Summary:        Include EPS in MetaPost figures
Version:        svn29349.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-epsincl
The package facilitates including EPS files in MetaPost
figures; it makes use of (G)AWK.

%package -n texlive-epsincl-doc
Summary:        Documentation for epsincl
Version:        svn29349.0.2

Provides:       tex-epsincl-doc
AutoReqProv:    No

%description -n texlive-epsincl-doc
Documentation for epsincl

%package -n texlive-expressg
Provides:       tex-expressg = %{tl_version}
License:        LPPL
Summary:        Diagrams consisting of boxes, lines, and annotations
Version:        svn29349.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-expressg
A MetaPost package providing facilities to assist in drawing
diagrams that consist of boxes, lines, and annotations.
Particular support is provided for creating EXPRESS-G diagrams,
for example IDEF1X, OMT, Shlaer-Mellor, and NIAM diagrams. The
package may also be used to create UML and most other Box-Line-
Annotation charts, but not Gantt charts directly.

%package -n texlive-expressg-doc
Summary:        Documentation for expressg
Version:        svn29349.1.5

Provides:       tex-expressg-doc
AutoReqProv:    No

%description -n texlive-expressg-doc
Documentation for expressg

%package -n texlive-exteps
Provides:       tex-exteps = %{tl_version}
License:        GPL+
Summary:        Include EPS figures in MetaPost
Version:        svn19859.0.41

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-exteps
Exteps is a module for including external EPS figures into
MetaPost figures. It is written entirely in MetaPost, and does
not therefore require any post processing of the MetaPost
output.

%package -n texlive-exteps-doc
Summary:        Documentation for exteps
Version:        svn19859.0.41

Provides:       tex-exteps-doc
AutoReqProv:    No

%description -n texlive-exteps-doc
Documentation for exteps

%package -n texlive-epsf-dvipdfmx
Provides:       tex-epsf-dvipdfmx = %{tl_version}
License:        Public Domain
Summary:        Plain TeX file for using epsf.tex with (x)dvipdfmx
Version:        svn35575.2014

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(epsf-dvipdfmx.tex) = %{tl_version}

%description -n texlive-epsf-dvipdfmx
epsf-dvipdfmx.tex is a plain TeX file to be \input after
epsf.tex when using plain TeX with dvipdfmx. As in: \input epsf
\input epsf-dvipdfmx It is needed when an .eps file has
anything except the origin (0,0) for the lower-left of its
bounding box.

%package -n texlive-epsf-dvipdfmx-doc
Summary:        Documentation for epsf-dvipdfmx
Version:        svn35575.2014

Provides:       tex-epsf-dvipdfmx-doc
AutoReqProv:    No

%description -n texlive-epsf-dvipdfmx-doc
Documentation for epsf-dvipdfmx

%package -n texlive-ebook
Provides:       tex-ebook = %{tl_version}
License:        Public Domain
Summary:        ebook
Version:        svn29466.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ebook.sty) = %{tl_version}

%description -n texlive-ebook
The package defines a command \ebook that defines page layout,
fonts, and font-sizes for documents to be rendered as PDF-
ebooks on small ebook-readers. The package has been tested with
Kindle e-ink and iPad mini.

%package -n texlive-ebook-doc
Summary:        Documentation for ebook
Version:        svn29466.0

Provides:       tex-ebook-doc
AutoReqProv:    No

%description -n texlive-ebook-doc
Documentation for ebook

%package -n texlive-ebsthesis
Provides:       tex-ebsthesis = %{tl_version}
License:        LPPL
Summary:        Typesetting theses for economics
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(setspace.sty), tex(rotfloat.sty), tex(caption.sty)
Requires:       tex(ragged2e.sty), tex(footmisc.sty), tex(remreset.sty), tex(titlesec.sty)
Requires:       tex(calc.sty), tex(titletoc.sty), tex(array.sty), tex(tocbibind.sty)
Requires:       tex(nomencl.sty), tex(mdwlist.sty), tex(acronym.sty), tex(amsmath.sty)
Requires:       tex(onlyamsmath.sty), tex(comment.sty), tex(amssymb.sty), tex(dsfont.sty)
Requires:       tex(ifthen.sty), tex(amsthm.sty)
Provides:       tex(ebsthesis.cls) = %{tl_version}

%description -n texlive-ebsthesis
The ebsthesis class and ebstools package facilitate the
production of camera-ready manuscripts in conformance with the
guidelines of Gabler Verlag and typographical rules established
by the European Business School.

%package -n texlive-ebsthesis-doc
Summary:        Documentation for ebsthesis
Version:        svn15878.1.0

Provides:       tex-ebsthesis-doc
AutoReqProv:    No

%description -n texlive-ebsthesis-doc
Documentation for ebsthesis

%package -n texlive-ejpecp
Provides:       tex-ejpecp = %{tl_version}
License:        LPPL 1.2
Summary:        Class for EJP and ECP
Version:        svn42003
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphicx.sty), tex(pstricks.sty), tex(auto-pst-pdf.sty), tex(mathtools.sty)
Requires:       tex(fixltx2e.sty), tex(microtype.sty), tex(lastpage.sty), tex(latexsym.sty)
Requires:       tex(dsfont.sty), tex(amsmath.sty), tex(amsfonts.sty), tex(amssymb.sty)
Requires:       tex(amsthm.sty), tex(geometry.sty), tex(bera.sty), tex(hyperref.sty)
Provides:       tex(ejpecp.cls) = %{tl_version}

%description -n texlive-ejpecp
The class is designed for typesetting articles for the
mathematical research periodicals Electronic Journal of
Probability (EJP) and Electronic Communications in Probability
(ECP).

%package -n texlive-ejpecp-doc
Summary:        Documentation for ejpecp
Version:        svn42003
Provides:       tex-ejpecp-doc
AutoReqProv:    No

%description -n texlive-ejpecp-doc
Documentation for ejpecp

%package -n texlive-ekaia
Provides:       tex-ekaia = %{tl_version}
License:        LPPL 1.2
Summary:        Article format for publishing the Basque Country Science and Technology Journal "Ekaia"
Version:        svn42578
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(babel.sty), tex(geometry.sty), tex(sectsty.sty), tex(fancyhdr.sty)
Requires:       tex(indentfirst.sty)
Provides:       tex(ekaia.sty) = %{tl_version}

%description -n texlive-ekaia
The package provides the article format for publishing the
Basque Country Science and Technology Journal "Ekaia" at the
University of the Basque Country.

%package -n texlive-ekaia-doc
Summary:        Documentation for ekaia
Version:        svn42578
Provides:       tex-ekaia-doc
AutoReqProv:    No

%description -n texlive-ekaia-doc
Documentation for ekaia

%package -n texlive-elbioimp
Provides:       tex-elbioimp = %{tl_version}
License:        LPPL
Summary:        A LaTeX document class for the Journal of Electrical Bioimpedance
Version:        svn21758.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(url.sty), tex(geometry.sty), tex(mathptmx.sty)
Requires:       tex(type1cm.sty), tex(type1ec.sty), tex(caption.sty)
Provides:       tex(elbioimp.cls) = %{tl_version}

%description -n texlive-elbioimp
A document class for writing articles to the Journal of
Electrical Bioimpedance.

%package -n texlive-elbioimp-doc
Summary:        Documentation for elbioimp
Version:        svn21758.1.2

Provides:       tex-elbioimp-doc
AutoReqProv:    No

%description -n texlive-elbioimp-doc
Documentation for elbioimp

%package -n texlive-elsarticle
Provides:       tex-elsarticle = %{tl_version}
License:        LPPL 1.2
Summary:        Class for articles for submission to Elsevier journals
Version:        svn48134
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(txfonts.sty), tex(times.sty), tex(graphicx.sty), tex(pifont.sty)
Requires:       tex(natbib.sty), tex(geometry.sty)
Provides:       tex(elsarticle.cls) = %{tl_version}

%description -n texlive-elsarticle
The class is for typeset journal articles, is accepted for
submitted articles, both in Elsevier's electronic submission
system and elsewhere.

%package -n texlive-elsarticle-doc
Summary:        Documentation for elsarticle
Version:        svn48134
Provides:       tex-elsarticle-doc
AutoReqProv:    No

%description -n texlive-elsarticle-doc
Documentation for elsarticle

%package -n texlive-elteikthesis
Provides:       tex-elteikthesis = %{tl_version}
License:        LPPL 1.2
Summary:        Thesis class for ELTE University Informatics wing
Version:        svn22513.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(geometry.sty), tex(setspace.sty)
Provides:       tex(elteikthesis.cls) = %{tl_version}

%description -n texlive-elteikthesis
This is not an official University class, and has not been
approved by the University.

%package -n texlive-elteikthesis-doc
Summary:        Documentation for elteikthesis
Version:        svn22513.1.2

Provides:       tex-elteikthesis-doc
AutoReqProv:    No

%description -n texlive-elteikthesis-doc
Documentation for elteikthesis

%package -n texlive-erdc
Provides:       tex-erdc = %{tl_version}
License:        LPPL
Summary:        Style for Reports by US Army Corps of Engineers
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(color.sty), tex(caption.sty), tex(longtable.sty)
Requires:       tex(dcolumn.sty), tex(natbib.sty), tex(amsmath.sty), tex(ragged2e.sty)
Requires:       tex(geometry.sty), tex(fancyhdr.sty)
Provides:       tex(erdc.cls) = %{tl_version}

%description -n texlive-erdc
A class for typesetting Technical Information Reports of the
Engineer Research and Development Center, US Army Corps of
Engineers. The class was commissioned and paid for by US Army
Corps of Engineers, Engineer Research and Development Center,
3909 Halls Ferry Road, Vicksburg, MS 39180-6199.

%package -n texlive-erdc-doc
Summary:        Documentation for erdc
Version:        svn15878.1.1

Provides:       tex-erdc-doc
AutoReqProv:    No

%description -n texlive-erdc-doc
Documentation for erdc

%package -n texlive-estcpmm
Provides:       tex-estcpmm = %{tl_version}
License:        LPPL
Summary:        Style for Munitions Management Project Reports
Version:        svn17335.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(caption.sty), tex(geometry.sty), tex(fancyhdr.sty)
Provides:       tex(estcpmm.cls) = %{tl_version}

%description -n texlive-estcpmm
Provides a class which supports typesetting Cost and
Performance Reports and Final Reports for Munitions Management
Reports, US Environmental Security Technology Certification
Program. The class was commissioned and paid for by US Army
Corps of Engineers, Engineer Research and Development Center,
3909 Halls Ferry Road, Vicksburg, MS 39180-6199.

%package -n texlive-estcpmm-doc
Summary:        Documentation for estcpmm
Version:        svn17335.0.4

Provides:       tex-estcpmm-doc
AutoReqProv:    No

%description -n texlive-estcpmm-doc
Documentation for estcpmm

%package -n texlive-eltex
Provides:       tex-eltex = %{tl_version}
License:        LPPL
Summary:        Simple circuit diagrams in LaTeX picture mode
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(eltex1.tex) = %{tl_version}, tex(eltex2.tex) = %{tl_version}
Provides:       tex(eltex3.tex) = %{tl_version}, tex(eltex4.tex) = %{tl_version}
Provides:       tex(eltex5.tex) = %{tl_version}, tex(eltex6.tex) = %{tl_version}
Provides:       tex(eltex7.tex) = %{tl_version}

%description -n texlive-eltex
The macros enable the user to draw simple circuit diagrams in
the picture environment, with no need of special resources. The
macros are appropriate for drawing for school materials. The
circuit symbols accord to the various parts of the standard IEC
617.

%package -n texlive-eltex-doc
Summary:        Documentation for eltex
Version:        svn15878.2.0

Provides:       tex-eltex-doc
AutoReqProv:    No

%description -n texlive-eltex-doc
Documentation for eltex

%package -n texlive-endiagram
Provides:       tex-endiagram = %{tl_version}
License:        LPPL 1.3
Summary:        Easy creation of potential energy curve diagrams
Version:        svn34486.0.1d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty), tex(tikz.sty)
Requires:       tex(siunitx.sty)
Provides:       tex(endiagram.sty) = %{tl_version}

%description -n texlive-endiagram
The package provides the facility of drawing potential energy
curve diagrams with just a few simple commands. The package
cannot (yet) be considered stable.

%package -n texlive-endiagram-doc
Summary:        Documentation for endiagram
Version:        svn34486.0.1d

Provides:       tex-endiagram-doc
AutoReqProv:    No

%description -n texlive-endiagram-doc
Documentation for endiagram

%package -n texlive-engtlc
Provides:       tex-engtlc = %{tl_version}
License:        LPPL 1.3
Summary:        Support for users in Telecommunications Engineering
Version:        svn28571.3.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(engtlc.sty) = %{tl_version}

%description -n texlive-engtlc
The package provides a wide range of abbreviations for terms
used in Telecommunications Engineering.

%package -n texlive-engtlc-doc
Summary:        Documentation for engtlc
Version:        svn28571.3.2

Provides:       tex-engtlc-doc
AutoReqProv:    No

%description -n texlive-engtlc-doc
Documentation for engtlc

%package -n texlive-ecobiblatex-doc
Provides:       tex-ecobiblatex-doc = %{tl_version}
License:        LPPL
Summary:        doc files of ecobiblatex
Version:        svn39233

AutoReqProv:    No

%description -n texlive-ecobiblatex-doc
Documentation for ecobiblatex

%package -n texlive-ecobiblatex
Provides:       tex-ecobiblatex = %{tl_version}
License:        LPPL
Summary:        Global Ecology and Biogeography BibLaTeX styles for the Biber backend
Version:        svn39233

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-ecobiblatex
This bundle provides a set of styles for creating
bibliographies using BibLaTeX in the style of the Global
Ecology and Biogeography journal. It comprises styles based on
the conventions of John Wiley & Sons Ltd and Global Ecology and
Biogeography Conventions (c).

%package -n texlive-econometrics-doc
Provides:       tex-econometrics-doc = %{tl_version}
License:        LPPL
Summary:        doc files of econometrics
Version:        svn39396

AutoReqProv:    No

%description -n texlive-econometrics-doc
Documentation for econometrics

%package -n texlive-econometrics
Provides:       tex-econometrics = %{tl_version}
License:        LPPL
Summary:        defines some commands that simplify mathematic notation in economic and econometric writing
Version:        svn39396

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(econometrics.sty) = %{tl_version}

%description -n texlive-econometrics
Econometrics is a package that defines some commands that
simplify mathematic notation in economic and econometrics
writing. The commands are related to the notation of vectors,
matrices, sets, calligraphic and roman letters statistical
distributions constants and symbols matrix operators and
statistical operators. The package is based on "Notation in
Econometrics: a proposal for a standard" by Karim Abadir and
Jan R. Magnus, The Econometrics Journal (2002), 5, 76-90.

%package -n texlive-einfuehrung2-doc
Provides:       tex-einfuehrung2-doc = %{tl_version}
License:        LPPL
Summary:        doc files of einfuehrung2
Version:        svn39153

AutoReqProv:    No

%description -n texlive-einfuehrung2-doc
Documentation for einfuehrung2

%package -n texlive-ellipse-doc
Provides:       tex-ellipse-doc = %{tl_version}
License:        LPPL
Summary:        doc files of ellipse
Version:        svn39025

AutoReqProv:    No

%description -n texlive-ellipse-doc
Documentation for ellipse

%package -n texlive-ellipse
Provides:       tex-ellipse = %{tl_version}
License:        LPPL
Summary:        Draw ellipses and elliptical arcs using the standard LaTeX2e picture environment
Version:        svn39025

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ellipse.sty) = %{tl_version}

%description -n texlive-ellipse
Draw ellipses and elliptical arcs using the standard LaTeX2e
picture environment.

%package -n texlive-emisa-doc
Provides:       tex-emisa-doc = %{tl_version}
License:        LPPL
Summary:        doc files of emisa
Version:        svn46734
AutoReqProv:    No

%description -n texlive-emisa-doc
Documentation for emisa

%package -n texlive-emisa
Provides:       tex-emisa = %{tl_version}
License:        LPPL
Summary:        A LaTeX package for preparing manuscripts for the journal EMISA
Version:        svn46734
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(emisa.cls) = %{tl_version}

%description -n texlive-emisa
The EMISA LaTeX package is provided for preparing manuscripts
for submission to EMISA, and for preparing accepted submissions
for publication as well as for typesetting the final document
by the editorial office. Articles in EMISA are published online
at EMISA (in the Portable Document Format or PDF format).

%package -n texlive-exercises-doc
Provides:       tex-exercises-doc = %{tl_version}
License:        LPPL
Summary:        doc files of exercises
Version:        svn42428
AutoReqProv:    No

%description -n texlive-exercises-doc
Documentation for exercises

%package -n texlive-exercises
Provides:       tex-exercises = %{tl_version}
License:        LPPL
Summary:        Typeset exercises and solutions with automatic addition of points
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(exercises.sty) = %{tl_version}

%description -n texlive-exercises
This package defines the environments exercise and solution.
The layout of these environments can be customized. The --
optional -- points in the exercises can be added automatically.
The package also permits to hide the solutions.

%package -n texlive-easyformat
Summary:        Add easier bolds and italics
Version:        svn44543
License:        GPLv3+
Requires:       texlive-base texlive-kpathsea
Provides:       tex(easyformat.sty) = %{tl_version}

%description -n texlive-easyformat
This package allows the use of underscores and circumflexes to
begin resp. end \textit{italic}, \textbf{bold} or
\textsc{smallcaps} formatting as an alternative to the standard
LaTeX \verb|\textit{\dots}|, \verb|\textbf{\dots}| and/or
\verb|\textsc{\dots}|. The underscore and circumflex's meaning
in mathmode remain the same.

%package -n texlive-ecgdraw
Summary:        Draws electrocardiograms (ECG)
Version:        svn41617
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ecgdraw.sty) = %{tl_version}

%description -n texlive-ecgdraw
This package provides the \ECG{<code>} command which draws
electrocardiograms (ECG). The <code> represents a series of
abbreviations which allow to draw different types of wave.

%package -n texlive-endofproofwd
Summary:        An "end of proof" sign
Version:        svn45116
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(endofproofwd.sty) = %{tl_version}

%description -n texlive-endofproofwd
This package provides an additional "end of proof" sign. The
command's name is \wasserdicht.

%package -n texlive-eqnalign
Summary:        Make eqnarray behave like align
Version:        svn43278
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(eqnalign.sty) = %{tl_version}

%description -n texlive-eqnalign
The package makes eqnarray environment behave like align from
amsmath'. It is intended for quick-fixing documents that use
eqnarray. In cases where it fails, manual conversion to align
is required, but these cases should be seldom.

%package -n texlive-eulerpx
Summary:        A modern interface for the Euler math fonts
Version:        svn43735
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(eulerpx.sty) = %{tl_version}

%description -n texlive-eulerpx
This package provides the "eulerpx" font, which started as a
hybrid of multiple other font packages, notably eulervm and
newpxmath. Its purpose is twofold: To use the eulervm symbols
for greek and latin, but the newpxmath font for braces and
brackets, and the text font for digits and operators; and to
make it easy to change between a sans and a serif font for the
digits and operators so that the font can be used seamlessly in
documents using both. This package was put together with the
intent to use it with the Palatino and Optima fonts, but it may
work with other combinations, too.

%package -n texlive-emf
Summary:        Support for the EMF symbol
Version:        svn42023
License:        GPLv3
Requires:       texlive-base texlive-kpathsea
Provides:       tex(emf.sty) = %{tl_version}

%description -n texlive-emf
This package provides LaTeX support for the symbol for the EMF
in electric circuits and electrodynamics. It provides support
for multiple symbols but does not provide any fonts. The fonts
themselves must be acquired otherwise. However the fonts are
part of a normal TeX Live installation.

%package -n texlive-endnotesj
Summary:        Japanese-style endnotes
Version:        svn47703
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(endnotesj.sty) = %{tl_version}

%description -n texlive-endnotesj
This package provides customized styles for endnotes to be used
with Japanese documents. It can be used on pLaTeX, upLaTeX, and
LuaLaTeX (LuaTeX-ja).

%package -n texlive-eqnnumwarn
Summary:        Modifies the amsmath equation environments to warn for a displaced equation number
Version:        svn45511
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(eqnnumwarn.sty) = %{tl_version}

%description -n texlive-eqnnumwarn
Sometimes an equation is too long that an equation number will
be typeset below the equation itself, but yet not long enough
to yield an "overfull \hbox" warning. The eqnnumwarn package
modifies the standard amsmath numbered equation environments to
throw a warning whenever this occurs.

%package -n texlive-erw-l3
Summary:        A bundle of small utilities built around expl3
Version:        svn48069
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(expl3.sty)
Provides:       tex(erw-l3.sty) = %{tl_version}

%description -n texlive-erw-l3
Bundles LaTeX3 packages sharing the erw-l3 prefix. List of
packages in this bundle: compose: compose control sequences,
whether predefined or inline csutil: narrow purpose control
sequences (backend to other packages) disambig: wrapper around
\NewDocumentCommand to prevent name conflicts with external
cmds numbrdcs: numbered control sequences built from other
control sequences or inline

%package -n texlive-etsvthor
Summary:        Some useful abbreviations for members of e.t.s.v. Thor
Version:        svn48186
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(etsvthor.sty) = %{tl_version}

%description -n texlive-etsvthor
"e.t.s.v. Thor" stands for "Elektrotechnische Studievereniging
Thor", a study association of Electrical Engeering at the
Eindhoven University of Technology. The author of the package
tells us: "Most of our committees use LaTeX to create meeting
notes or other formal documents within the association. When
you create a lot of these documents (which I do a lot, since I
am currently the candidate Secretary of the new board), some
abbreviations are extremely useful. I discovered that more
people from our association are interested in using these, so I
decided to put them in a package, so they can use it very
easily too."

%package -n texlive-euro-ce
Summary:        Euro and CE sign font
Version:        svn25714
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ceit.mf) = %{tl_version}, tex(cemac.mf) = %{tl_version}
Provides:       tex(cerm.mf) = %{tl_version}, tex(cesl.mf) = %{tl_version}
Provides:       tex(eurobf.mf) = %{tl_version}, tex(eurobfit.mf) = %{tl_version}
Provides:       tex(eurobfsl.mf) = %{tl_version}, tex(euroit.mf) = %{tl_version}
Provides:       tex(euromac.mf) = %{tl_version}, tex(euroof.mf) = %{tl_version}
Provides:       tex(eurorm.mf) = %{tl_version}, tex(eurosl.mf) = %{tl_version}
Provides:       tex(eurosp.mf) = %{tl_version}, tex(ceit.tfm) = %{tl_version}
Provides:       tex(cerm.tfm) = %{tl_version}, tex(cesl.tfm) = %{tl_version}
Provides:       tex(eurobf.tfm) = %{tl_version}, tex(eurobfit.tfm) = %{tl_version}
Provides:       tex(eurobfsl.tfm) = %{tl_version}, tex(euroit.tfm) = %{tl_version}
Provides:       tex(euroof.tfm) = %{tl_version}, tex(eurorm.tfm) = %{tl_version}
Provides:       tex(eurosl.tfm) = %{tl_version}, tex(eurosp.tfm) = %{tl_version}

%description -n texlive-euro-ce
Metafont source for the symbols in several variants, designed
to fit with the Computer Modern-set text.

%package -n texlive-exercisebank
Summary:        Creating and managing exercises, and reusing them as composed sets
Version:        svn48242
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(exercisebank.sty) = %{tl_version}

%description -n texlive-exercisebank
This package makes it easier to maintain and edit your exercise
sets. Exercises are saved as separate files containing part
problems. These files can be used to make sets, and you can
cherry-pick or exclude certain part problems as you see fit.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD
cd %{buildroot}%{_texdir}/texmf-dist/tex/plain/etex/
patch -p0 < %{_sourcedir}/etex-addlanguage-fix-bz1215257.patch


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/erewhon"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
cp -R %{buildroot}/%{_texdir}/texmf-dist/doc/man %{buildroot}/%{_datadir}/
rm -f %{buildroot}%{_datadir}/man/man1/etex.man1.pdf*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/fonts/type1/public/epiolmec/Epi-Olmec.pfb
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man/man1/etex.*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-enctex
%license gpl.txt
%{_texdir}/texmf-dist/tex/generic/enctex/

%files -n texlive-enctex-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/generic/enctex/

%files -n texlive-etex
%license knuth.txt
%{_mandir}/man1/etex.1*
%{_texdir}/texmf-dist/fonts/source/public/etex/
%{_texdir}/texmf-dist/fonts/tfm/public/etex/
%{_texdir}/texmf-dist/tex/plain/etex/

%files -n texlive-etex-doc
%license knuth.txt
%{_texdir}/texmf-dist/doc/etex/base/

%files -n texlive-etex-pkg
%{_texdir}/texmf-dist/tex/latex/etex-pkg/

%files -n texlive-etex-pkg-doc
%{_texdir}/texmf-dist/doc/latex/etex-pkg/

%files -n texlive-economic
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/economic/
%{_texdir}/texmf-dist/tex/latex/economic/

%files -n texlive-economic-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/bibtex/economic/

%files -n texlive-ean
%license gpl.txt
%{_texdir}/texmf-dist/tex/generic/ean/

%files -n texlive-ean-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/generic/ean/

%files -n texlive-ebgaramond
%license ofl.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/ebgaramond/
%{_texdir}/texmf-dist/fonts/map/dvips/ebgaramond/
%{_texdir}/texmf-dist/fonts/opentype/public/ebgaramond/
%{_texdir}/texmf-dist/fonts/tfm/public/ebgaramond/
%{_texdir}/texmf-dist/fonts/type1/public/ebgaramond/
%{_texdir}/texmf-dist/fonts/vf/public/ebgaramond/
%{_texdir}/texmf-dist/tex/latex/ebgaramond/

%files -n texlive-ebgaramond-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/ebgaramond/

%files -n texlive-ebgaramond-maths
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/ebgaramond-maths/
%{_texdir}/texmf-dist/fonts/map/dvips/ebgaramond-maths/
%{_texdir}/texmf-dist/fonts/tfm/public/ebgaramond-maths/
%{_texdir}/texmf-dist/tex/latex/ebgaramond-maths/

%files -n texlive-ebgaramond-maths-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/ebgaramond-maths/

%files -n texlive-ecc
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/ecc/
%{_texdir}/texmf-dist/fonts/tfm/public/ecc/

%files -n texlive-ecc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/ecc/

%files -n texlive-eco
%license gpl.txt
%{_texdir}/texmf-dist/fonts/tfm/public/eco/
%{_texdir}/texmf-dist/fonts/vf/public/eco/
%{_texdir}/texmf-dist/tex/latex/eco/

%files -n texlive-eco-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/eco/

%files -n texlive-eiad
%{_texdir}/texmf-dist/fonts/source/public/eiad/
%{_texdir}/texmf-dist/fonts/tfm/public/eiad/
%{_texdir}/texmf-dist/tex/latex/eiad/

%files -n texlive-eiad-doc
%{_texdir}/texmf-dist/doc/fonts/eiad/

%files -n texlive-eiad-ltx
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/eiad-ltx/
%{_texdir}/texmf-dist/tex/latex/eiad-ltx/

%files -n texlive-eiad-ltx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/eiad-ltx/

%files -n texlive-electrum
%{_texdir}/texmf-dist/fonts/afm/arkandis/electrum/
%{_texdir}/texmf-dist/fonts/enc/dvips/electrum/
%{_texdir}/texmf-dist/fonts/map/dvips/electrum/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/electrum/
%{_texdir}/texmf-dist/fonts/type1/arkandis/electrum/
%{_texdir}/texmf-dist/fonts/vf/arkandis/electrum/
%{_texdir}/texmf-dist/tex/latex/electrum/

%files -n texlive-electrum-doc
%{_texdir}/texmf-dist/doc/fonts/electrum/

%files -n texlive-elvish
%{_texdir}/texmf-dist/fonts/source/public/elvish/
%{_texdir}/texmf-dist/fonts/tfm/public/elvish/

%files -n texlive-elvish-doc
%{_texdir}/texmf-dist/doc/fonts/elvish/

%files -n texlive-epigrafica
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/epigrafica/
%{_texdir}/texmf-dist/fonts/enc/dvips/epigrafica/
%{_texdir}/texmf-dist/fonts/map/dvips/epigrafica/
%{_texdir}/texmf-dist/fonts/tfm/public/epigrafica/
%{_texdir}/texmf-dist/fonts/type1/public/epigrafica/
%{_texdir}/texmf-dist/fonts/vf/public/epigrafica/
%{_texdir}/texmf-dist/tex/latex/epigrafica/

%files -n texlive-epigrafica-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/epigrafica/

%files -n texlive-epsdice
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/epsdice/

%files -n texlive-epsdice-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/epsdice/

%files -n texlive-erewhon
%license ofl.txt
%{_datadir}/fonts/erewhon
%{_texdir}/texmf-dist/fonts/afm/public/erewhon/
%{_texdir}/texmf-dist/fonts/enc/dvips/erewhon/
%{_texdir}/texmf-dist/fonts/map/dvips/erewhon/
%{_texdir}/texmf-dist/fonts/opentype/public/erewhon/
%{_texdir}/texmf-dist/fonts/tfm/public/erewhon/
%{_texdir}/texmf-dist/fonts/type1/public/erewhon/
%{_texdir}/texmf-dist/fonts/vf/public/erewhon/
%{_texdir}/texmf-dist/tex/latex/erewhon/

%files -n texlive-erewhon-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/erewhon/

%files -n texlive-esrelation
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/map/dvips/esrelation/
%{_texdir}/texmf-dist/fonts/source/public/esrelation/
%{_texdir}/texmf-dist/fonts/tfm/public/esrelation/
%{_texdir}/texmf-dist/fonts/type1/public/esrelation/
%{_texdir}/texmf-dist/tex/latex/esrelation/

%files -n texlive-esrelation-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/esrelation/

%files -n texlive-esstix
%{_texdir}/texmf-dist/fonts/afm/esstix/
%{_texdir}/texmf-dist/fonts/map/dvips/esstix/
%{_texdir}/texmf-dist/fonts/tfm/public/esstix/
%{_texdir}/texmf-dist/fonts/type1/public/esstix/
%{_texdir}/texmf-dist/fonts/vf/public/esstix/
%{_texdir}/texmf-dist/tex/latex/esstix/

%files -n texlive-esstix-doc
%{_texdir}/texmf-dist/doc/fonts/esstix/

%files -n texlive-esvect
%license gpl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/esvect/
%{_texdir}/texmf-dist/fonts/source/public/esvect/
%{_texdir}/texmf-dist/fonts/tfm/public/esvect/
%{_texdir}/texmf-dist/fonts/type1/public/esvect/
%{_texdir}/texmf-dist/tex/latex/esvect/

%files -n texlive-esvect-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/esvect/

%files -n texlive-eulervm
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/tfm/public/eulervm/
%{_texdir}/texmf-dist/fonts/vf/public/eulervm/
%{_texdir}/texmf-dist/tex/latex/eulervm/

%files -n texlive-eulervm-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/eulervm/

%files -n texlive-euxm
%{_texdir}/texmf-dist/fonts/source/public/euxm/
%{_texdir}/texmf-dist/fonts/tfm/public/euxm/

%files -n texlive-ec
%{_texdir}/texmf-dist/fonts/source/jknappen/ec/
%{_texdir}/texmf-dist/fonts/tfm/jknappen/ec/

%files -n texlive-ec-doc
%{_texdir}/texmf-dist/doc/fonts/ec/

%files -n texlive-euro
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/euro/

%files -n texlive-euro-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/euro/

%files -n texlive-eurosym
%{_texdir}/texmf-dist/fonts/map/dvips/eurosym/
%{_texdir}/texmf-dist/fonts/source/public/eurosym/
%{_texdir}/texmf-dist/fonts/tfm/public/eurosym/
%{_texdir}/texmf-dist/fonts/type1/public/eurosym/
%{_texdir}/texmf-dist/tex/latex/eurosym/

%files -n texlive-eurosym-doc
%{_texdir}/texmf-dist/doc/fonts/eurosym/

%files -n texlive-edmac
%license gpl2.txt
%{_texdir}/texmf-dist/tex/generic/edmac/

%files -n texlive-edmac-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/edmac/

%files -n texlive-egameps
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/egameps/

%files -n texlive-egameps-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/egameps/

%files -n texlive-eijkhout
%license collection.txt
%{_texdir}/texmf-dist/tex/generic/eijkhout/

%files -n texlive-encxvlna
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/encxvlna/
%{_texdir}/texmf-dist/tex/plain/encxvlna/

%files -n texlive-encxvlna-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/encxvlna/

%files -n texlive-epigram
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/epigram/

%files -n texlive-epsf
%license pd.txt
%{_texdir}/texmf-dist/tex/generic/epsf/

%files -n texlive-epsf-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/generic/epsf/

%files -n texlive-ecltree
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ecltree/

%files -n texlive-ecltree-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ecltree/

%files -n texlive-edfnotes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/edfnotes/

%files -n texlive-edfnotes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/edfnotes/

%files -n texlive-ednotes
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ednotes/

%files -n texlive-ednotes-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ednotes/

%files -n texlive-eledform
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/eledform/

%files -n texlive-eledform-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/eledform/

%files -n texlive-eledmac
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/eledmac/

%files -n texlive-eledmac-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/eledmac/

%files -n texlive-expex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/expex/

%files -n texlive-expex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/expex/

%files -n texlive-ethiop
%license gpl.txt
%{_texdir}/texmf-dist/fonts/ofm/public/ethiop/
%{_texdir}/texmf-dist/fonts/ovf/public/ethiop/
%{_texdir}/texmf-dist/fonts/ovp/public/ethiop/
%{_texdir}/texmf-dist/fonts/source/public/ethiop/
%{_texdir}/texmf-dist/fonts/tfm/public/ethiop/
%{_texdir}/texmf-dist/omega/ocp/ethiop/
%{_texdir}/texmf-dist/omega/otp/ethiop/
%{_texdir}/texmf-dist/tex/latex/ethiop/

%files -n texlive-ethiop-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/ethiop/

%files -n texlive-ethiop-t1
%license gpl.txt
%{_texdir}/texmf-dist/fonts/map/dvips/ethiop-t1/
%{_texdir}/texmf-dist/fonts/type1/public/ethiop-t1/

%files -n texlive-ethiop-t1-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/ethiop-t1/

%files -n texlive-eskd
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/eskd/

%files -n texlive-eskd-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/eskd/

%files -n texlive-eskdx
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/eskdx/

%files -n texlive-eskdx-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/eskdx/

%files -n texlive-e-french
%license lppl1.3.txt
%{_texdir}/texmf-dist/makeindex/e-french/
%{_texdir}/texmf-dist/tex/generic/e-french/

%files -n texlive-e-french-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/e-french/

%files -n texlive-epslatex-fr-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/epslatex-fr/

%files -n texlive-einfuehrung-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/einfuehrung/

%files -n texlive-etdipa-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/etdipa/

%files -n texlive-etoolbox-de-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/etoolbox-de/

%files -n texlive-es-tex-faq-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/es-tex-faq/

%files -n texlive-eso-pic
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/eso-pic/

%files -n texlive-eso-pic-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/eso-pic/

%files -n texlive-euenc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/euenc/

%files -n texlive-euenc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/euenc/

%files -n texlive-euler
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/euler/

%files -n texlive-euler-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/euler/

%files -n texlive-extsizes
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/extsizes/

%files -n texlive-extsizes-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/extsizes/

%files -n texlive-eepic
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/eepic/

%files -n texlive-eepic-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/eepic/

%files -n texlive-epspdfconversion
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/epspdfconversion/

%files -n texlive-epspdfconversion-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/epspdfconversion/

%files -n texlive-esk
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/esk/

%files -n texlive-esk-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/esk/

%files -n texlive-ean13isbn
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ean13isbn/

%files -n texlive-ean13isbn-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ean13isbn/

%files -n texlive-easy
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/easy/

%files -n texlive-easy-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/easy/

%files -n texlive-easy-todo
%license apache2.txt
%{_texdir}/texmf-dist/tex/latex/easy-todo/

%files -n texlive-easy-todo-doc
%license apache2.txt
%{_texdir}/texmf-dist/doc/latex/easy-todo/

%files -n texlive-easyfig
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/easyfig/

%files -n texlive-easyfig-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/easyfig/

%files -n texlive-easylist
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/easylist/

%files -n texlive-easylist-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/easylist/

%files -n texlive-easyreview
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/easyreview/

%files -n texlive-easyreview-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/easyreview/

%files -n texlive-ebezier
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ebezier/

%files -n texlive-ebezier-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ebezier/

%files -n texlive-ecclesiastic
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ecclesiastic/

%files -n texlive-ecclesiastic-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ecclesiastic/

%files -n texlive-ecv
%{_texdir}/texmf-dist/tex/latex/ecv/

%files -n texlive-ecv-doc
%{_texdir}/texmf-dist/doc/latex/ecv/

%files -n texlive-ed
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ed/

%files -n texlive-ed-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ed/

%files -n texlive-edmargin
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/edmargin/

%files -n texlive-edmargin-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/edmargin/

%files -n texlive-eemeir
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/eemeir/

%files -n texlive-eemeir-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/eemeir/

%files -n texlive-efbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/efbox/

%files -n texlive-efbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/efbox/

%files -n texlive-egplot
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/egplot/

%files -n texlive-egplot-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/egplot/

%files -n texlive-elements
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/elements/

%files -n texlive-elements-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/elements/

%files -n texlive-ellipsis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ellipsis/

%files -n texlive-ellipsis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ellipsis/

%files -n texlive-elmath
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/elmath/

%files -n texlive-elmath-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/elmath/

%files -n texlive-elocalloc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/elocalloc/

%files -n texlive-elocalloc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/elocalloc/

%files -n texlive-elpres
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/elpres/

%files -n texlive-elpres-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/elpres/

%files -n texlive-elzcards
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/elzcards/

%files -n texlive-elzcards-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/elzcards/

%files -n texlive-emarks
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/emarks/

%files -n texlive-emarks-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/emarks/

%files -n texlive-embedall
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/embedall/

%files -n texlive-embedall-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/embedall/

%files -n texlive-embrac
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/embrac/

%files -n texlive-embrac-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/embrac/

%files -n texlive-emptypage
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/emptypage/

%files -n texlive-emptypage-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/emptypage/

%files -n texlive-emulateapj
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/emulateapj/

%files -n texlive-emulateapj-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/emulateapj/

%files -n texlive-endfloat
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/endfloat/

%files -n texlive-endfloat-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/endfloat/

%files -n texlive-endheads
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/endheads/

%files -n texlive-endheads-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/endheads/

%files -n texlive-endnotes
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/endnotes/

%files -n texlive-endnotes-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/endnotes/

%files -n texlive-engpron
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/engpron/

%files -n texlive-engpron-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/engpron/

%files -n texlive-engrec
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/engrec/

%files -n texlive-engrec-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/engrec/

%files -n texlive-enotez
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/enotez/

%files -n texlive-enotez-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/enotez/

%files -n texlive-enumitem
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/enumitem/

%files -n texlive-enumitem-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/enumitem/

%files -n texlive-enumitem-zref
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/enumitem-zref/

%files -n texlive-enumitem-zref-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/enumitem-zref/

%files -n texlive-envbig
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/envbig/

%files -n texlive-envbig-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/envbig/

%files -n texlive-environ
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/environ/

%files -n texlive-environ-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/environ/

%files -n texlive-envlab
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/envlab/

%files -n texlive-envlab-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/envlab/

%files -n texlive-epigraph
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/epigraph/

%files -n texlive-epigraph-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/epigraph/

%files -n texlive-epiolmec
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/epiolmec/
%{_texdir}/texmf-dist/fonts/tfm/public/epiolmec/
%{_texdir}/texmf-dist/tex/latex/epiolmec/

%files -n texlive-epiolmec-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/epiolmec/

%files -n texlive-eqell
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/eqell/

%files -n texlive-eqell-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/eqell/

%files -n texlive-eqlist
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/eqlist/

%files -n texlive-eqlist-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/eqlist/

%files -n texlive-eqname
%{_texdir}/texmf-dist/tex/latex/eqname/

%files -n texlive-eqparbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/eqparbox/

%files -n texlive-eqparbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/eqparbox/

%files -n texlive-errata
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/errata/

%files -n texlive-errata-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/errata/

%files -n texlive-esami
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/esami/

%files -n texlive-esami-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/esami/

%files -n texlive-esdiff
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/esdiff/

%files -n texlive-esdiff-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/esdiff/

%files -n texlive-esint
%license pd.txt
%{_texdir}/texmf-dist/fonts/source/public/esint/
%{_texdir}/texmf-dist/fonts/tfm/public/esint/
%{_texdir}/texmf-dist/tex/latex/esint/

%files -n texlive-esint-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/esint/

%files -n texlive-esint-type1
%license pd.txt
%{_texdir}/texmf-dist/dvips/esint-type1/
%{_texdir}/texmf-dist/fonts/map/dvips/esint-type1/
%{_texdir}/texmf-dist/fonts/type1/public/esint-type1/
%{_texdir}/texmf-dist/tex/plain/esint-type1/

%files -n texlive-esint-type1-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/esint-type1/

%files -n texlive-etaremune
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/etaremune/

%files -n texlive-etaremune-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/etaremune/

%files -n texlive-etextools
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/etextools/

%files -n texlive-etextools-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/etextools/

%files -n texlive-etoc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/etoc/

%files -n texlive-etoc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/etoc/

%files -n texlive-etoolbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/etoolbox/

%files -n texlive-etoolbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/etoolbox/

%files -n texlive-eukdate
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/eukdate/

%files -n texlive-eukdate-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/eukdate/

%files -n texlive-europasscv
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/europasscv/

%files -n texlive-europasscv-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/europasscv/

%files -n texlive-europecv
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/europecv/

%files -n texlive-europecv-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/europecv/

%files -n texlive-everyhook
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/everyhook/

%files -n texlive-everyhook-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/everyhook/

%files -n texlive-everypage
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/everypage/

%files -n texlive-everypage-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/everypage/

%files -n texlive-exam
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/exam/

%files -n texlive-exam-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/exam/

%files -n texlive-exam-n
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/exam-n/

%files -n texlive-exam-n-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/exam-n/

%files -n texlive-examdesign
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/examdesign/

%files -n texlive-examdesign-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/examdesign/

%files -n texlive-example
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/example/

%files -n texlive-examplep
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/examplep/

%files -n texlive-examplep-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/examplep/

%files -n texlive-excludeonly
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/excludeonly/

%files -n texlive-excludeonly-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/excludeonly/

%files -n texlive-exercise
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/exercise/

%files -n texlive-exercise-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/exercise/

%files -n texlive-exp-testopt
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/exp-testopt/

%files -n texlive-exp-testopt-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/exp-testopt/

%files -n texlive-expdlist
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/expdlist/

%files -n texlive-expdlist-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/expdlist/

%files -n texlive-export
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/export/

%files -n texlive-export-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/export/

%files -n texlive-exsheets
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/exsheets/

%files -n texlive-exsheets-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/exsheets/

%files -n texlive-exsol
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/exsol/

%files -n texlive-exsol-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/exsol/

%files -n texlive-extract
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/extract/

%files -n texlive-extract-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/extract/

%files -n texlive-enigma
%license bsd.txt
%{_texdir}/texmf-dist/scripts/context/lua/third/enigma/
%{_texdir}/texmf-dist/tex/context/third/enigma/
%{_texdir}/texmf-dist/tex/generic/enigma/
%{_texdir}/texmf-dist/tex/latex/enigma/
%{_texdir}/texmf-dist/tex/plain/enigma/

%files -n texlive-enigma-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/context/third/enigma/

%files -n texlive-ebproof
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ebproof/

%files -n texlive-ebproof-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ebproof/

%files -n texlive-eqnarray
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/eqnarray/

%files -n texlive-eqnarray-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/eqnarray/

%files -n texlive-extarrows
%license lgpl2.1.txt
%{_texdir}/texmf-dist/tex/latex/extarrows/

%files -n texlive-extarrows-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/latex/extarrows/

%files -n texlive-extpfeil
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/extpfeil/

%files -n texlive-extpfeil-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/extpfeil/

%files -n texlive-emp
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/emp/

%files -n texlive-emp-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/emp/

%files -n texlive-epsincl
%license pd.txt
%{_texdir}/texmf-dist/metapost/epsincl/

%files -n texlive-epsincl-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/metapost/epsincl/

%files -n texlive-expressg
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/expressg/

%files -n texlive-expressg-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/expressg/

%files -n texlive-exteps
%license gpl.txt
%{_texdir}/texmf-dist/metapost/exteps/

%files -n texlive-exteps-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/metapost/exteps/

%files -n texlive-epsf-dvipdfmx
%license pd.txt
%{_texdir}/texmf-dist/tex/plain/epsf-dvipdfmx/

%files -n texlive-epsf-dvipdfmx-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/plain/epsf-dvipdfmx/

%files -n texlive-ebook
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/ebook/

%files -n texlive-ebook-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/ebook/

%files -n texlive-ebsthesis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ebsthesis/

%files -n texlive-ebsthesis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ebsthesis/

%files -n texlive-ejpecp
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/ejpecp/

%files -n texlive-ejpecp-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/ejpecp/

%files -n texlive-ekaia
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/ekaia/

%files -n texlive-ekaia-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/ekaia/

%files -n texlive-elbioimp
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/elbioimp/

%files -n texlive-elbioimp-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/elbioimp/

%files -n texlive-elsarticle
%license lppl1.2.txt
%{_texdir}/texmf-dist/bibtex/bst/elsarticle/
%{_texdir}/texmf-dist/tex/latex/elsarticle/

%files -n texlive-elsarticle-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/elsarticle/

%files -n texlive-elteikthesis
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/elteikthesis/

%files -n texlive-elteikthesis-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/elteikthesis/

%files -n texlive-erdc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/erdc/

%files -n texlive-erdc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/erdc/

%files -n texlive-estcpmm
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/estcpmm/

%files -n texlive-estcpmm-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/estcpmm/

%files -n texlive-eltex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/eltex/

%files -n texlive-eltex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/eltex/

%files -n texlive-endiagram
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/endiagram/

%files -n texlive-endiagram-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/endiagram/

%files -n texlive-engtlc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/engtlc/

%files -n texlive-engtlc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/engtlc/

%files -n texlive-ecobiblatex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ecobiblatex/

%files -n texlive-ecobiblatex
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ecobiblatex/

%files -n texlive-econometrics-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/econometrics/

%files -n texlive-econometrics
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/econometrics/

%files -n texlive-einfuehrung2-doc
%license lppl.txt
%{_texdir}/texmf-dist/doc/latex/einfuehrung2/

%files -n texlive-ellipse-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ellipse/

%files -n texlive-ellipse
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ellipse/

%files -n texlive-emisa-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/emisa/

%files -n texlive-emisa
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/emisa/

%files -n texlive-exercises-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/exercises/

%files -n texlive-exercises
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/exercises/

%files -n texlive-easyformat
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/easyformat/
%{_texdir}/texmf-dist/tex/latex/easyformat/

%files -n texlive-ecgdraw
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/ecgdraw/
%{_texdir}/texmf-dist/tex/latex/ecgdraw/

%files -n texlive-endofproofwd
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/endofproofwd/
%{_texdir}/texmf-dist/tex/latex/endofproofwd/

%files -n texlive-eqnalign
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/eqnalign/
%{_texdir}/texmf-dist/tex/latex/eqnalign/

%files -n texlive-eulerpx
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/fonts/eulerpx/
%{_texdir}/texmf-dist/tex/latex/eulerpx/

%files -n texlive-emf
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/emf/
%doc %{_texdir}/texmf-dist/doc/latex/emf/

%files -n texlive-endnotesj
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/endnotesj/
%doc %{_texdir}/texmf-dist/doc/latex/endnotesj/

%files -n texlive-eqnnumwarn
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/eqnnumwarn/
%doc %{_texdir}/texmf-dist/doc/latex/eqnnumwarn/

%files -n texlive-erw-l3
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/erw-l3/
%doc %{_texdir}/texmf-dist/doc/latex/erw-l3/

%files -n texlive-etsvthor
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/etsvthor/
%doc %{_texdir}/texmf-dist/doc/latex/etsvthor/

%files -n texlive-euro-ce
%license bsd.txt
%{_texdir}/texmf-dist/fonts/source/public/euro-ce/
%{_texdir}/texmf-dist/fonts/tfm/public/euro-ce/
%doc %{_texdir}/texmf-dist/doc/fonts/euro-ce/

%files -n texlive-exercisebank
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/exercisebank/
%doc %{_texdir}/texmf-dist/doc/latex/exercisebank/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init

#!/usr/bin/env python3
r"""Assemble the monograph from the paper sources.

Reads the foundational paper and Papers I-XXV, and writes

    chapters/NN-<tag>.tex     one chapter per paper
    generated/chapters.tex    the \part / \input skeleton, in book order
    generated/macros.tex      the union of all paper macros
    generated/guide.tex       chapter <-> paper correspondence table
    generated/dependencies.tex  prerequisite chapters, from the citation graph
    generated/bibliography.tex  merged bibliography

What is transformed, mechanically and reversibly:
  * labels/refs are prefixed by the chapter tag (no label collisions);
  * self-citations [Main, Thm. 3.6] become [Ch. 1, Thm. 3.6] with \ref;
  * the five clashing bibliography keys are renamed, two duplicates merged;
  * per-chapter \tableofcontents lines are dropped;
  * each chapter opens with the paper's abstract as a summary.

Nothing in the mathematical text is altered.  Run from monograph/.
"""
import re, pathlib, collections, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(__file__).resolve().parent
(OUT / "chapters").mkdir(exist_ok=True)
(OUT / "generated").mkdir(exist_ok=True)

# ---------------------------------------------------------------- book plan
# (tag, directory) in book order; tags are the series numerals.
PARTS = [
    ("The classification", [("Main", "paper")]),
    ("Structure of the abelian systems",
        [("I", "papers/I-type-spectrum"), ("II", "papers/II-structure"),
         ("III", "papers/III-invariants"), ("XXXIX", "papers/XXXIX-cohomology"), ("IV", "papers/IV-metric"), ("XXIX", "papers/XXIX-wasserstein"), ("XXXIII", "papers/XXXIII-coupling"), ("XXXVII", "papers/XXXVII-cone-geometry"), ("XXX", "papers/XXX-affine-ktheory"), ("XXXI", "papers/XXXI-rayclass"), ("XXXII", "papers/XXXII-descent"), ("XXXVIII", "papers/XXXVIII-inert-ktheory"),
         ("V", "papers/V-free")]),
    ("Towards non-abelian systems",
        [("VI", "papers/VI-nonabelian"), ("VII", "papers/VII-galois-groupoid"),
         ("XXVII", "papers/XXVII-nonabelian-groupoids"),
         ("XXXIV", "papers/XXXIV-bottleneck"),
         ("XXXVI", "papers/XXXVI-angular-transport")]),
    ("Rigidity and reconstruction",
        [("IX", "papers/IX-rigidity"), ("XIII", "papers/XIII-equivariant"),
         ("XIV", "papers/XIV-equalnorm"), ("XV", "papers/XV-spectral"),
         ("XVI", "papers/XVI-transport")]),
    ("Non-commutative semigroups and $GL_2$",
        [("X", "papers/X-semigroup-search"), ("XI", "papers/XI-C4"),
         ("XII", "papers/XII-mismatch"), ("XXI", "papers/XXI-GL2"),
         ("XXVIII", "papers/XXVIII-spectral-gap")]),
    ("Geometric and function-field analogues",
        [("VIII", "papers/VIII-arithmetic-topology"),
         ("XVII", "papers/XVII-function-fields"),
         ("XVIII", "papers/XVIII-equivariant-kirchberg"),
         ("XIX", "papers/XIX-isogeny"), ("XX", "papers/XX-twin-curves")]),
    ("$p$-adic aspects",
        [("XXII", "papers/XXII-iwasawa"), ("XXIII", "papers/XXIII-leopoldt")]),
    ("Families of primes",
        [("XXIV", "papers/XXIV-sieve"), ("XXV", "papers/XXV-sato-tate"), ("XXXV", "papers/XXXV-twin-regime")]),
]
ORDER = [t for _, chs in PARTS for t, _ in chs]
DIR = {t: d for _, chs in PARTS for t, d in chs}

# self-citation keys -> chapter tags
SELF = {"Main": "Main"}
for t in ORDER[1:]:
    SELF["Series" + t] = t
    SELF["Paper" + t] = t

# bibliography key repairs: (tag, old key) -> new key
RENAME = {
    ("VI", "CM"): "ConnesMarcolli2006", ("XVI", "CM"): "ConnesMoscovici",
    ("XXI", "CM"): "ConnesMarcolliBook",
    ("I", "CT"): "ConnesTakesaki", ("III", "CT"): "ConnesThom",
    ("XIX", "Howe"): "HoweWeil", ("XX", "Howe"): "HowePP",
    ("VII", "Renault"): "RenaultGroupoid",
}
MERGE = {"Neu": "Neukirch", "Rieffel99": "Rieffel", "Neshveyev": "Nesh13"}

# ---------------------------------------------------------------- helpers
def balanced(s, i):
    """s[i] == '{'; return index just past the matching '}'."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{" and (j == 0 or s[j-1] != "\\"):
            depth += 1
        elif s[j] == "}" and s[j-1] != "\\":
            depth -= 1
            if depth == 0:
                return j + 1
    raise ValueError("unbalanced braces")

def parse_newcommands(pre):
    """Return list of (name, nargs, definition) from a preamble."""
    out = []
    for m in re.finditer(r"\\newcommand\{(\\[A-Za-z]+)\}(\[(\d)\])?", pre):
        name, nargs = m.group(1), m.group(3)
        i = m.end()
        j = balanced(pre, i)
        out.append((name, nargs, pre[i+1:j-1]))
    return out

def read_paper(tag):
    src = (ROOT / DIR[tag]).glob("*.tex")
    src = [p for p in src if "note" not in p.name]
    assert len(src) == 1, (tag, src)
    s = src[0].read_text()
    pre, rest = s.split("\\begin{document}", 1)
    m = re.search(r"\\title\[([^\]]*)\]\{(.*?)\}\s*\n\\author", pre, flags=re.S)
    short, long = m.group(1), m.group(2)
    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", rest, flags=re.S).group(1)
    body = rest.split("\\maketitle", 1)[1].split("\\begin{thebibliography}", 1)[0]
    bib = re.search(r"\\begin\{thebibliography\}\{\w+\}(.*?)\\end\{thebibliography\}", rest, flags=re.S).group(1)
    bibitems = [(it.group(1), re.sub(r"\s+", " ", it.group(2)).strip())
                for it in re.finditer(r"\\bibitem\{([^}]*)\}(.*?)(?=\\bibitem|\Z)", bib, flags=re.S)]
    pages = None
    pdf = list((ROOT / DIR[tag]).glob(src[0].stem + ".pdf"))
    return dict(tag=tag, file=src[0], short=short, long=long, abstract=abstract.strip(),
                body=body, bibitems=bibitems, macros=parse_newcommands(pre), pre=pre)

def chapter_title(p):
    long = p["long"]
    m = re.match(r"Localized Bost--Connes systems [IVX]+:\\\\\s*(.*)", long, flags=re.S)
    if m:
        long = m.group(1).strip()
        long = long[0].upper() + long[1:]
    return long.replace("\n", " ")

def transform(p):
    tag = p["tag"]
    t = p["body"]
    t = re.sub(r"^\s*\\tableofcontents\s*$", "", t, flags=re.M)
    # labels and references
    for cmd in ("label", "ref", "eqref", "pageref"):
        t = re.sub(r"\\" + cmd + r"\{([^}]*)\}", lambda m: "\\" + cmd + "{" + tag + ":" + m.group(1) + "}", t)
    # citations
    def cite(m):
        opt, keys = m.group(1), [k.strip() for k in m.group(2).split(",")]
        selfs = [k for k in keys if k in SELF]
        exts = [k for k in keys if k not in SELF]
        exts = [RENAME.get((tag, k), MERGE.get(k, k)) for k in exts]
        parts = []
        if selfs:
            refs = ", ".join("\\ref{ch:%s}" % SELF[k] for k in selfs)
            if len(selfs) == 4 and selfs == ["SeriesI", "SeriesII", "SeriesIII", "SeriesIV"]:
                refs = "\\ref{ch:I}--\\ref{ch:IV}"
            head = ("Ch.~" if len(selfs) == 1 else "Ch.~") + refs
            parts.append("[" + head + (", " + opt if opt else "") + "]")
            if exts:
                parts.append("\\cite{" + ",".join(exts) + "}")
        else:
            parts.append("\\cite" + ("[" + opt + "]" if opt else "") + "{" + ",".join(exts) + "}")
        return " ".join(parts)
    t = re.sub(r"\\cite(?:\[([^\]]*)\])?\{([^}]*)\}", cite, t)
    # ---- monograph prose pass: series boilerplate out, "Paper N" -> chapter refs
    # drop policy sentences that only make sense for standalone papers
    t = re.sub(r"[^.!?]*unpublished companions?[^.!?]*\.\s*", "", t)
    t = re.sub(r"[^.!?]*cited by DOI[^.!?]*\.\s*", "", t)
    t = re.sub(r"[^.!?]*no unpublished companion[^.!?]*\.\s*", "", t)
    t = re.sub(r"\\emph\{The series\.\}.*?\n\n", "", t, flags=re.S)
    ok = set(ORDER)
    def chref(n): return "Chapter~\\ref{ch:%s}" % n
    # ranges: Papers IX--XII
    def prange(m):
        a,b = m.group(1), m.group(2)
        return "Chapters~\\ref{ch:%s}--\\ref{ch:%s}" % (a,b) if a in ok and b in ok else m.group(0)
    t = re.sub(r"Papers ([IVX]+)--([IVX]+)", prange, t)
    # lists: Papers A, B and C
    def plist(m):
        nums = re.findall(r"[IVX]+", m.group(1))
        if not all(n in ok for n in nums): return m.group(0)
        refs = ["\\ref{ch:%s}" % n for n in nums]
        if len(refs) == 1: return "Chapter~" + refs[0]
        return "Chapters~" + ", ".join(refs[:-1]) + " and " + refs[-1]
    t = re.sub(r"Papers ((?:[IVX]+)(?:,\s*[IVX]+)*(?:,?\s+and\s+[IVX]+))", plist, t)
    # singular
    t = re.sub(r"Paper ([IVX]+)\b", lambda m: chref(m.group(1)) if m.group(1) in ok else m.group(0), t)
    # headings must not carry \ref (uppercased running heads break the label): short title
    t = re.sub(r"\\section\{([^{}]*Chapter~\\ref\{ch:([IVX]+)\}[^{}]*)\}",
               lambda m: "\\section[" + re.sub(r"Chapter~\\ref\{ch:[IVX]+\}", "Chapter " + m.group(2), m.group(1)) + "]{" + m.group(1) + "}", t)
    # cleanups: duplicated ref after cite conversion; "of the/this series" after a ref
    t = re.sub(r"Chapter~(\\ref\{ch:[IVX]+\})\s*\[Ch\.~\1\]", r"Chapter~\1", t)
    t = re.sub(r"(\\ref\{ch:[IVX]+\}) of (?:the|this) series", r"\1", t)
    t = re.sub(r"(\\ref\{ch:[IVX]+\}\]?) of the present series", r"\1", t)
    return t

# ---------------------------------------------------------------- read all
papers = {tag: read_paper(tag) for tag in ORDER}

# global macro table: first definition wins; chapters redefine what differs
GLOBAL = {}
for tag in ORDER:
    for name, nargs, defn in papers[tag]["macros"]:
        GLOBAL.setdefault(name, (nargs, defn))

with open(OUT / "generated/macros.tex", "w") as f:
    f.write("%% union of the macros of all papers (generated by assemble.py)\n")
    for name, (nargs, defn) in sorted(GLOBAL.items()):
        f.write("\\newcommand{%s}%s{%s}\n" % (name, "[%s]" % nargs if nargs else "", defn))

# ---------------------------------------------------------------- chapters
num = 0
skeleton = []
guide = []
for part, chs in PARTS:
    skeleton.append("\\part{%s}\n" % part)
    for tag, d in chs:
        num += 1
        p = papers[tag]
        title = chapter_title(p)
        fname = "chapters/%02d-%s.tex" % (num, tag)
        local = ["\\renewcommand{%s}%s{%s}" % (n, "[%s]" % a if a else "", dfn)
                 for n, a, dfn in p["macros"] if GLOBAL[n] != (a, dfn)]
        origin = ("the foundational paper of the series" if tag == "Main"
                  else "Paper %s of the series" % tag)
        with open(OUT / fname, "w") as f:
            f.write("%% generated from %s -- edit the paper, then rerun assemble.py\n" % p["file"].relative_to(ROOT))
            f.write("\\chapter[%s]{%s}\\label{ch:%s}\n" % (p["short"], title, tag))
            if local:
                f.write("\n".join(local) + "\n")
            f.write("\\chapterorigin{This chapter is %s (\\texttt{%s/}).}\n" % (origin, DIR[tag]))
            f.write("\\begin{summary}\n%s\n\\end{summary}\n" % transform(dict(p, body=p["abstract"])))
            f.write(transform(p))
        skeleton.append("\\input{%s}\n" % fname[:-4])
        guide.append((num, tag, title, DIR[tag]))

with open(OUT / "generated/chapters.tex", "w") as f:
    f.writelines(skeleton)

with open(OUT / "generated/guide.tex", "w") as f:
    f.write("\\begin{center}\\footnotesize\n\\begin{longtable}{rlp{7.4cm}p{4.6cm}}\n\\hline\nCh. & Paper & Title & Source directory\\\\\n\\hline\n\\endhead\n")
    for n, tag, title, d in guide:
        lab = "---" if tag == "Main" else tag
        f.write("%d & %s & %s & \\nolinkurl{%s/}\\\\\n" % (n, lab, title.replace("\\\\", " "), d))
    f.write("\\hline\n\\end{longtable}\n\\end{center}\n")

# dependency table from the citation graph
deps = collections.defaultdict(set)
for tag in ORDER:
    for m in re.finditer(r"\\cite(?:\[[^\]]*\])?\{([^}]*)\}", papers[tag]["body"]):
        for k in m.group(1).split(","):
            k = k.strip()
            if k in SELF and SELF[k] != tag:
                deps[tag].add(SELF[k])
# augment deps with prose chapter references from the assembled chapter files
for n, tag, title, d in guide:
    body = (OUT / ("chapters/%02d-%s.tex" % (n, tag))).read_text()
    for m2 in re.finditer(r"\\ref\{ch:([A-Za-z]+)\}", body):
        c = m2.group(1)
        if c in DIR and c != tag:
            deps[tag].add(c)
with open(OUT / "generated/dependencies.tex", "w") as f:
    f.write("\\begin{center}\\small\n\\begin{tabular}{rl}\n\\hline\nChapter & cites (chapters)\\\\\n\\hline\n")
    for n, tag, title, d in guide:
        cited = sorted(deps[tag], key=ORDER.index)
        f.write("%d & %s\\\\\n" % (n, ", ".join("\\ref{ch:%s}" % c for c in cited) or "---"))
    f.write("\\hline\n\\end{tabular}\n\\end{center}\n")

# ---------------------------------------------------------------- bibliography
entries = collections.defaultdict(list)   # global key -> [texts]
for tag in ORDER:
    for k, text in papers[tag]["bibitems"]:
        if k in SELF:
            continue
        gk = RENAME.get((tag, k), MERGE.get(k, k))
        entries[gk].append(text)

def author_sort_key(text):
    first = text.split(",")[0]
    first = re.sub(r"\\['\"^`~]", "", first)
    surname = first.split()[-1] if first.split() else first
    return surname.lower()

with open(OUT / "generated/bibliography.tex", "w") as f:
    f.write("\\begin{thebibliography}{999}\n")
    for gk, texts in sorted(entries.items(), key=lambda kv: (author_sort_key(kv[1][0]), kv[0])):
        text = max(texts, key=len)   # keep the most complete variant
        f.write("\\bibitem{%s} %s\n" % (gk, text))
    f.write("\\end{thebibliography}\n")

print("assembled %d chapters, %d bibliography entries, %d macros" % (num, len(entries), len(GLOBAL)))

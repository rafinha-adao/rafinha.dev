#!/usr/bin/env python3
"""
Gera curriculo.pdf e curriculo.png a partir de curriculo.html.

Uso:
    python3 build.py                # gera PDF + PNG
    python3 build.py --pdf          # só PDF
    python3 build.py --png          # só PNG (gera PDF temporário)

Requisitos:
    pip install weasyprint
    poppler-utils (pdftoppm) — para o PNG
        Ubuntu/Debian: sudo apt install poppler-utils
        macOS:         brew install poppler
        Windows:       https://github.com/oschwartz10612/poppler-windows
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
HTML = HERE / "curriculo.html"
PDF = HERE / "curriculo.pdf"
PNG = HERE / "curriculo.png"
DPI = 200  # resolução do PNG


def build_pdf() -> None:
    from weasyprint import HTML as WeasyHTML

    WeasyHTML(filename=str(HTML)).write_pdf(str(PDF))
    print(f"✔ PDF gerado: {PDF}")


def build_png() -> None:
    # pdftoppm gera curriculo-1.png; renomeamos para curriculo.png
    subprocess.run(
        ["pdftoppm", "-png", "-r", str(DPI), str(PDF), str(HERE / "curriculo")],
        check=True,
    )
    tmp = HERE / "curriculo-1.png"
    if tmp.exists():
        tmp.replace(PNG)
    print(f"✔ PNG gerado: {PNG}")




def enrich_pdf() -> None:
    """Metadados XMP (padrão moderno) + idioma do documento."""
    import pikepdf

    with pikepdf.open(PDF, allow_overwriting_input=True) as pdf:
        pdf.Root.Lang = pikepdf.String("pt-BR")
        with pdf.open_metadata() as meta:
            meta["dc:title"] = "Rafael de Oliveira Adão · Currículo · Desenvolvedor Full Stack"
            meta["dc:creator"] = ["Rafael de Oliveira Adão"]
            meta["dc:description"] = (
                "Currículo de Rafael de Oliveira Adão, desenvolvedor full stack. "
                "Stack: Next.js, React, TypeScript, Node.js, Supabase, PostgreSQL, "
                "AWS e IA (Claude, MCP, agentes e automações). Criador do NoShorts. "
                "Contato: rafaeldeoliveiraadao@gmail.com · rafinha.dev"
            )
            meta["dc:subject"] = [
                "desenvolvedor full stack", "full stack developer", "desenvolvedor web",
                "Next.js", "React", "TypeScript", "Node.js", "Supabase", "PostgreSQL",
                "AWS", "IA", "Claude", "MCP", "automações", "NoShorts", "rafinha.dev",
            ]
            meta["dc:language"] = ["pt-BR"]
            meta["pdf:Keywords"] = ", ".join(meta["dc:subject"])
        pdf.save(PDF)
    print(f"✔ XMP e idioma gravados: {PDF}")


if __name__ == "__main__":
    args = sys.argv[1:]
    only_pdf = "--pdf" in args
    only_png = "--png" in args

    build_pdf()
    enrich_pdf()
    if not only_pdf:
        build_png()
        if only_png:
            PDF.unlink(missing_ok=True)

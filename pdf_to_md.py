#!/usr/bin/env python3
"""
Extract text content from PDF files in the /files directory
and save as .md files in the /refs directory.
"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import fitz  # PyMuPDF


REPO_ROOT = Path(__file__).parent
FILES_DIR = REPO_ROOT / "files"
REFS_DIR = REPO_ROOT / "refs"
RDF_FILE = REPO_ROOT / "Autonomous Driving.rdf"


def parse_rdf_metadata(rdf_path: Path) -> dict:
    """Parse the Zotero RDF file to extract metadata for each paper."""
    metadata = {}
    try:
        tree = ET.parse(rdf_path)
        root = tree.getroot()
    except Exception as e:
        print(f"Warning: Could not parse RDF file: {e}")
        return metadata

    ns = {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "z": "http://www.zotero.org/namespaces/export#",
        "dc": "http://purl.org/dc/elements/1.1/",
        "foaf": "http://xmlns.com/foaf/0.1/",
        "bib": "http://purl.org/net/biblio#",
        "link": "http://purl.org/rss/1.0/modules/link/",
        "dcterms": "http://purl.org/dc/terms/",
        "prism": "http://prismstandard.org/namespaces/1.2/basic/",
    }

    # Build a map from attachment about-id -> relative PDF path
    attachment_to_resource = {}
    for attachment in root.findall("z:Attachment", ns):
        about = attachment.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
        resource_elem = attachment.find("rdf:resource", ns)
        if resource_elem is not None:
            resource_path = resource_elem.get(
                "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"
            )
            if resource_path and resource_path.endswith(".pdf"):
                attachment_to_resource[about] = resource_path

    # Iterate over all direct children to handle different paper element types
    # (rdf:Description, bib:BookSection, bib:Article, etc.)
    for desc in root:
        title_elem = desc.find("dc:title", ns)
        abstract_elem = desc.find("dcterms:abstract", ns)
        date_elem = desc.find("dc:date", ns)

        title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""
        abstract = abstract_elem.text.strip() if abstract_elem is not None and abstract_elem.text else ""
        date = date_elem.text.strip() if date_elem is not None and date_elem.text else ""

        # Collect authors
        authors = []
        for person in desc.findall(".//foaf:Person", ns):
            surname = person.find("foaf:surname", ns)
            given = person.find("foaf:givenName", ns)
            if surname is not None and surname.text:
                name = surname.text.strip()
                if given is not None and given.text:
                    name = given.text.strip() + " " + name
                authors.append(name)

        # Collect linked attachment references
        for link_elem in desc.findall("link:link", ns):
            ref = link_elem.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource")
            if ref and ref in attachment_to_resource:
                pdf_rel_path = attachment_to_resource[ref]
                meta = {
                    "title": title,
                    "authors": authors,
                    "abstract": abstract,
                    "date": date,
                }
                metadata[pdf_rel_path] = meta

    return metadata


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract text from a PDF using PyMuPDF."""
    try:
        doc = fitz.open(str(pdf_path))
        pages_text = []
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text("text")
            if text.strip():
                pages_text.append(f"<!-- Page {page_num} -->\n{text.strip()}")
        doc.close()
        return "\n\n".join(pages_text)
    except Exception as e:
        return f"Error extracting text: {e}"


def clean_text(text: str) -> str:
    """Clean up extracted PDF text."""
    # Normalize multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def build_markdown(pdf_path: Path, metadata: dict) -> str:
    """Build a markdown document for a PDF file."""
    # Try to look up metadata using relative path key (posix-style)
    rel_key = pdf_path.relative_to(REPO_ROOT).as_posix()
    meta = metadata.get(rel_key, {})

    lines = []

    # Title
    title = meta.get("title") or pdf_path.stem
    lines.append(f"# {title}\n")

    # Authors
    authors = meta.get("authors", [])
    if authors:
        lines.append(f"**Authors:** {', '.join(authors)}\n")

    # Date
    date = meta.get("date", "")
    if date:
        lines.append(f"**Date:** {date}\n")

    # Abstract
    abstract = meta.get("abstract", "")
    if abstract:
        lines.append(f"\n## Abstract\n\n{abstract}\n")

    lines.append("\n---\n")
    lines.append("\n## Full Text\n")

    # Extract and append full PDF text
    raw_text = extract_text_from_pdf(pdf_path)
    cleaned = clean_text(raw_text)
    lines.append(cleaned)

    return "\n".join(lines)


def main():
    REFS_DIR.mkdir(exist_ok=True)

    print(f"Parsing RDF metadata from: {RDF_FILE}")
    metadata = parse_rdf_metadata(RDF_FILE)
    print(f"Found metadata for {len(metadata)} attachments.")

    pdf_files = sorted(FILES_DIR.rglob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files.\n")

    for pdf_path in pdf_files:
        # Derive output filename from the PDF stem
        out_name = pdf_path.stem + ".md"
        out_path = REFS_DIR / out_name

        print(f"Processing: {pdf_path.relative_to(REPO_ROOT)}")
        md_content = build_markdown(pdf_path, metadata)

        out_path.write_text(md_content, encoding="utf-8")
        print(f"  -> Saved: refs/{out_name}")

    print(f"\nDone. {len(pdf_files)} markdown files written to {REFS_DIR}")


if __name__ == "__main__":
    main()

"""Dependency-free checks for missing files, broken anchors and public content."""
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

PUBLIC = Path(__file__).resolve().parents[1] / "public"


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.references, self.headings = [], [], []
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.references.append(attrs[key])
        if tag == "h1":
            self.headings.append(tag)


class SiteChecks(unittest.TestCase):
    def test_pages_and_local_references(self):
        for file in PUBLIC.glob("*.html"):
            with self.subTest(file=file.name):
                page = Page(file.read_text())
                self.assertEqual(len(page.ids), len(set(page.ids)))
                self.assertEqual(len(page.headings), 1)
                for reference in page.references:
                    url = urlsplit(reference)
                    if url.scheme or url.netloc:
                        self.assertIn(url.scheme, ("https", "mailto"))
                        continue
                    target = (PUBLIC / unquote(url.path.lstrip("/"))) if url.path else file
                    if target.is_dir():
                        target = target / "index.html"
                    self.assertTrue(target.is_file(), f"Missing {reference} in {file.name}")
                    if url.fragment:
                        self.assertIn(unquote(url.fragment), Page(target.read_text()).ids)

    def test_portfolio_content(self):
        text = (PUBLIC / "index.html").read_text()
        for expected in ("Aman Agarwal", "IIT (BHU)", "IIIT Bhopal", "Daily Score Tracker", "PocketLog", "mailto:iiitbhopal23u01070@gmail.com", "https://linkedin.com/in/solitarybear"):
            self.assertIn(expected, text)
        self.assertNotIn("tel:", text)
        self.assertNotIn(".pdf", text)
        self.assertIn('src="portfolio.js" defer', text)
        self.assertIn('href="https://solitarybear.com/"', text)
        for repo in ("Task-Aware-Semantic-Grasp-Quality-Prediction", "Daily-Score-Tracker", "PocketLog"):
            self.assertIn("https://github.com/solitarybear/" + repo, text)

    def test_contribution_and_public_email(self):
        text = (PUBLIC / "index.html").read_text()
        self.assertIn("https://github.com/deepset-ai/haystack/pull/13576", text)
        self.assertIn('id="open-source"', text)
        start = text.index("<!--email_off-->")
        end = text.index("<!--/email_off-->")
        self.assertLess(start, text.index('href="mailto:'))
        self.assertLess(text.index('href="mailto:'), end)

    def test_search_metadata(self):
        sitemap = ET.parse(PUBLIC / "sitemap.xml")
        locations = sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        self.assertEqual([node.text for node in locations], ["https://solitarybear.com/"])
        self.assertIn("https://solitarybear.com/sitemap.xml", (PUBLIC / "robots.txt").read_text())


if __name__ == "__main__":
    unittest.main()

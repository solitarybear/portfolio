# Aman Agarwal · Portfolio

Personal portfolio focused on AI, machine learning, and practical software.

**[Visit solitarybear.com](https://solitarybear.com/)**

## About

The site brings together selected projects, research experience, education, skills, and open-source contributions. It includes work in multimodal learning and computer vision, Python desktop applications, and a merged contribution to [Haystack](https://github.com/deepset-ai/haystack/pull/13576).

The design uses a restrained dark palette, readable typography, and responsive navigation.

## Built with

- Semantic HTML and CSS
- Cloudflare Pages hosting with GitHub integration
- Python's standard library for local checks

No JavaScript framework, package installation, or build step is required. Contact links work through email and Gmail; there is no contact-form backend or visitor tracking.

## Run locally

From the repository root:

```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory public
```

Open [localhost:8000](http://localhost:8000). Stop the server with Ctrl+C. If port 8000 is already in use, choose another port, such as 8001.

## Project structure

```text
public/             Website pages, styles, icon, and hosting headers
  index.html        Portfolio content
  styles.css        Responsive styling
  404.html          Missing-page screen
tests/              Link, content, and metadata checks
docs/deployment.md  Hosting and custom-domain notes
```

## Maintenance

Edit `public/index.html` for content and `public/styles.css` for appearance. Project descriptions and contribution statuses are maintained manually.

Run the checks before publishing:

```bash
python3 -B -m unittest discover -s tests -v
```

See [deployment documentation](docs/deployment.md) for the hosting configuration, domain setup, and update workflow.

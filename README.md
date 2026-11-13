# Aman Agarwal · Solitarybear

An AI and machine learning portfolio for **solitarybear.com**, built with plain HTML and CSS. No packages, build step, API keys, or paid plugins are required by this code.

The intended setup is **GitHub for the code → Cloudflare Pages for hosting → solitarybear.com as the address**. You do not need to enable GitHub Pages or transfer your domain.

## 1. Preview on your computer

Open a terminal and run:

```bash
cd "$HOME/GitHub Projects/solitarybear-portfolio"
python3 -m http.server 8000 --bind 127.0.0.1 --directory public
```

Open <http://localhost:8000>. Press Ctrl+C in that terminal to stop it.

To check local links, page anchors, project/contact content, and the sitemap:

```bash
python3 -m unittest discover -s tests -v
```

## 2. Review and personalize

Only `public/` gets published. Edit `public/index.html` for text and links; edit `public/styles.css` for colors and layout. Refresh the browser to see changes.

This version emphasizes AI and machine learning using the supplied résumé and public GitHub projects. Robotics remains an application area in the research and experience sections; the desktop apps are presented as analytics and software work, not AI projects. Review the wording before publishing, especially internship details, education dates, and the “Present” robotics-club entry. Project diagrams are concept illustrations, not screenshots or experimental results. No unverified performance numbers or employment availability are displayed.

The email `iiitbhopal23u01070@gmail.com` will be publicly visible. LinkedIn and GitHub links are included. The original résumé PDF, phone number, certificates, and private files are not included. If you later want a downloadable résumé, first make a public copy with only the details you want to share, put it in `public/`, and add a link. Update the footer year as needed.

## 3. Push to your GitHub

1. Sign in to <https://github.com/new> as `solitarybear`.
2. Name the repository **solitarybear-portfolio**. Choose your preferred visibility. Leave “Add a README”, license, and .gitignore unchecked because this folder already contains files.
3. Create the repository. Then run:

```bash
cd "$HOME/GitHub Projects/solitarybear-portfolio"
git status
git add .
git commit -m "Create personal portfolio"
git remote add origin https://github.com/solitarybear/solitarybear-portfolio.git
git push -u origin main
```

The folder has already been initialized as a Git repository with a `main` branch. No commit, remote, or GitHub repository was created automatically. If Git asks for your identity, set `git config user.name "Aman Agarwal"` and `git config user.email "YOUR_GITHUB_COMMIT_EMAIL"` in this folder using your actual verified or GitHub no-reply address. Replace the placeholder before running the email command.

GitHub requires a supported sign-in method, such as a credential manager, a personal access token for HTTPS, or SSH; your account password will not work for Git pushes. Do not paste tokens into website files or this README. If you use SSH already, use `git@github.com:solitarybear/solitarybear-portfolio.git` as the remote instead. If `origin` already exists, inspect it with `git remote -v` before changing it.

## 4. Deploy to Cloudflare Pages

In the Cloudflare account containing your domain, open **Workers & Pages → Create application → Pages → Import an existing Git repository**. Connect GitHub, grant access to this repository, and select it. If the dashboard opens the Workers flow, find the Pages option instead.

Use:

| Setting | Value |
| --- | --- |
| Project name | `solitarybear-portfolio` (or an available name) |
| Production branch | `main` |
| Framework preset | None |
| Build command | `exit 0` |
| Build output directory | `public` |
| Root directory | Leave blank (repository root) |
| Environment variables | None |

Save and deploy. Open the **actual `*.pages.dev` address Cloudflare returns** and check the site before changing the domain. Future pushes to `main` trigger new deployments.

Reference: [Cloudflare’s static HTML deployment guide](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/).

## 5. Connect solitarybear.com and retire the redirect

The domain returned a permanent redirect to `https://github.com/solitarybear` when checked on 13 November 2026 (India time). DNS changes alone may not remove that redirect.

1. Record the existing DNS entries and GitHub forwarding rule so you can restore them if necessary.
2. In the Pages project, open **Custom domains → Set up a domain**, enter `solitarybear.com`, and follow the DNS confirmation. Cloudflare can create the required CNAME in your account. If it reports a conflicting root A/AAAA/CNAME record, replace only that conflicting website record. Keep unrelated records, especially email MX/TXT entries.
3. Under the domain’s **Rules**, find and disable the rule forwarding visitors to GitHub. It may be in Redirect Rules, an older Page Rule with “Forwarding URL”, or account-level Bulk Redirects. If a Worker performs the redirect, remove only its matching website route. Do this during the domain cutover; it can also prevent validation from completing.
4. Wait for the Pages custom domain and HTTPS certificate to become active. Open `https://solitarybear.com` in a fresh private browser window to avoid a cached permanent redirect.
5. To support `www.solitarybear.com`, add it separately under the same Pages project's Custom domains and complete its DNS setup too.

Do not add an arbitrary hosting IP or only create a DNS CNAME: associate each hostname with the Pages project first. Your domain remains registered with Cloudflare.

Reference: [Cloudflare’s custom-domain instructions and redirect behavior](https://developers.cloudflare.com/pages/configuration/custom-domains/).

## 6. Check the live site

- Check both desktop and phone layouts, navigation links, GitHub projects, LinkedIn, and the email link.
- Confirm the address stays on `solitarybear.com`, HTTPS works, and `/not-a-page` shows the custom 404.
- If the domain still opens GitHub, check forwarding rules and cached redirects. Use a fresh browser profile or run `curl -I https://solitarybear.com` to inspect the current response.
- If Pages reports a DNS conflict, inspect the existing website records before removing anything. Leave mail-related records intact.
- If the Pages address shows 404, confirm output directory `public`, branch `main`, and the presence of `public/index.html` in GitHub.

## Updating later

```bash
cd "$HOME/GitHub Projects/solitarybear-portfolio"
python3 -m unittest discover -s tests -v
git add public README.md tests
git commit -m "Update portfolio"
git push
```

Wait for the deployment to finish in Cloudflare. Use its deployment history to roll back if needed; retain the old redirect details until the new site is verified.

## Files

```text
public/
  index.html       Portfolio content
  styles.css       Desktop and mobile styling
  favicon.svg      Browser icon
  404.html         Missing-page screen
  robots.txt       Search crawler instructions
  sitemap.xml      Canonical site URL
  _headers         Cloudflare response security headers
tests/
  test_site.py    Small standard-library checks
README.md          This setup guide
```

There is no JavaScript, visitor tracking, contact-form backend, or third-party font request. The email link opens the visitor’s configured mail app. If you later add scripts, forms, embedded content, or external assets, review `public/_headers` because the current content security policy intentionally allows only this static site.

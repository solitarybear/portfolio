# Deployment and domain notes

## Hosting overview

GitHub stores the source, Cloudflare Pages serves the `public/` directory, and the custom domain points to that Pages project. Domain registration and website hosting are separate services, even when both are managed through Cloudflare.

For this portfolio, the public address is [solitarybear.com](https://solitarybear.com/). The domain previously forwarded visitors to GitHub; it now serves the portfolio directly.

## Pages configuration

Connect the GitHub repository to a **Cloudflare Pages** project and use:

| Setting | Value |
| --- | --- |
| Production branch | `main` |
| Framework preset | None |
| Build command | `exit 0` |
| Build output directory | `public` |
| Root directory | Repository root |
| Environment variables | None |

Only `public/` is served as the website. Documentation and tests remain repository files.

## Custom-domain setup

1. Deploy the site and verify the assigned `*.pages.dev` address.
2. Add the domain through the Pages project's **Custom domains** settings.
3. Confirm the root CNAME points to the project's assigned Pages address. Replace only conflicting website records; preserve unrelated DNS records.
4. Disable any old forwarding rule that sends visitors to another website. Changing DNS alone does not remove a redirect rule.
5. Wait for activation, then verify HTTPS and the website in a private browser window to avoid cached redirects.

This migration replaced the previous root AAAA record with a CNAME targeting the Pages project. Domain registration stayed with Cloudflare. The `www` hostname, if desired, must be added separately through Pages; it is not assumed to be configured.

## Publishing updates

Preview changes locally, run the checks described in the README, and review the diff. When ready to publish, commit the intended files and push to `main`. Cloudflare automatically deploys that branch. Changes saved only on a computer do not change the live website.

After deployment, check the layout, navigation, project links, and email link. Update the stylesheet's version query in the HTML when changing its styling so returning visitors do not reuse an older cached version. Keep the main page and 404 page stylesheet references consistent.

## Email display

The website blocks JavaScript through its content security policy. Cloudflare's email obfuscation normally needs a decoding script, so the public contact section uses `<!--email_off-->` and `<!--/email_off-->` comments to keep the address readable without scripts. Preserve these markers when editing contact content.

The email link uses an existing mailbox. Publishing a website on a domain does not create email inboxes for that domain.

## Local-only notes

The ignored `private/` directory can hold personal setup notes. Keep credentials and personal machine paths out of shared documentation. `.gitignore` prevents untracked files from being added normally; it does not remove files or information already committed to Git history.

## References

- [Deploy static HTML with Cloudflare Pages](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/)
- [Configure a custom domain](https://developers.cloudflare.com/pages/configuration/custom-domains/)
- [Cloudflare email obfuscation](https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/)

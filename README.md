<div align="center">

![osa-mailer](assets/logo.png)

**Send dynamic and sophisticated E-mails using Smart Templates**

[Guidebook](https://dk26.github.io/osa-mailer/) |
[Discussions](https://github.com/DK26/osa-mailer/discussions)


[![Build](https://github.com/DK26/osa-mailer/actions/workflows/general.yml/badge.svg?branch=main)](https://github.com/DK26/osa-mailer/actions/workflows/general.yml)
[![Security Audit & License Compatibility](https://github.com/DK26/osa-mailer/actions/workflows/security-audit.yml/badge.svg?branch=main)](https://github.com/DK26/osa-mailer/actions/workflows/security-audit.yml)
[![pages-build-deployment](https://github.com/DK26/osa-mailer/actions/workflows/pages/pages-build-deployment/badge.svg?branch=main)](https://github.com/DK26/osa-mailer/actions/workflows/pages/pages-build-deployment)  

</div>

## Features

- Currently supports 3 template engines: `tera`, `handlebars` and `liquid`
- Automatically attaches all your HTML resources to the SMTP message
- Provides you the ability to aggregate multiple E-mails of the same subject and recipients, into a single E-mail with accumulated context
- Supports multiple SMTP connection types: `NOAUTH`, `TLS` and `STARTTLS`

[Download Alpha 2 (i686-pc-windows)](https://github.com/DK26/osa-mailer/releases/tag/alpha-2)

## Template Designing

Try the [`rendit` CLI tool](https://github.com/DK26/rendit)


## Prototype Note

This is still an MVP (Minimal Viable Product) and there is still work to be done and features to be added. Features may be added or removed later with no notice (but typically documented in the changelog notes of each release)

## License
MIT
# Requests: HTTP for Humans

Requests is the only *Non-GMO* HTTP library for Python, safe for human
consumption.

**Warning:** Recreational use of other HTTP libraries may result in dangerous side-effects,
including: security vulnerabilities, verbose code, reinventing the wheel,
constantly reading documentation, depression, headaches, or even death.

Behold, the power of Requests:

```python
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
```

See the similar code, sans Requests.

Requests allows you to send *organic, grass-fed* HTTP/1.1 requests, without the
need for manual labor. There's no need to manually add query strings to your
URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling
are 100% automatic, powered by urllib3,
which is embedded within Requests.

Besides, all the cool kids are doing it. Requests is one of the most
downloaded Python packages of all time, pulling in over 7,000,000 downloads
every month. You don't want to be left out!

## Feature Support

Requests is ready for today's web.

- International Domains and URLs
- Keep-Alive & Connection Pooling
- Sessions with Cookie Persistence
- Browser-style SSL Verification
- Basic/Digest Authentication
- Elegant Key/Value Cookies
- Automatic Decompression
- Automatic Content Decoding
- Unicode Response Bodies
- Multipart File Uploads
- HTTP(S) Proxy Support
- Connection Timeouts
- Streaming Downloads
- `.netrc` Support
- Chunked Requests
- Thread-safety

Requests officially supports Python 2.6–2.7 & 3.3–3.7, and runs great on PyPy.

## Installation

To install Requests, simply:

```bash
$ pip install requests
```

Satisfaction, guaranteed.

## Documentation

Fantastic documentation is available at http://docs.python-requests.org/, for a limited time only.

## How to Contribute

1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a Contributor Friendly tag for issues that should be ideal for people who are not very familiar with the codebase yet.
2. Fork the repository on GitHub to start making your changes to the **master** branch (or branch off of it).
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS.

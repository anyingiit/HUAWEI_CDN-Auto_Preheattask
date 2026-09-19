<!-- Source: Best-README-Template BLANK_README (Unlicense) — https://github.com/othneildrew/Best-README-Template -->
<a id="readme-top"></a>

# HUAWEI CDN Auto Preheattask

A polling script that watches a local Git checkout of a website for new commits on origin/master, then asks Huawei Cloud CDN to refresh and preheat every file under the site directory once one lands.

**English** · [简体中文](README.zh-CN.md)

[![CI](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask/actions/workflows/ci.yml/badge.svg)](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/anyingiit/HUAWEI_CDN-Auto_Preheattask)](LICENSE)

[Report a bug](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask/issues/new?template=bug_report.yml) · [Request a feature](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask/issues/new?template=feature_request.yml)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

`main.py` runs forever: on each pass of its loop it runs `git fetch` and
`git rev-parse` against a local checkout of a website's Git repository (the
paths live in `globalVariable.py`), and once `origin/master` has moved past
the local `master`, it pulls the new commit. It then walks every file under
the site directory with `getDirAllFilename.py`, and hands the resulting list
of URLs to `huaweiSDK/refreshTask.py` and, five minutes later,
`huaweiSDK/preheatTask.py`, so that Huawei Cloud CDN's cached copies are
refreshed and then preheated for everything the new commit touched.

The Huawei Cloud SDK connection itself is opened once by `connect.py`, using
a project ID, region, and an access key / secret key pair that
`globalVariable.py` supplies.

See the [open issues](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask/issues) for planned features and known issues.

## Getting Started

### Prerequisites

- Python 3 — the repository has no `requirements.txt` or `pyproject.toml`,
  so no version is pinned anywhere.
- The `openstack` SDK package that `connect.py` imports (published on PyPI
  as `openstacksdk`); it is not declared in any manifest here, so it has to
  be installed separately.
- A Huawei Cloud account with the CDN service enabled, plus its access key
  ID and secret access key: `connect.py` reads a project ID, region, and
  those two credentials from `globalVariable.py` to open the SDK connection.
- A local Git clone of the website repository to be served, at the path
  `main.py` expects: it runs `git fetch` / `git rev-parse` / `git pull`
  against `globalVariable.py`'s configured directory.

### Installation

This is a script you run in place rather than a package you install, so
there is no build step beyond installing its one dependency:

```sh
git clone https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask.git
cd HUAWEI_CDN-Auto_Preheattask
pip install openstacksdk
```

Before running it, open `globalVariable.py` and replace its local paths,
Huawei Cloud project ID, region, access key and secret key with your own —
the values committed there belong to whoever set this repository up, not to
your environment, and this script will act against whatever it finds there.

## Usage

Start it and leave it running, for example under `systemd`, `screen`, or
`tmux`, since it loops forever rather than exiting:

```sh
python main.py
```

Each pass checks whether the configured repository's `origin/master` has
moved; when it has, the script pulls the new commit, then refreshes and
preheats every file under the site directory on Huawei Cloud CDN. Progress
and errors go to standard output through Python's `logging` module.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for how to open an issue or a pull request, and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for the standards expected of everyone taking part.

Please do not report security issues in public issues or pull requests. [SECURITY.md](SECURITY.md) explains how to report them privately.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

Project link: [https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

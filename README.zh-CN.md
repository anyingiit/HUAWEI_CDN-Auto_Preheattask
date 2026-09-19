[English](README.md) · **简体中文**

> 英文版是规范版本。本页与 [README.md](README.md) 不一致时，以英文版为准。

<!-- translation-of: README.md sha256:9f794fe8a443cba5 -->

<!-- Source: Best-README-Template BLANK_README (Unlicense) — https://github.com/othneildrew/Best-README-Template -->
<a id="readme-top"></a>

# HUAWEI CDN Auto Preheattask

一个轮询脚本：监视网站本地 Git 仓库的 origin/master 是否出现新提交，一旦出现，就让华为云 CDN 刷新并预热网站目录下的每一个文件。

[![CI](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask/actions/workflows/ci.yml/badge.svg)](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/anyingiit/HUAWEI_CDN-Auto_Preheattask)](LICENSE)

[报告问题](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask/issues/new?template=bug_report.yml) · [提出需求](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask/issues/new?template=feature_request.yml)

<details>
  <summary>目录</summary>
  <ol>
    <li><a href="#about-the-project">关于本项目</a></li>
    <li><a href="#getting-started">开始使用</a></li>
    <li><a href="#usage">用法</a></li>
    <li><a href="#contributing">参与贡献</a></li>
    <li><a href="#license">许可证</a></li>
    <li><a href="#contact">联系方式</a></li>
  </ol>
</details>

## 关于本项目

`main.py` 会一直运行下去：每一轮循环都会对网站的本地 Git 仓库执行 `git fetch`
和 `git rev-parse`（路径写在 `globalVariable.py` 里），一旦 `origin/master`
领先于本地的 `master`，就会拉取新提交。随后它用 `getDirAllFilename.py`
遍历网站目录下的所有文件，把得到的 URL 列表交给 `huaweiSDK/refreshTask.py`，
五分钟后再交给 `huaweiSDK/preheatTask.py`，从而让华为云 CDN 对这次新提交
涉及的内容先刷新缓存、再执行预热。

华为云 SDK 连接本身由 `connect.py` 建立一次，所用的项目 ID、区域，以及一对
访问密钥（AK/SK），都来自 `globalVariable.py`。

计划中的功能与已知问题，见 [open issues](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask/issues)。

## 开始使用

### 环境要求

- Python 3——本仓库没有 `requirements.txt` 或 `pyproject.toml`，因此没有在
  任何地方锁定具体版本。
- `connect.py` 导入的 `openstack` SDK（在 PyPI 上以 `openstacksdk` 发布）；
  本仓库没有在任何清单文件中声明它，需要自行安装。
- 一个已开通 CDN 服务的华为云账号，以及它的访问密钥 ID 和密钥：`connect.py`
  会从 `globalVariable.py` 读取项目 ID、区域和这两个凭据来建立 SDK 连接。
- 一份要对外提供服务的网站仓库的本地 Git 克隆，路径要与 `main.py` 期望的
  一致：它会针对 `globalVariable.py` 中配置的目录执行
  `git fetch`／`git rev-parse`／`git pull`。

### 安装

这是一个就地运行的脚本，而不是需要安装的软件包，因此除了安装它唯一的依赖之外
没有别的构建步骤：

```sh
git clone https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask.git
cd HUAWEI_CDN-Auto_Preheattask
pip install openstacksdk
```

运行之前，请打开 `globalVariable.py`，把其中的本地路径、华为云项目 ID、
区域、访问密钥和密钥都换成你自己的——仓库里提交的那些值属于最初搭建它的人，
不属于你的环境，而这个脚本会照着它读到的值去操作。

## 用法

启动后让它一直运行，例如放到 `systemd`、`screen` 或 `tmux` 里，因为它不会
自己退出：

```sh
python main.py
```

每一轮都会检查所配置仓库的 `origin/master` 是否有新提交；一旦有，脚本就会
拉取新提交，然后在华为云 CDN 上刷新并预热网站目录下的每一个文件。运行过程
和错误信息通过 Python 的 `logging` 模块输出到标准输出。

## 参与贡献

欢迎参与。[CONTRIBUTING.md](CONTRIBUTING.md) 说明如何提交 issue 或 pull request，[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 说明对所有参与者的行为要求。

请不要在公开的 issue 或 pull request 中报告安全问题。[SECURITY.md](SECURITY.md) 说明了私下报告的方式。

## 许可证

以 MIT 许可证分发。详见 [LICENSE](LICENSE)。

## 联系方式

项目地址：[https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask](https://github.com/anyingiit/HUAWEI_CDN-Auto_Preheattask)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

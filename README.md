# foosbot

[![Python: 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Actions status](https://github.com/hugovk/pypistats/workflows/Test/badge.svg)](https://github.com/hugovk/foosbot/actions)
[![codecov](https://codecov.io/gh/hugovk/foosbot/branch/master/graph/badge.svg)](https://codecov.io/gh/hugovk/foosbot)
[![Licence](https://img.shields.io/github/license/hugovk/foosbot.svg)](LICENSE.txt)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

Slackbot for arranging foosball games.

## Installation

```bash
pip install slackbot
git clone https://github.com/hugovk/foosbot
cd foosbot
cp example_slackbot_settings.py slackbot_settings.py
```

Create API token at https://my.slack.com/apps/new/A0F7YS25R-bots and add to
`slackbot_settings.py`

## Usage

```bash
python run.py
```

In Slack, `@foosbot help`

# PhoneAnalyzer

**PhoneAnalyzer** is an OSINT tool designed to identify websites where a given phone number appears.

![PhoneAnalyzer](https://i.imgur.com/lc4BR9Z.png)

## Installation

```bash
git clone https://github.com/NeKroFR/PhoneAnalyzer.git
cd PhoneAnalyzer/
pip3 install -r requirements.txt
```
## Usage

**Using the gui:**
```
python3 PhoneAnalyzer.py 
```
**Or directly provide a phone number:**
```
python3 PhoneAnalyzer.py phone_number
```

## ⚠️ Disclaimer ⚠️

- Currently, the script is working for French phone numbers only.
- The script may won't provide results if used repeatedly in a short period of time without using proxy.
- The tool may return a significant number of false positives. Always verify the results manually.

## Contributing

Interested in contributing? Check out the [to-do list](todo.md).
Submit a pull request, and if it's a good fit, I'll be happy to merge it!


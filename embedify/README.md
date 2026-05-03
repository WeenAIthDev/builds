
# Embedify

Embedify is a command-line tool that converts **YouTube Shorts** and **Instagram Reels** links into:

- Embed links  
- `<iframe>` embed code  

All results are saved into an `<file>.txt` file that's needs to be created by user.

---

## Features

- Supports YouTube Shorts and Instagram Reels  
- Generates embed links and iframe code  
- Built using Python argparse  
- Accepts flexible input:
  - Single URL (`--url`)
  - File input (`--file`)
  - Both together  

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/WeenAIthDev/builds.git
cd embedify
```
--- 

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

```
python main.py [-h] [--url URL] [--file FILE]
```

### Arguments

* `-h`, `--help`
  Show help message

* `--url URL`
  Process a single link

* `--file FILE`
  Process multiple links from a file

---

## Input Behavior (Important)

With argparse, flags can be used **in any combination**:

| Command          | What happens                |
| ---------------- | --------------------------- |
| `--url` only     | Processes one link          |
| `--file` only    | Processes all links in file |
| `--url + --file` | Processes both              |
| no arguments     | Shows error message         |

---

## Examples

### Single URL

```bash
python main.py --url https://youtube.com/shorts/abc123
```

---

### File input

```bash
python main.py --file links.txt
```

Example file:

```
https://youtube.com/shorts/abc123
https://www.instagram.com/reel/xyz789/
```

---

### Combined input (argparse behavior)

```
python main.py --url https://youtube.com/shorts/abc123 --file links.txt
```

Processes:

* the single URL
* all links inside the file
* both URL and file
---

## Output

Saved in `<file>.txt` that should be created by the user:

```
Original: https://youtube.com/shorts/abc123
Embed Link: https://www.youtube.com/embed/abc123
Embed Code: <iframe src="https://www.youtube.com/embed/abc123"></iframe>

Original: https://www.instagram.com/reel/xyz789/
Embed Link: https://www.instagram.com/p/xyz789/embed
Embed Code: <iframe src="https://www.instagram.com/p/xyz789/embed"></iframe>
```

---

## Supported Links

### YouTube Shorts

```
https://youtube.com/shorts/<id>
→ https://www.youtube.com/embed/<id>
```

### Instagram Reels

```
https://www.instagram.com/reel/<id>/
→ https://www.instagram.com/p/<id>/embed
```

---

## Error Handling

Invalid or unsupported links:

```
Error message
```

---

## Requirements

- Python >= 3.8

Install dependencies:

```
pip install -r requirements.txt
```

---

## Project Structure

```
embedify/
├── main.py
├── requirements.txt
└── README.md
```

---

## Credits

In collaboration with Jesus
Made with <3 by WeenAIthDev




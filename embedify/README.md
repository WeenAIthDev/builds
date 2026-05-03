# Embedify

Embedify is a command-line tool that converts **YouTube Shorts** and **Instagram Reels** links into:

- Embed links  
- `<iframe>` embed code  

The results are saved into a `.txt` file.

---

## Features

- Supports YouTube Shorts and Instagram Reels  
- Generates embed links and iframe code  
- Accepts:
  - Single URL (`--url`)
  - Multiple URLs via file (`--file`)
  - Both together  
- Supports appending results (`--append`)  
- Allows custom output file name (`--outputfile`)  

---

## Requirements

- Python >= 3.8  

```bash
pip install -r requirements.txt
````

---
## Installation

1. Clone the repository:
```bash
git clone https://github.com/WeenAIthDev/builds.git
```
2. Navigate to embedify folder
```bash
cd embedify
```
---
## Usage

```bash
python main.py [-h] [--url URL] [--file FILE] [--append] [--outputfile OUTPUTFILE]
```

---

## Options

| Option                    | Description                                          |
| ------------------------- | ---------------------------------------------------- |
| `-h`, `--help`            | Show help message and exit                           |
| `--url URL`               | Add a YouTube Shorts or Instagram Reel link          |
| `--file FILE`             | Add a file containing multiple links (one per line)  |
| `--append`                | Append results to output file instead of overwriting |
| `--outputfile OUTPUTFILE` | Specify output file name (must be `.txt`)            |

---

## Input Behavior

| Command          | Behavior                    |
| ---------------- | --------------------------- |
| `--url`          | Processes one link          |
| `--file`         | Processes all links in file |
| `--url + --file` | Processes both              |

---

## Examples

### 1. YouTube Shorts URL

```bash
python main.py --url https://youtube.com/shorts/ZwaAgG54KXc?si=nvyvOcbtftOE207-
```

**Output:**

```
For yt shorts: https://youtube.com/shorts/ZwaAgG54KXc?si=nvyvOcbtftOE207-
Embed Link: https://www.youtube.com/embed/ZwaAgG54KXc
Embed Code: <iframe src="https://www.youtube.com/embed/ZwaAgG54KXc"></iframe>
```

---

### 2. Instagram Reel URL

```
python main.py --url https://www.instagram.com/reel/DXhLqG7jBVn/?igsh=NnFudzdjbTM3ejRq
```

**Output:**

```
For instagram reel: https://www.instagram.com/reel/DXhLqG7jBVn/?igsh=NnFudzdjbTM3ejRq
Embed Link: https://www.instagram.com/p/DXhLqG7jBVn/embed
Embed Code: <iframe src="https://www.instagram.com/p/DXhLqG7jBVn/embed"></iframe>
```

---

### 3. File input

Example `links.txt`:

```
https://youtube.com/shorts/ZwaAgG54KXc?si=nvyvOcbtftOE207-
https://www.instagram.com/reel/DXhLqG7jBVn/?igsh=NnFudzdjbTM3ejRq
```

Run:

```
python main.py --file links.txt
```

---

### 4. Combined usage

```
python main.py --url https://youtube.com/shorts/ZwaAgG54KXc?si=nvyvOcbtftOE207- --file links.txt
```

---

### 5. Append mode

```
python main.py --url https://youtube.com/shorts/ZwaAgG54KXc?si=nvyvOcbtftOE207- --append
```

---

### 6. Custom output file

```
python main.py --file links.txt --outputfile results.txt
```

---

### 7. Full combination

```bash
python main.py --url https://youtube.com/shorts/ZwaAgG54KXc?si=nvyvOcbtftOE207- --file links.txt --append --outputfile results.txt
```

---

## Output

Default file: `output.txt`

```
For yt shorts: https://youtube.com/shorts/ZwaAgG54KXc?si=nvyvOcbtftOE207-
Embed Link: https://www.youtube.com/embed/ZwaAgG54KXc
Embed Code: <iframe src="https://www.youtube.com/embed/ZwaAgG54KXc"></iframe>

For instagram reel: https://www.instagram.com/reel/DXhLqG7jBVn/?igsh=NnFudzdjbTM3ejRq
Embed Link: https://www.instagram.com/p/DXhLqG7jBVn/embed
Embed Code: <iframe src="https://www.instagram.com/p/DXhLqG7jBVn/embed"></iframe>
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
Error Message
```

---

## Project Structure

```
embedify/
├── main.py
├── requirements.txt
├── .gitignore
├── output.txt
└── README.md
```

---

## Credits

In collaboration with Jesus
Made with <3 by WeenAIthDev


---


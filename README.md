# AIS JSON Decryptor

A simple and secure utility to decrypt AIS (Annual Information Statement) JSON files. This tool provides both a Command-Line Interface (CLI) and a Graphical User Interface (GUI) for ease of use.

## Features

- **Double Interface**: Choose between a modern PyQt6 GUI or a lightweight CLI.
- **Secure Decryption**: Uses standard AES-256 decryption with PBKDF2 key derivation.
- **Automated Releases**: Integrated GitHub Actions to build standalone Windows executables.
- **Input Validation**: Clear error messaging for incorrect PAN, DOB, or file paths.

## Prerequisites

- Python 3.12+
- A virtual environment (recommended)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd aisdecrypt
   ```

2. **Set up the virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Graphical User Interface (GUI)
The GUI is the most user-friendly way to decrypt your files. It includes file pickers and status updates.

```bash
python gui.py
```

- **PAN**: Enter your 10-digit PAN (case-insensitive).
- **DOB**: Enter your Date of Birth in `DDMMYYYY` format.
- **Browse**: Select your encrypted `.json` (or extension-less) file.
- **Decrypt**: Click the button to generate the formatted JSON output.

### Command-Line Interface (CLI)
For users who prefer the terminal or want to script the decryption process.

```bash
python AIS_Decryptor.py
```

Follow the on-screen prompts to provide the required credentials and file paths.

## Building for Windows

To create a standalone `.exe` file that doesn't require Python to be installed:

```bash
pyinstaller --onefile --windowed --name AIS_Decryptor_GUI gui.py
```
The executable will be found in the `dist/` folder.

## CI/CD and Releases

This repository is configured with GitHub Actions. To trigger an automated build and release:

1. Commit your changes.
2. Tag the commit with a version number (e.g., `v1.0.0`).
3. Push the tag to GitHub.

```bash
git tag v1.2.0
git push origin --tags
```
GitHub will automatically build the Windows executable and upload it to the "Releases" section of your repository.

## Project Structure

- `AIS_Decryptor.py`: Core decryption logic and CLI interface.
- `gui.py`: PyQt6-based desktop application.
- `requirements.txt`: Project dependencies.
- `.github/workflows/release.yml`: Automation for building and releasing.

## License

This project is for educational/personal use. Please ensure you comply with all data privacy regulations regarding financial statements.

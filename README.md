# AIS JSON Decryptor

A secure utility to decrypt AIS (Annual Information Statement) JSON files. This tool allows you to convert your encrypted financial data into a readable, formatted JSON file using your PAN and Date of Birth.

---

## 🚀 How to Use

Choose the method that works best for you:

### 1. Using the Windows Executable (Easiest)
If you downloaded the `.exe` file from the [Releases](https://github.com/iambalaji-k/aisdecrypt/releases) page:
1.  **Run** `AIS_Decryptor_GUI.exe`.
2.  **Enter your PAN** (e.g., ABCDE1234F).
3.  **Enter your Date of Birth** in `DDMMYYYY` format (e.g., 01011990).
4.  **Click "Browse"** to select your encrypted AIS file.
5.  **Click "Decrypt File"**. Your decrypted file will be saved as `decrypted.json` by default.

### 2. Using the Graphical Interface (Python)
If you have Python installed and want to run the GUI from source:
1.  Open your terminal/command prompt in the project folder.
2.  Run the following command:
    ```bash
    python gui.py
    ```
3.  Use the window to enter your credentials and select your file. The interface will guide you through the process and show a success message once finished.

### 3. Using the Command-Line Interface (CLI)
For users who prefer working directly in the terminal:
1.  Open your terminal/command prompt in the project folder.
2.  Run the following command:
    ```bash
    python AIS_Decryptor.py
    ```
3.  **Follow the prompts**:
    - Input your PAN and DOB.
    - Provide the full path to the encrypted file.
    - (Optional) Provide a name for the output file.
4.  The tool will output the decryption status directly in the terminal.

---

## 🔐 Privacy & Security
- **Local Decryption**: All decryption happens locally on your computer. Your PAN, DOB, and financial data are **never** uploaded to the internet or any server.
- **Open Source**: The logic is transparent and can be reviewed in `AIS_Decryptor.py`.

---

## 🛠 Technical Setup (For Developers)

If you are setting this up to run from source, ensure you have Python 3.12+ installed.

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Dependencies**:
    - `pycryptodome`: For AES-256 decryption.
    - `PyQt6`: For the graphical interface.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

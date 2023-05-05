# Password Manager App

The Password Manager App is a Python-based application that allows users to securely store and manage their passwords. The app uses the [cryptography](https://cryptography.io/en/latest/) library to encrypt and decrypt the passwords, and the [pyperclip](https://pypi.org/project/pyperclip/) library to copy the passwords to the clipboard for easy retrieval.

## Installation

To install and run the Password Manager App locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/password-manager.git
   ```

2. Change into the project directory:

   ```bash
   cd password-manager
   ```

3. Create a virtual environment for the project and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Set the encryption key environment variable:

   ```bash
   export PASSWORD_MANAGER_KEY=your-secret-key
   ```

   Note: replace "your-secret-key" with a secure key of your choice.

6. Run the app:

   ```bash
   python app.py
   ```

7. Access the app in your web browser at [http://localhost:8000](http://localhost:8000)

## Running with Docker

To run the Password Manager App with Docker, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/password-manager.git
   ```

2. Change into the project directory:

   ```bash
   cd password-manager
   ```

3. Build the Docker image:

   ```bash
   docker build -t password-manager .
   ```

4. Set the encryption key environment variable:

   ```bash
   export PASSWORD_MANAGER_KEY=your-secret-key
   ```

   Note: replace "your-secret-key" with a secure key of your choice.

5. Run the Docker container:

   ```bash
   docker run -p 8000:8000 -e PASSWORD_MANAGER_KEY=$PASSWORD_MANAGER_KEY password-manager
   ```

6. Access the app in your web browser at [http://localhost:8000](http://localhost:8000)

## Usage

Once the app is running, you can use the command-line interface or the web-based user interface to interact with the app. Here are some examples of usage:

- Add a new password to the password manager:

  ```bash
  python app.py add gmail mypassword123
  ```

- Retrieve a password from the password manager and copy it to the clipboard:

  ```bash
  python app.py get gmail
  ```

  Note: this will copy the password to the clipboard automatically.

- List all the passwords stored in the password manager:

  ```bash
  python app.py list
  ```

- Delete a password from the password manager:

  ```bash
  python app.py delete gmail
  ```

## Disclaimers and Warnings

- The Password Manager App is provided "as is" and without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability.

- It is the responsibility of the user to choose a secure encryption key and to keep it safe. The Password Manager App does not store the encryption key

# Certificate Expiration
python script for validate expiration date of ssl cert

# Instructions for use

- Get and smtp server configured.
- Clone this repository.
  ```bash
  git clone https://github.com/mrlpm/certificateexpiration.git
  ```
- Set permissions to the script
  ```bash
  chmod 700 ~/certificateexpiration/certificateexpiration.py
  ```
- Create a cron job like the following:
  ```cron
  0 0 * * * ~/certificateexpiration/certificateexpiration.py
  ```

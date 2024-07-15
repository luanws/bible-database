# Bible database

This repository contains a script that scrapes various Bible versions from the internet and converts them into a JSON format. The goal of this project is to make it easy for developers to access the Bible in a machine-readable format for their applications.

## Usage

To use the script, you will need Python 3 and the dependencies listed in the `requirements.txt` file installed. You can install them using `pip install -r requirements.txt`. Clone the repository and navigate to the folder in your terminal. Run the script by typing `python main.py`. The script will open a menu with a few options, including one for scraping the Bible. The copied biblical data will be uploaded to `data/language/version.json`.

## Available Bible versions

Currently, the script is able to scrape most versions of the Bible, but some versions in English and Portuguese are already available in the JSON format in the data folder. The following versions are available for download:

### en:
[AMP](https://github.com/luanws/bible-database/raw/main/data/json/en/AMP.json),
[AMPC](https://github.com/luanws/bible-database/raw/main/data/json/en/AMPC.json),
[ASV](https://github.com/luanws/bible-database/raw/main/data/json/en/ASV.json),
[BOOKS](https://github.com/luanws/bible-database/raw/main/data/json/en/BOOKS.json),
[BSB](https://github.com/luanws/bible-database/raw/main/data/json/en/BSB.json),
[CEB](https://github.com/luanws/bible-database/raw/main/data/json/en/CEB.json),
[CEVUK](https://github.com/luanws/bible-database/raw/main/data/json/en/CEVUK.json),
[CJB](https://github.com/luanws/bible-database/raw/main/data/json/en/CJB.json),
[CSB](https://github.com/luanws/bible-database/raw/main/data/json/en/CSB.json),
[DARBY](https://github.com/luanws/bible-database/raw/main/data/json/en/DARBY.json),
[DRC1752](https://github.com/luanws/bible-database/raw/main/data/json/en/DRC1752.json),
[EASY](https://github.com/luanws/bible-database/raw/main/data/json/en/EASY.json),
[ERV](https://github.com/luanws/bible-database/raw/main/data/json/en/ERV.json),
[ESV](https://github.com/luanws/bible-database/raw/main/data/json/en/ESV.json),
[FNVNT](https://github.com/luanws/bible-database/raw/main/data/json/en/FNVNT.json),
[GNBDC](https://github.com/luanws/bible-database/raw/main/data/json/en/GNBDC.json),
[GNBDK](https://github.com/luanws/bible-database/raw/main/data/json/en/GNBDK.json),
[GNBUK](https://github.com/luanws/bible-database/raw/main/data/json/en/GNBUK.json),
[GNT](https://github.com/luanws/bible-database/raw/main/data/json/en/GNT.json),
[GNTD](https://github.com/luanws/bible-database/raw/main/data/json/en/GNTD.json),
[GNV](https://github.com/luanws/bible-database/raw/main/data/json/en/GNV.json),
[GW](https://github.com/luanws/bible-database/raw/main/data/json/en/GW.json),
[GWC](https://github.com/luanws/bible-database/raw/main/data/json/en/GWC.json),
[HCSB](https://github.com/luanws/bible-database/raw/main/data/json/en/HCSB.json),
[ICB](https://github.com/luanws/bible-database/raw/main/data/json/en/ICB.json),
[JUB](https://github.com/luanws/bible-database/raw/main/data/json/en/JUB.json),
[KJV](https://github.com/luanws/bible-database/raw/main/data/json/en/KJV.json),
[KJVAAE](https://github.com/luanws/bible-database/raw/main/data/json/en/KJVAAE.json),
[KJVAE](https://github.com/luanws/bible-database/raw/main/data/json/en/KJVAE.json),
[LEB](https://github.com/luanws/bible-database/raw/main/data/json/en/LEB.json),
[LSB](https://github.com/luanws/bible-database/raw/main/data/json/en/LSB.json),
[MEV](https://github.com/luanws/bible-database/raw/main/data/json/en/MEV.json),
[MP1650](https://github.com/luanws/bible-database/raw/main/data/json/en/MP1650.json),
[MP1781](https://github.com/luanws/bible-database/raw/main/data/json/en/MP1781.json),
[MSG](https://github.com/luanws/bible-database/raw/main/data/json/en/MSG.json),
[NABRE](https://github.com/luanws/bible-database/raw/main/data/json/en/NABRE.json),
[NASB1995](https://github.com/luanws/bible-database/raw/main/data/json/en/NASB1995.json),
[NASB2020](https://github.com/luanws/bible-database/raw/main/data/json/en/NASB2020.json),
[NCV](https://github.com/luanws/bible-database/raw/main/data/json/en/NCV.json),
[NET](https://github.com/luanws/bible-database/raw/main/data/json/en/NET.json),
[NIrV](https://github.com/luanws/bible-database/raw/main/data/json/en/NIrV.json),
[NIV](https://github.com/luanws/bible-database/raw/main/data/json/en/NIV.json),
[NIVUK](https://github.com/luanws/bible-database/raw/main/data/json/en/NIVUK.json),
[NKJV](https://github.com/luanws/bible-database/raw/main/data/json/en/NKJV.json),
[NLT](https://github.com/luanws/bible-database/raw/main/data/json/en/NLT.json),
[NMV](https://github.com/luanws/bible-database/raw/main/data/json/en/NMV.json),
[NRSV](https://github.com/luanws/bible-database/raw/main/data/json/en/NRSV.json),
[NRSVUE](https://github.com/luanws/bible-database/raw/main/data/json/en/NRSVUE.json),
[OYBCENGL](https://github.com/luanws/bible-database/raw/main/data/json/en/OYBCENGL.json),
[PEV](https://github.com/luanws/bible-database/raw/main/data/json/en/PEV.json),
[RAD](https://github.com/luanws/bible-database/raw/main/data/json/en/RAD.json),
[RSV](https://github.com/luanws/bible-database/raw/main/data/json/en/RSV.json),
[RSVCI](https://github.com/luanws/bible-database/raw/main/data/json/en/RSVCI.json),
[RV1885](https://github.com/luanws/bible-database/raw/main/data/json/en/RV1885.json),
[RV1895](https://github.com/luanws/bible-database/raw/main/data/json/en/RV1895.json),
[TCENT](https://github.com/luanws/bible-database/raw/main/data/json/en/TCENT.json),
[TEG](https://github.com/luanws/bible-database/raw/main/data/json/en/TEG.json),
[TLV](https://github.com/luanws/bible-database/raw/main/data/json/en/TLV.json),
[TOJB2011](https://github.com/luanws/bible-database/raw/main/data/json/en/TOJB2011.json),
[TPT](https://github.com/luanws/bible-database/raw/main/data/json/en/TPT.json),
[TS2009](https://github.com/luanws/bible-database/raw/main/data/json/en/TS2009.json),
[WBMS](https://github.com/luanws/bible-database/raw/main/data/json/en/WBMS.json),
[WEBBE](https://github.com/luanws/bible-database/raw/main/data/json/en/WEBBE.json),
[WEBUS](https://github.com/luanws/bible-database/raw/main/data/json/en/WEBUS.json),
[WMB](https://github.com/luanws/bible-database/raw/main/data/json/en/WMB.json),
[WMBBE](https://github.com/luanws/bible-database/raw/main/data/json/en/WMBBE.json),
[YLT98](https://github.com/luanws/bible-database/raw/main/data/json/en/YLT98.json).

### pt:
[A21](https://github.com/luanws/bible-database/raw/main/data/json/pt/A21.json),
[ARA](https://github.com/luanws/bible-database/raw/main/data/json/pt/ARA.json),
[ARC](https://github.com/luanws/bible-database/raw/main/data/json/pt/ARC.json),
[BLT](https://github.com/luanws/bible-database/raw/main/data/json/pt/BLT.json),
[NAA](https://github.com/luanws/bible-database/raw/main/data/json/pt/NAA.json),
[NBV-P](https://github.com/luanws/bible-database/raw/main/data/json/pt/NBV-P.json),
[NTLH](https://github.com/luanws/bible-database/raw/main/data/json/pt/NTLH.json),
[NVI](https://github.com/luanws/bible-database/raw/main/data/json/pt/NVI.json),
[NVT](https://github.com/luanws/bible-database/raw/main/data/json/pt/NVT.json),
[TB](https://github.com/luanws/bible-database/raw/main/data/json/pt/TB.json),
[VFL](https://github.com/luanws/bible-database/raw/main/data/json/pt/VFL.json).

### es-ES:
[RV2020](https://github.com/luanws/bible-database/raw/main/data/json/es-ES/RV2020.json),
[DHHE](https://github.com/luanws/bible-database/raw/main/data/json/es-ES/DHHE.json),
[BLP](https://github.com/luanws/bible-database/raw/main/data/json/es-ES/BLP.json),
[DHHED](https://github.com/luanws/bible-database/raw/main/data/json/es-ES/DHHED.json),
[NVI](https://github.com/luanws/bible-database/raw/main/data/json/es-ES/NVI.json),
[BTI](https://github.com/luanws/bible-database/raw/main/data/json/es-ES/BTI.json).

## Limitations

Please note that this script is for personal use only, and should not be used for commercial purposes. Additionally, certain books or chapters may be missing from the scraped data.

## Contributing

We welcome contributions to this project. If you would like to add a new Bible version or improve the script, please submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

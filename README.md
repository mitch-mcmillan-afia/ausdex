# ausdex

![pipline](https://github.com/rbturnbull/ausdex/actions/workflows/coverage.yml/badge.svg)
[<img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/rbturnbull/49262550cc8b0fb671d46df58de213d4/raw/coverage-badge.json">](<https://rbturnbull.github.io/ausdex/coverage/>)
[<img src="https://github.com/rbturnbull/ausdex/actions/workflows/docs.yml/badge.svg">](<https://rbturnbull.github.io/ausdex/>)
[<img src="https://img.shields.io/badge/code%20style-black-000000.svg">](<https://github.com/psf/black>)

An interface for several Australian socio-economic indices.

The Australian Bureau of Statistics (ABS) publishes a variety of indexes for the Australian
economic environment. These include the Consumer Price Index (CPI) used for calculating inflation
and a variety of indexes designed to measure socio-economic advantage. `ausdex` makes these data
available in a convenient Python package with a simple programatic and command line interfaces. 

## Installation

You can install `ausdex` from the Python Package Index (PyPI):

```
pip install ausdex
```

## Command Line Usage

Adjust single values using the command line interface:
```
ausdex inflation VALUE ORIGINAL_DATE
```
This adjust the value from the original date to the equivalent in today's dollars.

For example, to adjust $26 from July 21, 1991 to today run:
```
$ ausdex inflation 26 "July 21 1991" 
$ 52.35
```

To choose a different date for evaluation use the `--evaluation-date` option. e.g.
```
$ ausdex inflation 26 "July 21 1991"  --evaluation-date "Sep 1999"
$ 30.27
```

### seifa_vic command line usage
youc an use the seifa-vic command to interpolate an ABS census derived Socio economic score for a given year, suburb, and SEIFA metric
```
$ ausdex seifa-vic 2020 footscray ier_score
$ 861.68

```

## Module Usage

```
>>> import ausdex
>>> ausdex.calc_inflation(26, "July 21 1991")
52.35254237288135
>>> ausdex.calc_inflation(26, "July 21 1991",evaluation_date="Sep 1999")
30.27457627118644
```
The dates can be as strings or Python datetime objects.

The values, the dates and the evaluation dates can be vectors by using NumPy arrays or Pandas Series. e.g.
```
>>> df = pd.DataFrame(data=[ [26, "July 21 1991"],[25,"Oct 1989"]], columns=["value","date"] )
>>> df['adjusted'] = ausdex.calc_inflation(df.value, df.date)
>>> df
   value          date   adjusted
0     26  July 21 1991  52.352542
1     25      Oct 1989  54.797048
```
### seifa_vic submodule

```python
>>> from ausdex.seifa_vic import interpolate_vic_suburb_seifa
>>> interpolate_vic_suburb_seifa(2007, 'FOOTSCRAY', 'ier_score')
874.1489807920245
>>> interpolate_vic_suburb_seifa([2007, 2020], 'FOOTSCRAY', 'ier_score', fill_value='extrapolate')
array([874.14898079, 861.68112674])
```

## Dataset and Validation

### Inflation datasets
The Consumer Price Index dataset is taken from the [Australian Bureau of Statistics](https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/consumer-price-index-australia). It uses the nation-wide CPI value. The validation examples in the tests are taken from the [Australian Reserve Bank's inflation calculator](https://www.rba.gov.au/calculator/). This will automatically update each quarter as the new datasets are released.

The CPI data goes back to 1948. Using dates before this will result in a NaN.

### seifa_vic datasets
Data for the socio economic scores by suburbs comes from a variety of sources, and goes between 1986 to 2016 for the index of economic resources, and the index of education and opportunity, other indices are only available for a subset of census years

When this module is first used, data will be downloaded and preprocessed from several locations. Access to the aurin API is necessary via this [form](https://aurin.org.au/resources/aurin-apis/sign-up/). You will be prompted to enter the username and password when you first run the submodule. This will be saved in the app user directory for future use. You can also create a config.ini file in the repository folder with the following:

```toml
[aurin]
username = {aurin_api_username}
password = {aurin_api_password}
```

## Development

To devlop ausdex, clone the repo and install the dependencies using [poetry](https://python-poetry.org/):

```
git clone https://github.com/rbturnbull/ausdex.git
cd ausdex
poetry install
```

You can enter the environment by running:

```
poetry shell
```

The tests can be run using `pytest`.

## Credits

ausdex was written by [Dr Robert Turnbull](https://findanexpert.unimelb.edu.au/profile/877006-robert-turnbull) and [Dr Jonathan Garber](https://findanexpert.unimelb.edu.au/profile/787135-jonathan-garber) from the [Melbourne Data Analytics Platform](https://mdap.unimelb.edu.au/).

Please cite from the article when it is released. Details to come soon.

## Acknowledgements

This project came about through a research collaboration with [Dr Vidal Paton-Cole](https://findanexpert.unimelb.edu.au/profile/234417-vidal-paton-cole) and [A/Prof Robert Crawford](https://findanexpert.unimelb.edu.au/profile/174016-robert-crawford). We acknowledge the support of our colleagues at the Melbourne Data Analytics Platform: [Dr Aleksandra Michalewicz](https://findanexpert.unimelb.edu.au/profile/27349-aleks-michalewicz) and [Dr Emily Fitzgerald](https://findanexpert.unimelb.edu.au/profile/196181-emily-fitzgerald).

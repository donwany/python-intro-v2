## Frameworks
- Typer
- Click
- ArgParser
- Fire


## CLI
```bash
# long format
llamafactory-cli train --epochs 5 --stage sft --finetuning_type lora --dataset <DATASET>

# short format
llamafactory-cli train -e 5 -s sft -f lora -d <DATASET>

llamafactory-cli train -e 25 -s full -f dpo -d <DATASET>
```

```bash
# long cut
python app_v2.py --name Trump --age 120
python app_v2.py --name=Trump --age=120
python app_v2.py --age 20 --name Joe

# short cut
python app_v2.py -a 20 -n Joe 

# using uv
uv run app_v2.py -a 20 -n Joe
uv run app_v2.py -a=20 -n=Joe
uv run app_v2.py --name Trump --age 120

# giving our own special name
wontumi --name Trump --age 120
```

### Fare Estimator
```bash
uv run app_v3.py --base 3.5 --distance 120 --rate 0.09
uv run app_v3.py --base=3.5 --distance=120 --rate=0.09

uv run app_v3.py -b 3.5 -d 120 -r 0.09
uv run app_v3.py -b=3.5 -d=120 -r=0.09

uv run app_v3.py --rate=0.09

fare-calculator --base=3.5 --distance=120 --rate=0.09
uber-fare --base=3.5 --distance=120 --rate=0.09
```


```bash
python app_v3.py --help

python app_v3.py info customers.csv
python app_v3.py head customers.csv
python app_v3.py head customers.csv --rows 20
python app_v3.py search customers.csv --column name --value Alice

python app_v3.py info --help
python app_v3.py head --help
python app_v3.py search --help
```

## Weather CLI
```
weather-cli/
│
├── pyproject.toml
├── README.md
├── src/
│   └── weather_cli/
│       ├── __init__.py
│       └── cli.py
│
└── tests/
```
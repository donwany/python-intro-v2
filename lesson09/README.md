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
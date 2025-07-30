# Playwright DEMO POC

Jednoduchá ukázka automatizovaného testu v Pythonu pomocí Playwright.

## Jak spustit

1. Nainstaluj Playwright:
```bash
pip install -r requirements.txt
playwright install
```

2. Spusť test:
```bash
python run_tests.py
```
* spusti test_example ve slozce tests 


## Je tu nekolik moznosti spustit jednoduche testy 

```bash
python run_tests.py
```

## nebo vice komplexni , ktere spusti kontrolu ve vice prohlizecich

- jsou ve slozce run_test2
- tip:: pro jednoduchost je spoustime primo ze slozky

## mame moznosti 
 * spusti testy v kazdem prohlizeci a vypise kazdy prohlizec zvlast 
```bash
python test_complex.py
```

* spusti testy v kazdem prohlizeci a vypise jen testOK

```bash
python run_test2.py
```



import json

## Python , JSON verileriyle çalışmak için kullanılabilen, adlı yerleşik bir pakete sahiptir

## Bir JSON dizeniz varsa, yöntemi kullanarak onu ayrıştırabilirsiniz



x =  '{ "isim":"Berk", "yas":25, "sehir":"İstanbul"}'

y = json.loads(x)

print(y["age"])

## json.dumps() - Bir Python nesneniz varsa, yöntemi kullanarak onu bir JSON dizesine dönüştürebilirsiniz

x = {
  "isim": "Berk",
  "yas": 25,
  "sehir": "İstanbul"
}

y = json.dumps(x)

print(y)

## Example

print(json.dumps({"isim": "Berk", "yas": 30}))
print(json.dumps(["karpuz", "çilek"]))
print(json.dumps(("karpuz", "çilek")))
print(json.dumps("Merhaba"))
print(json.dumps(25))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "isim": "Berk",
  "yas": 25,
  "evlilik": True,
  "Ayrilmis": False,
  "cocuk": ("Lisa","Dean"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "BMW F30", "mpg": 24.1}
  ]
}

print(json.dumps(x))
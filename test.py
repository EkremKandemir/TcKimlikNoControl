from zeep import Client

service_url = "https://tckimlik.nvi.gov.tr/Service/KPSPublic.asmx?wsdl"
client = Client(service_url)

result = client.service.TCKimlikNoDogrula(
    TCKimlikNo='1111111111',
    Ad='Ekrem',
    Soyad='kandemir',
    DogumYili=1997
)
print(result)



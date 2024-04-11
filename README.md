
![Logo](https://www.mallpaseoross.cl/wp-content/uploads/2018/02/Logo-Cineplanet-1000x1000px-copia.png)


# CineSecureHub

CineSecureHub es un proyecto de encriptación y desencriptación de datos sensibles utilizando la lógica de una aplicación web para proteger la confidencialidad de la información. Este proyecto utiliza el algoritmo de encriptación AES (Advanced Encryption Standard) en modo CBC (Cipher Block Chaining) para garantizar la seguridad de los datos transmitidos.


## Características
- Encriptación de datos sensibles utilizando AES en modo CBC.
- Desencriptación segura de datos cifrados.
- Uso de claves y vectores de inicialización (IV) protegidos.
## Instalación
**1.-** Clona este repositorio en tu máquina local:
```bash
  $ git clone https://github.com/TU_USUARIO/CineSecureHub.git
```
**2.-** Asegúrate de tener Python 3.x instalado en tu sistema.

**3.-** Instala las dependencias requeridas:
```bash
  $ pip install -r requirements.txt
```
## Screenshots

- Desencriptación del payload de autenticación
![App Screenshot](https://i.ibb.co/XsC1Mqb/payload-Login.png)

- Información desencriptada
```json
{
  "ErrorDescription": null,
  "LoyaltyMember": {
    "MemberId": "PP10****43",
    "Hash": "",
    "MemberIdTagg": "51-52-**-57-**-53-48-**-80-80",
    "FirstName": "R***DO V****IR",
    "LastName": "VA****OS",
    "FullName": "R***DO V****IR VA****OS",
    "CardNumber": "10****43",
    "MobilePhone": "(99) 6**-**91",
    "HomePhone": "() ***-1665",
    "Email": "r*****7@gmail.com",
    "ClubID": "1",
    "BalanceList": [
      {
        "BalanceTypeID": "1",
        "LifetimePointsBalanceDisplay": 478,
        "Message": "",
        "Name": "PUNTOS",
        "NameAlt": "",
        "NameTranslations": [],
        "PoinsRemaining": 0,
        "RedentionRate": 0
      },
      {
        "BalanceTypeID": "2",
        "LifetimePointsBalanceDisplay": 16,
        "Message": "",
        "Name": "VISITAS",
        "NameAlt": "",
        "NameTranslations": [],
        "PoinsRemaining": 0,
        "RedentionRate": 0
      },
      {
        "BalanceTypeID": "4",
        "LifetimePointsBalanceDisplay": 0,
        "Message": "",
        "Name": "COMBO STAFF",
        "NameAlt": "",
        "NameTranslations": [],
        "PoinsRemaining": 0,
        "RedentionRate": 0
      },
      {
        "BalanceTypeID": "5",
        "LifetimePointsBalanceDisplay": 0,
        "Message": "",
        "Name": "CLub Intercorp",
        "NameAlt": "",
        "NameTranslations": [],
        "PoinsRemaining": 0,
        "RedentionRate": 0
      }
    ],
    "UserName": "10****43",
    "Password": "",
    "MiddleName": "DN",
    "Address1": "Jiron Be****rio Flores **** dpto ***",
    "State": "15",
    "City": "1501",
    "ZipCode": "150121",
    "SendNewsletter": true,
    "EducationLevel": 1,
    "HouseHoldInCome": 0,
    "PersonsInHousehold": 1,
    "DateOfBirth": "/Date(226022400000)/",
    "Status": "",
    "Suburb": "150109",
    "Gender": "Male",
    "PickupComplex": 0,
    "PreferredComplex": 28,
    "PreferredComplexList": [
      "5",
      "12",
      "28"
    ],
    "PreferenceList": [],
    "ClubName": "CINEPLANET",
    "ContactByThirdParty": false,
    "ExpireDate": null,
    "WishToReceiveSMS": false,
    "WorkZipCode": "CONTRERAS",
    "CardList": [
      "10559843"
    ],
    "PreferredGenres": [],
    "Occupation": 0,
    "MaritalStatus": "S",
    "MailingFrequency": "",
    "Pin": null,
    "Memberships": null,
    "ExpiryPointsList": [
      {
        "BalanceTypeId": 1,
        "ExpireOn": "/Date(1706763600000-0500)/",
        "PointsExpiring": 259.25
      },
      {
        "BalanceTypeId": 3,
        "ExpireOn": "/Date(1706763600000-0500)/",
        "PointsExpiring": 64.0
      }
    ],
    "MemberLevelId": 4,
    "MemberLevelName": "PLATA",
    "LoyaltySessionExpiry": "/Date(1691078796663-0500)/",
    "GiftCard": false,
    "GiftCardBalance": 0,
    "IsBannedFromMakingUnpaidBookingsUntil": null,
    "MembershipActivated": true,
    "MemberItemId": null,
    "ExternalID": "",
    "NationalID": "10****43",
    "PushNotificationSubscription": null,
    "IsAnonymous": false,
    "MemberLanguageIETFCode": "en",
    "SubscriptionCategories": null,
    "Custom1": null,
    "AllowProfilingByThirdParty": "false",
    "PhotoCanBeUpdated": "true",
    "PhotoUri": null,
    "PhotoWidth": null,
    "PhotoHeight": null,
    "PhotoExpiryUtc": null,
    "Subscriptions": null
  },
  "Result": 0,
  "IsWebAccountActivated": true,
  "MemberStatus": 0,
  "encResponse": null
}
```
## Nota
La key de **encriptación** y el **iv** no estan puestas, ya que no pienso publicarlas.

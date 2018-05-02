# JobNative Externe API

## Idee:

ˋGET/searchˋ sucht auf dem server nach den passenden Jobs und returned ein json mit einer ˋIDˋ und den ˋtitleˋ von den Jobs.
Diese IDs und Title werden dann auf der Suchergebis Seite angezeigt und beim klicken suf einen Job holt er eich 
die entsprechend vollständigen datenbank eintrag zu dem Job als JSON.

## GET
`GET/search/KEYWORD`

```json
{
  "search": "KEYWORD",
  "jobs": [
    {
      "jobtitle": "Job Title1(KEYWORD)",
      "username": "USERNAME",
      "datum": "1.1.2001",
      "tags": [
        "tag1",
        "tag4",
        "tag5"
      ],
      "beschreibung": "Eine Lange Beschreibung des Jobs",
      "kontakt": {
        "adresse": "An der Addrese 3, 45898 Addresstadt",
        "email": "mail@jobtitle.de",
        "telefon": 1242145315
      }
    },
    {
      "jobtitle": "Job Title2(KEYWORD)",
      "username": "USERNAME",
      "datum": "1.1.2001",
      "tags": [
        "tag2",
        "tag7",
        "tag8"
      ],
      "beschreibung": "Eine Lange Beschreibung des Jobs",
      "kontakt": {
        "adresse": "An der Addrese 3, 45898 Addresstadt",
        "email": "mail@jobtitle.de",
        "telefon": 1242145315
      }
    },
    {
      "jobtitle": "Job Title3(KEYWORD)",
      "username": "USERNAME",
      "datum": "1.1.2001",
      "tags": [
        "tag3",
        "tag9",
        "tag10"
      ],
      "beschreibung": "Eine Lange Beschreibung des Jobs",
      "kontakt": {
        "adresse": "An der Addrese 3, 45898 Addresstadt",
        "email": "mail@jobtitle.de",
        "telefon": 1242145315
      }
    }
  ]
}
```

`GET/search/KEYWORD?tags=tag1,tag3`

```json
{
  "search": "KEYWORD",
  "tags": [
    "tag1",
    "tag3"
  ],
  "jobs": [
    {
      "jobtitle": "Job Title1(KEYWORD)",
      "username": "USERNAME",
      "datum": "1.1.2001",
      "tags": [
        "tag1",
        "tag4",
        "tag5"
      ],
      "beschreibung": "Eine Lange Beschreibung des Jobs",
      "kontakt": {
        "adresse": "An der Addrese 3, 45898 Addresstadt",
        "email": "mail@jobtitle.de",
        "telefon": 1242145315
      }
    },
    {
      "jobtitle": "Job Title3(KEYWORD)",
      "username": "USERNAME",
      "datum": "1.1.2001",
      "tags": [
        "tag3",
        "tag9",
        "tag10"
      ],
      "beschreibung": "Eine Lange Beschreibung des Jobs",
      "kontakt": {
        "adresse": "An der Addrese 3, 45898 Addresstadt",
        "email": "mail@jobtitle.de",
        "telefon": 1242145315
      }
    }
  ]
}
```

## Post

`POST/register`

```json
{
  "username": "USERNAME",
  "unternehmen": "UNTERNEHMENS NAME",
  "email": "EMAIL", // for later use
  "password": "PASSWORD"
}
```

`POST/createJob`

```json
{
  "jobtitle": "Job Title1(KEYWORD)",
  "username": "USERNAME",
  "datum": "1.1.2001",
  "tags": [
    "tag1",
    "tag4",
    "tag5"
  ],
  "beschreibung": "Eine Lange Beschreibung des Jobs",
  "kontakt": {
    "adresse": "An der Addrese 3, 45898 Addresstadt",
    "email": "mail@jobtitle.de",
    "telefon": 1242145315
  }
}
```

> Authentication via Session Cookie

#Programming/Projects/JobNative
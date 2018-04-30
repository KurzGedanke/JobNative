# JobNative Externe API
## GET
`GET/search/KEYWORD`

```json
{
  "search": "KEYWORD",
  "jobs": [
    {
      "jobtitle": "Job Title1(KEYWORD)",
      "user_in": "TestNutzer*in",
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
      "user_in": "TestNutzer*in",
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
      "user_in": "TestNutzer*in",
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
	"tags": ["tag1", "tag3"]
  "jobs": [
    {
      "jobtitle": "Job Title1(KEYWORD)",
      "user_in": "TestNutzer*in",
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
      "user_in": "TestNutzer*in",
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
```

`POST/createJob`

```json
```

> Authentication via Session Cookie

#Programming/Projects/JobNative
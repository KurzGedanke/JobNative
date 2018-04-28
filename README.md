# JobNative (Arbeitstittel)
#Programming/Projects/JobNative

## Motivation
Eine Job Börse für Unternehmen/Organisationen/Institute*1 die versuchen sich aus Kapitalistischen Strukturen zu entziehen und eine faire Arbeitsweise, faire Bezahlung und Nachhaltigkeit bieten.
Im Grunde, *1 die Nachhaltig, Respektvoll und Bewusst handeln, sowohl für die Umwelt, als auch für Mensch oder Maschine. 

## Durchführung
Eine Online Job Börse (vielleicht irgendwann mal Job Messen?), wo solche Unternehmen Stellen einstellen können. 

## Anforderung
- [ ] Startseite + Suche
- [ ] Suche
- [ ] Suche nach bestimmten Tags (Feld, Befristung, Anstellungsart etc.)
- [ ] Erstellen von Unternehmen
- [ ] Einstellungen von Jobs
- [ ] Unternehmen Ratings System? 
- [ ] Auflistung der Unternehmen


## Stack
- Python 3.6
- Flask
- SQLITE (sqlalchemie)
- JavasScript
- jQuery
- VueJS
- HTML
- CSS Grid

## Architektur
Aufbau soll eine statische Website sein, die sich aus einer json API die Daten (Infos zu Unternemen, Infos zu Job, Erstellung der Angebot, anlegen von Accounts) holt um sie dann Lokal darzustellen. 
Bringt den Vorteil, dass einfache Entwicklungen von Apps, anderen Frontends möglich ist. 

## Probleme 
Wie verifizieren wir ein Unternehmen? 
-> Manuelle Verifikation aufgrund von Arbeitslast nicht möglich.

-> User*innen Rating könnte aufgrund von Angriffen verfälschst werden. Für größere bekannten Marken bestimmt auffangbar, für kleinere unbekannte definitiv nicht. 

-> Auf die Menschen vertrauen? Auf die Unternehmen vertrauen? 

-> Lieber den weg andersrum nehmen: auf Meldungen von Usern eingehen. 

-> Wikipedia Prinzip? User*innen können Kommentare einrichen, müssen diese aber belegen. 
# OTP Šifrēšanas un Dešifrēšanas Rīks 🛡️🔒

## Apraksts 📝

Šis Python skripts ir izstrādāts, lai nodrošinātu drošu failu šifrēšanu un dešifrēšanu, izmantojot vienreizējo piezīmjdatoru (One-Time Pad, OTP) metodi. Skripts var strādāt ar dažāda veida failiem, piemēram, teksta, video, attēlu un citiem binārajiem failiem.

## Funkcionalitāte 🎛️

- **Šifrēšana (`enc`)**: Šifrē jūsu izvēlēto failu, izmantojot kriptogrāfiski drošu gadījuma skaitļu ģeneratoru. Izveido OTP failu un šifrētu failu.
- **Dešifrēšana (`dec`)**: Atšifrē failu, izmantojot attiecīgo OTP failu.

## Kā izmantot? 🤔

1. **Šifrēšanai**:  
   ```
   python otp.py enc ieejas_fails.jpg otp.bin šifrētais_fails.bin
   ```
   
2. **Dešifrēšanai**:  
   ```
   python otp.py dec šifrētais_fails.bin otp.bin atšifrētais_fails.jpg
   ```

3. **Interaktīvajā režīmā**:  
   ```
   python otp.py
   ```
   un sekot aicinājumiem.


4. **Vizuālajā režīmā (Komentēta versija):**:  
   ```
   python main.py
   ```
   un sekot aicinājumiem.
   
   Šī ir komentēta versija šīm pašam kodam ar sīkākiem aprakstiem un pamācībām. Tā ir paredzēta, lai palīdzētu izprast kodu un tā darbību.



## Prasības 📋

- Python 3.
- Operētājsistēma, kura atbalsta Python
- Priekš Vizuālā režīma - PyQt6

## Drošība 🔐

Šis rīks izmanto `os.urandom()` funkciju, lai ģenerētu kriptogrāfiski drošus gadījuma baitus. Tas ir piemērots visām kriptogrāfiskajām lietojumprogrammām.


## Licence 📄

Šis projekts ir izstrādāts tikai apmācību nolūkos.

---

Šis projekts ir izstrādāts priekš "Applied Cryptography" kursa. Lai jums veicas! 🍀👨‍🎓

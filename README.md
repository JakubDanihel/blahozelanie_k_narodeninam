# blahozelanie_k_narodeninam
Jednoduchy projekt ktory rozposle mail pre osobu ktora ma teraz narodeniny. Program napisany v python3.11

## Ako to funguje

Skript vykoná nasledujúce kroky:

1.  **Zistenie Dátumu:** Zistí aktuálny mesiac a deň a uloží ich ako *tuple* (napr. `(11, 16)`).
2.  **Načítanie Dát:** Použije knižnicu `pandas` na načítanie súboru `birthdays.csv`.
3.  **Vytvorenie Slovníka:** Prevedie dáta z CSV na Python slovník (dictionary). Kľúčom je *tuple* `(mesiac, deň)` a hodnotou je celý riadok s údajmi o osobe (meno, email, atď.). Toto umožňuje veľmi rýchle vyhľadávanie.
4.  **Kontrola Zhody:** Skontroluje, či sa dnešný *tuple* `(mesiac, deň)` nachádza v kľúčoch slovníka.
5.  **Ak je zhoda (dnes sú narodeniny):**
    * Vyberie náhodnú šablónu zo zložky `letter_templates` (napr. `letter_1.txt`).
    * Načíta obsah šablóny a nahradí zástupný text `[NAME]` skutočným menom oslávenca.
    * Pomocou `smtplib` sa pripojí k SMTP serveru Gmailu.
    * Prihlási sa pomocou údajov `MY_MAIL` a `MY_PW`.
    * Odošle personalizovaný e-mail na e-mailovú adresu oslávenca.

## Požiadavky a Nastavenie

Aby skript fungoval, musíte mať splnené nasledujúce požiadavky.

### 1. Knižnice

Uistite sa, že máte nainštalovanú knižnicu `pandas`:
```bash
pip install pandas

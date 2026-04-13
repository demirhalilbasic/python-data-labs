import pandas as pd

izvjestaj = pd.read_csv("src/policijski_izvjestaj.csv")
osumnjiceni = pd.read_csv("src/osumnjiceni.csv")
kartice = pd.read_csv("src/pristupne_kartice.csv")
svjedoci = pd.read_csv("src/izjave_svjedoka.csv")
telefoni = pd.read_csv("src/telefonski_zapisi.csv")
finansije = pd.read_csv("src/finansijski_zapisi.csv")

print(f"Osumnjicenih: {len(osumnjiceni)}")
print(f"Pristupnih zapisa: {len(kartice)}")
print(f"Telefonskih zapisa: {len(telefoni)}")
print(f"Finansijskih zapisa: {len(finansije)}")

ubistvo = izvjestaj[izvjestaj["tip"] == "ubistvo"]
print(ubistvo[["datum", "vrijeme", "lokacija", "opis"]].to_string(index=False))

tech_hub_15 = kartice[(kartice["zgrada"] == "Tech Hub") &
                      (kartice["datum"] == "2026-03-15")]

u_zgradi = tech_hub_15.merge(osumnjiceni, on="ime_prezime")

print(f"Ukupno ulazaka: {len(tech_hub_15)}")
print(f"Od toga osumnjicenih: {len(u_zgradi)}")
print(u_zgradi[["ime_prezime", "vrijeme_ulaza",
                "vrijeme_izlaza", "veza_sa_zrtvom"]].to_string(index=False))

tech_hub_sve = kartice[kartice["zgrada"] == "Tech Hub"]
sve = tech_hub_sve.merge(osumnjiceni, on="ime_prezime")
print(sve.groupby("ime_prezime")["datum"].nunique()
      .sort_values(ascending=False).to_string())

print(u_zgradi["ime_prezime"].value_counts().to_string())

# Zadatak 1
tech_hub = kartice[(kartice["zgrada"] == "Tech Hub") &
                    (kartice["datum"] == "2026-03-15")]
spojeno = tech_hub.merge(osumnjiceni, on="ime_prezime")
print(spojeno[["ime_prezime", "vrijeme_ulaza", "vrijeme_izlaza",
                "veza_sa_zrtvom"]].to_string(index=False))

tokom = spojeno[
    (spojeno["vrijeme_izlaza"] > "19:30") |
    (spojeno["vrijeme_izlaza"].isna())
]
print(tokom[["ime_prezime", "vrijeme_ulaza",
              "vrijeme_izlaza"]].to_string(index=False))

# Zadatak 2
emir_izjave = svjedoci[svjedoci["spominje_osumnjicenog"] == "Emir Begović"]
print(emir_izjave[["izjava_id", "vrijeme", "svjedok", "opis"]].to_string(index=False))

dino_izjave = svjedoci[svjedoci["svjedok"] == "Dino Delić"]
print(dino_izjave[["vrijeme", "lokacija", "opis"]].to_string(index=False))

nepoznati = svjedoci[svjedoci["spominje_osumnjicenog"].isna() |
                      (svjedoci["spominje_osumnjicenog"] == "")]
print(nepoznati[["izjava_id", "vrijeme", "opis"]].to_string(index=False))

print(osumnjiceni[(osumnjiceni["visina_cm"] > 180) &
                   (osumnjiceni["boja_kose"] == "crna")]
      [["ime_prezime", "visina_cm", "boja_kose"]].to_string(index=False))

# Zadatak 3
sa_imenima = telefoni.merge(
    osumnjiceni[["ime_prezime", "telefon"]],
    left_on="telefon_pozivatelja",
    right_on="telefon", how="left")
sa_imenima = sa_imenima.rename(columns={"ime_prezime": "pozivatelj"})

sa_imenima = sa_imenima.merge(
    osumnjiceni[["ime_prezime", "telefon"]],
    left_on="telefon_primaoca",
    right_on="telefon", how="left",
    suffixes=("", "_primalac"))
sa_imenima = sa_imenima.rename(columns={"ime_prezime": "primalac"})

emir_kasno = sa_imenima[
    (sa_imenima["pozivatelj"] == "Emir Begović") &
    (sa_imenima["datum"] == "2026-03-15") &
    (sa_imenima["vrijeme"] > "20:00")]
print(emir_kasno[["vrijeme", "telefon_primaoca", "primalac",
                   "trajanje_sekundi"]].sort_values("vrijeme")
      .to_string(index=False))

# Zadatak 4
finansije["iznos_KM"] = finansije["iznos_KM"].astype(float)

bilans = finansije.groupby("ime_prezime")["iznos_KM"].sum().sort_values()
print(bilans)

osiguranje = finansije[finansije["kategorija"] == "osiguranje"]
print(osiguranje[["ime_prezime", "iznos_KM", "opis"]].to_string(index=False))

neuspjele = finansije[finansije["iznos_KM"] == 0]
print(neuspjele[["ime_prezime", "datum", "opis"]].to_string(index=False))

print("=" * 55)
print("IZVJEŠTAJ O ISTRAZI — Slučaj Dr. Emina Softić")
print("=" * 55)
print(f"Počinilac: Emir Begović (42), poslovni partner")
print(f"Motiv: Dugovi od -42,600 KM + polica životnog")
print(f"       osiguranja na žrtvu (korisnik: Emir)")
print(f"Dokaz 1: Pristupna kartica — ušao 18:45,")
print(f"         izašao 21:10. Jedini osumnjičeni u")
print(f"         zgradi tokom ubistva (19:30-20:30).")
print(f"Dokaz 2: Svjedok vidio visokog muškarca, tamna")
print(f"         kosa (188cm, crna) kako izlazi iz")
print(f"         kancelarije 301 u 20:15, uznemiren.")
print(f"Dokaz 3: U 20:20 zvao nepoznat broj 066999000")
print(f"         (45s). Ponovo u 22:00 (30s).")
print(f"Dokaz 4: groupby().sum() = -42,600 KM duga.")
print(f"         Polica osiguranja: korisnik u slučaju")
print(f"         smrti žrtve je Emir Begović.")
print("=" * 55)
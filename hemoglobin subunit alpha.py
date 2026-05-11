from Bio import Entrez, SeqIO

Entrez.email = "antoni@example.com"

def pobierz_gen(gene_id):
    try:
        print(f"📡 Łączenie z serwerem NCBI dla ID: {gene_id}...")
        with Entrez.efetch(db="nucleotide", id=gene_id, rettype="gb", retmode="text") as handle:
            record = SeqIO.read(handle, "genbank")

        for f in record.features:
            if f.type == "CDS":
                bialko = f.qualifiers.get('translation', [''])[0]
                produkt = f.qualifiers.get('product', ['Nieznane'])[0]
                print(f"\n✅ PRODUKT: {produkt}")
                print(f"🧬 SEKWENCJA: {bialko}")

               
                with open("wynik_bio.txt", "w") as plik:
                    plik.write(f"Produkt: {produkt}\nBialko: {bialko}")
                print("\n💾 Wynik zapisano w pliku wynik_bio.txt")
                return
    except Exception as e:
        print(f"❌ Coś poszło nie tak: {e}")

pobierz_gen("NM_000558")

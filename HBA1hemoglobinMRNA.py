from Bio import Entrez, SeqIO

Entrez.email = "antoni@example.com"

print("🚀 Łączenie z bazami w USA...")

with Entrez.efetch(db="nucleotide", id="NM_000558", rettype="fasta", retmode="text") as handle:
    record = SeqIO.read(handle, "fasta")

print(f"\n✅ Pobrano: {record.description}")
print(f"🧬 Długość genu: {len(record.seq)} nukleotydów")
print(f"🔍 Pierwsze 50 liter: {record.seq[:50]}...")

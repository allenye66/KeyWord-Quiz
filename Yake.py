import yake

text = "Endonucleases are enzymes that cleave the phosphodiester bond within a polynucleotide chain."
kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(text)

for kw in keywords:
	print(kw)

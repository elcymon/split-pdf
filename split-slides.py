import PyPDF2

outNames = ['FoV-Ath-Simulations-Uniform', 'FoV-Ath-Simulations-OneCluster',
			'FoV-Ath-Simulations-TwoClusters','Fov-Ath-Simulations-FourClusters',
			'FoV-Ath-Simulations-HalfCluster','TwoClusters-5-vs-10-rps-v1',
			'TwoClusters-5-vs-10-rps-v2','TwoCluster-RepAtt-Noise-v-qSize']

with open('Results-PowerPoint.pdf', 'rb') as infile:
	reader = PyPDF2.PdfFileReader(infile)
	
	for i in range(reader.getNumPages()):
		writer = PyPDF2.PdfFileWriter()
		writer.addPage(reader.getPage(i))
		
		with open(outNames[i]+'.pdf','wb') as outfile:
			writer.write(outfile)
	

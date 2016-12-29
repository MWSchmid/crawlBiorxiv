# crawlBiorxiv
Small script to crawl biorxiv (and extract the info where the articles are published)

I was once asked where the articles on biorxiv are published later on. Well - I wasn't exactly asked for this - the statement was rather: "once your manuscript is on biorxiv, no good journal wants it anymore". As I couldn't find any information on where the articles on biorxiv get published afterwards, I wrote this small crawler script and created a [table with the number of publications per journal on biorxiv](journalCounts.csv). Note that the table is sorted and contains only Journals with more than one article. The table [linkPublishedIn.txt](linkPublishedIn.txt) contains the original data with each article and the info where it's published (28th of December 2016). I changed "ELife" into "eLife", but some other journals may still have double names and are therefore not recognized correctly in the table with the counts (some counts may therefore be underestimated).

I think that the top 50 entries of the table are enough to disprove the statement that "once your manuscript is on biorxiv, no good journal wants it anymore":

| journal                                | frequency |
|----------------------------------------|----------:|
| unpublished                            | 4918      |
| PLOS ONE                               | 157       |
| Bioinformatics                         | 120       |
| Scientific Reports                     | 103       |
| eLife                                  | 97        |
| Genetics                               | 91        |
| PLOS Genetics                          | 73        |
| PNAS                                   | 70        |
| PLOS Computational Biology             | 69        |
| G3: Genes\|Genomes\|Genetics             | 66        |
| Nucleic Acids Research                 | 55        |
| Genome Biology                         | 54        |
| Nature Communications                  | 48        |
| Genome Research                        | 46        |
| BMC Genomics                           | 44        |
| Molecular Biology and Evolution        | 38        |
| BMC Bioinformatics                     | 34        |
| Molecular Ecology                      | 27        |
| Nature Genetics                        | 27        |
| NeuroImage                             | 25        |
| PeerJ                                  | 24        |
| Evolution                              | 23        |
| Genome Biology and Evolution           | 23        |
| Nature Methods                         | 21        |
| American Journal of Human Genetics     | 20        |
| Systematic Biology                     | 20        |
| F1000Research                          | 18        |
| Cell Reports                           | 17        |
| Journal of the Royal Society Interface | 16        |
| Journal of Theoretical Biology         | 16        |
| PLOS Neglected Tropical Diseases       | 16        |
| Genome Medicine                        | 15        |
| Biology Open                           | 14        |
| Frontiers in Microbiology              | 14        |
| GigaScience                            | 14        |
| ACS Synthetic Biology                  | 13        |
| Biophysical Journal                    | 13        |
| Journal of Neuroscience                | 13        |
| Molecular Biology Of The Cell          | 13        |
| Molecular Ecology Resources            | 13        |
| Nature                                 | 13        |
| Nature Neuroscience                    | 13        |
| Molecular Biology And Evolution        | 12        |
| PLOS Biology                           | 12        |
| Proceedings B                          | 12        |
| Science                                | 12        |
| Development                            | 11        |
| Journal of Evolutionary Biology        | 11        |
| mBio                                   | 11        |
| Theoretical Population Biology         | 11        |

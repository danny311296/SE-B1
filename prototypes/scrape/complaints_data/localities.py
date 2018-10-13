import csv

l = [["locality"]]

localities = ['Ashoknagar','Austin Town','Avenue Road','Balepet','Balepete','Benson Town','Bestamaranahalli','Bharati Nagar','Brigade Road','Brunton Road','Central Street','Chakravarthy Lane','Chickpet','Chikpet','Chord Road','Church Street','Commercial Street','Cooke Town','Cox town','Coxtown','Crescent Road','Cubban Road','Cubbon Road','Cubbonpet','Cunningham','Cunningham Road','Dickenson Road','Dr. ambedkar veedhi','Ebrahim Sahib Street','Edward Road','Gayathrinagar','Gayatri Nagar','Haines Road','Harogadde','Hennagara','High Grounds','Hulimangala','Indalavadi','Infantry Road','Iyengar Road','J.C. Road','Jayachamaraja Road','Jumma Masjid Road','K. Kamraj Road','K.P.west','Kamaraj Road','Kasturba Road','Kilari Road','Kumara Krupa Road','KUMARAPARK','Lady Curzon Road','Lalbagh West','Langford Town','Lavelle Road','Madhava Nagar','Magadi Main Road','Magadi Road','Magrath Road','Mahatma Gandhi road','Mamulpet','Manjunatha Nagar','Marsur','Mavalli','MG Railway Colony','Millers Road','Minerva Circle','Mission Road','Museum Road','Nagarathpet','Narayan Pillai street','Narayana Pillai Street','Nrupathunga Road','Okalipuram','P&t Col. kavalbyrasandra','Palace Road','Pasmpamahakavi Road','Prakash Nagar','Promenade Road','Queens Road','Raj Bhavan Road','Raja Ram Mohan Roy Road','Rajbhavan','Ramachandrapuram','Residency Road','Rest House Road','Richmond Road','Richmond Town','S. R. Nagar','Samandur','Sampangiram Nagar','Sampangiramnagar','Seppings Road','Seshadri Road','Shankarapuram','Shankarpura','Shanthinagar','Shivaji Nagar','Shivajinagar','Sidihoskote','Sivan Chetty gardens','Srirampuram','St. Johns Road','St. Marks Road','Subbarama Chetty Road','Subedar Chatram Rd','Subedar Chatram Road','Thammanayakanahalli','Thimmaiah Road','Ulsoor','Vanakanahalli','Vasanth Nagar','Vasanthnagar','Victoria Layout','Visveswarapuram','Vittal Mallya Road','Vittalnagar','Agrahara','Airport Road','Akshaya Nagar','Ali Asker Road','Amruthahalli','Baiyappanahalli','Ballandur','Bangalore Air port','Basavanagar','Bellandur','Brookefield','Brookfield Road','Brookfields','C. V. Raman Nagar','C.V. Raman Nagar','C.V.raman nagar','Devanagundi','Devasandra','Doddanakundi','Doddanekkundi','Domlur','Domlur Layout','Dooravani Nagar','Doorvaninagar','Fraser Town','Frazer Town','Frazertown','Gangadhar Chetty Road','GR Tech Park','Gunjur','H.A.l ii stage','HAL Airport','HAL Airport Road','HAL Road','Haralur Road','Harlur Road','Hoodi','HRBR Layout','Immedihalli','Indira Nagar','Indiranagar','Indiranagar Com. complex','ITPL Road','J C Nagar','J. C. Nagar','J.C. Nagar','J.C.nagar','Jayamahal Road','Jeevan Bheema Nagar','Jeevan Bhima Nagar','Jeevanbhima Nagar','Jeevanbhimanagar','Kadugodi','Kaggadasapura','Kaggalipura','Kaggdaspura','Kalkunte','Kannamangala','Kasavanahalli','Kasavanhalli','Kodihalli','Koramangala','Koramangala I block','Koramangala Vi bk','KR Puram','Krishnaraja Puram','Krishnarajapuram','Krishnarajapuram R s','Kundalahalli','M.H. Colony','Mahadevapura','Mahadevapura Post','Mahadevpura Post','Malleshpalya','Marathahalli','Marathahalli Colony','Medimallasandra','Murugeshpalya','Muthusandra','Naduvathi','Nal','Old Airport Road','Old Madras Road','Panathur','Ramagondanahalli','Ramamurthy Nagar','Rameshnagar','S M Road','S. V. Road','Samethanahalli','St. john\'s medical college','Thippasandra','Training Command iaf','Udaypura Post','Varthur','Vartur','Vibhutipura','Vimanapura','Vimapura','Whitefield','Whitefield','Whitefield Sarjapur','Whitefield-Sarjapur','Yemalur','Allalasandra','Anandnagar','Arabic College','Aranya Bhavan','Attur','Bagalgunte','Bagalkunte','Bagalur Road','Banaswadi','Bel Road','Bellary Road','Bennigana Halli','Bhuvaneshwari Nagar','Bsf Campus yelahanka','Byappanahalli','Byatarayanapura','Byatarayanapura','Cholanayakkanahilli','Coles Road','Crpf Campus yelahanka','Damodaran Road','Dasarahalli','Dasarahalli','Devanahalli','Devarjeevanahalli','Dodda Bomasandra','Dollars Colony','Embassy Manyatha Tech Park','G.K.V.K','G.K.V.K Post','G.K.v.k.','Ganga Nagar','Ganga Nagar Extension','Gangenahalli','Geddalahalli','GKVK Post','Gokula Extension','Goraguntepalya','Govindapalya','Guddadahalli','Guttahalli','H M t','H.A. farm','H.M.T','HBR Layout','Hebbal','Hebbal Agrl Farm','Hebbal Kempapura','Hebbal-Kempapura','Hennur','Hesaraghatta','Hesaraghatta Lake','Hesarghatta Main Rd','Hessaraghatta','HMT Layout','HMT Road','Horamavu','Hutchins Road','Industrial Estate','Industrial state','Jakkur','Jala Hobli','Jalahalli','Jalahalli East','Jalahalli Village','Jalahalli West','Jalavayuvihar','Jaymahal','Jeevanahalli','Kacharakanahalli','Kadugondanahalli','Kalasipalyam','Kalyan Nagar','Kalyanagar','Kamagondanahalli','Kammagondahalli','Kanteeravanagar','Kasturi Nagar','Kasturinagar','Kaval Bairasandra','Kavalbyrasandra','Kempaura','Kendriya Vihar','Kodigehalli','Kothanur','KUMARA PARK','KUMARAPARK SHESHADRIPURAM','Lingarajapuram','M S r road','Malkand Lines','Malleshwaram','Malleswaram','Malleswaram West','Mandalay Lines','Maruthi Nagar','Maruthi Sevanagar','Mathikere','Mathikere Extension','MS Ramaiah Road','Msrit','Nagarvar Kari','Nagasandra','Nagashetty Halli','Nagavara','Nagavara Road','Nalagadderanahalli','Nandhini Layout','Nandidurg Road','Nandidurga Road','Nandini Layout','Nandinilayout','Nelamangala','OMBR Layout','Palace Guttahalli','Peenya','Peenya I stage','Peenya Ii stage','Peenya S.I.','Peenya Small industries','Pulikeshi Nagar','R T nagar','R. K. Puram','R.M.V. Extension','R.M.v. extension ii stage','R.T. Nagar','Rajanakunte','Rajankunte','Ramakrishna Hegde nagar','RMV 2nd stage','RT Nagar','Sadashiv Nagar','Sadashiva Nagar','Sadashivanagar','Sadashivnagar','Sahakara Nagar','Sahakaranagar P.o','Sahakarnagar','Sanjay Nagar','Sanjaynagar','Sankey Road','Saraswathipuram','Science Institute','Seshadripuram','Sharada Nagar','Singanayakanahalli','St. thomas town','Subbaiah Palaya','Sultanpalya','Swimming Pool extn','Tank Bund Road','Tata Nagar','Telecom Layouts','Vaiyyalikaval','Vasant Nagar','Venkatagiri Kote','Venkatarangapura','Venkateshapura','Vyalikaval Extn','Wheel And axle plant','Yelahanka','Yelahanka Road','Yelahanka Satellite town','Yeshwanthpur','Yeshwanthpur Bazar','Yeswanthpur','Yeswanthpura','Agara','Anekal','Anekal Taluk','Anekalbazar','Arakere','Attibele','B Sk ii stage','Banashankari','Banashankari Iii stage','Bannerghatta','Bannerghatta Rd','Bannerghatta Road','Basavanagudi','Basavangudi','Begur Koppa Road','Begur-Koppa Road','Bidaraguppe','Bilekahalli','Bommanahalli','BTM Layout','BTS Layout','Bull Temple Road','Chamrajpet Bazar','Chandrapura','Chikkalasandra','Davanagere','Davangere','Diagonal Road','Doddakallasandra','Doddamavalli','Doddathogur','Doddathogur village','Dommasandra','Ejipura','Electronics city','Electronics City','Gandhi Bazar','Gavipuram','Girinagar','Govindaraj Nagar','Halasuru','Handenahalli','Hanumanthanagar','Harapanahalli','Hebbagodi','Hongasandra','Hosakerehalli','Hosur Road','Hosur Road','Hsr Layout','Hulimavu','ISRO Layout','Ittamadu Layout','J P nagar','J. P. Nagar','J.P. Nagar','Jakkasandra Post','Jaya Nagar','Jayanagar','Jayanagar West','Jayangar East','Jayangar Iii block','Jigani','Journalist Colony','JP Nagar','Jp Nagar iii phase','K.R. Road','Kamanhalli','Kammanahalli','Kanakapura Road','Kathriguppe','Kempapura','Kendriya Sadan','Konanakunte','Kumaraswamy Layout','Kumbalgodu','Kumbaragundi','Lakkasandra','Lakshman Mudaliar Street','Lakshmipura','Madhavan Park','Madivala','Mayasandra','Mico Layout','Mount St joseph','Mudaliar Road','Muthanallur','Nayandahalli','Neelasandra','Neralur','O.T.C. Road','Off Sarjapur Road','Padmanabhanagar','Padmanabhnagar','R.V. Road','Raghavendra Nagar','Raja Rajeshwari Nagar','Rajpet','Ramanashree Nagar','Sarjapur','Sarjapur Road','Sarjapura','Shanti Nagar','Siddaiah Road','Singasandra','State Bank of mysore colony','Subramanyapura','Sunkalpet','Surya city','Tavarekere Road','Thyagarajanagar','Tilak Nagar','Tilaknagar','Uttarahalli','Uttrahlli','V.V.Puram','Vikramnagar','Vivek Nagar','Viveknagar','VV Puram','Walton Road','Wilson Garden','Yadavanahalli','Yediyur','Yelachenahalli','Anubhav Nagar','Avani Sringeri mutt','Bapuji Nagar','Bapujinagar','Basaveshwara Nagar','Basaveshwaranagar','Basaveshwarnagar','Basaveswaranagar Ii stage','Bhashyam Circle','Cambridge Layout','Chamarajpet','Chamrajpet','Chandra Lay out','Chandra Layout','Chikkabettahalli','Gandhi Nagar','Gaviopuram Extension','Gaviopuram Guttanahalli','Hegganahalli','K H b colony','Kamakshipalya','Kempe Gowda Road','Kengeri','Kengiri','KHB Colony','Laggere','Mahalakshmipuram','Mahalakshmipuram Layout','Mudalapalya','Mysore','Mysore Road','N. G. E. F Layout','Nagarbhavi','Narasimharaja Colony','Narasimjharaja Road','Nehru Main Rd','Rajaji Nagar','Rajajinagar','Rajajinagar I block','Rajajinagar Ivth block','Rajarajeshwarinagar','RPC Layout','Srinivas Nagar','Sunkadakatte','Tumkur Road','Ullal','Vidyaranyapura','Vijay Nagar','Vijayanagar','Vijayanagar East']

for locality in localities:
    l.append([locality])

with open('localities.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(l)

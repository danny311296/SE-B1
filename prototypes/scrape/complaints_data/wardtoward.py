from bs4 import BeautifulSoup
import requests
from collections import defaultdict, Counter
import csv
import pandas as pd
import map

import time


def get_top_four(d):
	d = Counter(d)
	l = d.most_common()[::-1]
	print(l)
	return [l[0][0],l[1][0],l[2][0],l[3][0]]


l = [["ward","closest_ward1","closest_ward2","closest_ward3","closest_ward4"]]
wards = ['Yelachenahalli', 'Singasandra', 'Begur', 'Gottigere', 'Anjanapur', 'Uttarahalli', 'Konanakunte', 'Vasanthapura', 'HSR Layout', 'Bommanahalli', 'Jaraganahalli', 'Puttenahalli', 'Bilekahalli', 'Hongasandra', 'Mangammanapalya', 'Arakere', 'Shettyhalli', 'Mallasandra', 'Bagalagunte', 'T-Dasarahalli', 'Chokkasandra', 'Peenya Industrial Area', 'Rajagopala Nagar', 'Hegganahalli', 'Benniganahalli', 'C.V.Raman Nagar', 'Hosathippasandra', 'Sarvagna Nagar', 'Hoysala Nagar', 'Jeevanbhima Nagar', 'Konena Agrahara', 'Radhakrishna Temple', 'Sanjay Nagar', 'Ganga Nagar', 'Hebbal', 'Vishwanathnagenahalli', 'Manorayanapalya', 'Gangenahalli', 'Jayachamarajendra Nagar', 'Kushal Nagar', 'Kavalbyrasandra', 'Devarajeevanahalli', 'Muneshwara Nagar', 'Sagayapuram', 'S.K.Garden', 'Pulikeshi Nagar', 'Nagavara', 'HBR Layout', 'Banasawadi', 'Kammanahalli', 'Kacharakanahalli', 'Kadugondanahalli', 'Lingarajapura', 'Maruthiseva Nagar', 'Jogupalya', 'Shanthala Nagar', 'Dommalur', 'Agaram', 'Vannarpet', 'Neelasandra', 'Shanthi Nagar', 'Ramaswamy Palya', 'Jayamahal', 'Ulsoor', 'Bharathi Nagar', 'Shivaji Nagar', 'Vasanth Nagar', 'Sampangiram Nagar', 'Horamavu', 'Ramamurthy Nagar', 'Vijinapura', 'K.R.Puram', 'Basavanapura', 'Devasandra', 'A.Narayanapura', 'Vignana Nagar', 'HAL Airport', 'Hoodi', 'Garudacharpalya', 'Kadugudi', 'Hagadooru', 'Doddanekkundi', 'Marathalli', 'Varthur', 'Bellandur', 'H.M.T', 'Lakshmidevi Nagar', 'Jalahalli', 'J.P.Park', 'Yeshwanthpur', 'Laggere', 'Kottigepalya', 'Jnanabharathi', 'Rajarajeshwari Nagar', 'Ullalu', 'Kengeri', 'Hemmigepura', 'Dodda Bidarkallu', 'Herohalli', 'Basavangudi', 'Hanumantha Nagar', 'Sri Nagar', 'Giri Nagar', 'Katriguppe', 'Vidyapeetha', 'Lakkasandra', 'Adugodi', 'Ejipura', 'Koramangala', 'Sudduguntepalya', 'Madiwala', 'Jakkasandra', 'BTM Layout', 'Sudam Nagar', 'Dharmarayaswamy Temple', 'Sunkenahalli', 'Visvesvarapuram', 'Siddapura', 'Hombegowda Nagar', 'Jayangar', 'Kaveripura', 'Govindraja Nagara', 'Agrahara Dasarahalli', 'Dr.Rajkumar', 'Marenahalli', 'Maruthi Mandira', 'Moodalapalya', 'Nagarabhavi', 'Nayandanahalli', 'Pattabhiram Nagar', 'Byrasandra', 'Jayanagar East', 'Gurappanapalya', 'J.P.Nagar', 'Sarakki', 'Shakambari Nagar', 'Hosakerehalli', 'Ganeshmandira', 'Karisandra', 'Yadiyuru', 'Banashankari Temple', 'Kumaraswamy Layout', 'Padmanabha Nagar', 'Chikkalasandra', 'Kempapura Agrahara', 'Vijay Nagar', 'Hosahalli', 'Attiguppe', 'Hampi Nagar', 'Bapuji Nagar', 'Gali Anjaneya Swamy Temple', 'Deepanjali Nagar', 'Padarayanapura', 'Jagareevanram Nagar', 'Rayapuram', 'Chalavadipalya', 'K.R.Market', 'Chamrajpet', 'Azad Nagar', 'Dattathreya Temple', 'Gandhi Nagar', 'Subhash Nagar', 'Okalipuram', 'Chikpete', 'Cottonpet', 'Binnipet', 'Nandini Layout', 'Marappana Palya', 'Nagapura', 'Mahalakshmipuram', 'Shakthiganapathi Nagar', 'Shankaramata', 'Vrushabhavathi', 'Aramane Nagar', 'Mathikere', 'Malleshwaram', 'Rajamahal', 'Kadumalleshwara', 'Subramanya Nagar', 'Gayathri Nagar', 'Dayananda Nagar', 'Prakash Nagar', 'Rajaji Nagar', 'Basaveshwara Nagar', 'Kamakshipalya', 'Shiva Nagar', 'Sri Rammandira', 'Jakkur', 'Thanisandra', 'Byatarayanapura', 'Kodigehalli', 'Vidyaranyapura', 'Doddabommasandra', 'Kuvempu Nagar', 'Kempegowda', 'Chowdeshwari', 'Attur', 'Yelahanka Satellite']
print(len(wards))
d1 = {}

for ward in wards:
	d1[ward] = map.get_latitude_and_longitude(ward + ' Bangalore')
	print(d1[ward])

for ward1 in wards:
	distances = {}
	for ward2 in wards:
		if(ward1!=ward2):
			distances[ward2] = map.get_distance_and_time(d1[ward1],d1[ward2])[2]
			print(distances[ward2])
	top_places = get_top_four(distances)
	l.append([ward1,top_places[0],top_places[1],top_places[2],top_places[3]])
	print(l)

print(l)

with open('closest_wards-2.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(l)
# Contenido de la demo La Piquera Hostal (Córdoba) (es/ca/en/fr). Hechos de lapiquerahostal.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hostal real.','ca':' Les imatges són il·lustracions i no mostren l\'hostal real.','en':' Images are illustrations and do not show the actual hostal.','fr':' Les images sont des illustrations et ne montrent pas l\'hostal réel.'}
H={'es':['Habitaciones','La suite con terraza','Los patios'],'ca':['Habitacions','La suite amb terrassa','Els patis'],'en':['Rooms','The suite with terrace','The patios'],'fr':['Chambres','La suite avec terrasse','Les patios']}
RD={
'es':['14 habitaciones con baño privado, calefacción, aire acondicionado, televisión, wifi gratis, secador y artículos de aseo.','Una terraza frente a la Mezquita-Catedral: «No encontrarás otro sitio así».','Una antigua casa de vecinos restaurada que conserva sus patios cordobeses para descansar tras un día de turismo.'],
'ca':['14 habitacions amb bany privat, calefacció, aire condicionat, televisió, wifi gratis, assecador i articles de bany.','Una terrassa davant de la Mesquita-Catedral: «No trobaràs cap altre lloc així».','Una antiga casa de veïns restaurada que conserva els seus patis cordovesos per descansar després d\'un dia de turisme.'],
'en':['14 rooms with private bathroom, heating, air conditioning, TV, free wifi, hair dryer and toiletries.','A terrace facing the Mosque-Cathedral: “You won\'t find another place like this”.','An old restored neighbourhood house that keeps its Cordoban patios, to rest after a day of sightseeing.'],
'fr':['14 chambres avec salle de bain privée, chauffage, climatisation, télévision, wifi gratuit, sèche-cheveux et produits d\'accueil.','Une terrasse face à la Mosquée-Cathédrale : « Vous ne trouverez pas d\'autre endroit comme celui-ci ».','Une ancienne maison de voisins restaurée qui garde ses patios cordouans, pour se reposer après une journée de visites.']}
ART={
'hero':('arches',7101,['#f6e9d6','#ebc48d','#b55f34','#5b6b2e','#36401b']),
'intro':('columns',7102,['#f5ece0','#fbf4ea','#c78f3e','#5b6b2e','#36401b']),
'r1':('arches',7111,['#f4e7d5','#e8bf8b','#b0603a','#5b6b2e','#36401b']),
'r2':('skyline',7112,['#5b6b2e','#e2955a','#f5d29a','#56662b','#434f22','#2b3416']),
'r3':('columns',7113,['#f3e9dd','#faf2e8','#c98f43','#5b6b2e','#36401b']),
'g1':('arches',7121,['#f6e9d8','#ebc590','#b9653a','#7a3a22','#4a2414']),
'g2':('columns',7122,['#f2e8dc','#f9f0e6','#c4893d','#5b6b2e','#36401b']),
'g3':('skyline',7123,['#5f702f','#e6995c','#f8d5a0','#5a6a2c','#465323','#2e3818']),
'g4':('hills',7124,['#eee6cf','#f5e3bd','#f4c886','#b9c398','#8fa47f','#627a60']),
'g5':('arches',7125,['#f5e7d4','#e6bc86','#b46736','#7a3a22','#4a2414']),
'g6':('columns',7126,['#f1e7db','#f8eee4','#c1873f','#5b6b2e','#36401b'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='La Piquera Hostal · Hostal con encanto frente a la Mezquita-Catedral de Córdoba',see_rooms='Ver alojamiento',hero_k='Córdoba · Judería',hero_t='La esquina con más encanto de la Mezquita-Catedral',hero_s='Calle Corregidor Luis de la Cerda, 68: literalmente a cinco pasos de la Mezquita-Catedral.',
 intro_t='Una «ventana» a Córdoba',intro_p1='El hostal toma su nombre de la piquera, la pequeña ventana por donde se servía el vino en las tabernas cordobesas de mediados del siglo XX.',
 intro_p2='Es una antigua casa de vecinos restaurada en el corazón de la Judería, cerca del Puente Romano, el Alcázar de los Reyes Cristianos y la Sinagoga.',
 stats=['14 habitaciones','Frente a la Mezquita','Wifi gratuito','Recepción de 9 a 21 h'],nav_rooms='Alojamiento',rooms_t='Alojamiento',rooms_s='Habitaciones, suite y patios de una casa cordobesa.',
 svcs=['Wifi gratuito','Limpieza diaria','Aire acondicionado y calefacción','Ascensor','Acceso para personas con movilidad reducida','Guardaequipaje','Café y té gratis por la tarde en los patios','Cuna o cama extra bajo petición'],
 loc_p='Calle Corregidor Luis de la Cerda, 68 · 14003 Córdoba. La calle tiene el tráfico restringido: si vienes en coche, el hostal te explica cómo acceder.',
 chips=['¿Qué tienen las habitaciones?','¿Dónde aparcar?','¿A qué hora es el check-in?','¿Cómo se reserva?']),
'ca':dict(title='La Piquera Hostal · Hostal amb encant davant de la Mesquita-Catedral de Còrdova',see_rooms='Veure allotjament',hero_k='Còrdova · Jueria',hero_t='La cantonada amb més encant de la Mesquita-Catedral',hero_s='Calle Corregidor Luis de la Cerda, 68: literalment a cinc passes de la Mesquita-Catedral.',
 intro_t='Una «finestra» a Còrdova',intro_p1='L\'hostal pren el nom de la piquera, la petita finestra per on se servia el vi a les tavernes cordoveses de mitjan segle XX.',
 intro_p2='És una antiga casa de veïns restaurada al cor de la Jueria, a prop del Pont Romà, l\'Alcázar de los Reyes Cristianos i la Sinagoga.',
 stats=['14 habitacions','Davant de la Mesquita','Wifi gratuït','Recepció de 9 a 21 h'],nav_rooms='Allotjament',rooms_t='Allotjament',rooms_s='Habitacions, suite i patis d\'una casa cordovesa.',
 svcs=['Wifi gratuït','Neteja diària','Aire condicionat i calefacció','Ascensor','Accés per a persones amb mobilitat reduïda','Consigna d\'equipatge','Cafè i te gratis a la tarda als patis','Bressol o llit extra a petició'],
 loc_p='Calle Corregidor Luis de la Cerda, 68 · 14003 Còrdova. El carrer té el trànsit restringit: si vens amb cotxe, l\'hostal t\'explica com accedir-hi.',
 chips=['Què tenen les habitacions?','On aparcar?','A quina hora és el check-in?','Com es reserva?']),
'en':dict(title='La Piquera Hostal · Charming hostal facing the Mosque-Cathedral of Córdoba',see_rooms='See the stay',hero_k='Córdoba · Jewish Quarter',hero_t='The most charming corner of the Mosque-Cathedral',hero_s='Calle Corregidor Luis de la Cerda, 68: literally five steps from the Mosque-Cathedral.',
 intro_t='A “window” onto Córdoba',intro_p1='The hostal takes its name from the piquera, the small window through which wine was served in Cordoban taverns in the mid-20th century.',
 intro_p2='It is an old restored neighbourhood house in the heart of the Jewish Quarter, close to the Roman Bridge, the Alcázar de los Reyes Cristianos and the Synagogue.',
 stats=['14 rooms','Facing the Mosque','Free wifi','Reception 9 am–9 pm'],nav_rooms='Stay',rooms_t='Your stay',rooms_s='Rooms, a suite and the patios of a Cordoban house.',
 svcs=['Free wifi','Daily cleaning','Air conditioning and heating','Lift','Access for reduced mobility','Luggage storage','Free coffee and tea every evening in the patios','Cot or extra bed on request'],
 loc_p='Calle Corregidor Luis de la Cerda, 68 · 14003 Córdoba. Traffic on the street is restricted: if you come by car, the hostal explains how to get in.',
 chips=['What do the rooms have?','Where can I park?','What time is check-in?','How do I book?']),
'fr':dict(title='La Piquera Hostal · Hostal de charme face à la Mosquée-Cathédrale de Cordoue',see_rooms='Voir l\'hébergement',hero_k='Cordoue · Quartier juif',hero_t='Le coin le plus charmant de la Mosquée-Cathédrale',hero_s='Calle Corregidor Luis de la Cerda, 68 : littéralement à cinq pas de la Mosquée-Cathédrale.',
 intro_t='Une « fenêtre » sur Cordoue',intro_p1='L\'hostal tient son nom de la piquera, la petite fenêtre par laquelle on servait le vin dans les tavernes de Cordoue au milieu du XXe siècle.',
 intro_p2='C\'est une ancienne maison de voisins restaurée au cœur du quartier juif, près du Pont romain, de l\'Alcázar de los Reyes Cristianos et de la Synagogue.',
 stats=['14 chambres','Face à la Mosquée','Wifi gratuit','Réception de 9 h à 21 h'],nav_rooms='Hébergement',rooms_t='Hébergement',rooms_s='Chambres, suite et patios d\'une maison cordouane.',
 svcs=['Wifi gratuit','Ménage quotidien','Climatisation et chauffage','Ascenseur','Accès pour personnes à mobilité réduite','Bagagerie','Café et thé offerts le soir dans les patios','Lit bébé ou lit d\'appoint sur demande'],
 loc_p='Calle Corregidor Luis de la Cerda, 68 · 14003 Cordoue. La circulation est restreinte dans la rue : si vous venez en voiture, l\'hostal vous explique comment accéder.',
 chips=['Qu\'ont les chambres ?','Où se garer ?','À quelle heure est le check-in ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES_ES='https://www.lapiquerahostal.com/book-a-room'; RES_EN='https://en.lapiquerahostal.com/book-a-room'
BOOK=dict(mode='engine',url={'es':RES_ES,'ca':RES_ES,'en':RES_EN,'fr':RES_EN})
D=dict(name='La Piquera Hostal',ac='#4a5724',ac2='#b55f34',ac2_a11y='#8a4a1e',book=BOOK,around=[],foot=FOOT,
 address='Calle Corregidor Luis de la Cerda, 68 · 14003 Córdoba',phones=['+34 744 63 45 98'],emails=['info@lapiquerahostal.com'],maps='La Piquera Hostal, Calle Corregidor Luis de la Cerda 68, Córdoba',t=T)
META=dict(repo='demo-hostal-la-piquera-cordoba',name='La Piquera Hostal',legal_name='La Piquera Hostal ESPJ',registry_ids=['CIF E56134331','Registro de Turismo de Andalucía H/CO/00696'],
 url='https://www.lapiquerahostal.com/',domain='lapiquerahostal.com',municipality='Córdoba',province='Córdoba',sector='hostal con encanto frente a la Mezquita-Catedral de Córdoba',
 read_at='2026-10-29T11:12:00+01:00',created_at='2026-10-29T11:11:00+01:00',built_at='2026-10-29T11:20:00+01:00',audit_date='2026-10-29T11:13:06+01:00',
 rating=dict(value=4.6,coincide=['telefono','web'],date='2026-10-29T10:36:55+01:00',url='https://www.google.com/maps/place/La+Piquera+Hostal/@37.8787116,-4.7783225,17z/data=!4m9!3m8!1s0xd6d21983cc8acef:0xa03a87ad48f72fbd!5m2!4m1!1i2!8m2!3d37.8787116!4d-4.7783225!16s%2Fg%2F11jmbm772h'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van a la pagina de reservas real del hostal (lapiquerahostal.com/book-a-room, widget de reservas de Wix Hotels enlazado desde su boton «Reserva»); la demo no construye ningun motor.'),
 first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué tienen las habitaciones?','K01'),('¿Cuántas habitaciones hay?','K01'),('¿Hay suite?','K02'),('¿Dónde aparcar?','K03'),('¿Se puede llegar en coche?','K04'),('¿Dónde está el hostal?','K05'),('¿Qué ver cerca?','K06'),('¿Qué servicios tiene?','K07'),('¿A qué hora es el check-in?','K08'),('¿Cómo reservo?','K09'),('¿Hay descuento por reservar en la web?','K10'),('¿Ponen cuna?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('¿Tienen gimnasio?',None),('¿Hay piscina?',None)],
'ca':[('Què tenen les habitacions?','K01'),('Quantes habitacions hi ha?','K01'),('Hi ha suite?','K02'),('On aparcar?','K03'),('S\'hi pot arribar amb cotxe?','K04'),('On és l\'hostal?','K05'),('Què es pot veure a prop?','K06'),('Quins serveis té?','K07'),('A quina hora és el check-in?','K08'),('Com reservo?','K09'),('Hi ha descompte per reservar al web?','K10'),('Poseu bressol?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Teniu gimnàs?',None),('Hi ha piscina?',None)],
'en':[('What do the rooms have?','K01'),('How many rooms are there?','K01'),('Is there a suite?','K02'),('Where can I park?','K03'),('Can I drive to the hostal?','K04'),('Where is the hostal?','K05'),('What is there to see nearby?','K06'),('What services does it offer?','K07'),('What time is check-in?','K08'),('How do I book?','K09'),('Is there a discount for booking on the website?','K10'),('Can you add a cot?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Do you have a gym?',None),('Is there a swimming pool?',None)],
'fr':[('Qu\'ont les chambres ?','K01'),('Combien de chambres y a-t-il ?','K01'),('Y a-t-il une suite ?','K02'),('Où se garer ?','K03'),('Peut-on venir en voiture ?','K04'),('Où est l\'hostal ?','K05'),('Que voir à proximité ?','K06'),('Quels services propose-t-il ?','K07'),('À quelle heure est le check-in ?','K08'),('Comment réserver ?','K09'),('Y a-t-il une réduction en réservant sur le site ?','K10'),('Pouvez-vous ajouter un lit bébé ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Avez-vous une salle de sport ?',None),('Y a-t-il une piscine ?',None)]}

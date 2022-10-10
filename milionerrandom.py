from random import choice
dom=['Biologie','Chimie','Fizica','Istorie','It']
Biologie=['Care este culoarea ghioceilor?:rosie alba mov pamantie',
'Care este culoarea florilor de cireş?:alba verde albastra neagra',
'Astigmatismul este o afecțiune a:creirului mic ochiului pielii ficatului',
'Știi cum se numesc păsările care se hrănesc cu semințe?:crucifere granulocite grandomane granivore',
'Cum se numește sistarea sezonieră a funcțiilor vitale la insecte?:diapauza menopauza hibenare repaus',
'Ce este "gambuzia"?:o floare o insecta un peste un arbore',
'Câte degete(gheare)are"lenesul"din padurile amazoniene?:2 3 4 5',
'Tucanul este o specie de...?:Peste Mamifer Pasare Reptila',
'Știi cum se mai numesc algele brune?:fucus mucus humus labrum',
'Care dintre animalele de mai jos este complet surd?:koala  sarpele tigru  broasca testoasa  licuricul']
Chimie=['Prin ce simbol este reprezentat carbonul în tabelul lui Mendeleev?:Ca C K $',
'Alchimiştii cărei ţări au produs, în urmă cu aproximativ 2000 de ani, praful de puşcă?:China Anglia S.U.A Australia',
'Ce gaz are proprietatea de a subția vocea celui care inspiră amestecul format de acesta cu oxigenul?:hidrogenul propanul metanul  gazul natural',
'În 1935 s-a inventat în Statele Unite un material înlocuitor al textilelor numit:celuloza neylon musama  triclorat de celuloza', 
'Care este elementul de bază conținut de aliajul numit amalgam?:mercur aur cupru staniu', 
'Construit în 1958, ”Atomium”-ul din Bruxelles reprezintă celula cristalină a cărui element chimic?:oxigen hidrogen fier uraniu', 
'Care dintre următoarele elemente este cel mai abundent prezent în scoarța terestră?:aluminiu fier siliciu oxigen',
'Care este formula chimică a glucozei?:C6H8O6 C6H6 C6H12O6 C2H20',
'Prima materie plastică artificială inventată a fost:bachelita nylonul celuloidul  policlorura de venil',
'Chimistul german care a sintetizat în 1878 fructoza şi a primit premiul Nobel pentru chimie în 1902 este:Edwin Ficher  Hans Ficher  Ernst Otto Ficher  Elman Hermann Ficher']
Fizica=['În care dintre următoarele obiective se foloseşte apa grea?:centrala nucleara  palatul parlamentului  Ştrandul Tineretului  Uzina "Semănătoarea"',
'Punctul în care se întâlnesc înălţimile unui triunghi se numeşte:ortocentru  potir  mediu conducător  hidroizolant',
'Ce instrument ştiinţific a fost pus la punct în anii 90 la Mauna Key, în Hawaii?:un teleportor  telescop  magnitron  megatron',
'Care dintre următoarele maşini foloseşte un magnetou?:motorul disel raboteza  scaunul stomatologic  motorul cu electroaprindere', 
'Ce literă a alfabetului grec semnifică sumă în matematică?:alfa beta gama sigma',
'În ce secol s-a născut inventatorul scoţian James Watt?:17 18 19 20',
'Cum se numește producerea artificială a frigului, realizată la temperaturi foarte joase?:crioscopie criogenie crioterapie crenobiologie',
'Ce caracteristică are banda lui Möbius?:banda FM  banda video  20 de memebri  are o singură față',
'La ce domeniu se referă legea lui Hooke?:medicina sociologie mecanica drept',
'În ce an a primit premiul Nobel Albert Einstein?:1921 1910 1929 1938']
Istorie=['A cui fiică a fost Cleopatra VII, ultima reprezentantă a dinastiei Egiptului Antic?:Ptolomeu 14  Ptolomeu 12  Akhenaton  Ramses 2',
'Împotriva cărei ţări a luptat România în Războiul de Independenţă?:Turcia  Elvetia  China  Norvegia',
'Ce titlu purta şeful statului în India antică?:rajah comisar  mandala rabin',
'Ce titlu era conferit de soldaţi sau de senat generalilor din Roma antică, după repurtarea unei victorii?:presedinte administrator imperator  ministru de razboi ',
'Mihai Viteazu a domnit în Ţara Românească între anii...:1600-1613 1492-1501 1593-1601 1695-1701',
'Ce stat a finantat revolutia bolsevica?:Marea Britanie  Suedia  Franta Germania',
'"Phabiranum" este denumirea latină a oraşului german :Padova Amignon Sevila Bremen',
'Când a avut loc abdicarea fără condiții a lui Napoleon Bonaparte?:1805 1821 1814 1832',
'La ce bătălie navală a participat Miguel de Cervantes?:Preveza Lepanto Messina Gibraltar',
'Din ce cauză a murit domnitorul fanariot luminat Nicolae Mavrocordat?:ciuma decapitat otravit spanzurat']
It=['Ce se poate realiza cu ajutorul Internetului?:baterea unui cui  pescuirea platicillor  transfer de informatii  secerisul',
'Ce înseamnă prescurtarea www?:World Wide Web  World Wide Wild  Wear  World Wide WOOOO',
'Generația de computere Macintosh este creată de?:Microsoft Apple ASUS Acer',
'Cum se numeşte aparatul pentru trimiterea de text şi material grafic prin liniile telefonice?:Teletext Fax Faxlni Telefax',
'Cum se numeşte un mic fişier cu informaţii de tip text?:Tab  Tab History  Cookie  Tools',
'Cum se numeşte o pagină de internet?:HTML Site Website Web ',
'Unde a murit Norbert Wiener, fondatorul ciberneticii?:Suedia S.U.A  Germania Franta ',
'Primul calculator portabil comercial a fost lansat în septembrie 1975 de către compania...:Osborn Xerox IBM Apple',
'Ce stat are rezervat domeniul .ee?:Eritreia Ecuador Estonia Etiopia',
'Ce nume a purtat primul computer electronic(succesul Institutului de Cercetari Postale Americane)?:Colossus Zeus Arhimede Sfinx']
for d in range(1):
    s=choice(dom)    
    if s=='Biologie': 
        for x in range(1):
            y=choice(Biologie)
            print("Categoria:",s)
            print("Intrebare=",y)
    elif s=='Chimie': 
        for x in range(1):
            y=choice(Chimie)
            print("Categoria:",s)
            print("Intrebare=",y)
    elif s=='Istorie': 
        for x in range(1):
            y=choice(Istorie)
            print("Categoria:",s)
            print("Intrebare=",y)
    elif s=='Fizica': 
        for x in range(1):
            y=choice(Fizica)
            print("Categoria:",s)
            print("Intrebare=",y)
    elif s=='It': 
        for x in range(1):
            y=choice(It)
            print("Categoria:",s)
            print("Intrebare=",y)
            
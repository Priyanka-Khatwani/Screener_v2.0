#libraries
import pandas as pd
import numpy as np
import yfinance as yf
import time
import streamlit as st

#title of app
st.title("The Basic Screener ")

list_of_all_tickers=['20MICRONS','21STCENMGM','3IINFOLTD','3MINDIA','3PLAND','4THDIM','5PAISA','63MOONS','A2ZINFRA','AAKASH','AAREYDRUGS','AARON','AARTIDRUGS','AARTIIND','AARTISURF','AARVEEDEN','AARVI','AAVAS','ABAN','ABB','ABBOTINDIA','ABCAPITAL','ABFRL','ABMINTLLTD','ABSLAMC','ACC','ACCELYA','ACCURACY','ACE','ACRYSIL','ADANIENT','ADANIGREEN','ADANIPORTS','ADANIPOWER','ADANITRANS','ADFFOODS','ADL','ADORWELD','ADROITINFO','ADSL','ADVANIHOTR','ADVENZYMES','AEGISCHEM','AETHER','AFFLE','AGARIND','AGI','AGRITECH','AGROPHOS','AGSTRA','AHLADA','AHLEAST','AHLUCONT','AIAENG','AIRAN','AIROLAM','AJANTPHARM','AJMERA','AJOONI','AJRINFRA','AKASH','AKG','AKSHAR','AKSHARCHEM','AKSHOPTFBR','AKZOINDIA','ALANKIT','ALBERTDAVD','ALEMBICLTD','ALICON','ALKALI','ALKEM','ALKYLAMINE','ALLCARGO','ALLSEC','ALMONDZ','ALOKINDS','ALPA','ALPHAGEO','ALPSINDUS','AMARAJABAT','AMBER','AMBICAAGAR','AMBIKCO','AMBUJACEM','AMDIND','AMIORG','AMJLAND','AMRUTANJAN','ANANDRATHI','ANANTRAJ','ANDHRAPAP','ANDHRSUGAR','ANDREWYU','ANGELONE','ANIKINDS','ANKITMETAL','ANMOL','ANSALAPI','ANTGRAPHIC','ANUP','ANURAS','APARINDS','APCL','APCOTEXIND','APEX','APLAPOLLO','APLLTD','APOLLO','APOLLOHOSP','APOLLOPIPE','APOLLOTYRE','APOLSINHOT','APTECHT','APTUS','ARCHIDPLY','ARCHIES','ARENTERP','ARIES','ARIHANTCAP','ARIHANTSUP','ARMANFIN','AROGRANITE','ARROWGREEN','ARSHIYA','ARSSINFRA','ARTEMISMED','ARTNIRMAN','ARVEE','ARVIND','ARVINDFASN','ARVSMART','ASAHIINDIA','ASAHISONG','ASAL','ASALCBR','ASHAPURMIN','ASHIANA','ASHIMASYN','ASHOKA','ASHOKLEY','ASIANENE','ASIANHOTNR','ASIANPAINT','ASIANTILES','ASPINWALL','ASTEC','ASTERDM','ASTRAL','ASTRAMICRO','ASTRAZEN','ASTRON','ATFL','ATGL','ATLANTA','ATUL','ATULAUTO','AUBANK','AURIONPRO','AUROPHARMA','AURUM','AUSOMENT','AUTOAXLES','AUTOIND','AVADHSUGAR','AVANTIFEED','AVROIND','AVTNPL','AWHCL','AWL','AXISBANK','AXISCADES','AXITA','AYMSYNTEX','BAFNAPH','BAGFILMS','BAJAJ-AUTO','BAJAJCON','BAJAJELEC','BAJAJFINSV','BAJAJHCARE','BAJAJHIND','BAJAJHLDNG','BAJFINANCE','BALAJITELE','BALAMINES','BALAXI','BALKRISHNA','BALKRISIND','BALMLAWRIE','BALPHARMA','BALRAMCHIN','BANARBEADS','BANARISUG','BANCOINDIA','BANDHANBNK','BANG','BANKA','BANKBARODA','BANKINDIA','BANSWRAS','BARBEQUE','BARTRONICS','BASF','BASML','BATAINDIA','BAYERCROP','BBL','BBOX','BBTC','BCG','BCLIND','BCONCEPTS','BCP','BDL','BEARDSELL','BECTORFOOD','BEDMUTHA','BEL','BEML','BEPL','BERGEPAINT','BESTAGRO','BFINVEST','BFUTILITIE','BGRENERGY','BHAGCHEM','BHAGERIA','BHAGYANGR','BHAGYAPROP','BHANDARI','BHARATFORG','BHARATGEAR','BHARATRAS','BHARATWIRE','BHARTIARTL','BHEL','BIGBLOC','BIL','BINDALAGRO','BIOCON','BIOFILCHEM','BIRLACABLE','BIRLACORPN','BIRLAMONEY','BKMINDST','BLBLIMITED','BLISSGVS','BLKASHYAP','BLS','BLUEDART','BLUESTARCO','BODALCHEM','BOMDYEING','BOROLTD','BORORENEW','BOSCHLTD','BPCL','BPL','BRIGADE','BRITANNIA','BRNL','BROOKS','BSE','BSHSL','BSL','BSOFT','BURNPUR','BUTTERFLY','BVCL','BYKE','CALSOFT','CAMLINFINE','CAMPUS','CAMS','CANBK','CANDC','CANFINHOME','CANTABIL','CAPACITE','CAPLIPOINT','CAPTRUST','CARBORUNIV','CAREERP','CARERATING','CARTRADE','CASTROLIND','CCCL','CCHHL','CCL','CDSL','CEATLTD','CELEBRITY','CENTENKA','CENTEXT','CENTRALBK','CENTRUM','CENTUM','CENTURYPLY','CENTURYTEX','CERA','CEREBRAINT','CESC','CGCL','CGPOWER','CHALET','CHAMBLFERT','CHEMBOND','CHEMCON','CHEMFAB','CHEMPLASTS','CHENNPETRO','CHEVIOT','CHOICEIN','CHOLAFIN','CHOLAHLDNG','CIGNITITEC','CINELINE','CINEVISTA','CIPLA','CLEAN','CLEDUCATE','CLNINDIA','CLSEL','CMICABLES','CMSINFO','COALINDIA','COASTCORP','COCHINSHIP','COFFEEDAY','COFORGE','COLPAL','COMPINFO','COMPUSOFT','CONCOR','CONFIPET','CONSOFINVT','CONTROLPR','CORALFINAC','CORDSCABLE','COROMANDEL','COSMOFIRST','COUNCODOS','CRAFTSMAN','CREATIVE','CREATIVEYE','CREDITACC','CREST','CRISIL','CROMPTON','CROWN','CSBBANK','CSLFINANCE','CTE','CUB','CUBEXTUB','CUMMINSIND','CUPID','CYBERMEDIA','CYBERTECH','CYIENT','DAAWAT','DABUR','DALBHARAT','DALMIASUG','DAMODARIND','DANGEE','DATAMATICS','DATAPATTNS','DBCORP','DBL','DBOL','DBREALTY','DBSTOCKBRO','DCAL','DCBBANK','DCI','DCM','DCMFINSERV','DCMNVL','DCMSHRIRAM','DCMSRIND','DCW','DECCANCE','DEEPAKFERT','DEEPAKNTR','DEEPENR','DEEPINDS','DELHIVERY','DELPHIFX','DELTACORP','DELTAMAGNT','DEN','DENORA','DEVIT','DEVYANI','DFMFOODS','DGCONTENT','DHAMPURSUG','DHANBANK','DHANI','DHANUKA','DHARAMSI','DHARSUGAR','DHRUV','DHUNINV','DIAMONDYD','DICIND','DIGISPICE','DIL','DISHTV','DIVISLAB','DIXON','DLF','DLINKINDIA','DMART','DNAMEDIA','DODLA','DOLATALGO','DOLLAR','DONEAR','DPABHUSHAN','DPSCLTD','DPWIRES','DRCSYSTEMS','DREAMFOLKS','DREDGECORP','DRREDDY','DSSL','DTIL','DUCON','DVL','DWARKESH','DYCL','DYNAMATECH','DYNPRO','E2E','EASEMYTRIP','EASTSILK','ECLERX','EDELWEISS','EICHERMOT','EIDPARRY','EIFFL','EIHAHOTELS','EIHOTEL','EIMCOELECO','EKC','ELDEHSG','ELECON','ELECTCAST','ELECTHERM','ELGIEQUIP','ELGIRUBCO','EMAMILTD','EMAMIPAP','EMAMIREAL','EMIL','EMKAY','EMMBI','EMUDHRA','ENDURANCE','ENERGYDEV','ENGINERSIN','ENIL','EPL','EQUITAS','EQUITASBNK','ERIS','EROSMEDIA','ESABINDIA','ESCORTS','ESSARSHPNG','ESSENTIA','ESTER','ETHOSLTD','EUROTEXIND','EVEREADY','EVERESTIND','EXCEL','EXCELINDUS','EXIDEIND','EXPLEOSOL','EXXARO','FACT','FAIRCHEMOR','FCL','FCONSUMER','FCSSOFT','FDC','FEDERALBNK','FEL','FELDVR','FIBERWEB','FIEMIND','FILATEX','FINCABLES','FINEORG','FINOPB','FINPIPE','FLEXITUFF','FLFL','FLUOROCHEM','FMGOETZE','FMNL','FOCUS','FOODSIN','FORCEMOT','FORTIS','FOSECOIND','FSC','FSL','GABRIEL','GAEL','GAIL','GAL','GALAXYSURF','GALLANTT','GANDHITUBE','GANECOS','GANESHBE','GANESHHOUC','GANGAFORGE','GANGESSECU','GARFIBRES','GATEWAY','GATI','GAYAHWS','GAYAPROJ','GEECEE','GEEKAYWIRE','GENCON','GENESYS','GENUSPAPER','GENUSPOWER','GEOJITFSL','GEPIL','GESHIP','GET&D','GFLLIMITED','GFSTEELS','GHCL','GICHSGFIN','GICRE','GILLANDERS','GILLETTE','GINNIFILA','GIPCL','GKWLIMITED','GLAND','GLAXO','GLENMARK','GLFL','GLOBAL','GLOBALVECT','GLOBE','GLOBUSSPR','GLS','GMBREW','GMDCLTD','GMMPFAUDLR','GMRINFRA','GMRP&UI','GNA','GNFC','GOACARBON','GOCLCORP','GOCOLORS','GODFRYPHLP','GODHA','GODREJAGRO','GODREJCP','GODREJIND','GODREJPROP','GOENKA','GOKEX','GOKUL','GOKULAGRO','GOLDENTOBC','GOLDIAM','GOLDTECH','GOODLUCK','GOODYEAR','GPIL','GPPL','GPTINFRA','GRANULES','GRAPHITE','GRASIM','GRAUWEIL','GRAVITA','GREAVESCOT','GREENLAM','GREENPANEL','GREENPLY','GREENPOWER','GRINDWELL','GRINFRA','GRMOVER','GROBTEA','GRPLTD','GRSE','GRWRHITECH','GSCLCEMENT','GSFC','GSPL','GSS','GTL','GTLINFRA','GTPL','GUFICBIO','GUJALKALI','GUJAPOLLO','GUJGASLTD','GUJRAFFIA','GULFOILLUB','GULFPETRO','GULPOLY','GVKPIL','HAL','HAPPSTMNDS','HARDWYN','HARIOMPIPE','HARRMALAYA','HARSHA','HATHWAY','HATSUN','HAVELLS','HAVISHA','HBLPOWER','HBSL','HCC','HCG','HCL-INSYS','HCLTECH','HDFC','HDFCAMC','HDFCBANK','HDFCLIFE','HDIL','HEADSUP','HECPROJECT','HEG','HEIDELBERG','HEMIPROP','HERANBA','HERCULES','HERITGFOOD','HEROMOTOCO','HESTERBIO','HEXATRADEX','HFCL','HGINFRA','HGS','HIKAL','HIL','HILTON','HIMATSEIDE','HINDALCO','HINDCOMPOS','HINDCON','HINDCOPPER','HINDMOTORS','HINDOILEXP','HINDPETRO','HINDUNILVR','HINDWAREAP','HINDZINC','HIRECT','HISARMETAL','HITECH','HITECHCORP','HITECHGEAR','HLEGLAS','HLVLTD','HMT','HMVL','HNDFDS','HOMEFIRST','HONAUT','HONDAPOWER','HOTELRUGBY','HOVS','HPAL','HPL','HSCL','HTMEDIA','HUBTOWN','HUDCO','HUHTAMAKI','IBREALEST','IBULHSGFIN','ICDSLTD','ICEMAKE','ICICIBANK','ICICIGI','ICICIPRULI','ICIL','ICRA','IDBI','IDEA','IDFC','IDFCFIRSTB','IEX','IFBAGRO','IFBIND','IFCI','IFGLEXPOR','IGARASHI','IGL','IGPL','IIFL','IIFLSEC','IIFLWAM','IITL','IL&FSENGG','IL&FSTRANS','IMAGICAA','IMFA','IMPAL','IMPEXFERRO','INCREDIBLE','INDBANK','INDHOTEL','INDIACEM','INDIAGLYCO','INDIAMART','INDIANB','INDIANCARD','INDIANHUME','INDIGO','INDIGOPNTS','INDLMETER','INDNIPPON','INDOAMIN','INDOBORAX','INDOCO','INDORAMA','INDOSTAR','INDOTECH','INDOTHAI','INDOWIND','INDRAMEDCO','INDSWFTLAB','INDSWFTLTD','INDTERRAIN','INDUSINDBK','INDUSTOWER','INEOSSTYRO','INFIBEAM','INFOBEAN','INFOMEDIA','INFY','INGERRAND','INOXLEISUR','INOXWIND','INSECTICID','INSPIRISYS','INTELLECT','INTENTECH','INTLCONV','INVENTURE','IOB','IOC','IOLCP','IONEXCHANG','IPCALAB','IPL','IRB','IRCON','IRCTC','IRFC','IRIS','IRISDOREME','ISEC','ISFT','ISGEC','ISMTLTD','ITC','ITDC','ITDCEM','ITI','IVC','IVP','IWEL','IZMO','J&KBANK','JAGRAN','JAGSNPHARM','JAIBALAJI','JAICORPLTD','JAIPURKURT','JAMNAAUTO','JASH','JAYAGROGN','JAYBARMARU','JAYNECOIND','JAYSREETEA','JBCHEPHARM','JBFIND','JBMA','JCHAC','JETAIRWAYS','JETFREIGHT','JHS','JINDALPHOT','JINDALPOLY','JINDALSAW','JINDALSTEL','JINDRILL','JINDWORLD','JISLDVREQS','JISLJALEQS','JITFINFRA','JKCEMENT','JKIL','JKLAKSHMI','JKPAPER','JKTYRE','JMA','JMCPROJECT','JMFINANCIL','JOCIL','JPASSOCIAT','JPOLYINVST','JPPOWER','JSL','JSLHISAR','JSWENERGY','JSWHL','JSWISPL','JSWSTEEL','JTEKTINDIA','JTLINFRA','JUBLFOOD','JUBLINDS','JUBLINGREA','JUBLPHARMA','JUSTDIAL','JWL','JYOTHYLAB','JYOTISTRUC','KABRAEXTRU','KAJARIACER','KAKATCEM','KALPATPOWR','KALYANI','KALYANIFRG','KALYANKJIL','KAMATHOTEL','KAMDHENU','KANANIIND','KANORICHEM','KANPRPLA','KANSAINER','KAPSTON','KARMAENG','KARURVYSYA','KAUSHALYA','KAVVERITEL','KAYA','KBCGLOBAL','KCP','KCPSUGIND','KDDL','KEC','KECL','KEEPLEARN','KEI','KELLTONTEC','KENNAMET','KERNEX','KESORAMIND','KEYFINSERV','KHADIM','KHAICHEM','KHAITANLTD','KHANDSE','KICL','KILITCH','KIMS','KINGFA','KIOCL','KIRIINDUS','KIRLFER','KIRLOSBROS','KIRLOSENG','KIRLOSIND','KITEX','KKCL','KMSUGAR','KNRCON','KOHINOOR','KOKUYOCMLN','KOLTEPATIL','KOPRAN','KOTAKBANK','KOTARISUG','KOTHARIPET','KOTHARIPRO','KOVAI','KPIGREEN','KPITTECH','KPRMILL','KRBL','KREBSBIO','KRIDHANINF','KRISHANA','KRITI','KRITIKA','KRITINUT','KRSNAA','KSB','KSCL','KSHITIJPOL','KSL','KSOLVES','KTKBANK','KUANTUM','L&TFH','LAGNAM','LAKPRE','LALPATHLAB','LAMBODHARA','LANCER','LAOPALA','LASA','LATENTVIEW','LAURUSLABS','LAXMICOT','LAXMIMACH','LCCINFOTEC','LEMONTREE','LFIC','LGBBROSLTD','LGBFORGE','LIBAS','LIBERTSHOE','LICHSGFIN','LICI','LIKHITHA','LINC','LINCOLN','LINDEINDIA','LODHA','LOKESHMACH','LOTUSEYE','LOVABLE','LOYALTEX','LPDC','LSIL','LT','LTI','LTTS','LUMAXIND','LUMAXTECH','LUPIN','LUXIND','LXCHEM','LYKALABS','LYPSAGEMS','M&M','M&MFIN','MAANALU','MACPOWER','MADHAV','MADHUCON','MADRASFERT','MAGADSUGAR','MAGNUM','MAHABANK','MAHAPEXLTD','MAHASTEEL','MAHEPC','MAHESHWARI','MAHINDCIE','MAHLIFE','MAHLOG','MAHSCOOTER','MAHSEAMLES','MAITHANALL','MALLCOM','MALUPAPER','MANAKALUCO','MANAKCOAT','MANAKSIA','MANAKSTEEL','MANALIPETC','MANAPPURAM','MANGALAM','MANGCHEFER','MANGLMCEM','MANINDS','MANINFRA','MANORAMA','MANORG','MANUGRAPH','MANYAVAR','MAPMYINDIA','MARALOVER','MARATHON','MARICO','MARINE','MARKSANS','MARSHALL','MARUTI','MASFIN','MASKINVEST','MASTEK','MATRIMONY','MAWANASUG','MAXHEALTH','MAXIND','MAXVIL','MAYURUNIQ','MAZDA','MAZDOCK','MBAPL','MBECL','MBLINFRA','MCDOWELL-N','MCL','MCLEODRUSS','MCX','MEDICAMEQ','MEDICO','MEDPLUS','MEGASOFT','MEGASTAR','MELSTAR','MENONBE','MEP','MERCATOR','METALFORGE','METROBRAND','METROPOLIS','MFL','MFSL','MGEL','MGL','MHLXMIRU','MHRIL','MICEL','MIDHANI','MINDACORP','MINDTECK','MINDTREE','MIRCELECTR','MIRZAINT','MITCON','MITTAL','MMFL','MMP','MMTC','MODIRUBBER','MODISONLTD','MOHITIND','MOIL','MOKSH','MOL','MOLDTECH','MOLDTKPAC','MONARCH','MONTECARLO','MORARJEE','MOREPENLAB','MOTHERSON','MOTILALOFS','MOTOGENFIN','MPHASIS','MPSLTD','MRF','MRO-TEK','MRPL','MSPL','MSTCLTD','MSUMI','MTARTECH','MTEDUCARE','MTNL','MUKANDLTD','MUKTAARTS','MUNJALAU','MUNJALSHOW','MURUDCERA','MUTHOOTCAP','MUTHOOTFIN','NACLIND','NAGAFERT','NAGREEKCAP','NAGREEKEXP','NAHARCAP','NAHARINDUS','NAHARPOLY','NAHARSPING','NAM-INDIA','NATCOPHARM','NATHBIOGEN','NATIONALUM','NAUKRI','NAVA','NAVINFLUOR','NAVKARCORP','NAVNETEDUL','NAZARA','NBCC','NBIFIN','NCC','NCLIND','NDGL','NDL','NDRAUTO','NDTV','NECCLTD','NECLIFE','NELCAST','NELCO','NEOGEN','NESCO','NESTLEIND','NETWORK18','NEULANDLAB','NEWGEN','NEXTMEDIA','NFL','NGIL','NGLFINE','NH','NHPC','NIACL','NIBL','NIITLTD','NILAINFRA','NILASPACES','NILKAMAL','NIPPOBATRY','NIRAJ','NIRAJISPAT','NITCO','NITINSPIN','NITIRAJ','NKIND','NLCINDIA','NMDC','NOCIL','NOIDATOLL','NORBTEAEXP','NOVARTIND','NRAIL','NRBBEARING','NSIL','NTPC','NUCLEUS','NURECA','NUVOCO','NXTDIGITAL','NYKAA','OAL','OBCL','OBEROIRLTY','OCCL','OFSS','OIL','OILCOUNTUB','OLECTRA','OMAXAUTO','OMAXE','OMINFRAL','OMKARCHEM','ONELIFECAP','ONEPOINT','ONGC','ONMOBILE','ONWARDTEC','OPTIEMUS','ORBTEXP','ORCHPHARMA','ORICONENT','ORIENTABRA','ORIENTALTL','ORIENTBELL','ORIENTCEM','ORIENTELEC','ORIENTHOT','ORIENTLTD','ORIENTPPR','ORISSAMINE','ORTEL','ORTINLAB','OSWALAGRO','PAGEIND','PAISALO','PALASHSECU','PALREDTEC','PANACEABIO','PANACHE','PANAMAPET','PANSARI','PAR','PARACABLES','PARADEEP','PARAGMILK','PARAS','PARSVNATH','PASUPTAC','PATANJALI','PATELENG','PATINTLOG','PAYTM','PCBL','PCJEWELLER','PDMJEPAPER','PDPL','PDSL','PEARLPOLY','PEL','PENIND','PENINLAND','PERSISTENT','PETRONET','PFC','PFIZER','PFOCUS','PFS','PGEL','PGHH','PGHL','PGIL','PHOENIXLTD','PIDILITIND','PIIND','PILANIINVS','PILITA','PIONDIST','PIONEEREMB','PITTIENG','PIXTRANS','PKTEA','PLASTIBLEN','PNB','PNBGILTS','PNBHOUSING','PNC','PNCINFRA','PODDARHOUS','PODDARMENT','POKARNA','POLICYBZR','POLYCAB','POLYMED','POLYPLEX','PONNIERODE','POONAWALLA','POWERGRID','POWERINDIA','POWERMECH','PPAP','PPL','PPLPHARMA','PRAENG','PRAJIND','PRAKASH','PRAKASHSTL','PRAXIS','PRECAM','PRECOT','PRECWIRE','PREMEXPLN','PREMIER','PREMIERPOL','PRESSMN','PRESTIGE','PRICOLLTD','PRIMESECU','PRINCEPIPE','PRITI','PRITIKAUTO','PRIVISCL','PROZONINTU','PRSMJOHNSN','PRUDENT','PSB','PSPPROJECT','PTC','PTL','PUNJABCHEM','PURVA','PVP','PVR','QUESS','QUICKHEAL','RADAAN','RADHIKAJWE','RADICO','RADIOCITY','RAILTEL','RAIN','RAINBOW','RAJESHEXPO','RAJMET','RAJRATAN','RAJRILTD','RAJSREESUG','RAJTV','RALLIS','RAMANEWS','RAMAPHO','RAMASTEEL','RAMCOCEM','RAMCOIND','RAMCOSYS','RAMKY','RAMRAT','RANASUG','RANEENGINE','RANEHOLDIN','RATEGAIN','RATNAMANI','RAYMOND','RBA','RBL','RBLBANK','RCF','RCOM','RECLTD','REDINGTON','REFEX','REGENCERAM','RELAXO','RELCHEMQ','RELIANCE','RELIGARE','RELINFRA','REMSONSIND','RENUKA','REPCOHOME','REPL','REPRO','RESPONIND','REVATHI','RGL','RHFL','RHIM','RICOAUTO','RIIL','RITCO','RITES','RKDL','RKEC','RKFORGE','RMCL','RML','ROHLTD','ROLEXRINGS','ROLLT','ROLTA','ROML','ROSSARI','ROSSELLIND','ROTO','ROUTE','RPGLIFE','RPOWER','RPPINFRA','RPPL','RPSGVENT','RSSOFTWARE','RSWM','RSYSTEMS','RTNINDIA','RTNPOWER','RUBYMILLS','RUCHINFRA','RUCHIRA','RUPA','RUSHIL','RVHL','RVNL','S&SPOWER','SABEVENTS','SADBHAV','SADBHIN','SAFARI','SAGARDEEP','SAGCEM','SAIL','SAKAR','SAKHTISUG','SAKSOFT','SAKUMA','SALASAR','SALONA','SALSTEEL','SALZERELEC','SAMBHAAV','SANCO','SANDESH','SANDHAR','SANGAMIND','SANGHIIND','SANGHVIMOV','SANGINITA','SANOFI','SANSERA','SANWARIA','SAPPHIRE','SARDAEN','SAREGAMA','SARLAPOLY','SASKEN','SASTASUNDR','SATIA','SATIN','SBC','SBCL','SBICARD','SBILIFE','SBIN','SCAPDVR','SCHAEFFLER','SCHAND','SCHNEIDER','SCI','SDBL','SEAMECLTD','SECURCRED','SECURKLOUD','SELAN','SEPC','SEPOWER','SEQUENT','SERVOTECH','SESHAPAPER','SETCO','SETUINFRA','SFL','SGIL','SGL','SHAHALLOYS','SHAILY','SHAKTIPUMP','SHALBY','SHALPAINTS','SHANKARA','SHANTI','SHANTIGEAR','SHARDACROP','SHARDAMOTR','SHAREINDIA','SHEMAROO','SHILPAMED','SHIVALIK','SHIVAMAUTO','SHIVAMILLS','SHIVATEX','SHK','SHOPERSTOP','SHRADHA','SHREDIGCEM','SHREECEM','SHREEPUSHK','SHREERAMA','SHRENIK','SHREYANIND','SHREYAS','SHRIPISTON','SHRIRAMCIT','SHRIRAMPPS','SHYAMCENT','SHYAMMETL','SHYAMTEL','SIEMENS','SIGACHI','SIGIND','SIKKO','SIL','SILGO','SILINV','SILLYMONKS','SILVERTUC','SIMBHALS','SIMPLEXINF','SINTERCOM','SIRCA','SIS','SITINET','SIYSIL','SJS','SJVN','SKFINDIA','SKIPPER','SKMEGGPROD','SMARTLINK','SMCGLOBAL','SMLISUZU','SMLT','SMSLIFE','SMSPHARMA','SNOWMAN','SOBHA','SOFTTECH','SOLARA','SOLARINDS','SOMANYCERA','SOMATEX','SOMICONVEY','SONACOMS','SONAMCLOCK','SONATSOFTW','SOTL','SOUTHBANK','SOUTHWEST','SPAL','SPANDANA','SPARC','SPCENET','SPECIALITY','SPENCERS','SPIC','SPICEJET','SPLIL','SPLPETRO','SPMLINFRA','SPORTKING','SPTL','SREEL','SRF','SRHHYPOLTD','SRPL','SRTRANSFIN','SSWL','STAR','STARCEMENT','STARHEALTH','STARPAPER','STARTECK','STCINDIA','STEELCAS','STEELCITY','STEELXIND','STEL','STERTOOLS','STLTECH','STOVEKRAFT','STYLAMIND','SUBCAPCITY','SUBEXLTD','SUBROS','SUDARSCHEM','SUMEETINDS','SUMICHEM','SUMIT','SUMMITSEC','SUNCLAYLTD','SUNDARAM','SUNDARMFIN','SUNDARMHLD','SUNDRMBRAK','SUNDRMFAST','SUNFLAG','SUNPHARMA','SUNTECK','SUNTV','SUPERHOUSE','SUPERSPIN','SUPRAJIT','SUPREMEENG','SUPREMEIND','SUPREMEINF','SUPRIYA','SURANASOL','SURANAT&P','SURYALAXMI','SURYAROSNI','SURYODAY','SUTLEJTEX','SUULD','SUVEN','SUVENPHAR','SUVIDHAA','SUZLON','SVPGLOB','SWANENERGY','SWARAJENG','SWELECTES','SWSOLAR','SYMPHONY','SYNGENE','SYRMA','TAINWALCHM','TAJGVK','TAKE','TALBROAUTO','TANLA','TANTIACONS','TARAPUR','TARC','TARMAT','TARSONS','TASTYBITE','TATACHEM','TATACOFFEE','TATACOMM','TATACONSUM','TATAELXSI','TATAINVEST','TATAMETALI','TATAMOTORS','TATAMTRDVR','TATAPOWER','TATASTEEL','TATASTLLP','TATVA','TBZ','TCI','TCIDEVELOP','TCIEXP','TCNSBRANDS','TCPLPACK','TCS','TDPOWERSYS','TEAMLEASE','TECHIN','TECHM','TECHNOE','TEGA','TEJASNET','TEMBO','TERASOFT','TEXINFRA','TEXMOPIPES','TEXRAIL','TFCILTD','TFL','TGBHOTELS','THANGAMAYL','THEINVEST','THEMISMED','THERMAX','THOMASCOOK','THOMASCOTT','THYROCARE','TI','TIDEWATER','TIIL','TIINDIA','TIJARIA','TIL','TIMESGTY','TIMETECHNO','TIMKEN','TINPLATE','TIPSFILMS','TIPSINDLTD','TIRUMALCHM','TIRUPATIFL','TITAN','TMB','TNPETRO','TNPL','TNTELE','TOKYOPLAST','TORNTPHARM','TORNTPOWER','TOTAL','TOUCHWOOD','TPLPLASTEH','TRACXN','TREEHOUSE','TREJHARA','TRENT','TRF','TRIDENT','TRIGYN','TRIL','TRITURBINE','TRIVENI','TRU','TTKHLTCARE','TTKPRESTIG','TTL','TTML','TV18BRDCST','TVSELECT','TVSMOTOR','TVSSRICHAK','TVTODAY','TVVISION','TWL','UBL','UCALFUEL','UCOBANK','UDAICEMENT','UFLEX','UFO','UGARSUGAR','UGROCAP','UJAAS','UJJIVAN','UJJIVANSFB','ULTRACEMCO','UMAEXPORTS','UMANGDAIRY','UMESLTD','UNICHEMLAB','UNIDT','UNIENTER','UNIINFO','UNIONBANK','UNITECH','UNITEDPOLY','UNITEDTEA','UNIVASTU','UNIVCABLES','UNIVPHOTO','UNOMINDA','UPL','URJA','USHAMART','UTIAMC','UTTAMSUGAR','V2RETAIL','VADILALIND','VAIBHAVGBL','VAISHALI','VAKRANGEE','VALIANTORG','VARDHACRLC','VARDMNPOLY','VARROC','VASCONEQ','VASWANI','VBL','VCL','VEDL','VENKEYS','VENUSPIPES','VENUSREM','VERANDA','VERTOZ','VESUVIUS','VETO','VGUARD','VHL','VIDHIING','VIJAYA','VIJIFIN','VIKASECO','VIKASLIFE','VIKASPROP','VIKASWSP','VIMTALABS','VINATIORGA','VINDHYATEL','VINEETLAB','VINYLINDIA','VIPCLOTHNG','VIPIND','VIPULLTD','VISAKAIND','VISASTEEL','VISESHINFO','VISHAL','VISHNU','VISHWARAJ','VIVIDHA','VIVIMEDLAB','VLSFINANCE','VMART','VOLTAMP','VOLTAS','VRLLOG','VSSL','VSTIND','VSTTILLERS','VTL','WABAG','WALCHANNAG','WANBURY','WATERBASE','WEALTH','WEBELSOLAR','WEIZMANIND','WELCORP','WELENT','WELINV','WELSPUNIND','WENDT','WESTLIFE','WEWIN','WFL','WHEELS','WHIRLPOOL','WILLAMAGOR','WINDLAS','WINDMACHIN','WINPRO','WIPL','WIPRO','WOCKPHARMA','WONDERLA','WORTH','WSTCSTPAPR','XCHANGING','XELPMOC','XPROINDIA','YAARI','YESBANK','YUKEN','ZEEL','ZEELEARN','ZEEMEDIA','ZENITHEXPO','ZENITHSTL','ZENSARTECH','ZENTEC','ZFCVINDIA','ZODIAC','ZODIACLOTH','ZOMATO','ZOTA','ZUARI','ZUARIIND','ZYDUSLIFE','ZYDUSWELL']

loaf=[]
for i in range(0,len(list_of_all_tickers)):
  name=list_of_all_tickers[i]+'.NS'
  loaf.append(name)
  
sample=['ACC.NS','ADANIENT.NS','ADANIGREEN.NS','ADANIPORTS.NS','ATGL.NS','ADANITRANS.NS','AMBUJACEM.NS','APOLLOHOSP.NS','ASIANPAINT.NS','DMART.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BAJAJHLDNG.NS','BANDHANBNK.NS','BANKBARODA.NS','BERGEPAINT.NS','BEL.NS','BPCL.NS','BHARTIARTL.NS','BIOCON.NS','BOSCHLTD.NS','BRITANNIA.NS','CHOLAFIN.NS','CIPLA.NS','COALINDIA.NS','COLPAL.NS','DLF.NS','DABUR.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','NYKAA.NS','GAIL.NS','GLAND.NS','GODREJCP.NS','GRASIM.NS','HCLTECH.NS','HDFCAMC.NS','HDFCBANK.NS','HDFCLIFE.NS','HAVELLS.NS','HEROMOTOCO.NS','HINDALCO.NS','HAL.NS','HINDUNILVR.NS','HDFC.NS','ICICIBANK.NS','ICICIGI.NS','ICICIPRULI.NS','ITC.NS','IOC.NS','IRCTC.NS','INDUSTOWER.NS','INDUSINDBK.NS','NAUKRI.NS','INFY.NS','INDIGO.NS','JSWSTEEL.NS','KOTAKBANK.NS','LTI.NS','LT.NS','LICI.NS','M&M.NS','MARICO.NS','MARUTI.NS','MPHASIS.NS','MUTHOOTFIN.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','PAYTM.NS','PIIND.NS','PIDILITIND.NS','POWERGRID.NS','PGHH.NS','RELIANCE.NS','SBICARD.NS','SBILIFE.NS','SRF.NS','MOTHERSON.NS','SHREECEM.NS','SIEMENS.NS','SBIN.NS','SUNPHARMA.NS','TCS.NS','TATACONSUM.NS','TATAMOTORS.NS','TATAPOWER.NS','TATASTEEL.NS','TECHM.NS','TITAN.NS','TORNTPHARM.NS','UPL.NS','ULTRACEMCO.NS','MCDOWELL-N.NS','VEDL.NS','WIPRO.NS','ZOMATO.NS']
  
  
def upper_bollinger():
    name=[]
    UpperBollinger=[]
    for j in range(0,len(sample)):
        print("STOCK SYMBOL:",sample[j])

        intraday_data=yf.download(tickers=sample[j],period='5d',interval="5m")
        intraday_data.reset_index(inplace=True)
        #daily_data=yf.download(tickers=loaf[j],period='20d')
        intraday_data['Typical Price']=intraday_data['Close']
        intraday_data['std'] = intraday_data['Typical Price'].rolling(20).std(ddof=0)
        intraday_data['MA-TP'] = intraday_data['Typical Price'].rolling(20).mean()
        intraday_data['BOLU'] = intraday_data['MA-TP'] + 2*intraday_data['std']
        intraday_data['BOLD'] = intraday_data['MA-TP'] - 2*intraday_data['std']

        try:
            for k in range(0,len(intraday_data)):
                if intraday_data['Close'][k]>intraday_data['BOLU'][k]:
                    #print("Upper Bollinger Band Broken at: ",intraday_data['Datetime'][k])
                    name.append(sample[j])
                    UpperBollinger.append(intraday_data['Datetime'][k])        
        except:
            print("Try again later")
    
    Upper_df=pd.DataFrame()
    Upper_df['Name']=name
    Upper_df['Time of Upper Bollinger Breaking']=UpperBollinger
    return Upper_df
  
def lower_bollinger():
    name=[]
    LowerBollinger=[]

    for j in range(0,len(sample)):
        print("STOCK SYMBOL:",sample[j])

        intraday_data=yf.download(tickers=sample[j],period='5d',interval="5m")
        intraday_data.reset_index(inplace=True)
        daily_data=yf.download(tickers=loaf[j],period='20d')
        intraday_data['Typical Price']=intraday_data['Close']
        intraday_data['std'] = intraday_data['Typical Price'].rolling(20).std(ddof=0)
        intraday_data['MA-TP'] = intraday_data['Typical Price'].rolling(20).mean()
        intraday_data['BOLU'] = intraday_data['MA-TP'] + 2*intraday_data['std']
        intraday_data['BOLD'] = intraday_data['MA-TP'] - 2*intraday_data['std']

        try:
            for k in range(0,len(intraday_data)):
                if intraday_data['Close'][k]<intraday_data['BOLD'][k]:
                    #print("Lower Bollinger Band Broken at: ",intraday_data['Datetime'][k])
                    name.append(sample[j])
                    LowerBollinger.append(intraday_data['Datetime'][k])
        except:
            print("Try again later")
            
    Lower_df=pd.DataFrame()
    Lower_df['Name']=name
    Lower_df['Time of Lower Bollinger Breaking']=LowerBollinger
    return Lower_df
  
def engulfing_5minutes():
    datetime=[]
    engulfing_type=[]
    name=[]
    for j in range(0,len(sample)):
        print("For stock with ticker ",sample[j])
        intraday_data=yf.download(tickers=sample[j],period='22d',interval='5m')
        intraday_data.reset_index(inplace=True)
        intraday_data['Spread']=intraday_data['Close']-intraday_data['Open']
        try:
            for k in range(0,len(intraday_data)):
                if intraday_data['Close'][k]<intraday_data['Open'][k] and intraday_data['Close'][k+1]>intraday_data['Open'][k+1]: #green before red for bearish engulfing
                  if intraday_data['Close'][k]<intraday_data['Open'][k+1] and intraday_data['Open'][k]>intraday_data['Close'][k+1]:
                      #print('Bearish Engulfing at :',intraday_data['Datetime'][k+1])
                      engulfing_type.append("Bearish")
                      datetime.append(intraday_data['Datetime'][k+1])
                      name.append(sample[j])
                if intraday_data['Close'][k]>intraday_data['Open'][k] and intraday_data['Close'][k+1]<intraday_data['Open'][k+1]: # red before green for bullish engulfing
                  if intraday_data['Close'][k]>intraday_data['Open'][k+1] and intraday_data['Open'][k]<intraday_data['Close'][k+1]:
                      #print('Bullish engulfing at : ',intraday_data['Datetime'][k+1])
                      engulfing_type.append("Bullish")
                      datetime.append(intraday_data['Datetime'][k+1])
                      name.append(sample[j])
        except:
            print("Max reached")
    engulfing_df=pd.DataFrame()
    engulfing_df['Name']=name
    engulfing_df['DateTime']=datetime
    engulfing_df['Engulfing Type']=engulfing_type
    
    return engulfing_df
def engulfing_1hour():
    datetime=[]
    engulfing_type=[]
    name=[]
    for j in range(0,len(sample)):
        print("For stock with ticker ",sample[j])
        intraday_data=yf.download(tickers=sample[j],period='22d',interval='60m')
        intraday_data.reset_index(inplace=True)
        intraday_data['Spread']=intraday_data['Close']-intraday_data['Open']
        try:
            for k in range(0,len(intraday_data)):
                if intraday_data['Close'][k]<intraday_data['Open'][k] and intraday_data['Close'][k+1]>intraday_data['Open'][k+1]: #green before red for bearish engulfing
                    if intraday_data['Close'][k]<intraday_data['Open'][k+1] and intraday_data['Open'][k]>=intraday_data['Close'][k+1]:
                        print('Bearish Engulfing at :',intraday_data['Datetime'][k+1])
                        engulfing_type.append("Bearish")
                        datetime.append(intraday_data['Datetime'][k+1])
                        name.append(sample[j])
                if intraday_data['Close'][k]>intraday_data['Open'][k] and intraday_data['Close'][k+1]<intraday_data['Open'][k+1]: # red before green for bullish engulfing
                    if intraday_data['Close'][k]>=intraday_data['Open'][k+1] and intraday_data['Open'][k]<intraday_data['Close'][k+1]:
                        print('Bullish engulfing at : ',intraday_data['Datetime'][k+1])
                        engulfing_type.append("Bullish")
                        datetime.append(intraday_data['Datetime'][k+1])
                        name.append(sample[j])
        except:
            print("Max reached")
    engulfing_df=pd.DataFrame()
    engulfing_df['Name']=name
    engulfing_df['DateTime']=datetime
    engulfing_df['Engulfing Type']=engulfing_type
    
    return engulfing_df
choices=st.sidebar.radio(label="Select suitable option",options=("Upper Bollinger breaking for Nifty100","Lower Bollinger breaking for Nifty100","Engulfing 1 hour for Nifty100","Engulfing 5 mins for Nifty100"))
if choices == 'Upper Bollinger breaking for Nifty100':
                 st.dataframe(upper_bollinger(),use_container_width=True)
if choices=="Lower Bollinger breaking for Nifty100":
                 st.dataframe(lower_bollinger(),use_container_width=True)
if choices=="Engulfing 1 hour for Nifty100":
                 st.dataframe(engulfing_1hour(),use_container_width=True)
if choices=="Engulfing 5 mins for Nifty100":
                 st.dataframe(engulfing_5minutes(),use_container_width=True)
                 
                 
                 
                 

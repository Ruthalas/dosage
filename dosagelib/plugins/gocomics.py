# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..util import tagre
from ..helpers import bounceStarter

_imageSearch = compile(tagre("img", "src", r'(http://assets\.amuniversal\.com/[0-9a-f]+)'))
_prevSearch = compile(tagre("a", "href", r'(/[^"]+/\d+/\d+/\d+)', after="prev"))
_nextSearch = compile(tagre("a", "href", r'(/[^"]+/\d+/\d+/\d+)', after="next"))

def add(name, shortname):
    baseUrl = 'http://www.gocomics.com'
    url = baseUrl + shortname
    classname = 'GoComics_%s' % name

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        prefix, year, month, day = pageUrl.rsplit('/', 3)
        return "%s_%s%s%s.gif" % (name, year, month, day)

    globals()[classname] = make_scraper(classname,
        url = url,
        starter = bounceStarter(url, _nextSearch),
        name='GoComics/' + name,
        stripUrl=baseUrl + shortname + '/%s',
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help='Index format: yyyy/mm/dd',
        namer=namer,
    )


# do not edit anything below since these entries are generated from scripts/update.sh
# DO NOT REMOVE
add('060', '/0-60')
add('2CowsandaChicken', '/2cowsandachicken')
add('4PunkyPuppies', '/four-punky-puppies')
add('9ChickweedLane', '/9chickweedlane')
add('9to5', '/9to5')
add('ABenePlacito', '/a-bene-placito')
add('ACMEINKD', '/acme-inkd')
add('ARomanticLife', '/a-romantic-life')
add('Abaca', '/abaca')
add('AcadasiaDown', '/acadasia-down')
add('AdamAtHome', '/adamathome')
add('AdmiralSquirt', '/admiral-squirt')
add('AdultChildren', '/adult-children')
add('AdventuresofMartyandTurkey', '/marty-and-turkey')
add('AgainstTheGrain', '/against-the-grain')
#add('Agnes', '/agnes')
add('AlisonWard', '/alison-ward')
add('AlleyOop', '/alley-oop')
add('AlmostGrounded', '/almost-grounded')
add('AmaZnEvents', '/amaznevents')
add('Andertoons', '/andertoons')
add('Andnow', '/and-now')
#add('AndyCapp', '/andycapp')
add('Anecdote', '/anecdote')
add('AngryLittleGirls', '/angry-little-girls')
add('AnimalAntics', '/animal-antics')
add('AnimalCrackers', '/animalcrackers')
add('AnimalRaj', '/animal-raj')
add('Annie', '/annie')
add('AppleCreekComics', '/apple-creek')
add('ArDuffle', '/arduffle')
add('ArloandJanis', '/arloandjanis')
add('ArtPOWERS', '/artpowers')
#add('AskShagg', '/askshagg')
add('Asymptote', '/asymptote')
#add('BC', '/bc')
add('BERSERKALERT', '/berserk-alert')
add('BUNS', '/buns')
add('BUSHYTALES', '/bushy-tales')
add('BackintheDay', '/backintheday')
add('BadReporter', '/badreporter')
add('Badlands', '/badlands')
add('Baldo', '/baldo')
#add('BallardStreet', '/ballardstreet')
add('BananaTriangle', '/banana-triangle')
add('Barefoot', '/barefoot')
add('BarkeaterLake', '/barkeaterlake')
add('BarkingCrayon', '/barking-crayon')
add('BarneyAndClyde', '/barneyandclyde')
add('BasicInstructions', '/basicinstructions')
add('BeMisery', '/bemisery')
add('Beanie', '/beanie')
add('Beardo', '/beardo')
add('Beebleville', '/beebleville')
add('Ben', '/ben')
add('BenSargent', '/bensargent')
add('BenjaminBreadman', '/benjamin-breadman')
add('BergerAndWyse', '/berger-and-wyse')
add('BestInShow', '/best-in-show')
add('Betty', '/betty')
add('Bewley', '/bewley')
add('BiffAndRiley', '/biff-and-riley')
add('BigMonkeyComic', '/big-monkey-comic')
add('BigNate', '/bignate')
add('BigTop', '/bigtop')
add('Biographic', '/biographic')
add('Birdbrains', '/birdbrains')
add('Bliss', '/bliss')
add('BloomCounty', '/bloomcounty')
add('BlueSkiesToons', '/blue-skies-toons')
add('Bluebonnets', '/cowsandstuff')
add('BoNanas', '/bonanas')
add('BobGorrell', '/bobgorrell')
add('BobtheSquirrel', '/bobthesquirrel')
add('Boomerangs', '/boomerangs')
add('Bottomliners', '/bottomliners')
add('BoundandGagged', '/boundandgagged')
add('BreakofDay', '/break-of-day')
add('Brevity', '/brevity')
add('BrewsterRockit', '/brewsterrockit')
add('BrilliantMines', '/brilliant-mines')
add('Broham', '/broham')
add('BroomHilda', '/broomhilda')
add('BubblesandSnail', '/bubbles-and-snail')
add('Buni', '/buni')
add('BuzzaWuzza', '/buzza-wuzza')
add('CAFFEINATED', '/CAFFEINATED')
add('CANDYBLONDELL', '/candyblondell')
add('CafconLeche', '/cafeconleche')
add('CalvinandHobbes', '/calvinandhobbes')
add('Candorville', '/candorville')
add('CaricaturesbyKerryWaghorn', '/facesinthenews')
add('CarlsLife', '/carlslife')
add('Cartertoons', '/cartertoons')
add('CaseyandKyle', '/casey-and-kyle')
add('Cathy', '/cathy')
add('CestlaVie', '/cestlavie')
add('ChanLowe', '/chanlowe')
add('CharmysArmy', '/charmy-s-army')
add('CheapThrillsCuisine', '/cheap-thrills-cuisine')
add('ChipBok', '/chipbok')
add('ChrisBritt', '/chrisbritt')
add('ChubbyGirlComics', '/chubbygirlcomics')
add('ChuckAsay', '/chuckasay')
#add('ChuckleBros', '/chucklebros')
add('CircusPeople', '/circus-people')
add('CitizenDog', '/citizendog')
add('ClayBennett', '/claybennett')
add('Cleats', '/cleats')
add('ClosetoHome', '/closetohome')
add('CockroachComix', '/cockroachcomix')
add('CoffeeShopTidbits', '/coffee-shop-tidbits')
add('Committed', '/committed')
add('Computoon', '/compu-toon')
add('Confabulation', '/confabulation')
add('Cornered', '/cornered')
add('CowSheepandaGnomeNamedHelga', '/cow-sheep-and-a-gnome-named-helga')
add('CowTown', '/cowtown')
add('CowandBoyClassics', '/cowandboy')
add('Crabbels', '/crabbels')
add('Creek', '/creek')
add('Critterdoodles', '/critterdoodles')
add('CrocAndGator', '/croc-and-gator')
add('Crumb', '/crumb')
add('CubienBouncy', '/cubie-n-bouncy')
add('CuldeSac', '/culdesac')
add('DRAWINGTHELINECartoons', '/drawing-the-line')
add('DRail', '/d-rail')
#add('DaddysHome', '/daddyshome')
add('DailyPinky', '/daily-pinky')
add('DanWasserman', '/danwasserman')
add('DanaSummers', '/danasummers')
add('DarkSideoftheHorse', '/darksideofthehorse')
add('DarkWIndow', '/dark-window')
add('DeepCover', '/deepcover')
add('DevinCraneComicStripGhostwriter', '/devincranecomicstripghostwriter')
#add('DiamondLil', '/diamondlil')
add('DickLocher', '/dicklocher')
add('DickTracy', '/dicktracy')
add('DilbertClassics', '/dilbert-classics')
add('DitzAbledPrincess', '/ditzabled-princess')
add('DixieDrive', '/dixie-drive')
#add('DogEatDoug', '/dogeatdoug')
#add('DogsofCKennel', '/dogsofckennel')
add('DomesticAbuse', '/domesticabuse')
add('DontPicktheFlowers', '/dont-pick-the-flowers')
add('DoodleDaysComics', '/doodle-days')
add('Doonesbury', '/doonesbury')
add('Doublenegative', '/double-negative')
add('DrX', '/dr-x')
add('Drabble', '/drabble')
add('Dragin', '/dragin')
add('DrewLitton', '/drewlitton')
add('DrewSheneman', '/drewsheneman')
add('Dromo', '/dro-mo')
add('DudeandDude', '/dudedude')
add('DumbQuestionBadAnswer', '/dumb-question-bad-answer')
add('DustSpecks', '/dust-specks')
add('EGGMEN', '/eggmen')
add('Eddie', '/eddie')
add('Eek', '/eek')
add('EmmyLou', '/emmy-lou')
add('Endtown', '/endtown')
add('EngagAndNevets', '/engag-nevets')
add('Enlightoons', '/enlightoons')
add('ErictheCircle', '/eric-the-circle')
add('EttoreandBaldo', '/ettore-and-baldo')
add('FMinus', '/fminus')
add('FamilyTree', '/familytree')
add('FantasticMegaLeague', '/fantastiteam')
add('Farcus', '/farcus')
add('FaronSquare', '/faron-square')
add('FatCats', '/fat-cats')
add('Featherweight', '/featherweight')
#add('FloandFriends', '/floandfriends')
add('FoolishMortals', '/foolish-mortals')
add('ForBetterorForWorse', '/forbetterorforworse')
#add('ForHeavensSake', '/forheavenssake')
add('ForMyOwnGood', '/for-my-own-good')
add('FortKnox', '/fortknox')
add('FoxTrot', '/foxtrot')
add('FoxTrotClassics', '/foxtrotclassics')
add('FrankAndErnest', '/frankandernest')
add('FrankAndSteinway', '/frank-and-steinway')
add('FrankBlunt', '/frankblunt')
add('FrankSonata', '/frank-sonata')
add('Frazz', '/frazz')
add('FredBasset', '/fredbasset')
#add('FreeRange', '/freerange')
add('FreshlySqueezed', '/freshlysqueezed')
add('FrizziToons', '/frizzitoons')
add('FrogApplause', '/frogapplause')
add('Garfield', '/garfield')
add('GarfieldMinusGarfield', '/garfieldminusgarfield')
add('GaryMarkstein', '/garymarkstein')
add('GaryVarvel', '/garyvarvel')
add('GasolineAlley', '/gasolinealley')
add('Geech', '/geech')
add('Generations', '/generations')
add('GentleCreatures', '/gentle-creatures')
add('GetAGrip', '/get-a-grip')
add('GetFuzzy', '/getfuzzy')
add('GetaLife', '/getalife')
add('GilThorp', '/gilthorp')
add('GingerMeggs', '/gingermeggs')
add('GiveOver', '/give-over')
add('GlennMcCoy', '/glennmccoy')
add('GlenviewRevue', '/glenview-revue')
add('GoodwithCoffee', '/good-with-coffee')
add('Graffiti', '/graffiti')
add('GrandAvenue', '/grand-avenue')
add('GrandmaSnoops', '/grandmasnoops')
add('GrannyAnny', '/granny-anny')
add('GrayMatters', '/gray-matters')
add('GreenPieces', '/green-pieces')
add('GregAbeg', '/gregabeg')
add('Grizz', '/grizz')
add('GunstonStreet', '/gunston-street')
add('HIP', '/hip')
add('HUBRIS', '/hubris')
add('HaikuEwe', '/haikuewe')
add('HamShears', '/ham-shears')
add('HanginOut', '/hangin-out')
add('HankTheSock', '/hank-the-sock')
add('HankandDalesOurWorld', '/hank-and-dales-our-world')
add('HaphazardHumor', '/haphazard-humor')
add('HarambeeHills', '/harambeehills')
add('HartsPass', '/harts-pass')
add('Hbenson7', '/hbenson7')
add('HealthCapsules', '/healthcapsules')
add('HeartoftheCity', '/heartofthecity')
#add('Heathcliff', '/heathcliff')
add('HeavenlyNostrils', '/heavenly-nostrils')
add('HenryPayne', '/henrypayne')
#add('HerbandJamaal', '/herbandjamaal')
add('Herman', '/herman')
add('HistoryBluffs', '/historybluffs')
add('HomeandAway', '/homeandaway')
add('HoodootheUnwiseOwl', '/hoodootheunwiseowl')
add('HumblebeeandBob', '/humblebee-and-bob')
add('Humoresque', '/humoresque ')
add('HutchOwen', '/hutch-owen')
add('INCOMPATIBLES', '/incompatibles')
add('ImaDillo', '/i-m-a-dillo')
add('ImagineThis', '/imaginethis')
add('InTheSandbox', '/inthesandbox')
add('IncidentalComics', '/incidentalcomics')
add('InfinityBurger', '/infinity-burger')
add('InkPen', '/inkpen')
add('InspectorDangersCrimeQuiz', '/inspector-dangers-crime-quiz')
add('IntheBleachers', '/inthebleachers')
add('IntheSticks', '/inthesticks')
add('ItsAllAboutYou', '/itsallaboutyou')
add('JackOhman', '/jackohman')
add('JackRadioComics', '/jack-radio-comics')
add('JanesWorld', '/janesworld')
add('JeffDanziger', '/jeffdanziger')
add('JeffStahler', '/jeffstahler')
add('JenSorensen', '/jen-sorensen')
add('JerryHolbert', '/jerryholbert')
add('JillpokeBohemia', '/jillpoke-bohemia')
add('JimMorin', '/jimmorin')
add('JimsJournal', '/jimsjournal')
add('JoeHeller', '/joe-heller')
add('JoeVanilla', '/joevanilla')
add('JoelPett', '/joelpett')
add('JohnDeering', '/johndeering')
add('JolleyStuffBrowser', '/jolleystuff-browser')
add('JumpStart', '/jumpstart')
add('JustSayUncle', '/just-say-uncle')
add('KALEECHIKORNERS', '/kaleechi-korners')
add('KSquaredComics', '/k-squared-comics')
add('KeepingUpWithJones', '/keeping-up-with-jones')
add('KenCatalino', '/kencatalino')
add('KevinKallaugher', '/kevinkallaugher')
add('KidCity', '/kidcity')
add('KidInc', '/kid-inc')
add('KidSpot', '/kidspot')
add('KingMe', '/king-me')
add('KitNCarlyle', '/kitandcarlyle')
add('KitchenCapers', '/kitchen-capers')
add('Kliban', '/kliban')
add('KlibansCats', '/klibans-cats')
add('KookieCrumbz', '/kookie-crumbz')
add('KozmooftheCosmos', '/kozmoofthecosmos')
add('LaCucaracha', '/lacucaracha')
add('LaloAlcaraz', '/laloalcaraz')
add('LarryvilleBlue', '/larryville-blue')
add('LastKiss', '/lastkiss')
add('Laughwebcom', '/laughweb-com')
add('Leadbellies', '/leadbellies')
add('LegendofBill', '/legendofbill')
#add('LibertyMeadows', '/libertymeadows')
add('LifeafterDeath', '/life-after-death')
add('LilAbner', '/lil-abner')
add('LilEarlLovestoDRAW', '/lil-earl-loves-to-draw')
add('Lio', '/lio')
add('LisaBenson', '/lisabenson')
add('LittleDogLost', '/littledoglost')
add('Lola', '/lola')
add('LooseParts', '/looseparts')
add('LostSheep', '/lostsheep')
add('LostSideofSuburbia', '/lostsideofsuburbia')
add('LoveIs', '/loveis')
add('Luann', '/luann')
add('Lucan', '/lucan')
add('LucasLuminous', '/lucas-luminous')
add('LuckyCow', '/luckycow')
add('LumandAbner', '/lum-and-abner')
add('LumpedIn', '/lumped-in')
add('Mac', '/mac')
add('MadDogGhettoCop', '/maddogghettocop')
add('MadMouse', '/mad-mouse')
add('MagicCoffeeHair', '/magic-coffee-hair')
add('MagicinaMinute', '/magicinaminute')
add('Maintaining', '/maintaining')
add('MariasDay', '/marias-day')
add('Markonpaper', '/mark-on-paper')
add('Marmaduke', '/marmaduke')
add('MarshallRamsey', '/marshallramsey')
add('MartyandSpud', '/marty-and-spud')
add('MaryBWary', '/mary-b-wary')
add('MattBors', '/matt-bors')
add('MattDavies', '/mattdavies')
add('MattWuerker', '/mattwuerker')
add('McArroni', '/mcarroni')
add('MeandJerseyD', '/meandjerseyd')
add('MediumLarge', '/medium-large')
add('MegClassics', '/meg-classics')
add('MemoirsofaHoofDog', '/hoof-dog')
add('MichaelRamirez', '/michaelramirez')
add('MikeLester', '/mike-lester')
add('MikeLuckovich', '/mikeluckovich')
add('MikeThompson', '/mikethompson')
add('MikeduJour', '/mike-du-jour')
add('Milton50', '/milton-5-0')
add('Mindframe', '/mindframe')
add('MinimumSecurity', '/minimumsecurity')
add('MiscSoup', '/misc-soup')
add('MixedMedications', '/mixedmedications')
add('ModeratelyConfused', '/moderately-confused')
add('MollyandtheBear', '/mollyandthebear')
#add('Momma', '/momma')
add('Monday', '/monday')
add('Monty', '/monty')
add('MortMonday', '/mort-monday')
add('MortsIsland', '/noahs-island')
add('MotleyClassics', '/motley-classics')
add('MrGigiandtheSquid', '/mr-gigi-and-the-squid')
add('MrTodd', '/mr-todd')
add('MustardandBoloney', '/mustard-and-boloney')
add('MuttAndJeff', '/muttandjeff')
add('MyCage', '/mycage')
add('MyGuardianGrandpa', '/my-guardian-grandpa')
add('MythTickle', '/mythtickle')
add('NEUROTICA', '/neurotica')
add('Nancy', '/nancy')
add('Nanoworld', '/nano-world')
add('NavyBean', '/navybean')
add('NeatStep', '/neatstep')
add('NedAndLarry', '/ned-and-larry')
add('NeighborhoodZone', '/neightborhood-zone')
#add('NestHeads', '/nestheads')
add('NewAdventuresofQueenVictoria', '/thenewadventuresofqueenvictoria')
add('NickAnderson', '/nickanderson')
add('NoPlaceLikeHolmes', '/no-place-like-holmes')
add('NobodysHome', '/nobodys-home')
add('NonSequitur', '/nonsequitur')
add('NothingisNotSomething', '/nothing-is-not-something')
add('OHBABY', '/ohbaby')
add('ONIONAndPEA', '/onion-and-pea')
add('OddsandNubs', '/odds-and-nubs')
add('OfftheMark', '/offthemark')
add('OldUncleHoracesbookofGreatWisdom', '/old-uncle-horaces-book-of-great-wisdom')
add('OllieandQuentin', '/ollie-and-quentin')
#add('OnAClaireDay', '/onaclaireday')
#add('OneBigHappy', '/onebighappy')
add('OntheGrind', '/on-the-grind')
add('OrangesareFunny', '/oranges-are-funny')
add('OrdinaryBill', '/ordinary-bill')
add('OutoftheGenePoolReRuns', '/outofthegenepool')
add('Overboard', '/overboard')
add('OvertheHedge', '/overthehedge')
add('OzyandMillie', '/ozy-and-millie')
add('PCandPixel', '/pcandpixel')
add('PIGGENS', '/piggens')
add('PatOliphant', '/patoliphant')
add('PaulSzep', '/paulszep')
add('Peanizles', '/peanizles')
add('Peanuts', '/peanuts')
add('PearlsBeforeSwine', '/pearlsbeforeswine')
add('Peeples', '/peeples')
add('PeteyandthePack', '/petey-and-the-pack')
add('Pibgorn', '/pibgorn')
add('PibgornSketches', '/pibgornsketches')
add('Pickles', '/pickles')
add('Pinkerton', '/pinkerton')
add('PlanB', '/planb')
add('Pluggers', '/pluggers')
add('PoliceLimit', '/policelimit')
add('PoochCafe', '/poochcafe')
add('PopDog', '/pop-dog')
add('PreTeena', '/preteena')
add('PricklyCity', '/pricklycity')
add('Primusthebadphilosopher', '/primus-the-bad-philosopher')
add('PublicEd', '/publiced')
add('Putz', '/putz')
add('RANDUMBTHOUGHTS', '/randumb-thoughts')
add('RabbitsAgainstMagic', '/rabbitsagainstmagic')
add('Rackafracka', '/rackafracka')
add('RaisingDuncan', '/raising-duncan')
add('RalftheDestroyer', '/ralf-the-destroyer')
add('RandolphItch2am', '/randolphitch')
add('RealLifeAdventures', '/reallifeadventures')
add('RealityCheck', '/realitycheck')
add('Rechid', '/rechid')
add('RedMeat', '/redmeat')
add('RedandRover', '/redandrover')
add('ReplyAll', '/replyall')
add('RicigsToonTrivia', '/ricigs-toon-trivia')
add('RipHaywire', '/riphaywire')
add('RipleysBelieveItorNot', '/ripleysbelieveitornot')
add('Risible', '/risible')
add('RobRogers', '/robrogers')
add('RobertAriail', '/robert-ariail')
add('RogersBlues', '/roger-s-blues')
add('RogueSymmetry', '/rogue_symmetry')
add('RoseisRose', '/roseisrose')
#add('Rubes', '/rubes')
add('RudyPark', '/rudypark')
add('STEPDAD', '/stepdad')
add('Sabine', '/sabine')
add('SavageChickens', '/savage-chickens')
#add('ScaryGary', '/scarygary')
add('ScottStantis', '/scottstantis')
add('SecondPrize', '/secondprize')
add('SherlockUnleashed', '/sherlock-unleashed')
add('ShirleyandSonClassics', '/shirley-and-son-classics')
add('Shoe', '/shoe')
add('Shoecabbage', '/shoecabbage')
add('Shortcuts', '/shortcuts')
add('SickWit', '/sickwit')
add('SignGarden', '/signgarden')
add('SigneWilkinson', '/signewilkinson')
add('SkinHorse', '/skinhorse')
add('Skippy', '/skippy')
add('Skylarking', '/skylarking')
add('SmallWorld', '/smallworld')
add('Smith', '/smith')
add('SnowSez', '/snowsez')
add('SoccerEarth', '/soccer-earth')
add('SookyRottweiler', '/sooky-rottweiler')
add('SouptoNutz', '/soup-to-nutz')
add('SpaceTimeFunnies', '/spacetimefunnies')
add('Spareroom', '/spareroom')
add('Spectickles', '/spectickles')
#add('SpeedBump', '/speedbump')
add('SportsbyVoort', '/sports-by-voort')
add('SpottheFrog', '/spot-the-frog')
add('StankoAndTibor', '/stankotibor')
add('Starslip', '/starslip')
add('SteveBenson', '/stevebenson')
add('SteveBreen', '/stevebreen')
add('SteveKelley', '/stevekelley')
add('SteveSack', '/stevesack')
add('StoneSoup', '/stonesoup')
#add('StrangeBrew', '/strangebrew')
add('StrangerThings', '/stranger-things')
add('StuartCarlson', '/stuartcarlson')
add('SuburbanFairyTales', '/suburbanfairytales')
add('SuckerHeadSmack', '/suckerhead-smack')
add('SueReallyRules', '/sue-really-rules')
add('SunnyStreet', '/sunny-street')
add('SuperSiblings', '/super-siblings')
add('Sylvia', '/sylvia')
add('TOBY', '/toby')
add('TalesofTerraTopia', '/terratopia')
add('TankMcNamara', '/tankmcnamara')
add('Tarzan', '/tarzan')
add('Teacher', '/teacher')
add('TedRall', '/tedrall')
add('TenCats', '/ten-cats')
add('Thatababy', '/thatababy')
add('ThatisPriceless', '/that-is-priceless')
add('ThatsLife', '/thats-life')
add('TheAcademiaWaltz', '/academiawaltz')
add('TheAngryGamer', '/the-angry-gamer')
add('TheArgyleSweater', '/theargylesweater')
#add('TheBarn', '/thebarn')
add('TheBellies', '/the-bellies')
add('TheBigPicture', '/thebigpicture')
add('TheBoobiehatch', '/the-boobiehatch')
add('TheBoondocks', '/boondocks')
add('TheBornLoser', '/the-born-loser')
add('TheBuckets', '/thebuckets')
add('TheBureaucrats', '/bureaucrats')
add('TheCardinal', '/thecardinal')
add('TheCity', '/thecity')
add('TheCreeps', '/the-creeps')
add('TheDeadlys', '/the-deadlys')
#add('TheDinetteSet', '/dinetteset')
add('TheDoozies', '/thedoozies')
add('TheDuplex', '/duplex')
add('TheEdperiment', '/the-edperiment')
add('TheElderberries', '/theelderberries')
add('TheFastLane', '/fast-lane')
add('TheFlyingMcCoys', '/theflyingmccoys')
add('TheFurtherAdventuresofMackieWhite', '/the-further-adventures-of-mackie-white')
add('TheFuscoBrothers', '/thefuscobrothers')
add('TheGoldenKid', '/golden-kid')
add('TheGreatKhan', '/great-khan')
add('TheGreenMonkeys', '/thegreenmonkeys')
add('TheGrizzwells', '/thegrizzwells')
add('TheHouseofUnCommons', '/house-of-uncommons')
add('TheHumbleStumble', '/humble-stumble')
add('TheIllConceivedNotionsofJehosophatGrymm', '/the-ill-conceived-notions-of-jehosophat-grymm')
add('TheKChronicles', '/thekchronicles')
add('TheKnightLife', '/theknightlife')
add('TheLeftyBoscoPictureShow', '/leftyboscopictureshow')
add('TheLightedLab', '/the-lighted-lab')
add('TheLilMiesters', '/the-lil-miesters')
add('TheLostBear', '/the-lost-bear')
#add('TheMeaningofLila', '/meaningoflila')
add('TheMiddletons', '/themiddletons')
add('TheMightyWonderBrat', '/mighty-wonderbrat')
add('TheNormClassics', '/thenorm')
add('TheOgre', '/the-ogre')
add('TheOldManAndHisDog', '/old-man-and-his-dog')
add('TheOnesMyWifeLikes', '/the-ones-my-life-likes')
#add('TheOtherCoast', '/theothercoast')
add('TheSingleDadDiaries', '/single-dad-diaries')
add('TheSunnySideofKeuka', '/sunny-side-of-keuka')
add('TheSunshineClub', '/the-sunshine-club')
add('TheWagesofSin', '/wages-of-sin')
add('ThereisStrangenessintheUniverse', '/there-is-strangeness-in-the-universe')
#add('ThinLines', '/thinlines')
add('Think', '/think')
add('ThrompTM', '/thromp')
add('TinySepuku', '/tinysepuku')
add('TodaysDogg', '/todays-dogg')
add('TomToles', '/tomtoles')
add('TomtheDancingBug', '/tomthedancingbug')
add('Tomversation', '/tomversation')
add('TonyAuth', '/tonyauth')
add('TooMuchCoffeeMan', '/toomuchcoffeeman')
add('Toocrazy', '/too-crazy')
add('TopicToons', '/topictoons')
add('Trivquiz', '/trivquiz')
add('Twaggies', '/twaggies')
add('TwoBits', '/two-bits')
add('TyreAndKerb', '/tyre-and-kerb')
add('USAcres', '/us-acres')
add('UncleArtsFunland', '/uncleartsfunland')
add('UnstrangePhenomena', '/unstrange-phenomena')
add('VanGogh', '/van-gogh')
add('Vernscartoons', '/vernscartoons')
add('ViewsAfrica', '/viewsafrica')
add('ViewsAmerica', '/viewsamerica')
add('ViewsAsia', '/viewsasia')
add('ViewsBusiness', '/viewsbusiness')
add('ViewsEurope', '/viewseurope')
add('ViewsLatinAmerica', '/viewslatinamerica')
add('ViewsMidEast', '/viewsmideast')
add('ViewsoftheWorld', '/viewsoftheworld')
add('ViiviAndWagner', '/viivi-and-wagner')
add('WTDuck', '/wtduck')
add('WaltHandelsman', '/walthandelsman')
add('WatchYourHead', '/watchyourhead')
#add('WeePals', '/weepals')
add('WendlesLife', '/wendleslife')
add('WhiskeyFalls', '/whiskey-falls')
add('WhosOnDeck', '/whos-on-deck')
add('Windsock', '/windsock')
add('WitoftheWorld', '/witoftheworld')
#add('WizardofId', '/wizardofid')
add('WorkingDaze', '/working-daze')
#add('WorkingItOut', '/workingitout')
add('Wrobbertcartoons', '/wrobbertcartoons')
#add('ZackHill', '/zackhill')
add('ZhoodBahzvoi', '/zhood-bahzvoi')
add('Ziggy', '/ziggy')
add('ZonnosPeople', '/zonno-s-people')
add('Zootopia', '/zootopia')

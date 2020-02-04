# -*- coding: utf-8 -*-
# Copyright (C) 2019-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class WebToons(_ParserScraper):
    imageSearch = '//img[contains(@class, "_images")]/@data-url'
    prevSearch = '//a[contains(@class, "_prevEpisode")]'
    multipleImagesPerStrip = True

    def __init__(self, name, url, titlenum):
        super(WebToons, self).__init__('WebToons/' + name)

        baseUrl = 'https://www.webtoons.com/en/'
        self.url = baseUrl + url + '/episode/viewer?title_no=' + str(titlenum)
        self.listUrl = baseUrl + url + '/list?title_no=' + str(titlenum)
        self.stripUrl = self.url + '&episode_no=%s'
        self.firstStripUrl = self.stripUrl % '1'

    def starter(self):
        # Set age-check cookie
        self.session.cookies.set('ageGatePass', 'true', domain='webtoons.com')
        # Find current episode number
        listPage = self.getPage(self.listUrl)
        currentEpisode = listPage.xpath('//div[@class="detail_lst"]/ul/li')[0].attrib['data-episode-no']
        # Check for completed tag
        self.endOfLife = (listPage.xpath('//span[@class="txt_ico_completed2"]') != [])
        return self.stripUrl % currentEpisode

    def fetchUrls(self, url, data, urlSearch):
        # Save link order for position-based filenames
        self.imageUrls = super(WebToons, self).fetchUrls(url, data, urlSearch)
        # Update firstStripUrl with the correct episode title
        if url.rsplit('=', 1)[-1] == '1':
            self.firstStripUrl = url
        return self.imageUrls

    def namer(self, imageUrl, pageUrl):
        # Construct filename from episode number and image position on page
        episodeNum = pageUrl.rsplit('=', 1)[-1]
        imageNum = self.imageUrls.index(imageUrl)
        imageExt = pageUrl.rsplit('.', 1)[-1].split('?', 1)[0]
        return "%s-%02d.%s" % (episodeNum, imageNum, imageExt)

    @classmethod
    def getmodules(cls):
        return (
            # WebToons Canvas comics
            cls('Anthronauts', 'challenge/anthronauts', 358917),
            cls('Debunkers', 'challenge/debunkers', 148475),
            cls('InternetExplorer', 'challenge/internet-explorer', 219164),
            cls('PinchPoint', 'challenge/pinch-point-reborn', 334640),
            cls('SpaceVixen', 'challenge/space-vixen-deep-space-k9', 207049),

            # Unicode title
            cls('Lozolz', 'tiptoon/lozolz', 1268),

            # START AUTOUPDATE
            cls('1000', 'action/one-thousand', 1217),
            cls('10thDimensionBoys', 'comedy/10th-dimension-boys', 71),
            cls('1111Animals', 'comedy/1111-animals', 437),
            cls('2015SpaceSeries', 'sf/2015-space-series', 391),
            cls('3SecondStrip', 'comedy/3-second-strip', 380),
            cls('ABittersweetLife', 'slice-of-life/a-bittersweet-life', 294),
            cls('AboutDeath', 'drama/about-death', 82),
            cls('ABudgiesLife', 'slice-of-life/its-a-budgies-life', 985),
            cls('Acception', 'drama/acception', 1513),
            cls('Acursian', 'fantasy/acursian', 1452),
            cls('Adamsville', 'thriller/adamsville', 502),
            cls('AdventuresOfGod', 'comedy/adventures-of-god', 853),
            cls('AerialMagic', 'drama/aerial-magic', 1358),
            cls('AgeMatters', 'romance/age-matters', 1364),
            cls('AGoodDayToBeADog', 'drama/a-good-day-tobe-a-dog', 1390),
            cls('Aisopos', 'drama/aisopos', 76),
            cls('AliceElise', 'fantasy/alice-elise', 1481),
            cls('AllThatWeHopeToBe', 'slice-of-life/all-that-we-hope-to-be', 470),
            cls('AllThatYouAre', 'drama/all-that-you-are', 403),
            cls('AlwaysHuman', 'romance/always-human', 557),
            cls('Annarasumanara', 'drama/annarasumanara', 77),
            cls('AphroditeIX', 'sf/aphroditeix', 1451),
            cls('ApocalypticHorseplay', 'fantasy/apocalyptic-horseplay', 635),
            cls('AprilFlowers', 'fantasy/april-flowers', 1363),
            cls('Arma', 'action/arma', 1640),
            cls('AsPerUsual', 'comedy/as-per-usual', 599),
            cls('AssassinRoommate', 'romance/assassin-roommate', 1050),
            cls('AthenaComplex', 'fantasy/athena-complex', 867),
            cls('AuraFromAnotherPlanet', 'comedy/aura-from-another-planet', 369),
            cls('AverageAdventuresOfAnAverageGirl', 'slice-of-life/average-adventures-of-an-average-girl', 401),
            cls('AXED', 'comedy/axed', 1558),
            cls('Backchannel', 'super-hero/backchannel', 1456),
            cls('BadSigns', 'comedy/bad-signs', 1623),
            cls('Bastard', 'thriller/bastard', 485),
            cls('BehindTheGIFs', 'comedy/behind-the-gifs', 658),
            cls('BigJo', 'drama/big-jo', 854),
            cls('BiteMe', 'drama/bite-me', 1019),
            cls('Blessed', 'drama/blessed', 1193),
            cls('BloodInk', 'action/blood-ink', 1490),
            cls('BloodlessWars', 'action/bloodless-wars', 1622),
            cls('Bluechair', 'comedy/bluechair', 199),
            cls('BOOItsSex', 'slice-of-life/boo-its-sex', 1413),
            cls('BoyfriendOfTheDead', 'comedy/boyfriend-of-the-dead', 1102),
            cls('BrassAndSass', 'romance/brass-and-sass', 1652),
            cls('BrimstoneAndRoses', 'romance/brimstone-and-roses', 1758),
            cls('BrothersBond', 'action/brothersbond', 1458),
            cls('BrutallyHonest', 'comedy/brutally-honest', 799),
            cls('BuzzFeedComics', 'comedy/buzzfeed-comics', 585),
            cls('CapeOfSpirits', 'fantasy/cape-of-spirits', 1559),
            cls('CARL', 'comedy/carl', 1216),
            cls('Caster', 'action/caster', 1461),
            cls('CastleSwimmer', 'fantasy/castle-swimmer', 1499),
            cls('Catharsis', 'fantasy/catharsis', 396),
            cls('CatLoafAdventures', 'slice-of-life/cat-loaf-adventures', 1381),
            cls('CheeseInTheTrap', 'romance/cheese-in-the-trap', 99),
            cls('CherryBlossoms', 'romance/cherry-blossoms', 1005),
            cls('Chiller', 'thriller/chiller', 536),
            cls('ChocoLatte', 'romance/choco-latte', 1691),
            cls('CityOfWalls', 'action/city-of-wall', 505),
            cls('ClusterFudge', 'slice-of-life/cluster-fudge', 355),
            cls('CodeAdam', 'action/code-adam', 1657),
            cls('CookingComically', 'slice-of-life/cooking-comically', 622),
            cls('Crumbs', 'romance/crumbs', 1648),
            cls('CupidsArrows', 'romance/cupids-arrows', 1538),
            cls('CursedPrincessClub', 'comedy/cursed-princess-club', 1537),
            cls('Cyberbunk', 'sf/cyberbunk', 466),
            cls('Cyberforce', 'super-hero/cyberforce', 531),
            cls('CykoKO', 'comedy/cyko-ko', 560),
            cls('Darbi', 'action/darbi', 1098),
            cls('Davinchibi', 'drama/davinchibi', 1190),
            cls('DaYomanvilleGang', 'drama/da-yomanville-gang', 1578),
            cls('DaysOfHana', 'romance/days-of-hana', 1246),
            cls('DEADDAYS', 'thriller/dead-days', 293),
            cls('DEEP', 'thriller/deep', 364),
            cls('Denma', 'sf/denma', 921),
            cls('Dents', 'sf/dents', 671),
            cls('Deor', 'fantasy/deor', 1663),
            cls('DevilNumber4', 'romance/devil-no-4', 1695),
            cls('DICE', 'fantasy/dice', 64),
            cls('DistantSky', 'thriller/distant-sky', 75),
            cls('DONTHATE', 'comedy/dont-hate', 1574),
            cls('DoodleForFood', 'slice-of-life/doodle-for-food', 487),
            cls('Dragnarok', 'fantasy/dragnarok', 1018),
            cls('DragnarokDescendants', 'fantasy/dragnarok-descendants', 1433),
            cls('DrFrost', 'drama/dr-frost', 371),
            cls('Dustinteractive', 'comedy/dustinteractive', 907),
            cls('DutyAfterSchool', 'drama/duty-after-school', 370),
            cls('EatFighter', 'comedy/eat-fighter', 1460),
            cls('EcstasyHearts', 'romance/ecstasy-hearts', 604),
            cls('Edith', 'romance/edith', 1536),
            cls('Eggnoid', 'romance/eggnoid', 1229),
            cls('Eleceed', 'fantasy/eleceed', 1571),
            cls('Elena', 'thriller/elena', 484),
            cls('ElfAndWarrior', 'fantasy/elf-and-warrior', 908),
            cls('EMPYREA', 'fantasy/empyrea', 1407),
            cls('EpicV', 'comedy/epic-v', 353),
            cls('EverywhereAndNowhere', 'comedy/everywhere-and-nowhere', 1598),
            cls('FAMILYMAN', 'drama/family-man', 85),
            cls('FantasySketchTheGame', 'fantasy/fantasy-sketch', 1020),
            cls('Faust', 'fantasy/faust', 522),
            cls('FINALITY', 'thriller/finality', 1457),
            cls('Firebrand', 'fantasy/firebrand', 877),
            cls('Flow', 'fantasy/flow', 101),
            cls('FluffyBoyfriend', 'drama/fluffy-boyfriend', 1164),
            cls('ForTheSakeOfSita', 'romance/for-the-sake-of-sita', 349),
            cls('FourLeaf', 'fantasy/four-leaf', 1454),
            cls('FreakingRomance', 'romance/freaking-romance', 1467),
            cls('FridayForbiddenTales', 'thriller/friday', 388),
            cls('Gepetto', 'sf/gepetto', 81),
            cls('GhostsAmongTheWildFlowers', 'fantasy/ghosts-over-wild-flowers', 718),
            cls('GhostTeller', 'horror/ghost-teller', 1307),
            cls('GhostWife', 'romance/ghost-wife', 1471),
            cls('GirlsHaveABlog', 'slice-of-life/girls-have-a-blog', 1052),
            cls('GirlsOfTheWilds', 'action/girls-of-the-wilds', 93),
            cls('GodOfBath', 'comedy/god-of-bath', 91),
            cls('GOSU', 'action/gosu', 1099),
            cls('GourmetHound', 'drama/gourmet-hound', 1245),
            cls('GuardiansOfTheVideoGame', 'fantasy/guardians-of-the-video-game', 368),
            cls('HAPIBUNI', 'comedy/hapi-buni', 362),
            cls('HardcoreLevelingWarrior', 'action/hardcore-leveling-warrior', 1221),
            cls('HaveYouAnyFear', 'horror/have-you-any-fear', 1197),
            cls('Haxor', 'drama/haxor', 1325),
            cls('Heartwired', 'sf/heartwired', 1539),
            cls('HeirsGame', 'drama/heirs-game', 1445),
            cls('HeliosFemina', 'fantasy/helios-femina', 638),
            cls('HelloWorld', 'slice-of-life/hello-world', 827),
            cls('Hellper', 'action/hellper', 185),
            cls('HeroineChic', 'drama/heroine-chic', 561),
            cls('HIVE', 'thriller/hive', 65),
            cls('Hooky', 'fantasy/hooky', 425),
            cls('HoovesOfDeath', 'action/hooves-of-death', 1535),
            cls('HouseOfStars', 'fantasy/house-of-stars', 1620),
            cls('HowToLove', 'slice-of-life/how-to-love', 472),
            cls('IDontWantThisKindOfHero', 'fantasy/i-dont-want-this-kind-of-hero', 98),
            cls('IllusionsOfAdulting', 'drama/illusions-of-adulting', 922),
            cls('IllustratedInternet', 'comedy/illustrated-internet', 750),
            cls('ILoveYoo', 'romance/i-love-yoo', 986),
            cls('ImmortalNerd', 'comedy/immortal-nerd', 579),
            cls('ImTheGrimReaper', 'thriller/im-the-grim-reaper', 1697),
            cls('Inarime', 'fantasy/inarime', 675),
            cls('JackieRose', 'action/jackie-rose', 613),
            cls('JingleJungle', 'slice-of-life/jingle-jungle', 282),
            cls('JustAskYuli', 'slice-of-life/just-ask-yuli', 402),
            cls('JustForKicks', 'slice-of-life/just-for-kicks', 1152),
            cls('JustPancakes', 'comedy/just-pancakes', 1651),
            cls('KidsAreAllRight', 'drama/kids-are-all-right', 283),
            cls('KindOfConfidential', 'romance/kind-of-confidential', 663),
            cls('KnightRun', 'fantasy/knight-run', 67),
            cls('Kubera', 'fantasy/kubera', 83),
            cls('LalinsCurse', 'drama/lalins-curse', 1601),
            cls('Lars', 'slice-of-life/lars', 358),
            cls('LateBloomer', 'romance/late-bloomer', 988),
            cls('LavenderJack', 'thriller/lavender-jack', 1410),
            cls('LESSA', 'fantasy/lessa', 89),
            cls('LESSA2TheCrimsonKnight', 'fantasy/lessa-2', 507),
            cls('LetsPlay', 'romance/letsplay', 1218),
            cls('LibraryGhost', 'slice-of-life/library-ghost', 220),
            cls('LifeOutsideTheCircle', 'romance/life-outside-the-circle', 1260),
            cls('LittleMatchaGirl', 'fantasy/little-matcha-girl', 1665),
            cls('LiveForever', 'drama/live-forever', 1312),
            cls('LiveWithYourself', 'comedy/live-with-yourself', 919),
            cls('Lookism', 'drama/lookism', 1049),
            cls('LoreOlympus', 'romance/lore-olympus', 1320),
            cls('Lorna', 'slice-of-life/lorna', 1284),
            cls('LoveAdviceFromTheGreatDukeOfHell', 'comedy/love-advice', 1498),
            cls('LUFF', 'romance/luff', 1489),
            cls('Luggage', 'fantasy/luggage', 1642),
            cls('LUMINE', 'drama/lumine', 1022),
            cls('Lunarbaboon', 'slice-of-life/lunarbaboon', 523),
            cls('MageAndDemonQueen', 'fantasy/mage-and-demon-queen', 1438),
            cls('Magical12thGraders', 'fantasy/magical-12th-graders', 90),
            cls('Magician', 'fantasy/magician', 70),
            cls('MatchmakerHero', 'sf/matchmaker-hero', 1569),
            cls('MelvinasTherapy', 'horror/melvinas-therapy', 1021),
            cls('MeowMan', 'comedy/meow-man', 1677),
            cls('MercWorks', 'comedy/mercworks', 426),
            cls('Messenger', 'fantasy/messenger', 1382),
            cls('MetaphoricalHER', 'drama/metaphorical-her', 1475),
            cls('MidnightRhapsody', 'slice-of-life/midnight-rhapsody', 116),
            cls('MidnightRhapsodySeason2', 'slice-of-life/midnight-rhapsody-season2', 365),
            cls('MissAbbottAndTheDoctor', 'romance/miss-abbott-and-the-doctor', 707),
            cls('MOONBEARD', 'comedy/moon-beard', 471),
            cls('MoonYou', 'sf/moonyou', 1340),
            cls('Murrz', 'slice-of-life/murrz', 1281),
            cls('Muted', 'drama/muted', 1566),
            cls('MyBoo', 'drama/my-boo', 1185),
            cls('MyDearColdBloodedKing', 'romance/my-dear-cold-blooded-king', 961),
            cls('MyDeepestSecret', 'drama/my-deepest-secret', 1580),
            cls('MyDictatorBoyfriend', 'comedy/my-dictator-boyfriend', 1391),
            cls('MyGiantNerdBoyfriend', 'slice-of-life/my-giant-nerd-boyfriend', 958),
            cls('MyKittyAndOldDog', 'slice-of-life/my-kitty-and-old-dog', 184),
            cls('MyNameIsBenny', 'slice-of-life/my-name-is-benny', 1279),
            cls('NanoList', 'sf/nano-list', 700),
            cls('NationalDogDay2016', 'slice-of-life/national-dog-day', 747),
            cls('NewLifeProject', 'comedy/new-life-project', 279),
            cls('Newman', 'fantasy/newman', 405),
            cls('NewNormalClass8', 'comedy/new-normal-class-8', 100),
            cls('Nicholalala', 'slice-of-life/nicholalala', 418),
            cls('NightmareFactory', 'fantasy/nightmare-factory', 616),
            cls('Noblesse', 'fantasy/noblesse', 87),
            cls('NoblesseRaisAdventure', 'fantasy/noblesse-spin-off', 608),
            cls('NoScope', 'action/no-scope', 1572),
            cls('NotEvenBones', 'thriller/not-even-bones', 1756),
            cls('NothingSpecial', 'fantasy/nothing-special', 1188),
            cls('OddGirlOut', 'drama/odd-girl-out', 1420),
            cls('OhHoly', 'romance/oh-holy', 809),
            cls('ORANGEMARMALADE', 'romance/orange-marmalade', 97),
            cls('Outrage', 'super-hero/outrage', 1450),
            cls('PacificRimAmara', 'sf/pacific-rim-amara', 1327),
            cls('PenguinLovesMev', 'slice-of-life/penguin-loves-mev', 86),
            cls('PhantomParadise', 'fantasy/phantom-paradise', 1250),
            cls('Pigminted', 'slice-of-life/pigminted', 482),
            cls('Plum', 'sports/plum', 1605),
            cls('Polidiocy', 'comedy/polidiocy', 676),
            cls('Pound', 'action/pound', 1496),
            cls('PowerBallad', 'drama/power-ballad', 987),
            cls('PurpleHyacinth', 'drama/purple-hyacinth', 1621),
            cls('Punderworld', 'challenge/punderworld', 312584),
            cls('RandomChat', 'drama/random-chat', 1669),
            cls('RANDOMPHILIA', 'comedy/randomphilia', 386),
            cls('Rebirth', 'fantasy/rebirth', 1412),
            cls('RefundHighSchool', 'drama/refundhighschool', 1360),
            cls('RiseFromAshes', 'fantasy/rise-from-ashes', 959),
            cls('RoarStreetJournal', 'slice-of-life/roar-street-journal', 397),
            cls('RoomOfSwords', 'sf/room-of-swords', 1261),
            cls('SafelyEndangered', 'comedy/safely-endangered', 352),
            cls('SaltyStudio', 'romance/salty-studio', 74),
            cls('SaphieTheOneEyedCat', 'slice-of-life/saphie-one-eyed-cat', 670),
            cls('SAVEME', 'drama/bts-save-me', 1514),
            cls('ScorchingRomance', 'drama/scorching-romance', 1662),
            cls('Seed', 'sf/seed', 1480),
            cls('SHADOW', 'fantasy/shadow', 281),
            cls('ShadowPirates', 'fantasy/shadow-pirates', 1455),
            cls('Shard', 'drama/shard', 960),
            cls('Shiloh', 'thriller/shiloh', 1649),
            cls('ShootAround', 'drama/shoot-around', 399),
            cls('Shriek', 'thriller/shriek', 772),
            cls('SID', 'fantasy/sid', 497),
            cls('SIDEKICKS', 'super-hero/sidekicks', 92),
            cls('SimonSues', 'thriller/simon-sues', 1619),
            cls('SirensLament', 'romance/sirens-lament', 632),
            cls('Sithrah', 'fantasy/sithrah', 524),
            cls('SkateFire100', 'fantasy/skate-fire-100', 1674),
            cls('SmallWorld', 'slice-of-life/small-world', 1159),
            cls('SmileBrush', 'slice-of-life/smile-brush', 94),
            cls('SmileBrushMyOldPictures', 'slice-of-life/smile-brush-my-old-pictures', 302),
            cls('Snailogy', 'slice-of-life/snailogy', 387),
            cls('SOULCARTEL', 'fantasy/soul-cartel', 72),
            cls('SoulOnHold', 'fantasy/soul-on-hold', 1701),
            cls('SpaceBoy', 'drama/space-boy', 400),
            cls('SpiritFingers', 'drama/spirit-fingers', 1577),
            cls('Spirits', 'fantasy/spirits-re', 1348),
            cls('STARCROSS', 'super-hero/star-cross', 1599),
            cls('StarWars', 'sf/starwars', 544),
            cls('StrawberrySeafoam', 'drama/strawberry-seafoam', 1248),
            cls('SubtleDisaster', 'drama/subtle-disaster', 350),
            cls('SubZero', 'romance/subzero', 1468),
            cls('SuperSecret', 'romance/super-secret', 666),
            cls('SupersonicGirl', 'super-hero/supersonic-girl', 633),
            cls('SweetHome', 'thriller/sweethome', 1285),
            cls('SwordInterval', 'fantasy/sword-interval', 486),
            cls('TalesOfTheUnusual', 'thriller/tales-of-the-unusual', 68),
            cls('TheBadguys', 'super-hero/the-bad-guys', 701),
            cls('TheBrooklynite', 'super-hero/the-brooklynite', 813),
            cls('TheCliff', 'thriller/the-cliff', 80),
            cls('TheCroaking', 'fantasy/the-croaking', 1494),
            cls('TheDaneMen', 'comedy/the-danemen', 395),
            cls('TheDevilIsAHandsomeMan', 'romance/the-devil-is-a-handsome-man', 1311),
            cls('TheFeverKing', 'fantasy/the-fever-king', 1659),
            cls('TheFourOfThem', 'drama/the-four-of-them', 1524),
            cls('TheGamer', 'fantasy/the-gamer', 88),
            cls('TheGentlemansArmchair', 'comedy/the-gentlemans-armchair', 469),
            cls('THEGIRLFROMCLASS', 'drama/the-girl-from-class', 73),
            cls('TheGodOfHighSchool', 'action/the-god-of-high-school', 66),
            cls('TheKissBet', 'romance/the-kiss-bet', 1617),
            cls('TheLifeOfTheThreeBears', 'slice-of-life/the-life-of-the-three-bears', 390),
            cls('ThePurpleHeart', 'super-hero/the-purple-heart', 723),
            cls('TheRedBook', 'thriller/the-red-book', 467),
            cls('TheRedHook', 'super-hero/the-red-hook', 643),
            cls('TheRedKing', 'fantasy/the-red-king', 1687),
            cls('TheSoundOfYourHeart', 'comedy/the-sound-of-your-heart', 269),
            cls('TheSteamDragonExpress', 'fantasy/steam-dragon-express', 1270),
            cls('TheStoriesOfThoseAroundMe', 'romance/the-stories-of-those-around-me', 96),
            cls('TheStrangeTalesOfOscarZahn', 'fantasy/the-strange-tales-of-oscar-zahn', 685),
            cls('TheVaultOfHorrorACollectionOfNightmares', 'thriller/the-vault-of-horror-a-collection-of-nightmares', 295),
            cls('TheWeightOfOurSky', 'drama/the-weight-of-our-sky', 1739),
            cls('TheWorldWhereIBelong', 'drama/the-world-where-i-belong', 1318),
            cls('ThirdShiftSociety', 'thriller/third-shift-society', 1703),
            cls('Thornstone', 'fantasy/thornstone', 1612),
            cls('TickleTown', 'comedy/tickle-town', 428),
            cls('TowerOfGod', 'fantasy/tower-of-god', 95),
            cls('TrailerParkWarlock', 'fantasy/trailer-park-warlock', 1512),
            cls('TrashBird', 'comedy/trash-bird', 473),
            cls('TrueBeauty', 'drama/truebeauty', 1436),
            cls('Trump', 'fantasy/trump', 84),
            cls('UndeadEd', 'comedy/undeaded', 468),
            cls('UnderPrin', 'fantasy/underprin', 78),
            cls('UnderTheAegis', 'fantasy/under-the-aegis', 436),
            cls('UnknownCaller', 'thriller/ar-toon', 775),
            cls('UnluckyIsAsLuckyDoes', 'comedy/unlucky-is-as-lucky-does', 1554),
            cls('UnOrdinary', 'fantasy/unordinary', 679),
            cls('UnTouchable', 'romance/untouchable', 79),
            cls('UpAndOut', 'slice-of-life/up-and-out', 488),
            cls('UrbanAnimal', 'action/urban-animal', 1483),
            cls('Uriah', 'thriller/uriah', 1607),
            cls('VarsityNoir', 'drama/varsity-noir', 1613),
            cls('WafflesAndPancakes', 'slice-of-life/waffles-and-pancakes', 1310),
            cls('WarCry', 'super-hero/war-cry', 1247),
            cls('WarningLabel', 'romance/warning-label', 1051),
            cls('Watermelon', 'drama/watermelon', 1435),
            cls('WeakHero', 'drama/weakhero', 1726),
            cls('WestwoodVibrato', 'drama/westwood-vibrato', 537),
            cls('WhereTangentsMeet', 'romance/where-tangents-meet', 421),
            cls('WindBreaker', 'action/wind-breaker', 372),
            cls('WinterMoon', 'fantasy/winter-moon', 1093),
            cls('WinterWoods', 'romance/winter-woods', 344),
            cls('WitchCreekRoad', 'horror/witch-creek-road', 1453),
            cls('WitchHunt', 'drama/witch-hunt', 363),
            cls('XINK3R', 'super-hero/xinker', 541),
            cls('YourAdventure', 'comedy/your-adventure', 506),
            cls('YourLetter', 'drama/your-letter', 1540),
            cls('YumisCells', 'romance/yumi-cell', 478),
            cls('ZeroGame', 'action/zero-game', 1704),
            # END AUTOUPDATE
        )
